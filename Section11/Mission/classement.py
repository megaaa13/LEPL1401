from orderedlinkedlist import OrderedLinkedList


class Classement:

    __maxcapacity = 10

    def __init__(self):
        self.__resultats = OrderedLinkedList()
        self.__size = 0

    def size(self):
        return self.__size

    def add(self, r):
        if self.size() >= self.__maxcapacity:
            raise ValueError("Capacity of classement exceeded")
        else:
            self.__size += 1
            self.__resultats.add(r)

    def get(self, c):
        r, p = self.__resultats.get(c)
        return r

    def get_position(self, c):
        r, p = self.__resultats.get(c)
        return p

    def remove(self, c):
        self.__size -= 1
        return self.__resultats.remove(c)

    def __str__(self):
        s = ""
        d = self.__resultats.first()
        while d is not None:
            r, p = self.__resultats.get(d.value().coureur())
            s += "  " + str(p) + " > " + str(r) + "\n"
            d = d.next()
        return s
