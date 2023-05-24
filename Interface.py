from tkinter import *
import tkinter.font as tkfont
from math import sin, cos, pi
import numpy as np
from PIL import ImageTk, Image
from turtle import *


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
    zoom = 1
    liste_des_mouvements = []
    arc_sens = "droite"
    rot_sens = "droite"
    left = False
    right = False
    down = False
    up = False
    vitesse = 0
    Stop = False


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
    global bt_RESTART
    global bt_STOP
    global bt_GO
    global bt_Left
    global bt_Down
    global bt_Right
    global bt_Up
    global liste
    fenetre = Tk()
    fenetre.title("TEST robot")
    ecran = Canvas(fenetre, width=800, height=750, bg="grey")
    ecran.pack(side=LEFT)
    Ima = Canvas(fenetre, width=700, height=750, bg="blue")
    Ima.pack(side=RIGHT)
    draw = RawTurtle(Ima)
    # affichage des traits
    ecran.create_line(400, 0, 400, 750, width=2)
    ecran.create_line(0, 375, 800, 375, width=2)
    ecran.create_line(533, 447, 533, 750, width=2)
    ecran.create_line(666, 447, 666, 750, width=2)
    ecran.create_line(400, 447, 800, 447, width=2)
    # affichage des labels
    gen_traj = Label(ecran, text="Genérateur de trajectoire", bg="white", width=55, height=4)
    gen_traj.place(x=404, y=378)
    # Affichage de la liste
    liste = Listbox(ecran, width=60, height=20)
    liste.place(x=18, y=25)
    # Partie rectiligne
    Rectiligne = Label(ecran, text="Rectiligne", bg="white", width=17)
    Rectiligne.place(x=404, y=450)
    value_longueur_rec = StringVar()
    value_longueur_rec.set("")
    value_vitesse_rec = StringVar()
    value_vitesse_rec.set("")
    long_rec = Label(ecran, text="longueur", bg="white", width=17)
    long_rec.place(x=404, y=500)
    entree_long_rec = Entry(ecran, textvariable=value_longueur_rec, width=20)
    entree_long_rec.place(x=404, y=525)
    vit_rec = Label(ecran, text="vitesse", bg="white", width=17)
    vit_rec.place(x=404, y=550)
    entree_vit_rec = Entry(ecran, textvariable=value_vitesse_rec, width=20)
    entree_vit_rec.place(x=404, y=575)
    # Partie rotation
    Rotation = Label(ecran, text="Rotation", bg="white", width=17)
    Rotation.place(x=537, y=450)
    value_angle_rot = StringVar()
    value_angle_rot.set("")
    value_vitesse_rot = StringVar()
    value_vitesse_rot.set("")
    angle_rot = Label(ecran, text="angle", bg="white", width=17)
    angle_rot.place(x=537, y=500)
    entree_angle_rot = Entry(ecran, textvariable=value_angle_rot, width=20)
    entree_angle_rot.place(x=537, y=525)
    vit_rec = Label(ecran, text="vitesse", bg="white", width=17)
    vit_rec.place(x=537, y=550)
    entree_vit_rot = Entry(ecran, textvariable=value_vitesse_rot, width=20)
    entree_vit_rot.place(x=537, y=575)
    # Partie arc de cercle
    Arc_de_cercle = Label(ecran, text="Arc de cercle", bg="white", width=17)
    Arc_de_cercle.place(x=670, y=450)
    value_angle_arc = StringVar()
    value_angle_arc.set("")
    value_rayon_arc = StringVar()
    value_rayon_arc.set("")
    entree_angle_arc = Entry(ecran, textvariable=value_angle_arc, width=20)
    entree_angle_arc.place(x=670, y=525)
    rayon_arc = Label(ecran, text="rayon", bg="white", width=17)
    rayon_arc.place(x=670, y=550)
    entree_rayon_arc = Entry(ecran, textvariable=value_rayon_arc, width=20)
    entree_rayon_arc.place(x=670, y=575)
    angle_arc = Label(ecran, text="angle", bg="white", width=17)
    angle_arc.place(x=670, y=500)
    # affichage curseur
    curseur1 = Scale(ecran, length=254, from_=254, to=0, tickinterval=100, sliderrelief='flat', highlightthickness=0, background='grey', fg='white', troughcolor='#73B5FA', activebackground='#1065BF')
    curseur1.place(x=410, y=17, anchor=NW)
    curseur1.set(254)
    # les boutons
    bt_arc_GAUCHE = Button(ecran, text='gauche', fg="white", bg="green", command=lambda: arc_gauche())
    bt_arc_GAUCHE.config(width=16)
    bt_rot_GAUCHE = Button(ecran, text='gauche', fg="white", bg="green", command=lambda: rot_gauche())
    bt_rot_GAUCHE.config(width=16)
    bt_valid_rec = Button(ecran, text='generate', fg="white", bg="green", command=lambda: valid_rec())
    bt_valid_rec.config(width=16)
    bt_valid_rec.place(x=405, y=700, anchor=SW)
    bt_valid_rot = Button(ecran, text='generate', fg="white", bg="green", command=lambda: valid_rot())
    bt_valid_rot.config(width=16)
    bt_valid_rot.place(x=538, y=700, anchor=SW)
    bt_valid_arc = Button(ecran, text='generate', fg="white", bg="green", command=lambda: valid_arc())
    bt_valid_arc.config(width=16)
    bt_valid_arc.place(x=672, y=700, anchor=SW)
    bt_arc_DROITE = Button(ecran, text='droite', fg="white", bg="green", command=lambda: arc_droite())
    bt_arc_DROITE.config(width=16)
    bt_arc_DROITE.place(x=672, y=650, anchor=SW)
    bt_rot_DROITE = Button(ecran, text='droite', fg="white", bg="green", command=lambda: rot_droite())
    bt_rot_DROITE.config(width=16)
    bt_rot_DROITE.place(x=538, y=650, anchor=SW)
    bt_START = Button(ecran, text='START', fg="white", bg="green", command=lambda: start())
    bt_START.config(height=4, width=55)
    bt_START.place(x=403, y=375, anchor=SW)
    bt_RESTART = Button(ecran, text='RESET', fg="white", bg="green", command=lambda: reset())
    bt_RESTART.config(height=4, width=27)
    bt_STOP = Button(ecran, text='STOP', fg="white", bg="green", command=lambda: stop())
    bt_STOP.config(height=4, width=55)
    bt_GO = Button(ecran, text='GO', fg="white", bg="green", command=lambda: go())
    bt_GO.config(height=4, width=27)
    bt_Left = Button(ecran, text='Left', fg="white", bg="green", state=NORMAL)
    bt_Left.config(width=9, height=4)
    bt_Left.place(x=520, y=250, anchor=SW)
    bt_Down = Button(ecran, text='Down', fg="white", bg="green")
    bt_Down.config(width=9, height=4)
    bt_Down.place(x=610, y=250, anchor=SW)
    bt_Right = Button(ecran, text='Right', fg="white", bg="green")
    bt_Right.config(width=9, height=4)
    bt_Right.place(x=700, y=250, anchor=SW)
    bt_Up = Button(ecran, text='Up', fg="white", bg="green")
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
    if isNumeric(value_angle_rot.get()):
        if isNumeric(value_vitesse_rot.get()):
            vitesse = float(value_vitesse_rot.get())
        else:
            vitesse = 1
        angle = float(value_angle_rot.get())
        pos = position_curseur()
        liste.insert(pos, f"Rotation {angle} rad à {vitesse}degre/s à {rot_sens}")

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
    if isNumeric(value_longueur_rec.get()):
        if isNumeric(value_vitesse_rec.get()):
            vitesse = float(value_vitesse_rec.get())
        else:
            vitesse = 1
        pos = position_curseur()
        liste.insert(pos, f"Trajectoire rectiligne {value_longueur_rec.get()} cm à {vitesse}m/s")

        if pos == END:
            dessine_ligne(float(value_longueur_rec.get()))
            liste_des_mouvements.append(('rec', value_longueur_rec.get(), vitesse))
        else:
            liste_des_mouvements.insert(pos, ('rec', float(value_longueur_rec.get()), vitesse))
            mise_a_jour_turtle()
        (value_longueur_rec).set("")
        (value_vitesse_rec).set("")


def valid_arc():
    if isNumeric(value_angle_arc.get()) and isNumeric(value_rayon_arc.get()):
        pos = position_curseur()
        liste.insert(pos, f"Arc de cercle de {value_angle_arc.get()} rad de rayon {value_rayon_arc.get()} cm à {arc_sens}")
        angle = float(f"{value_angle_arc.get()}")
        rayon = float(f"{value_rayon_arc.get()}")
        rayon_ = rayon
        if arc_sens == "gauche":
            rayon_ = -rayon
        if pos == END:
            dessine_arc(angle, rayon, arc_sens)
            liste_des_mouvements.append(('arc', rayon_, angle))
        else:
            liste_des_mouvements.insert(pos, ('arc', rayon_, angle))
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


def start():
    changebt()
    print(curseur1.get())


def changebt():
    bt_START.place_forget()
    bt_STOP.place(x=401, y=375, anchor=SW)


def reset():
    bt_START.place(x=401, y=375, anchor=SW)
    bt_STOP.place_forget()
    bt_RESTART.place_forget()
    bt_GO.place_forget()


def stop():
    bt_STOP.place_forget()
    bt_GO.place(x=401, y=375, anchor=SW)
    bt_RESTART.place(x=600, y=375, anchor=SW)


def go():
    bt_GO.place_forget()
    bt_STOP.place(x=401, y=375, anchor=SW)


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
        if a < 255:
            curseur1.set(a)
        else:
            curseur1.set(254)
    if t == "s":
        a = curseur1.get() - 10
        if a >= 0:
            curseur1.set(a)
        else:
            curseur1.set(0)
    if t == "space":
        mise_a_jour_turtle()
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
        liste.delete(0, liste.size() - 1)
        liste_des_mouvements = []
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
    liste_des_mouvements.append(('rec', l, 1))
    direction = 'avant'
    if l < 0:
        l = -l
        direction = 'arrière'
    liste.insert(END, f"Trajectoire rectiligne {l} cm à {1} m/s en {direction}")
    remise_a_zero_pointeur()


def creer_arc(rayon, angle):
    if angle == 0:
        return None
    sens = 'droite'
    direction = 'avant'
    liste_des_mouvements.append(('arc', rayon, angle))
    if rayon < 0:
        rayon = -rayon
        sens = 'gauche'
    if angle < 0:
        angle = -angle
        direction = 'arrière'
    liste.insert(END, f"Arc de cercle de {angle} degre de rayon {rayon} cm à {sens} en {direction}")
    remise_a_zero_pointeur()


def creer_rotation(angle):
    if angle == 0:
        return None
    sens = 'droite'
    liste_des_mouvements.append(('rot', angle, 1))
    if angle < 0:
        angle = -angle
        sens = 'gauche'
    liste.insert(END, f"Rotation {angle} rad à 1 degre/s à {sens}")
    remise_a_zero_pointeur()


def valid_left():
    global left
    global right
    global Stop
    if Stop:
        return False
    return left and not right


def valid_right():
    global left
    global right
    global Stop
    if Stop:
        return False
    return right and not left


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
    draw.sety(-200)
    draw.pendown()
    draw.setheading(90)
    for x, y, z in liste_des_mouvements:
        if x == 'rec':
            dessine_ligne(y)
        elif x == 'rot':
            draw.right(y)
        elif x == 'arc':
            rayon = y
            angle = z
            dessine_arc_express(angle, rayon)
def output_trajectoire():
    out=[]
    traduction={'rec':'LIN','arc':'CIR','rot':'ROT'}
    for k in liste_des_mouvements:
        x1,y1,z1=k
        x2=traduction[x1]
        if x1=='rec':
            y2=y1/100
            z2=100*z1
        if x1=='arc':
            y2=y1/100
            z2=z1
        if x1=='rot':
            y2=y1
            z2=z1*100
        out.append((x2,y2,z2))
    return out

initialisation_generale()

fenetre.mainloop()
