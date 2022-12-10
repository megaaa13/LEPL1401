class Pair:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        return str(self.a) + ", " + str(self.b)

    def opposite(self):
        """
        @pre  -
        @post Retourne une nouvelle instance de Pair dont les deux
              éléments sont les opposés de ceux de cette paire-ci.
              L'instance appelante reste inchangée.
        """
        return Pair(- self.a, - self.b)


class OrderedPair:
    '''
    Représente une paire de deux entiers (représenté en interne par une instance p de la classe Pair).
    Cette paire est considérée comme ordonnée si l'attribut a de p est plus petit ou égal à son attribut b
    '''

    def __init__(self):
        self.p = Pair(0, 0)
        self.ordered = True

    def set_a(self, n_a):
        self.p.a = n_a
        if  self.p.a <= self.p.b:
            self.ordered = True
        else:
            self.ordered = False
        
    def set_b(self, n_a):
        self.p.b = n_a
        if  self.p.a <= self.p.b:
            self.ordered = True
        else:
            self.ordered = False    