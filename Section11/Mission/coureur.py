class Coureur:

    def __init__(self, nom, age):
        self.__nom = nom  # Le nom du coureur
        self.__age = age  # L'age du coureur.

    def nom(self):
        return self.__nom

    def age(self):
        return self.__age

    def __eq__(self, other):
        return (type(other) == Coureur) and (self.nom() == other.nom()) and (self.age() == other.age())

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return "Coureur " + self.nom() + " (âge " + str(self.age()) + ")"
