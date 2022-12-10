class Duree:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
        if self.s // 60 != 0:
            self.m += self.s // 60
            self.s = self.s % 60
        if self.m // 60 != 0:
            self.h += self.m // 60
            self.m = self.m % 60

    def to_secondes(self):
        return self.h * 3600 + self.m * 60 + self.s

    def delta(self, d):
        return self.to_secondes() - d.to_secondes()

    def apres(self, d):
        return True if self.to_secondes() > d.to_secondes() else False

    def ajouter(self, d):
        self.h += d.h
        self.s += d.s
        if self.s // 60 != 0:
            self.m += self.s // 60
            self.s = self.s % 60
        self.m += d.m
        if self.m // 60 != 0:
            self.h += self.m // 60
            self.m = self.m % 60

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"


class Chanson:
    def __init__(self, t, auteur, d):
        self.t = t
        self.a = auteur
        self.d = d

    def __str__(self):
        return f"{self.t} - {self.a} - {str(self.d)}"


class Album:
    def __init__(self, id=0):
        self.alb = []
        self.name = f"Album {id}"
        self.duree = Duree(0, 0, 0)

    def add(self, chanson):
        if (self.duree.to_secondes() + chanson.d.to_secondes() > 75 * 60) or len(self.alb) == 100:
            return False
        self.alb.append(str(chanson))
        self.duree.ajouter(chanson.d)
        return True

    def __str__(self):
        album = f"{self.name} ({len(self.alb)} chansons, {str(self.duree)})\n"
        for n, j in enumerate(self.alb):
            album += f"{n + 1:02}: {j}\n"
        return album


if __name__ == "__main__":
    with open("music-db.txt", "r") as file:
        i = 1
        a = Album(i)
        while True:
            for line in file:
                word = line.split()
                ch = Chanson(word[0], word[1], Duree(0, int(word[2]), int(word[3])))
                if not a.add(ch):
                    print(a)
                    i += 1
                    a = Album(i)
                    a.add(ch)
            else:
                print(a)
                del i, line, word, ch, a, file
                break
