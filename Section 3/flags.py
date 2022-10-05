import turtle
import math
from tkinter import colorchooser

# ------------------------------------------------------------------------------------- #
#  Turtle and window creation
caroline = turtle.Turtle()
ws = turtle.Screen()
ws.title("People with flags")
caroline.resizemode()
caroline.speed(0)
caroline.hideturtle()
caroline.penup()
ws.bgcolor("lightblue")
caroline.setx(-420)
caroline.sety(250)
turtle.tracer(0, 0)
ws.setup(1500, 700)
# ------------------------------------------------------------------------------------- #


def rectangle(width: float, height: float, color: str, t):
    """pre : width > 0, height > 0, color = color or hexadecimal, t = turtle object
    \n post : dessine un rectangle"""
    t.color(color)
    t.begin_fill()
    for i in range(2):  # Dessine le rectangle en 2 fois : Longueur + hauteur puis se répète
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


def star(width: float, color: str, t):
    """pre : width > 0, color = color or hexadecimal, t = turtle object
    \n post : dessine une étoile à 5 branches"""
    t.color(color)
    coorx = t.xcor()  # Permet de positionner les étoiles sur un cercle, passant par leur centre
    coory = t.ycor()
    t.setx(t.xcor() - width / 2)
    t.begin_fill()
    t.setheading(0)
    for i in range(5):
        t.forward(width)
        t.right(144)
    t.end_fill()
    setpos(coorx, coory, t)  # Recentre la tortue sur sa position avant la création de l'étoile


def square(size: float, color: str, t):
    """pre : size > 0 color = color or hexadecimal, t = turtle object
    \n post : dessine un carré"""
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()


def belgian_flag(width, t):
    """pre : width > 0, t = turtle object
    \n post : dessine un drapeau belge"""
    for i in ["#000000", "#FFE936", "#FF0F21"]:
        rectangle(width / 2, width, i, caroline)
        t.forward(width / 2)


def three_color_flag(width, color1, color2, color3, t):
    """pre : width > 0, color1, color2, color3 = color or hexadecimal, t = turtle object
    \n post : dessine un drapeau vertical tricolore"""
    for i in [color1, color2, color3]:
        rectangle(width / 2, width, i, caroline)
        t.forward(width / 2)


def three_color_flag_hor(width, color1, color2, color3, t):
    """pre : width > 0, color1, color2, color3 = color or hexadecimal, t = turtle object
    \n post : dessine un drapeau horizontal tricolore"""
    for i in [color1, color2, color3]:
        rectangle(width / 2 * 3, width / 3, i, caroline)
        t.right(90)
        t.forward(width / 3)
        t.left(90)
    t.forward(width / 2 * 3)  # Repositionne la tortue correctement pour que les rectangles soient correctement placés
    t.left(90)
    t.forward(width)


def danemark_flag(width: float, t):
    """pre : width > 0, t = turtle object
    \n post : dessine le drapeau du Danemark"""
    rectangle(width / 2 * 3, width, "#C7042C", t)
    t.forward(width / 2 * 3 / 7 * 2)
    rectangle(width / 2 * 3 / 7, width, "#FFFFFF", t)
    t.backward(width / 2 * 3 / 7 * 2)
    t.right(90)
    t.forward(width / 7 * 3)
    t.left(90)
    rectangle(width / 2 * 3, width / 7, "#FFFFFF", t)
    t.left(90)
    t.forward(width / 7 * 3)
    t.right(90)
    t.forward(width / 2 * 3)


def european_flag(width: float, t):
    """pre : width > 0, t = turtle object
    \n post : dessine le drapeeau européen"""
    t.setheading(0)
    rectangle(width / 2 * 3, width, "#003399", caroline)
    t.setx(t.xcor() + width // 4 * 3)
    t.sety(t.ycor() - width // 6)
    for i in range(12):  # Positionne les étoiles sur un "cercle" (dodécagone régulier)
        star(width=width // 8 - width / 60, color="#FFCC00", t=caroline)
        t.right(30 * i + 15)  # Permet de centrer les étoiles aux heures d'une horloge
        t.forward((width - 2 * width // 6) * math.pi / 12)


def fan(t, width):  # Crée un stickman auquel on ajoutera un drapeau
    """pre : width > 0, t = turtle object
    \n post : dessine un stickman tenant un mât de drapeau"""
    t.pensize(4)
    t.color("black")
    t.setheading(0)
    t.down()
    t.circle(width // 4)
    t.right(90)
    t.forward(width // 5)
    tx = t.xcor()
    ty = t.ycor()
    t.left(10)
    t.forward(width // 2)
    t.right(20)
    t.forward(width // 2)
    t2x = t.xcor()
    t2y = t.ycor()
    t.right(20)
    t.forward(width // 3)
    t.left(60)
    t.forward(width // 3)
    t.right(75)
    t.forward(width // 3)
    setpos(t2x, t2y, t)
    t.setheading(0)
    t.down()
    t.right(70)
    t.forward(width // 3)
    t.left(30)
    t.forward(width // 3)
    t.right(80)
    t.forward(width // 5)
    setpos(tx, ty, t)
    t.down()
    t.setheading(200)
    t.forward(width // 2)
    t.left(50)
    t.forward((width // 3) + (width // 8))
    setpos(tx, ty, t)
    t.down()
    t.left(10)
    t.forward(width // 2)
    t.right(70)
    t.forward((width // 3) + (width // 6))
    t.setheading(45)
    t.pensize(6)
    t.color("brown")
    t.forward(width * 2)
    t.right(90)
    t.up()


def setpos(x, y, t):  # Fonction permettant d'éviter à avoir à répéter un set de position en 3 lignes au lieu d'une
    """pre : x, y quelconques, t = turtle object
    \n post : repositionne la tortue en des coordonnées définies"""
    t.up()
    t.setx(x)
    t.sety(y)


def main(t):  # Coeur du code, tout s'exécute à travers elle
    """pre : t = turtle object
        \n post : exécute l'entièreté du code, et dessine des stickmans autour d'un drapeau européen"""
    choix = True
    sens = 'e'
    while choix:
        sens = turtle.textinput("Drapeau custom ?", "vertical, horizontal ou non ?")
        sens = sens.lower() if type(sens) == str else None
        if sens == "vertical" or sens == "horizontal" or sens == "non":
            choix = False
        else:
            choix = True
    if sens != "non":  # Si l'utilisateur ne veut pas un drapeau customisé, le code imprimera un drapeau russe
        clr1 = colorchooser.askcolor(title="Select 1st color")
        if type(clr1[1]) != str:
            clr1 = ["", "red"]
        clr2 = colorchooser.askcolor(title="Select 2th color")
        if type(clr2[1]) != str:
            clr2 = ["", "green"]
        clr3 = colorchooser.askcolor(title="Select 3th color")
        if type(clr3[1]) != str:
            clr3 = ["", "blue"]
    fan(t, 100)
    three_color_flag_hor(66, "#000000", "#FF0000", "#FFCC00", t)
    x = t.xcor()
    y = t.ycor()
    setpos(x + 50, y + 7, t)
    fan(t, 100)
    three_color_flag_hor(66, "#C73F4A", "#FFFFFF", "#0089B6", t)
    x = t.xcor()
    y = t.ycor()
    setpos(x + 50, y + 7, t)
    fan(t, 100)
    belgian_flag(66, t)
    x = t.xcor()
    y = t.ycor()
    setpos(x + 50, y + 7, t)
    fan(t, 100)
    three_color_flag_hor(66, "#A91B27", "#F7F7F7", "#204487", t)
    x = t.xcor()
    y = t.ycor()
    setpos(x + 50, y + 7, t)
    fan(t, 100)
    three_color_flag(66, "#051440", "#FFFFFF", "#EC1920", t)
    setpos(-650, -100, t)
    fan(t, 100)
    three_color_flag(66, "#009246", "#F1F2F1", "#CE2B37", t)
    x = t.xcor()
    y = t.ycor()
    setpos(x + 50, y + 7, t)
    fan(t, 100)
    three_color_flag(66, "#169B62", "#FFFFFF", "#FF883E", t)
    setpos(310, -100, t)
    fan(t, 100)
    danemark_flag(66, t)
    x = t.xcor()
    y = t.ycor()
    setpos(x + 50, y + 7, t)
    fan(t, 100)
    if sens == "vertical":
        three_color_flag(66, clr1[1], clr2[1], clr3[1], t)
    elif sens == "horizontal":
        three_color_flag_hor(66, clr1[1], clr2[1], clr3[1], t)
    else:
        three_color_flag_hor(66, "#FFFFFF", "#0039A6", "#D52B1E", t)
    setpos(-240, 0, t)
    european_flag(300, t)
    t.color("black")
    setpos(-240, -312, t)
    t.write("Stickman conceived on paper by B. Masureel", font=("Comic Sans MS", 7, "normal"))
    if sens != "non":
        setpos(470, -340, t)
        t.write("Custom flag\n(made by user)", font=("Comic Sans MS", 12, "bold"))


main(caroline)
ws.mainloop()
