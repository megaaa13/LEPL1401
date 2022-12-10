class Employe: 
    def __init__(self, n, s): self.nom, self.salaire = n, s
    def augmente(self, a): self.salaire += self.salaire / 100 * a
    def __str__(self): return f"{self.nom} : {self.salaire}"