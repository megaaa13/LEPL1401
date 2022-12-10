import turtle
import math
from Robot import Robot

turtle.tracer(0, 0)


class TurtleBot(Robot):

    def __init__(self, n):
        super().__init__(n)
        self.__t = turtle.Turtle()
        self.__win = turtle.Screen()
        self.__t.speed(3)

    def t(self):
        return self.__t

    def __travel(self, distance, sense):
        if sense == 1:
            self.t().forward(distance)
            self.history.insert(0, ("forward", distance))
        elif sense == -1:
            self.t().backward(distance)
            self.history.insert(0, ("backward", distance))

    def __move(self, distance, sense):
        self.setx(self.getx() + distance * sense * math.cos(self.getanglerad()))
        self.sety(self.gety() + distance * sense * math.sin(self.getanglerad()))

    def moveforward(self, distance):
        self.__move(distance, 1)
        self.__travel(distance, 1)

    def movebackward(self, distance):
        self.__move(distance, -1)
        self.__travel(distance, -1)

    def resetangle(self):
        self.t().setheading(0)

    def turnright(self):
        self.__turn(1)

    def turnleft(self):
        self.__turn(-1)

    def __turn(self, direction):
        self.set_angle(self.getanglerad() + direction * math.pi / 2)
        self.history.insert(0, ("left" if direction < 0 else "right", direction * 90))
        self.t().right(direction * 90)
