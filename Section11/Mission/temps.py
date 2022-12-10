class Temps:

    def __init__(self, h=0, m=0, s=0):
        self.__heures = h  # le nombre d'heures
        self.__minutes = m  # le nombre de minutes, entre 0 et 59.
        self.__secondes = s  # le nombre de secondes, entre 0 et 59.

    def heures(self):
        return self.__heures

    def minutes(self):
        return self.__minutes

    def secondes(self):
        return self.__secondes

    def __str__(self):
        return '{:02}:{:02}:{:02}'.format(self.heures(), self.minutes(), self.secondes())

    def to_secondes(self):
        return self.secondes() + 60 * (self.minutes() + 60 * self.heures())

    def delta(self, autre):
        return self.to_secondes() - autre.to_secondes()

    def __eq__(self, autre):
        return self.delta(autre) == 0

    def __ge__(self, autre):
        return self.delta(autre) >= 0

    def add_secondes(self, temps_en_secondes):
        time = self.to_secondes() + temps_en_secondes
        self.__secondes = time % 60
        self.__minutes = (time // 60) % 60
        self.__heures = (time // 3600) % 24

    def add(self, autre):
        self.add_secondes(autre.to_secondes())
