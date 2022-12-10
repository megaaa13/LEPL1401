class LinkedList:

    def __init__(self):
        self.__length = 0
        self.__head = None
        self.__last = None
    
    def add(self, a):
        if self.__length == 0:
            snode = Node(a, None)
            self.__head = snode
            self.__last = snode
            self.__length += 1
        else:
            snode = Node(a, self.__last)
            self.__last = snode
            self.__length += 1
    def get_reverse(self):
        s = ""
        node = self.__last
        while node is not None:
            s += node.get_value()
            node = node.get_next()
        return s
    
class Node:

    def __init__(self, cargo=None, next=None):
        self.__cargo = cargo
        self.__next = next
    
    def get_value(self):
        return self.__cargo
    
    def get_next(self):
        return self.__next