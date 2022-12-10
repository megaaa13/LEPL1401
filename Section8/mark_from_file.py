class Student:
    def __init__(self, firstname, surname, mark):
        self.firstname = firstname
        self.surname = surname
        self.mark = mark


def marks_from_file(filename):
    list_inst = []
    with open(filename, "r") as file:
        for line in file:
            chaine = line.split()
            n = Student(chaine[0], chaine[1], int(chaine[2]))
            list_inst.append(n)
    return list_inst

