import random

class Local:

    def __init__(self, name, grps):
        self.__name = name
        self.__grps = grps

    def __str__(self):
        str = f"La classe {self.name()} contient les groupes suivants : \n"
        for grp in self.grps():
            str += f"{grp} \n"
        return str
    
    def grps(self):
        return self.__grps
    
    def name(self):
        return self.__name

class Groupe:
    
        def __init__(self, name, eleves, projet):
            self.__name = name
            self.__eleves = eleves
            self.__projet = projet
    
        def __str__(self):
            str = f"Le groupe {self.name()}, qui contient les élèves suivants : \n"
            for eleve in self.eleves():
                str += f"\t - {eleve} \n"
            str += f"\t Le projet du groupe {self.name()} est : {self.projet().name()} et il a parcouru {self.projet().distance():.2f} mètres.\n"
            return str
        
        def projet(self):
            return self.__projet
        
        def eleves(self):
            return self.__eleves
        
        def name(self):
            return self.__name

class Personne :
    def __init__(self, prenom, age):
        self.__prenom = prenom
        self.__age = age

    def __str__(self):
        return f"{self.prenom}, {self.age} ans"
    
    def prenom(self):
        return self.__prenom
    
    def age(self):
        return self.__age

class Eleve(Personne):
    def __init__(self, prenom, age, etudes):
        super().__init__(prenom, age)
        self.__etudes = etudes

    def __str__(self):
        return f"{self.prenom()}, {self.age()} ans, étudie {self.etudes()}"
    
    def etudes(self):
        return self.__etudes

class Projet:
    def __init__(self, nom, distance):
        self.__nom = nom
        self.__distance = distance

    def name(self):
        return self.__nom
    
    def distance(self):
        return self.__distance

if __name__ == "__main__":
    def randomMatiere():
        return random.choice(["Maths appliquées", "Informatique", "Electricité", "Génie civil", "Mécanique", "Chimie et Physique appliquée", "Génie biologique"])
    
    def randomAge():
        return random.choice([18, 18, 18, 18, 18, 19, 20, 21])
    
    with open("names.txt", "r") as f:
        names = f.read().split("\n")

    def randomPrenom():
        return random.choice(names)
    
    def randomEleve():
        return Eleve(randomPrenom(), randomAge(), randomMatiere())
    
    eleves1 = [randomEleve() for _ in range(6)]
    eleves2 = [randomEleve() for _ in range(6)]
    eleves3 = [randomEleve() for _ in range(6)]
    eleves4 = [randomEleve() for _ in range(6)]   

    groupe1 = Groupe("Groupe 1", eleves1, Projet("Projet 1", (random.random().__round__(3) * 10).__round__(2)))
    groupe2 = Groupe("Groupe 2", eleves2, Projet("Projet 2", (random.random().__round__(3) * 10).__round__(2)))
    groupe3 = Groupe("Groupe 3", eleves3, Projet("Projet 3", (random.random().__round__(3) * 10).__round__(2)))
    groupe4 = Groupe("Groupe 4", eleves4, Projet("Projet 4", (random.random().__round__(3) * 10).__round__(2)))
    barb = Local("BARB " + str(random.randint(10, 39)), [groupe1, groupe2, groupe3, groupe4])
    print(barb)

