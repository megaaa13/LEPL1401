def taux_tva():
    return Article.getTVA()


class Article:
    __taux_tva = 0.21  # TVA a 21%

    @classmethod
    def getTVA(cls):
        return cls.__taux_tva

    def __init__(self, d, p):
        self.__description = d
        self.__prix = p

    def description(self):
        return self.__description

    def prix(self):
        return self.__prix

    def tva(self):
        return self.prix() * taux_tva()

    def prix_tvac(self):
        return self.prix() + self.tva()

    def __str__(self):
        return "{0}: {1:.2f}".format(self.description(), self.prix())


def barre_str():
    b = ""
    barre_longeur = 83
    for i in range(barre_longeur):
        b += "="
    return b + "\n"


def article_str(art, a, b, c, d):
    return "| {0:40} | {1} | {2} | {3} |\n".format(a, b, c, d)


def totaux_str(desc, prix, tva, prixtva):
    b = barre_str()
    b += "| {0:40} | {1:10} | {2} | {3} |\n".format(desc, prix, tva, prixtva)
    b += barre_str()
    return b


class Facture:
    __numero = 0

    def __init__(self, description, articles):
        Facture.__numero += 1
        self.__reference = description
        self.__articles = articles

    def description(self):
        return self.__reference

    def articles(self):
        return self.__articles

    def __str__(self):
        s = self.entete_str("Description", "prix HTVA", "TVA", "prix TVAC")
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.articles():
            s += article_str(art, art.description(),
                             f"{art.prix():10.2f}", f"{art.tva():10.2f}", f"{art.prix_tvac():10.2f}")
            totalPrix += art.prix()
            totalTVA += art.tva()
        s += totaux_str("T O T A L", f"{totalPrix:10.2f}", f"{totalTVA:10.2f}", f"{totalPrix + totalTVA:10.2f}")
        return s

    def entete_str(self, d, p, t, pt):
        e = f"Facture No {Facture.__numero} " + self.description() + "\n"
        e += barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format(d, p, t, pt)
        e += barre_str()
        return e

    def nombre(self, pce):
        count = 0
        for art in self.articles():
            if art is pce:
                count += 1
        return count

    # Cette méthode doit être ajoutée lors de l'étape 5 de la miasion
    def livraison_str(self):
        s = "Livraison - "
        s += self.entete_str("Description", "poids/pce", "nombre", "poids")
        totalkg, totalart, count = 0, 0, 0
        fragilehere = False
        for art in self.articles():
            if type(art) == ArticlePiece:
                count += 1
                s += article_str(art, f"""{art.piece().description()} {"(!)" if art.piece().fragile() else ""}""",
                                 f"{art.piece().poids():8.2f}kg", f"{art.nbr():10}",
                                 f"{art.piece().poids() * art.nbr():8.2f}kg")
                totalkg += art.piece().poids() * art.nbr()
                totalart += art.nbr()
                if art.piece().fragile() and not fragilehere:
                    fragilehere = True
        s += totaux_str(f"{count} articles", "", f"{totalart:10}", f"{totalkg:8.2f}kg")
        if fragilehere:
            s += " (!) *** livraison fragile ***"
        return s

    def nbr_livr(self):
        count = 0
        for art in self.articles():
            if type(art) == ArticlePiece:
                count += 1
        return count


class ArticleReparation(Article):
    def __init__(self, duree):
        self.__duree = duree
        super().__init__(f"Reparation ({self.duree()} heures)", 20)

    def prix(self):
        return super().prix() + 35 * self.__duree

    def duree(self):
        return self.__duree


class Piece:
    def __init__(self, desc, price, weight=0, fragile=False, tvanorm=True):
        self.__desc = desc
        self.__price = price
        self.__weight = weight
        self.__fragile = fragile
        self.____tvanorm = tvanorm

    def __eq__(self, other):
        return True if self.description() == other.description() and self.prix() == other.prix() else False

    def description(self):
        return self.__desc

    def prix(self):
        return self.__price

    def poids(self):
        return self.__weight

    def fragile(self):
        return self.__fragile

    def tva_reduit(self):
        return self.____tvanorm


class ArticlePiece(Article):
    def __init__(self, nbr, piece: Piece):
        self.__nbr = nbr
        self.__piece = piece
        super().__init__(self.piece().description(), self.piece().prix())

    def nbr(self):
        return self.__nbr

    def piece(self):
        return self.__piece

    def description(self):
        return f"{self.nbr()} * {self.piece().description()} @ {self.piece().prix()}"

    def prix(self):
        return self.piece().prix() * self.nbr()

    def tva(self):
        return 0.06 * self.piece().prix() * self.nbr() if not self.piece().tva_reduit() \
            else 0.21 * self.piece().prix() * self.nbr()
