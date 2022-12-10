import math


class Robot:
    def __init__(self, n):
        self.__nom__ = n
        self.__x = 0
        self.__y = 0
        self.__angle = 0
        self.history = []

    def __str__(self):
        return str(self.getnom()) + "@(" + str(round(self.getx())) + "," + str(round(self.gety())) + ") angle: " + str(
            self.getangle())

    def getnom(self):
        return self.__nom__

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def getanglerad(self):
        return self.__angle

    def getangle(self):
        return (self.__angle * 180 / math.pi) % 360

    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y

    def position(self):
        return self.getx(), self.gety()

    def set_angle(self, na):
        self.__angle = na

    def get_history(self):
        return self.history

    def unplay(self):
        history = self.get_history().copy()
        for (x, y) in history:
            if x == "backward":
                self.moveforward(y)
            elif x == "forward":
                self.movebackward(y)
            elif x == "left":
                self.turnright()
            elif x == "right":
                self.turnleft()
        self.history.clear()

    def moveforward(self, y):
        pass

    def movebackward(self, y):
        pass

    def turnright(self):
        pass

    def turnleft(self):
        pass
