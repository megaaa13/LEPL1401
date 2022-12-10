import Missions.Mission10.XYRobot as xy
import unittest
import random
import string


class TestXYRobot(unittest.TestCase):

    def setUp(self):
        self.name = ''.join(random.choice(string.ascii_lowercase) for i in range(9))
        self.r = xy.XYRobot(self.name)

    def test_init(self):
        self.assertEqual(self.r.getangle(), 0, "Ono l'angle est pas pareil !")
        self.assertEqual((round(self.r.getx(), 1), round(self.r.gety(), 1)), (0, 0), "Mauvais départ")

    def test_forward_backward(self):
        self.r.moveforward(20)
        self.assertEqual((round(self.r.getx(), 1), round(self.r.gety(), 1)), (20, 0), "N'a pas avancé correctement")
        self.r.movebackward(30)
        self.assertEqual((round(self.r.getx(), 1), round(self.r.gety(), 1)), (-10, 0), "N'a pas reculé correctement")

    def test_turn_right_left(self):
        self.r.turnleft()
        self.r.turnleft()
        self.assertEqual(self.r.getangle(), 180, "Ne tourne pas vers la gauche correctement")
        self.r.turnright()
        self.r.turnright()
        self.r.turnright()
        self.assertEqual(self.r.getangle(), 90, "Ne tourne pas vers la droite correctement")

    def test_caract(self):
        self.assertEqual(self.r.getnom(), self.name, "Le nom n'a pas été correctement enregistré")

    def test_x_y(self):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        self.r.sety(y)
        self.r.setx(x)
        self.assertEqual((round(self.r.getx(), 1), round(self.r.gety(), 1)), (x, y), "Positions mal changées")

    def test_move_complex(self):
        self.r.turnleft()
        self.r.setx(0)
        self.r.sety(0)
        self.r.movebackward(100)
        self.r.turnleft()
        self.r.movebackward(100)
        self.r.turnright()
        self.assertEqual(self.r.getangle(), 270), "Le robot a mal tourné"
        self.assertEqual((round(self.r.getx(), 1), round(self.r.gety(), 1)), (100, 100),
                         "Le robot n'a pas bien exécuté les instructions")

    def test_pos(self):
        self.assertEqual(self.r.position(), (self.r.getx(), self.r.gety()))

    def test_history(self):
        oldx = self.r.getx()
        oldy = self.r.gety()
        self.r.turnleft()
        self.r.movebackward(100)
        self.r.turnleft()
        self.r.movebackward(100)
        self.r.turnright()
        self.r.unplay()
        self.assertEqual((oldx, oldy), (round(self.r.getx(), 1), round(self.r.gety(), 1)),
                         "Le retour en arrière a une erreur")


if __name__ == '__main__':
    unittest.main(verbosity=2)
