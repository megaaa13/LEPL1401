class Node:
    def __init__(self, s):
        self.value = s
        self.previous = None
        self.next = None

    def get_text(self):
        return self.value()

    def set_text(self, s):
        self.value = s

    def set_previous(self, node):
        self.previous = node

    def set_next(self, node):
        self.previous = node



class Tape:

    def __init__(self):
        self.size = 0
        self.curr = None
        self.last = None

    def next(self):
        if self.curr is not None and self.curr.next is not None:
            self.curr = self.curr.next
            return self.curr.get_text()

    def previous(self):
        if self.curr is not None and self.curr.previous is not None:
            self.curr = self.curr.previous
            return self.curr.get_text()

    def get_length(self):
        return self.size

    def add(self, s):
        node = Node(s)
        self.size += 1
        if self.size == 1:
            self.curr = node
            self.last = node
        else:
            self.last.next = node
            node.previous = self.last
            self.last = node

    def write(self, s):
        if self.size > 0:
            self.curr.value = s

    def read(self):
        if self.size > 0:
            return self.curr.value
        return None
