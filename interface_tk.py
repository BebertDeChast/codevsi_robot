from tkinter import *
import tkinter.font as tkfont
from math import sin, cos, pi
import numpy as np
from PIL import ImageTk, Image
from turtle import *
import trajectoire as traj
import communication as com
from math import atan



def initialisation_generale():

    initialisation_systeme_variable()
    initialisation_systeme_mise_en_page()
    remise_a_zero_pointeur()
    mise_a_jour_turtle()
    etat()


def initialisation_systeme_variable():
    global liste_des_mouvements
    global zoom
    global arc_sens
    global rot_sens
    global left
    global right
    global down
    global up
    global vitesse
    global Stop
    global lissage
    global Pilotage_live
    global T_live_s
    global T_live_ms
    T_live_ms=200
    T_live_s=T_live_ms/1000
    zoom = 1
    lissage=True
    liste_des_mouvements = []
    arc_sens = "droite"
    rot_sens = "droite"
    left = False
    right = False
    down = False
    up = False
    vitesse = 0
    Stop = False
    Pilotage_live=False


def initialisation_systeme_mise_en_page():

    # fenetre general
    global draw
    global curseur1
    global fenetre
    global bt_arc_GAUCHE
    global bt_valid_rec
    global bt_valid_rot
    global bt_valid_arc
    global bt_arc_DROITE
    global bt_rot_DROITE
    global bt_START
    global bt_START_LIVE
    global bt_STOP_LIVE
    global bt_STOP
    global bt_Left
    global bt_Down
    global bt_Right
    global bt_Up
    global liste
    global value_longueur_rec
    global value_vitesse_rec
    global value_angle_rot
    global value_vitesse_rot
    global value_angle_arc
    global value_rayon_arc
    global bt_START_LISS
    global bt_STOP_LISS
    global bt_rot_GAUCHE
    global bt_double
    fenetre = Tk()
    fenetre.title("TEST robot")
    ecran = Canvas(fenetre, width=800, height=750, bg="whitesmoke")
    ecran.pack(side=LEFT)
    Ima = Canvas(fenetre, width=700, height=750, bg="whitesmoke")
    Ima.pack(side=RIGHT)
    draw = RawTurtle(Ima)
    # affichage des traits
    ecran.create_line(400, 0, 400, 750, width=2)
    ecran.create_line(0, 375, 800, 375, width=2)
    ecran.create_line(533, 447, 533, 750, width=2)
    ecran.create_line(666, 447, 666, 750, width=2)
    ecran.create_line(400, 447, 800, 447, width=2)
    # affichage des labels
    gen_traj = Label(ecran, text="Genérateur de trajectoire", bg="dimgrey", width=55, height=4)
    gen_traj.place(x=404, y=378)
    # Affichage de la liste
    liste = Listbox(ecran, width=60, height=20)
    liste.place(x=18, y=25)
    # Partie rectiligne
    Rectiligne = Label(ecran, text="Rectiligne", bg="dimgrey", width=17)
    Rectiligne.place(x=404, y=450)
    value_longueur_rec = StringVar()
    value_longueur_rec.set("")
    value_vitesse_rec = StringVar()
    value_vitesse_rec.set("")
    long_rec = Label(ecran, text="longueur (cm)", bg="grey", width=17)
    long_rec.place(x=404, y=500)
    entree_long_rec = Entry(ecran, textvariable=value_longueur_rec, width=20)
    entree_long_rec.place(x=404, y=525)
    vit_rec = Label(ecran, text="vitesse (m/s)", bg="grey", width=17)
    vit_rec.place(x=404, y=550)
    entree_vit_rec = Entry(ecran, textvariable=value_vitesse_rec, width=20)
    entree_vit_rec.place(x=404, y=575)
    # Partie rotation
    Rotation = Label(ecran, text="Rotation", bg="dimgrey", width=17)
    Rotation.place(x=537, y=450)
    value_angle_rot = StringVar()
    value_angle_rot.set("")
    value_vitesse_rot = StringVar()
    value_vitesse_rot.set("")
    angle_rot = Label(ecran, text="angle (deg)", bg="grey", width=17)
    angle_rot.place(x=537, y=500)
    entree_angle_rot = Entry(ecran, textvariable=value_angle_rot, width=20)
    entree_angle_rot.place(x=537, y=525)
    vit_rec = Label(ecran, text="vitesse roues (m/s)", bg="grey", width=17)
    vit_rec.place(x=537, y=550)
    entree_vit_rot = Entry(ecran, textvariable=value_vitesse_rot, width=20)
    entree_vit_rot.place(x=537, y=575)
    # Partie arc de cercle
    Arc_de_cercle = Label(ecran, text="Arc de cercle", bg="dimgrey", width=17)
    Arc_de_cercle.place(x=670, y=450)
    value_angle_arc = StringVar()
    value_angle_arc.set("")
    value_rayon_arc = StringVar()
    value_rayon_arc.set("")
    entree_angle_arc = Entry(ecran, textvariable=value_angle_arc, width=20)
    entree_angle_arc.place(x=670, y=525)
    rayon_arc = Label(ecran, text="rayon (cm)", bg="grey", width=17)
    rayon_arc.place(x=670, y=550)
    entree_rayon_arc = Entry(ecran, textvariable=value_rayon_arc, width=20)
    entree_rayon_arc.place(x=670, y=575)
    angle_arc = Label(ecran, text="angle (deg)", bg="grey", width=17)
    angle_arc.place(x=670, y=500)
    # affichage curseur
    curseur1 = Scale(ecran, length=254, from_=100, to=0, tickinterval=100, sliderrelief='flat', highlightthickness=0, background='whitesmoke', troughcolor='#73B5FA', activebackground='#1065BF')
    curseur1.place(x=410, y=17, anchor=NW)
    curseur1.set(80)
    # les boutons
    bt_arc_GAUCHE = Button(ecran, text='gauche', fg="white", bg="darkolivegreen", command=lambda: arc_gauche())
    bt_arc_GAUCHE.config(width=16)
    bt_rot_GAUCHE = Button(ecran, text='gauche', fg="white", bg="darkolivegreen", command=lambda: rot_gauche())
    bt_rot_GAUCHE.config(width=16)
    bt_valid_rec = Button(ecran, text='generate', fg="white", bg="darkolivegreen", command=lambda: valid_rec())
    bt_valid_rec.config(width=16)
    bt_back = Button(ecran, text='back', fg="white", bg="darkolivegreen", command=lambda: valid_back())
    bt_back.config(width=16)
    bt_back.place(x=405, y=650, anchor=SW)
    bt_valid_rec.place(x=405, y=700, anchor=SW)
    bt_valid_rot = Button(ecran, text='generate', fg="white", bg="darkolivegreen", command=lambda: valid_rot())
    bt_valid_rot.config(width=16)
    bt_valid_rot.place(x=538, y=700, anchor=SW)
    bt_valid_arc = Button(ecran, text='generate', fg="white", bg="darkolivegreen", command=lambda: valid_arc())
    bt_valid_arc.config(width=16)
    bt_valid_arc.place(x=672, y=700, anchor=SW)
    bt_arc_DROITE = Button(ecran, text='droite', fg="white", bg="darkolivegreen", command=lambda: arc_droite())
    bt_arc_DROITE.config(width=16)
    bt_arc_DROITE.place(x=672, y=650, anchor=SW)
    bt_rot_DROITE = Button(ecran, text='droite', fg="white", bg="darkolivegreen", command=lambda: rot_droite())
    bt_rot_DROITE.config(width=16)
    bt_rot_DROITE.place(x=538, y=650, anchor=SW)
    bt_START = Button(ecran, text='START', fg="white", bg="darkolivegreen", command=lambda: start())
    bt_START.config(height=4, width=27)
    bt_START.place(x=402, y=375, anchor=SW)
    bt_START_LIVE = Button(ecran, text='PILOTAGE LIVE', fg="white", bg="darkolivegreen", command=lambda: start_live())
    bt_START_LIVE.config(height=4, width=27)
    bt_START_LIVE.place(x=601, y=375, anchor=SW)
    bt_STOP_LIVE = Button(ecran, text='STOP LIVE', fg="white", bg="red", command=lambda: stop_live())
    bt_STOP_LIVE.config(height=4, width=55)
    bt_START_LISS = Button(ecran, text='Lissage trajectoire activé', bg="yellow", command=lambda: stop_liss())
    bt_START_LISS.config(height=3, width=30)
    bt_START_LISS.place(x=10, y=444, anchor=SW)
    bt_double = Button(ecran, text='Double trajectoire', bg="yellow", command=lambda: double_tr())
    bt_double.config(height=3, width=30)
    bt_double.place(x=10, y=504, anchor=SW)
    bt_STOP_LISS = Button(ecran, text='Lissage trajectoire désactivé', bg="yellow", command=lambda: start_liss())
    bt_STOP_LISS.config(height=3, width=30)
    bt_STOP = Button(ecran, text='COMMUNICATION AVEC LE ROBOT EN COURS...', fg="white", bg="darkolivegreen")
    bt_STOP.config(height=4, width=55)

    bt_Left = Button(ecran, text='Left', fg="white", bg="darkolivegreen", state=NORMAL)
    bt_Left.config(width=9, height=4)
    bt_Left.place(x=520, y=250, anchor=SW)
    bt_Down = Button(ecran, text='Down', fg="white", bg="darkolivegreen")
    bt_Down.config(width=9, height=4)
    bt_Down.place(x=610, y=250, anchor=SW)
    bt_Right = Button(ecran, text='Right', fg="white", bg="darkolivegreen")
    bt_Right.config(width=9, height=4)
    bt_Right.place(x=700, y=250, anchor=SW)
    bt_Up = Button(ecran, text='Up', fg="white", bg="darkolivegreen")
    bt_Up.config(width=9, height=4)
    bt_Up.place(x=610, y=165, anchor=SW)
    # configuration cavier
    fenetre.bind("<Key>", push)
    fenetre.bind("<KeyRelease>", release)


def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def position_curseur():
    sel = liste.curselection()
    if len(sel) >= 1:
        return sel[0]
    return END


def valid_rot():
    vitesse = curseur1.get() /100
    global value_angle_rot
    global value_vitesse_rot
    if isNumeric(value_angle_rot.get()):
        if isNumeric(value_vitesse_rot.get()) and float(value_vitesse_rot.get())<=1 and float(value_vitesse_rot.get())>0:
            vitesse = float(value_vitesse_rot.get())
        else:
            vitesse = 1
        angle = float(value_angle_rot.get())
        pos = position_curseur()
        liste.insert(pos, f"Rotation {angle} deg à {vitesse*1.9}deg/s à {rot_sens}")

        if rot_sens == "gauche":
            angle = -angle
        if pos == END:
            tourne(float(angle), rot_sens)
            liste_des_mouvements.append(('rot', angle, vitesse))
        else:
            liste_des_mouvements.insert(pos, ('rot', angle, vitesse))
            mise_a_jour_turtle()
    (value_angle_rot).set("")
    (value_vitesse_rot).set("")


def valid_rec():
    vitesse = curseur1.get() /100
    global value_longueur_rec
    global value_vitesse_rec
    if isNumeric(value_longueur_rec.get()) :
        if isNumeric(value_vitesse_rec.get())and float(value_vitesse_rec.get())<=1 and float(value_vitesse_rec.get())>0:
            vitesse = float(value_vitesse_rec.get())
        pos = position_curseur()
        liste.insert(pos, f"Trajectoire rectiligne {value_longueur_rec.get()} cm à {vitesse}m/s")

        if pos == END:
            dessine_ligne(float(value_longueur_rec.get()))
            liste_des_mouvements.append(('rec', float(value_longueur_rec.get()), vitesse))
        else:
            liste_des_mouvements.insert(pos, ('rec', float(value_longueur_rec.get()), vitesse))
            mise_a_jour_turtle()
    (value_longueur_rec).set("")
    (value_vitesse_rec).set("")


def valid_arc():
    vitesse = curseur1.get() /100
    global value_angle_arc
    global value_rayon_arc
    if isNumeric(value_angle_arc.get()) and isNumeric(value_rayon_arc.get()):
        pos = position_curseur()
        liste.insert(pos, f"Arc de cercle de {value_angle_arc.get()} deg de rayon {value_rayon_arc.get()} cm à {arc_sens}")
        angle = float(f"{value_angle_arc.get()}")
        rayon = float(f"{value_rayon_arc.get()}")
        rayon_ = rayon
        if arc_sens == "gauche":
            rayon_ = -rayon
        if pos == END:
            dessine_arc_express(angle, rayon_)
            liste_des_mouvements.append(( rayon_, angle,vitesse))
        else:
            liste_des_mouvements.insert(pos, ( rayon_, angle,vitesse))
            mise_a_jour_turtle()
    (value_angle_arc).set("")
    (value_rayon_arc).set("")


def arc_gauche():
    bt_arc_GAUCHE.place_forget()
    global arc_sens
    arc_sens = "droite"
    bt_arc_DROITE.place(x=672, y=650, anchor=SW)


def arc_droite():
    global arc_sens
    arc_sens = "gauche"
    bt_arc_DROITE.place_forget()
    bt_arc_GAUCHE.place(x=672, y=650, anchor=SW)


def rot_gauche():
    bt_rot_GAUCHE.place_forget()
    global rot_sens
    rot_sens = "droite"
    bt_rot_DROITE.place(x=538, y=650, anchor=SW)


def rot_droite():
    global rot_sens
    rot_sens = "gauche"
    bt_rot_DROITE.place_forget()
    bt_rot_GAUCHE.place(x=538, y=650, anchor=SW)

def double_tr():
    global liste
    if len(liste_des_mouvements)>50:
        return None
    for k in range(len(liste_des_mouvements)):
        liste_des_mouvements.append(liste_des_mouvements[k])
        liste.insert(END,liste.get(k))
    mise_a_jour_turtle()
        
        
    
    
def start():
    global lissage
    instr = output_trajectoire()
    print("Liste des instructions : ")
    print(instr)
    if instr != []:
        fenetre.after(3000, stop)
        changebt()
        list_v = traj.get_trajectoire(instr,lissage=lissage)
        com.send_instruction(list_v)
        


def changebt():
    bt_START.place_forget()
    bt_START_LIVE.place_forget()
    bt_STOP.place(x=403, y=375, anchor=SW)


def stop():
    bt_START.place(x=401, y=375, anchor=SW)
    bt_STOP.place_forget()
    bt_START_LIVE.place(x=600, y=375, anchor=SW)


def start_live():
    global Pilotage_live
    Pilotage_live=True
    output_live()
    bt_START.place_forget()
    bt_START_LIVE.place_forget()
    bt_STOP_LIVE.place(x=403, y=375, anchor=SW)


def stop_live():
    global Pilotage_live
    Pilotage_live=False
    bt_START.place(x=401, y=375, anchor=SW)
    bt_STOP_LIVE.place_forget()
    bt_START_LIVE.place(x=600, y=375, anchor=SW)
    
def stop_liss():
    global lissage
    lissage=False
    bt_START_LISS.place_forget()
    bt_STOP_LISS.place(x=10, y=444, anchor=SW)


def start_liss():
    global lissage
    lissage=True
    bt_STOP_LISS.place_forget()
    bt_START_LISS.place(x=10, y=444, anchor=SW)

def valid_back():
    pos = position_curseur()
    if pos != END:
        a,b,c=liste_des_mouvements[pos-1]
        t,u,v=liste_des_mouvements[pos]
        if a=='back' or t=='back':
            return None
        liste.insert(pos, f"BACK")
        liste_des_mouvements.insert(pos, ('back', 'back', 'back'))
        mise_a_jour_turtle()
    else:
        a,b,c=liste_des_mouvements[-1]
        if a=='back':
            return None
        liste.insert(pos, f"BACK")
        liste_des_mouvements.append(('back', 'back', 'back'))
        dessine_back()
    
def dessine_back():
    x=draw.xcor()
    y=draw.ycor()
    if x>0:
        angle=atan(y/x)
    elif x<0:
        angle=atan(y/x)+pi
    elif y<0:
        angle=-pi
    elif y>0:
        angle=pi
    else :
        return None
    draw.setheading((angle+pi)*180/pi)
    l=(x**2+y**2)**0.5
    draw.forward(l / zoom)


        

    


def push(event):
    t = event.keysym
    global liste_des_mouvements
    global left
    global right
    global down
    global up
    if t == "Left":
        left = True
        bt_Left['state'] = DISABLED
    if t == "Right":
        right = True
        bt_Right['state'] = DISABLED
    if t == "Up":
        up = True
        bt_Up['state'] = DISABLED
    if t == "Down":
        down = True
        bt_Down['state'] = DISABLED
    if t == "z":
        a = curseur1.get() + 10
        if a < 100:
            curseur1.set(a)
        else:
            curseur1.set(100)
    if t == "s":
        a = curseur1.get() - 10
        if a >= 0:
            curseur1.set(a)
        else:
            curseur1.set(0)
    if t == "space":
        mise_a_jour_turtle()
        print(output_trajectoire())
    if t == "BackSpace":
        sel = liste.curselection()
        if len(sel) >= 1:
            liste.delete(sel[0])
            del liste_des_mouvements[sel[0]]
            mise_a_jour_turtle()
    if t == "a":
        print(draw.xcor())
        print(draw.ycor())
    if t == "r":
        fait_reset()


def fait_reset():
    global zoom
    global liste_des_mouvements
    global liste
    liste.delete(0, liste.size() - 1)
    liste_des_mouvements = []
    zoom = 1
    mise_a_jour_turtle()


def remise_a_zero_pointeur():
    global nb_left
    global nb_right
    global nb_up
    global nb_down
    nb_left = 0
    nb_right = 0
    nb_up = 0
    nb_down = 0


def creer_rec(l):
    if l == 0:
        return None
    vitesse = curseur1.get()/100
    liste_des_mouvements.append(('rec', l, vitesse))
    direction = 'avant'
    if l < 0:
        l = -l
        direction = 'arrière'
    liste.insert(END, f"Trajectoire rectiligne {int(l)} cm à {vitesse} m/s en {direction}")
    remise_a_zero_pointeur()


def creer_arc(rayon, angle):
    vitesse = curseur1.get() /100
    if angle == 0:
        return None
    sens = 'droite'
    direction = 'avant'
    liste_des_mouvements.append((rayon, angle, vitesse))
    if rayon < 0:
        rayon = -rayon
        sens = 'gauche'
    if angle < 0:
        angle = -angle
        direction = 'arrière'
    liste.insert(END, f"Arc de cercle de {int(angle)} deg de rayon {int(rayon)} cm à {sens} en {direction}")
    remise_a_zero_pointeur()


def creer_rotation(angle):
    vitesse = curseur1.get() /100
    if angle == 0:
        return None
    sens = 'droite'

    liste_des_mouvements.append(('rot', angle, vitesse))
    if angle < 0:
        angle = -angle
        sens = 'gauche'
    liste.insert(END, f"Rotation {int(angle)} rad à {int(vitesse*190)} deg/s à {sens}")
    remise_a_zero_pointeur()


def valid_left():
    global left
    global right
    global Stop
    if Stop:
        return False
    return (left and (not right) and (not down)) or (right and (not left) and down)


def valid_right():
    global left
    global right
    global Stop
    if Stop:
        return False
    return (right and (not left) and (not down)) or (left and (not right) and down)


def valid_up():
    global up
    global down
    global Stop
    if Stop:
        return False
    return up and not down


def valid_down():
    global up
    global down
    global Stop
    if Stop:
        return False
    return down and not up


def inadequation_left_plus():
    global nb_left
    return not valid_left() and nb_left != 0


def inadequation_right_plus():
    global nb_right
    return not valid_right() and nb_right != 0


def inadequation_up_plus():
    global nb_up
    return not valid_up() and nb_up != 0


def inadequation_down_plus():
    global nb_down
    return not valid_down() and nb_down != 0


def inadequation_left_moins():
    global nb_left
    global nb_up
    global nb_down
    return valid_left() and nb_left == 0 and (nb_up != 0 or nb_down != 0)


def inadequation_right_moins():
    global nb_right
    global nb_up
    global nb_down
    return valid_right() and nb_right == 0 and (nb_up != 0 or nb_down != 0)


def inadequation_up_moins():
    global nb_up
    global nb_left
    global nb_right
    return valid_up() and nb_up == 0 and (nb_left != 0 or nb_right != 0)


def inadequation_down_moins():
    global nb_down
    global nb_left
    global nb_right
    return valid_down() and nb_down == 0 and (nb_left != 0 or nb_right != 0)


def head_adequation():
    global nb_left
    global nb_right
    global nb_up
    global nb_down
    if inadequation_left_plus():
        if nb_up != 0:
            creer_arc(-360 * nb_up / nb_left / 2 / pi, nb_left)
        elif nb_down != 0:
            creer_arc(360 * nb_down / nb_left / 2 / pi, -nb_left)
        else:
            creer_rotation(-nb_left)
    if inadequation_right_plus():
        if nb_down != 0:
            creer_arc(-360 * nb_down / nb_right / 2 / pi, -nb_right)
        elif nb_up != 0:
            creer_arc(360 * nb_up / nb_right / 2 / pi, nb_right)
        else:
            creer_rotation(nb_right)
    if inadequation_up_plus():
        if nb_left != 0:
            creer_arc(-360 * nb_up / nb_left / 2 / pi, nb_left)
        if nb_right != 0:
            creer_arc(360 * nb_up / nb_right / 2 / pi, nb_right)
        else:
            creer_rec(nb_up)
    if inadequation_down_plus():
        if nb_right != 0:
            creer_arc(-360 * nb_down / nb_right / 2 / pi, -nb_right)
        if nb_left != 0:
            creer_arc(360 * nb_down / nb_left / 2 / pi, -nb_left)
        else:
            creer_rec(-nb_down)
    if inadequation_left_moins() or inadequation_right_moins() or inadequation_up_moins() or inadequation_down_moins():
        if nb_left != 0:
            creer_rotation(-nb_left)
        if nb_right != 0:
            creer_rotation(nb_right)
        if nb_up != 0:
            creer_rec(nb_up)
        if nb_down != 0:
            creer_rec(-nb_down)


def reglage_zoom():
    global zoom
    global Stop
    if draw.xcor() < -300 or draw.xcor() > 300 or draw.ycor() < -300 or draw.ycor() > 300:
        zoom *= 2
        Stop = True
        head_adequation()
        mise_a_jour_turtle()
        Stop = False


def head_mouvement():
    global vitesse
    global zoom
    global nb_left
    global nb_right
    global nb_up
    global nb_down
    if valid_up():
        nb_up += vitesse / 25.4
        draw.forward(vitesse / 25.4 / zoom)
    if valid_down():
        nb_down += vitesse / 25.4
        draw.forward(-vitesse / 25.4 / zoom)
    if valid_left():
        nb_left += 4
        draw.left(4)
    if valid_right():
        nb_right += 4
        draw.right(4)


def etat():
    global vitesse
    global nb_left
    global nb_right
    global nb_up
    global nb_down
    if nb_left == 0 and nb_right == 0 and nb_up == 0 and nb_down == 0:
        vitesse = curseur1.get()
    if not Pilotage_live:
        head_adequation()
        head_mouvement()
        reglage_zoom()
    fenetre.after(50, etat)


def release(event):
    global left
    global right
    global down
    global up
    t = event.keysym
    if t == "Left":
        left = False
        bt_Left['state'] = NORMAL
    if t == "Right":
        right = False
        bt_Right['state'] = NORMAL
    if t == "Up":
        up = False
        bt_Up['state'] = NORMAL
    if t == "Down":
        down = False
        bt_Down['state'] = NORMAL


def tourne(r, direction):
    if direction == "gauche":
        draw.left(r)
    else:
        draw.right(r)


def dessine_arc_express(angle, rayon):
    global zoom
    draw.circle(-rayon / zoom, angle)


def dessine_ligne(l):
    global zoom
    draw.forward(l / zoom)


def mise_a_jour_turtle():
    draw.clear()
    draw.penup()
    draw.setx(00)
    draw.sety(0)
    draw.pendown()
    draw.setheading(90)
    for x, y, z in liste_des_mouvements:
        if x == 'rec':
            dessine_ligne(y)
        elif x == 'rot':
            draw.right(y)
        elif isNumeric(x):
            rayon = x
            angle = y
            dessine_arc_express(angle, rayon)
        elif x=='back':
            dessine_back()


def output_trajectoire():

    out = []
    traduction = {'rec': 'LIN', 'rot': 'ROT','back':'back'}
    for k in liste_des_mouvements:
        x1, y1, z1 = k
        if isNumeric(x1):
            x2 = x1 / 100
            y2 = y1
            z2=100*z1
            out.append(['CIR', x2, y2, z2])
        else:
            x2 = traduction[x1]
            if x1 == 'rec':
                y2 = y1 / 100
                z2 = 100 * z1
                out.append([x2, y2, z2])

            if x1 == 'rot':
                y2 = y1
                z2 = z1 * 100
                out.append([x2, y2, z2])
            if x1=='back':
                out.append(["BACK"])
    return out

def output_live():
    global T_live_ms
    if valid_up():
        if valid_left():
            ext_output_live(0.5,1)
        elif valid_right():
            ext_output_live(1,0.5)
        else:
            ext_output_live(1,1)
    elif valid_down():
        if valid_left():
            ext_output_live(-0.5,-1)
        elif valid_right():
            ext_output_live(-1,-0.5)
        else:
            ext_output_live(-1,-1)
    elif valid_left():
        ext_output_live(-1,1)
    elif valid_right():
        ext_output_live(1,-1)
    if Pilotage_live:
        fenetre.after(T_live_ms, output_live)

def ext_output_live(v1,v2):
    global T_live_s
    global vitesse
    vmax=traj.vmax *vitesse/100
    r=traj.r
    list_v=[[[vmax*v1/r,vmax*v2/r],T_live_s]]
    com.send_instruction(list_v)


def main():
    initialisation_generale()
    fenetre.mainloop()
