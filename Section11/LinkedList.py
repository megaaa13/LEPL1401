class LinkedList:

    def __init__(self):
        self.__length = 0
        self.__head = None

    def size(self):
        return self.__length

    def first(self):
        return self.__head

    def add(self, cargo):
        node = Node(cargo, self.__head)
        self.__head = node
        self.__length += 1

    def print(self):
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_list()
        print("]")

    def print_backward(self):
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_backward()
        print("]")

    def remove(self):
        if self.first() is None:
            return
        self.__head = self.first().next()
        self.__length -= 1

    def insert(self, s):
        n = self.first()
        if n is None:
            self.add(s)
        else:
            if n.value() > s:
                self.add(s)
                n = None
        while n is not None:
            if n.next() is None:
                n.set_next(Node(s, None))
                break
            if n.next().value() >= s:
                n.set_next(Node(s, n.next()))
                break
            n = n.next()

    def __str__(self):
        s = ""
        if self.__length == 0:
            return "[ ]"
        s += "[ "
        tail = self.__head
        while tail is not None:
            s += str(tail) + " "
            tail = tail.next()
        s += "]"
        return s

    def remove_from_end(self):
        node = self.first()
        if node is None:
            return
        if self.__length == 1:
            self.__head = None
            self.__length -= 1
            return
        previous = None
        while node.next() is not None:
            previous = node
            node = node.next()
        previous.set_next(None)
        self.__length -= 1


class Node:

    def __init__(self, cargo=None, next=None):
        self.__cargo = cargo
        self.__next = next

    def value(self):
        return self.__cargo

    def next(self):
        return self.__next

    def __str__(self):
        return str(self.value())

    def print_list(self):
        print(self, end=" ")  # print my head
        tail = self.__next  # go to my next node
        if tail is not None:  # as long as the end of the list has not been reached
            tail.print_list()  # recursively print remainder of the list

    def print_backward(self):
        tail = self.__next  # go to my next node
        if tail is not None:  # as long as the end of the list has not been reached
            tail.print_backward()  # recursively print remainder of the list backwards
        print(self.value(), end=" ")  # print my head

    def set_next(self, node):
        self.__next = node
