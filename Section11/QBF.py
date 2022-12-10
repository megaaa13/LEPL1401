class TourDeRole :

    @classmethod
    def main(cls):
        l = CircularLinkedList()
        l.add("Charles")
        l.add("Kim")
        l.add("Siegfried")
        l.add("Sébastien")
        l.add("Charles")
        l.add("Siegfried")
        l.remove("Kim")
        l.add("Charles")
        l.removeAll("Charles")

TourDeRole.main()

class CircularLinkedList :

    class Node:
        def __init__(self,cargo=None,next=None):
            """ Initialises a new Node object. """
            self.__cargo = cargo
            self.__next  = next

        def value(self):
            """ Returns the value of the cargo contained in this node. """
            return self.__cargo

        def next(self):
            """ Returns the next node to which this node links. """
            return self.__next

        def set_next(self,node):
            """ Sets the next node to which this node links to a new node. """
            self.__next = node

    def __init__(self):
        """ Initialises a new empty circular linked list.
        @pre:  -
        @post: A new circular linked list with no nodes has been initialised.
               The first pointer refers to None.
        """
        self.__first = None       # pointer to the first node
        self.__last  = None       # pointer to the last node

    def first(self):
        """ Returns the first node of this circular linked list.
        @pre:  -
        @post: Returns a reference to the first node of this circular linked list,
               or None if the circular linked list contains no nodes.
        """
        return self.__first

    def last(self):
        """ Returns the last node of this circular linked list.
        @pre:  -
        @post: Returns a reference to the last node of this circular linked list,
               or None if the circular linked list contains no nodes.
        """
        return self.__last

    def add(self, cargo):
        """ Adds new Node with given cargo to front of this circular linked list.
        @pre:  self is a (possibly empty) CircularLinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the circular linked list.
               The head of the list now points to this new node.
               The last node now points to this new node.
        """
        node = self.Node(cargo,self.first())
        self.__first = node
        if self.last() == None :   # when this was the first element being added,
            self.__last = node     # set the last pointer to this new node
        self.last().set_next(node)


    def remove(self,cargo):
        """ Removes a node with given cargo from the circular linked list.
        @pre:  -
        @post: A node with given cargo was removed from the circular linked list.
               The removed node, with next pointer set to None, is returned.
               In case multiple nodes with this cargo exist, only one is removed.
               The list is unchanged if no such node exists or the list is empty.
               In that case, None is returned as result.
        """
        previous = self.first()
        if self.__first == None:
            return None
        if self.__first == self.__last:
            if self.__first.value() == cargo:
                node = self.__first
                self.__first = None
                self.__last = None
                node.set_next(None)
                return node
        if previous.value() == cargo:
            last = self.last()
            self.__first = previous.next()
            last.set_next(previous.next())
            previous.set_next(None)
            return previous
        while previous.next().value() != cargo and previous.next() != self.__last.next():
            previous = previous.next()
        if previous.next() == self.__last.next():
            return None
        if previous.next().value() == cargo:
            if self.__last == previous.next():
                self.__last = previous
            removed = previous.next()
            previous.set_next(previous.next().next())
            removed.set_next(None)
            return removed

    def removeAll(self,cargo):
        """ Removes all nodes with given cargo. """
        r = 2
        while r is not None:
            r = self.remove(cargo)