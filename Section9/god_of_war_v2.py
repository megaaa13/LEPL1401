class Character:

    def __init__(self, life, attack_point):
        self.life = life
        self.attack_point = attack_point

    def attack(self, target):
        target.get_hit(self.attack_point)

    def get_hit(self, damage):
        self.life -= damage


class Cratos(Character):

    def __init__(self):
        self.experience = 0
        super(Cratos, self).__init__(100, 10)

    def gain_XP(self, amount):
        self.experience += amount
        self.attack_point += self.experience // 10
        self.experience %= 10


class Drauf(Character):
    def __init__(self, life, attack_point):
        super(Drauf, self).__init__(life, attack_point)