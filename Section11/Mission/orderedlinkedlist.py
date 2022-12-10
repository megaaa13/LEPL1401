class OrderedLinkedList:

    def __init__(self, lst=None):
        if lst is None:
            lst = []
        self.__length = 0
        self.__head = None
        self.__last = None
        lst.reverse()
        for e in lst:
            self.add(e)

    def size(self):
        return self.__length

    def inc_size(self):
        self.__length += 1

    def dec_size(self):
        self.__length -= 1

    def first(self):
        return self.__head

    def set_first(self, n):
        self.__head = n

    def get(self, c):
        if self.size() == 0:
            return None, 0
        else:
            pos = 2
            previous = self.first()
            if previous.value().coureur() == c:
                return previous.value(), 1
            while previous.next() is not None and previous.next().value().coureur() != c:
                previous = previous.next()
                pos += 1
            if previous.next() is None:
                return None, 0
            return previous.next().value(), pos

    def add(self, cargo):
        if self.size() == 0:
            node = self.Node(cargo, self.first())
            self.__last = node
            self.set_first(node)
            self.inc_size()
        else:
            previous = self.first()
            while previous.next() is not None and previous.next().value() < cargo:
                previous = previous.next()
            if previous == self.__last:
                if previous.value() <= cargo:
                    self.add_to_end(cargo)
                    return
            if previous == self.first() and previous.value() > cargo:
                snode = self.Node(cargo, previous)
                self.set_first(snode)
                self.inc_size()
                return
            snode = self.Node(cargo, previous.next())
            previous.set_next(snode)
            self.inc_size()

    def remove(self, c):
        if self.size() == 0:
            return False
        else:
            previous = self.first()
            if previous.value().coureur() == c:
                self.set_first(previous.next())
                self.dec_size()
                return c
            while previous.next() is not None and previous.next().value().coureur() != c:
                previous = previous.next()
            if previous.next() is None:
                return False
            previous.set_next(previous.next().next())
            self.dec_size()
            return c

    def add_to_end(self, cargo):
        if self.size() == 0:
            self.add(cargo)
        else:
            node = self.Node(cargo)
            self.__last.set_next(node)
            self.__last = node
            self.inc_size()

    def print(self):
        self.print_avec_separateur()

    def print_avec_separateur(self, separateur=" "):
        print("[", end=" ")
        if self.first() is not None:
            self.first().print_list_avec_separateur(separateur)
        print("]")

    def print_avec_virgule(self):
        self.print_avec_separateur(", ")

    def print_backward(self):
        print("[", end=" ")
        if self.first() is not None:
            self.first().print_backward()
        print("]")

    class Node:

        def __init__(self, cargo=None, next=None):
            self.__cargo = cargo
            self.__next = next

        def value(self):
            return self.__cargo

        def next(self):
            return self.__next

        def set_next(self, node):
            self.__next = node

        def __str__(self):
            return str(self.value())

        def __eq__(self, other):
            if other is not None:
                return self.value() == other.value()
            else:
                return False

        def print_list(self):
            head = self
            tail = self.__next  # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                print(head, end=" ")  # print my head
                tail.print_list()  # recursively print remainder of the list
            else:  # print the last element
                print(head, end=" ")

        def print_backward(self):
            head = self
            tail = self.__next  # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                tail.print_backward()  # recursively print remainder of the list backwards
            print(head, end=" ")  # print my head

        def print_avec_separateur(self, separateur):
            print("[", end=" ")
            if self.first() is not None:
                self.head.print_list_avec_separateur(separateur)
            print("]")

        def print_list_avec_separateur(self, separateur):
            head = self
            tail = self.__next  # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                print(head, end=separateur)  # print my head, with separateur
                tail.print_list_avec_separateur(separateur)  # recursively print remainder of the list
            else:  # print the last element
                print(head, end=" ")
