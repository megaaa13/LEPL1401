class Student:
    noma = 0

    def __init__(self, f, s, b, e):
        self.noma = Student.noma
        Student.noma += 1
        self.f = f
        self.s = s
        self.b = b
        self.e = e

    def __str__(self):
        return f"L'étudiant numéro {self.noma} : {self.f} {self.s} né le {self.b}, peut être contacté par {self.e}"