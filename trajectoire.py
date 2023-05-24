import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
T0 = 0.1  # (s) periode de consigne
amax = 5  # (m/s²) accélération maximale nominale des roues (moins une marge)
vmax = 1  # (m/s) vitesse maximale nominale des roues (moins une marge)
r = 0.04  # (m) rayon des roues
L = 0.5  # (m) largeur du habot
G0 = (0, 0)  # position initiale du barycentre du habot
a0 = 0  # angle initial formant l'axe des roues du habot avec le repère
m = 6  # (kg) masse du habot

# Caractéristiques des moteurs-roues :
R = 1.33  # Résistance thermique
L_ = 0.115E-6  # Inductance thermique
Jmotor = 9.49E-14  # Moment d'inertie du moteur
KE = 0.0163  # Proportion entre la tension appliqué au moteur et à la vitesse angulaire
KT = 0.0163  # Proportion entre le courant passant dans le moteur et le couple de sortie
Nreduc = 36  # Coeficient de réduction
J = Jmotor + (m * (r**2) / Nreduc**2)  # Moment d'inertie total sur les roues
eps = 1
epsstall = 4


def integ(df, f0, T0):
    f = [f0]
    for i in df:
        f.append(f[-1] + i * T0)
    return (f[:-1])


def d(f):
    df = [(f[t + 1] - f[t]) / T0 for t in range(len(f) - 1)]
    df.append(df[-1])
    return (df)

# Approche réaliste de la réponse du habot (ordre 2) :


def f_(f, df, c, dc, k1, k2, k3):
    return (c + k3 * dc - k1 * df - f) / k2


def Euler(f_, f0, df0, t, c, k1, k2, k3):
    dc = d(c)
    f = [f0]
    df = df0
    d2f = f_(f0, df0, c[0], dc[0], k1, k2, k3)

    for k in range(len(t)):
        f.append(f[-1] + T0 * df)
        df += T0 * d2f
        d2f = f_(f[-1], df, c[k], dc[k], k1, k2, k3)
    return (f[:len(f) - 1])


def v_to_rv(v):
    return [k * (1 - eps / epsstall) for k in v]


def rv_to_cv(v, cv):
    return (v)

# Réponse du habot aux ordres (dans le cas idéal) et affichage graphique


def aff(xr, yr, xl, yl):
    if not (len(xr) == len(yr), len(yr) == len(xl), len(xl) == len(yl)):
        return ("Manque ou excès d'info sur les positions")
    fig = plt.figure()
    pl, = plt.plot([], [], 'bo')
    pr, = plt.plot([], [], 'ro')
    plt.ylim(min(min(yr), min(yl), min(xr), min(xl)) - 0.1, max(max(yr), max(yl), max(xr), max(xl)) + 0.1)
    plt.xlim(min(min(xr), min(xl), min(yr), min(yl)) - 0.1, max(max(xr), max(xl), max(yr), max(yl)) + 0.1)
    plt.gca().set_aspect('equal')
    metadata = dict(title='Anim', artist='Habot')
    writer = PillowWriter(fps=1 / T0, metadata=metadata)
    with writer.saving(fig, "Anim.gif", 100):
        for i in range(len(yr)):
            pl.set_data(xl[i], yl[i])
            pr.set_data(xr[i], yr[i])
            writer.grab_frame()


def mvt_habot(vr, vl, al, ar, t, real):
    plt.subplot(2, 1, 1)
    plt.plot(t, vr, "b")
    plt.subplot(2, 1, 2)
    plt.plot(t, vl, "b")
    cvr = vr[:]
    cvl = vl[:]
    if real == True:
        vr = v_to_rv(vr)
        vl = v_to_rv(vl)
        plt.subplot(2, 1, 1)
        plt.plot(t, vr, "r")
        plt.subplot(2, 1, 2)
        plt.plot(t, vl, "r")
    plt.show()
    if not (len(vr) == len(vl), len(vl) == len(t)):
        return ("Manque ou excès d'info sur les positions")
    l = range(len(vr))
    w = [(vl[k] - vr[k]) / L for k in l]
    a = integ(w, a0, T0)
    vx = [(vl[k] + vr[k]) * np.sin(a[k]) / 2 for k in l]
    vy = [(vl[k] + vr[k]) * np.cos(a[k]) / 2 for k in l]
    x = integ(vx, G0[0], T0)
    y = integ(vy, G0[1], T0)
    xr = [x[k] + np.cos(a[k]) * L / 2 for k in l]
    xl = [x[k] - np.cos(a[k]) * L / 2 for k in l]
    yr = [y[k] - np.sin(a[k]) * L / 2 for k in l]
    yl = [y[k] + np.sin(a[k]) * L / 2 for k in l]
    return (xr, yr, xl, yl, t)

# Calcul des consignes de vitesses de chaque roue à envoyer au habot


def gen_trap(a, v, l):
    tau = v / a
    T = abs(l / v)
    if T < tau:
        tau = abs(l / a)**(1 / 2)
        T = 0
    nbptpente = int(tau // T0)
    nbptplateau = int((T - tau) // T0)
    return ([a * l / abs(l) for k in range(nbptpente)] + [0 for k in range(nbptplateau)] + [-a * l / abs(l) for k in range(nbptpente)], nbptpente, nbptplateau)


def read_LIN(l, prc):
    al, nbptpente, nbptplateau = gen_trap(amax, vmax * prc, l)
    ar = al
    return ([al, ar, [k * T0 for k in range(len(al))]], nbptpente, nbptplateau)


def read_ROT(a, prc):
    a = a * (np.pi / 180)
    al, nbptpente, nbptplateau = gen_trap(amax, vmax * prc, a * L / 2)
    ar = [-k for k in al]
    return ([al, ar, [k * T0 for k in range(len(al))]], nbptpente, nbptplateau)


def read_CIR(r, a, prc):
    a = a * (np.pi / 180)
    if r >= 0:
        al, nbptpente, nbptplateau = gen_trap(amax, vmax * prc, a * (abs(r) + L / 2))
        ar = [k * (abs(r) - L / 2) / (abs(r) + L / 2) for k in al]
    else:
        ar, nbptpente, nbptplateau = gen_trap(amax, vmax * prc, a * (abs(r) + L / 2))
        al = [k * (abs(r) - L / 2) / (abs(r) + L / 2) for k in ar]
    if a != 0 and max(al) > amax or max(ar) > amax:
        print("L'accélération d'une des roues dépasse l'accélération maximale nominale")
        return ()
    return ([al, ar, [k * T0 for k in range(len(al))]], nbptpente, nbptplateau)


def read_BACK(x, y, xr, yr, xl, yl):
    ver = (yl - yr, xr - xl)
    bi = ((xr + xl) / 2, (yr + yl) / 2)
    vet = (bi[0] - x, bi[1] - y)
    ant = np.arctan2(vet[1], vet[0])
    anr = np.arctan2(ver[1], ver[0])
    a = np.pi - (ant - anr)
    l = np.linalg.norm(vet)
    ar = read_ROT(a * 180 / np.pi, 1)[1] + read_LIN(l, 1)[1]
    al = read_ROT(a * 180 / np.pi, 1)[0] + read_LIN(l, 1)[0]
    return (al, ar, [k * T0 for k in range(len(al))])


def overlap(A, B, p):
    for j in range(p):
        A[-j - 1] += B.pop(0)


def lis_chem(A):
    i = 0
    while i < len(A) - 1:
        if i + 1 < len(A) and A[i][0] == 'LIN' and A[i + 1][0] == 'LIN' and A[i][2] == A[i + 1][2]:
            a1 = A.pop(i)
            a2 = A.pop(i)
            A.insert(i, ['LIN', a1[1] + a2[1], a1[2]])
        elif i + 1 < len(A) and A[i][0] == 'ROT' and A[i + 1][0] == 'ROT' and A[i][2] == A[i + 1][2]:
            a1 = A.pop(i)
            a2 = A.pop(i)
            A.insert(i, ['ROT', a1[1] + a2[1], a1[2]])
        elif i + 1 < len(A) and A[i][0] == 'CIR' and A[i + 1][0] == 'CIR' and A[i][1] == A[i + 1][1] and A[i][3] == A[i + 1][3]:
            a1 = A.pop(i)
            a2 = A.pop(i)
            A.insert(i, ['CIR', a1[1], a1[2] + a2[2], a1[3]])
        else:
            i += 1
    for elmt in A:
        if elmt[0] == 'ROT':
            if elmt[1] >= 0:
                elmt[1] = elmt[1] % 360
            else:
                elmt[1] = -(abs(elmt[1]) % 360)
            if elmt[1] > 180:
                elmt[1] = elmt[1] - 360
        if elmt[0] == 'CIR':
            if elmt[2] >= 0:
                elmt[2] = elmt[2] % 360
            else:
                elmt[2] = -(abs(elmt[2]) % 360)


def chaine(A, lissage):
    if lissage:
        lis_chem(A)
        print("Chemin éffectué : ", A)
    al, ar = [], []
    nbptpente_, nbptplateau_ = 0, 0
    for i in A:
        if i[0] == 'LIN':
            s, nbptpente, nbptplateau = read_LIN(i[1], i[2])
        if i[0] == 'ROT':
            s, nbptpente, nbptplateau = read_ROT(i[1], i[2])
        if i[0] == 'CIR':
            s, nbptpente, nbptplateau = read_CIR(i[1], i[2], i[3])
        if i[0] == 'BACK':
            t = [k * T0 for k in range(len(ar))]
            mvt = mvt_habot(integ(ar, 0, T0), integ(al, 0, T0), ar, al, t, False)
            s = read_BACK(G0[0], G0[1], mvt[0][-1], mvt[1][-1], mvt[2][-1], mvt[3][-1])
        sl = [k for k in s[0]]
        sr = [k for k in s[1]]
        if lissage:
            overlap(al, sl, min(nbptpente, nbptpente_))
            overlap(ar, sr, min(nbptpente, nbptpente_))
        nbptpente_ = nbptpente
        nbptplateau_ = nbptplateau
        al.extend(sl)
        ar.extend(sr)
    t = [0]
    for i in range(len(ar) - 1):
        t.append(t[-1] + T0)
    return (al, ar, t)


def do(B, real, lissage):
    M = [[k for k in l] for l in B]
    al, ar, t = chaine(M, lissage)
    vl = integ(al, 0, T0)
    vr = integ(ar, 0, T0)
    xr, yr, xl, yl, t = mvt_habot(vr, vl, al, ar, t, real)
    aff(xr, yr, xl, yl)

# return [((vg,vr),t)]


def Pakstelle_to_Flobert(vg, vd):
    """Prend les vitessses des moteurs et les renvoie en consigne de vitesse avec dt"""
    dt = T0
    rep = [[[vg[0], vd[0]], dt]]
    for i in range(1, len(vg)):
        if rep[-1][0][0] == vg[i] and rep[-1][0][1] == vd[i]:
            rep[-1][1] += dt
        else:
            rep.append([[vg[i], vd[i]], dt])
    return rep

# Euler (f_, vr[0], ar[0], t, vr, (J*R/KT*KE), (J*L_/KT*KE), 0)


def get_trajectoire(instruction):
    """Format of input [[LIN|ROT|CIR|BACK, param1, param2, param3], ...]
    return [[[vg, vd], dt], ...]
    """
    al, ar, t = chaine(instruction, False)
    vl = integ(al, 0, T0)
    vr = integ(ar, 0, T0)
    result = Pakstelle_to_Flobert(vl, vr)
    result.append([[0, 0], T0])  # Stop
    return result


r = get_trajectoire([["LIN", -5, 1]])
