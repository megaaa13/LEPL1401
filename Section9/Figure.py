class Figure:

    def __init__(self, x, y, visible=False):
        self.__x = x
        self.__y = y
        self.__visible = visible

    def estVisible(self):
        return self.__visible

    def surface(self):
        pass

    def x(self):
        return self.__x

    def y(self):
        return self.__y


class Rectangle(Figure):

    def __init__(self, lo, la, x, y):
        super(Rectangle, self).__init__(x, y)
        self.longeur = lo
        self.largeur = la

    def __str__(self):
        return str((self.longeur, self.largeur, self.x(), self.y(), self.estVisible()))

    def surface(self):
        return self.longeur * self.largeur
