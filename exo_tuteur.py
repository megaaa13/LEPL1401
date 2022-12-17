class Classe:

    def __init__(self, name, grps):
        self.name = name
        self.grps = grps

    def __str__(self):
        str = f"La classe {self.name} contient les groupes suivants : \n"
        for grp in self.grps:
            
