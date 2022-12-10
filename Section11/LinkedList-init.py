def __init__(self, lst=[]):
    self.__length, self.__head = 0, None
    for i in range(len(lst) - 1, -1, -1):
        self.add(lst[i])