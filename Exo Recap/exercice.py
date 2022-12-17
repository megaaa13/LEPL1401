import random

"""
Author : Martin Gyselinck

Petit exo inventé pour vous faire réviser les notions d'orienté objet et d'héritage.

Afin de créer un classement des résultats du projet par local, on vous a demandé à vous, le meilleur étudiant de l'univers, 
de créer un programme qui permet recenser les élèves par groupes, et par local.

Vous devez créer les classes suivantes :
    - Eleve : Un élève est une personne (de la classe Personne) (! héritage !) qui a des études.
    - Local : Une local a un nom et un ensemble de groupes qui y passe ses TPs.
    - Groupe : Un groupe a un nom, un ensemble d'élèves qui le représente et un projet.
    - Projet : Un projet a un nom et parcoure une certaine distance (aléatoire).

Petits conseils :
    - Essayez de faire en sorte que toutes vos attributs soient privés (-> méthodes get_...)
    - Essayez de faire en sorte que toutes vos classes aient une méthode __str__ qui permet d'afficher ses informations.


Pour aller plus loin, vous pouvez essayer de faire en sorte d'utiliser des LinkedList et non des listes.
"""

class Personne :
    """
    Je vous la donne, vous n'avez rien à faire ici ! :)
    """
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
        ... # TODO
    # TODO
    # Vous pouvez implémenter ce que vous jugez nécéssaire !

class Local:
    ... # TODO
    # Vous pouvez implémenter ce que vous jugez nécéssaire !

class Groupe:
    ... # TODO
    # Vous pouvez implémenter ce que vous jugez nécéssaire !

class Projet:
    ... # TODO
    
    # Vous pouvez ajouter vos propres fonctions si nécéssaire !

if __name__ == "__main__":
    # Rien à faire ici, c'est juste pour vous aider à tester votre code !
    # Evitez de trop y regarder si vous ne comprenez pas tout, il n'est pas fait pour être compris !
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

"""
Voici un exemple de résultat attendu :

La classe BARB28 contient les groupes suivants : 
Le groupe Groupe 61, qui contient les élèves suivants :
         - Nicolas, 20 ans, étudie Chimie et Physique appliquée
         - Joachim, 20 ans, étudie Génie biologique
         - Dorian, 19 ans, étudie Mécanique
         - Nicolas, 21 ans, étudie Electricité
         - Jean, 18 ans, étudie Chimie et Physique appliquée
         - Maxime, 19 ans, étudie Informatique
         Le projet du groupe Groupe 61 est : Projet 61 et il a parcouru 2.03 mètres.

Le groupe Groupe 62, qui contient les élèves suivants :
         - Aglaë, 21 ans, étudie Génie civil
         - Briac, 18 ans, étudie Electricité
         - Charles, 19 ans, étudie Maths appliquées
         - Marius, 21 ans, étudie Génie civil
         - Maxime, 19 ans, étudie Mécanique
         - Zélia, 18 ans, étudie Chimie et Physique appliquée
         Le projet du groupe Groupe 62 est : Projet 62 et il a parcouru 3.58 mètres.

Le groupe Groupe 63, qui contient les élèves suivants :
         - Yvan, 19 ans, étudie Chimie et Physique appliquée
         - Louis, 21 ans, étudie Génie civil
         - Zoé, 18 ans, étudie Chimie et Physique appliquée
         - Mathis, 21 ans, étudie Maths appliquées
         - Alice, 18 ans, étudie Génie biologique
         - Alexandre, 18 ans, étudie Génie civil
         Le projet du groupe Groupe 63 est : Projet 63 et il a parcouru 6.29 mètres.

Le groupe Groupe 64, qui contient les élèves suivants :
         - Layla, 18 ans, étudie Chimie et Physique appliquée
         - Bastien, 19 ans, étudie Chimie et Physique appliquée
         - Florian, 18 ans, étudie Electricité
         - Victor, 18 ans, étudie Informatique
         - Joanne, 18 ans, étudie Génie civil
         - Andréa, 18 ans, étudie Electricité
         Le projet du groupe Groupe 64 est : Projet 64 et il a parcouru 7.51 mètres.
"""

