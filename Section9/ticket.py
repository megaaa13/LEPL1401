"""
Un ticket de parking
"""
class Ticket :

    __prochain_numero = 1  # variable de classe pour générer le numéro du ticket

    def __init__(self):
        self.__numero = Ticket.__prochain_numero
        Ticket.__prochain_numero += 1

    def numero(self):
        """
        @pre  -
        @post retourne le numero de billet
        """
        return self.__numero