class Pair:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __eq__(self, p):
        if p == None: return False
        if self.a == p.a and self.b  == p.b:
            return True
        return False