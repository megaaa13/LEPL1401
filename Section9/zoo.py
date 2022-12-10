import random
import time


class Animal:
    def __init__(self, n):
        self.name = n
        self.asleep = False
        self.diurnal = None
        self.nb_legs = None
        self.hunger = 0
        self.food = 100

    def sleep(self):
        if self.asleep:
            raise RuntimeError("DEJA DODO")
        else:
            self.asleep = True

    def wake_up(self):
        if not self.asleep:
            raise RuntimeError("DEJA PAS DODO")
        else:
            self.asleep = False

    def faim(self):
        if random.randint(1, 15) == 1:
            if self.hunger > 50:
                print(
                    f'\033[93mJour {day} : {self.name} est mort de faim. Il avait accumulé {self.hunger} points de faim...\033[0m')
                return "Dead"
            if not random.randint(1, 3) == 1:
                f = random.randint(1, 15)
                self.food -= f
                self.hunger -= 3
                if self.hunger < 0:
                    self.hunger = 0
                if self.food < 0:
                    self.food = 0
                print(f'\033[92mJour {day} : {self.name} avait faim. Il a mangé {f} points de nourriture. '
                      f'Il lui reste {self.food}\033[0m')
            else:
                f = random.randint(1, 15)
                self.hunger += f
                print(f"\033[91mJour {day} : {self.name} a faim. Il n'a pas mangé. (Quel con) "
                      f"Il a pris {f} points de faim. Il est maintenant à {self.hunger}\033[0m")
                return
            if self.hunger >= self.food:
                self.food += 50
                self.hunger -= random.randint(5, 15)
                if self.hunger < 0:
                    self.hunger = 0
                print(
                    f"\033[96mJour {day} : {self.name} avait trop peu de nourriture, on lui a remis + 50 de nourriture. "
                    f"Il a maintenant {self.food} points de nourriture et sa faim à baissé à {self.hunger} points.\033[0m")

    """Tu etends le code de zoo game en mettant un truc que les animaux doivent avoir 
    un attribut nourriture et un attribut faim. 
    Si nourriture < faim il faut leur donner +50 nourriture. Chaque fois qu'ils mangent 
    (un random toutes les 1 seconde pour dire si oui ou non)  
    les animaux consomment 1,2,3 nourriture en fonction de leur attribut poids. 
    L'objet zoo a un attribut argent qui détermine l'argent, et un revenu par animal 
    (10,20 ou 30 euros selon la mignonitude se l'animal) par seconde. Il a aussi une réserve de nourriture et peut 
    en acheter moyennant de l'argent quand ses réserves sont bientôt à sec (200 nourriture pour 100 argent). 
    Tu dois trouver le nombre minimal d'argent de départ qu'il faut pour que le zoo soit auto suffisant."""


class Lion(Animal):
    def __init__(self, n):
        super().__init__(n)
        self.diurnal = True
        self.nb_legs = 4

    def roar(self):
        return "ROARRR!!!"


class Owl(Animal):
    def __init__(self, n):
        super().__init__(n)
        self.diurnal = False
        self.nb_legs = 2

    def fly(self):
        pass


class Giraffe(Animal):
    def __init__(self, n, nl):
        if type(nl) == int or type(nl) == float:
            if nl > 0:
                self.neck_length = nl
            else:
                raise ValueError("NON ME O")
        else:
            raise ValueError("NON ME O")
        super().__init__(n)
        self.diurnal = True
        self.nb_legs = 4


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if type(animal) != Animal and type(animal) != Lion and type(animal) != Owl and type(animal) != Giraffe:
            raise ValueError(type(animal))
        self.animals.append(animal)


def create_my_zoo():
    zoo = Zoo()
    zoo.add_animal(Lion("Léo le Lion"))
    zoo.add_animal(Owl("Edwige la Chouette"))
    zoo.add_animal(Giraffe("Jacqueline La Girafe", 1))
    zoo.add_animal(Giraffe("Jeanne La girafe", 1))
    zoo.add_animal(Animal("Robert le Rhino"))
    return zoo.animals


day = 0
zoo = create_my_zoo()

while True:
    for i in zoo:
        e = i.faim()
        if e == "Dead":
            zoo.remove(i)
    if len(zoo) == 1:
        print(f"Félicitations à {zoo[0].name} qui a gagné le battle royal des animaux !")
        break
    time.sleep(0)
    day += 1
