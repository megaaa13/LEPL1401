from graphics import *  # une bibliothèque pour dessiner des figures simple sur un plan XY
import math  # nous avoins besoin des fonctions cos et sin pour notre calcul de la position d'un point
from Robot import Robot


class XYRobot(Robot):

    def __init__(self, n):
        super().__init__(n)
        self.__win = GraphWin()

    def __drawFrom(self, oldx, oldy):
        line = Line(Point(oldx, oldy), Point(self.getx(), self.gety()))
        line.draw(self.__win)

    def __turn(self, direction):
        self.set_angle(self.getanglerad() + direction * math.pi / 2)
        self.history.insert(0, ("left" if direction < 0 else "right", direction * 90))

    def __move(self, distance, sense):
        oldx = self.getx()
        oldy = self.gety()
        orientationx = math.cos(self.getanglerad())
        orientationy = math.sin(self.getanglerad())
        self.setx(oldx + orientationx * distance * sense)
        self.sety(oldy + orientationy * distance * sense)
        self.__drawFrom(oldx, oldy)

    def moveforward(self, distance):
        self.__move(distance, 1)
        self.history.insert(0, ("forward", distance))

    def movebackward(self, distance):
        self.__move(distance, -1)
        self.history.insert(0, ("backward", distance))

    def turnright(self):
        self.__turn(1)

    def turnleft(self):
        self.__turn(-1)


# Exemple d'utilisation de cette classe (il suffit d'exécuter ce fichier)
if __name__ == '__main__':
    r2d2 = XYRobot("R2-D2")

    # first move to position (100,100) facing East, to be more or less in the center of the window
    r2d2.moveforward(100)
    r2d2.turnright()
    r2d2.moveforward(100)
    r2d2.turnleft()

    print(r2d2)
    # R2-D2@(100, 100) angle: 0.0
    r2d2.moveforward(50)
    print(r2d2)
    r2d2.turnleft()
    # R2-D2@(150, 100) angle: 270.0
    r2d2.moveforward(50)
    r2d2.turnleft()
    print(r2d2)
    # R2-D2@(150.0, 50.0) angle: 180.0
    r2d2.moveforward(50)
    r2d2.turnleft()
    print(r2d2)
    # R2-D2@(100.0, 50.0) angle: 90.0
    r2d2.moveforward(50)
    print(r2d2)
    # R2-D2@(100, 100) angle: 90.0
    r2d2.moveforward(50)
    r2d2.turnright()
    print(r2d2)
    r2d2.moveforward(50)
    r2d2.turnright()
    print(r2d2)
    r2d2.moveforward(50)
    r2d2.turnright()
    print(r2d2)
    r2d2.moveforward(50)
    r2d2.turnright()
    print(r2d2)
