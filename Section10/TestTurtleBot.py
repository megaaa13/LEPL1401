import unittest
import TurtleBot as tb


class TestTurtleBot(unittest.TestCase):

    def setUp(self):
        self.t = tb.TurtleBot("tBot")

    def test_init(self):
        self.assertEqual(self.t.getangle(), 0, "Your turtleBot is not facing EAST as expected")
        self.assertEqual(self.t.position(), (0, 0), "Your turtleBot is not in 0,0 as expected")

    def test_turnleft(self):
        expected_position = self.t.position()
        expected_angle = (self.t.getangle() - 90) % 360
        self.t.turnleft()
        # below we are using assertAlmostEqual instead if assertEqual to allow for inaccurate calculations
        self.assertAlmostEqual(self.t.getangle(), expected_angle,
                               msg="Your turtleBot took a wrong turn or did not update its angle while turning left")
        self.assertEqual(self.t.position(), expected_position, "Your turtleBot changed position while turning left")

    def test_turnright(self):
        expected_position = self.t.position()
        expected_angle = (self.t.getangle() + 90) % 360
        self.t.turnright()
        self.assertAlmostEqual(self.t.getangle(), expected_angle,
                               msg="Your turtleBot took a wrong turn or did not update its angle while turning right")
        self.assertEqual(self.t.position(), expected_position, "Your turtleBot changed position while turning right")

    def test_turn(self):
        expected_position = self.t.position()
        expected_angle = self.t.getangle()
        self.t.turnleft()
        self.t.turnleft()
        self.t.turnright()
        self.t.turnright()
        self.assertAlmostEqual(self.t.getangle(), expected_angle,
                               msg="Your turtleBot took a wrong turn or did not update its angle")
        self.assertEqual(self.t.position(), expected_position, "Your turtleBot changed position while turning")

    def test_moveforward(self):
        forward = 50
        x, y = self.t.position()
        expected_position = (x + forward, 0 + y)
        expected_angle = self.t.getangle()
        self.t.moveforward(50)
        self.assertEqual(self.t.position(), expected_position,
                         "Your turtleBot has not moved forward " + str(forward) + " as expected")
        self.assertAlmostEqual(self.t.getangle(), expected_angle,
                               msg="Your turtleBot changed heading while moving forward")

    def test_movebackward(self):
        backward = 50
        x, y = self.t.position()
        expected_position = (x - backward, y - 0)
        expected_angle = self.t.getangle()
        self.t.movebackward(50)
        self.assertEqual(self.t.position(), expected_position,
                         "Your turtleBot has not moved backward " + str(backward) + " as expected")
        self.assertAlmostEqual(self.t.getangle(), expected_angle,
                               msg="Your turtleBot changed heading while moving backward")

    def test_move(self):
        expected_position = self.t.position()
        expected_angle = self.t.getangle()
        self.t.moveforward(50)
        self.t.movebackward(10)
        self.t.movebackward(90)
        self.t.moveforward(50)
        self.assertAlmostEqual(self.t.getangle(), expected_angle,
                               msg="Your turtleBot took a wrong turn or did not update its angle")
        self.assertEqual(self.t.position(), expected_position, "Your turtleBot changed position while turning")

    def test_move_complex(self):
        self.t.setx(0)
        self.t.sety(0)
        self.t.resetangle()
        self.t.turnleft()
        self.t.movebackward(150)
        self.t.turnleft()
        self.t.movebackward(60)
        self.t.turnright()
        self.assertEqual(self.t.getangle(), 270), "Le robot a mal tourné"
        self.assertEqual((round(self.t.getx(), 1), round(self.t.gety(), 1)), (60, 150),
                         "Le robot n'a pas bien exécuté les instructions")

    def test_history(self):
        oldx = self.t.getx()
        oldy = self.t.gety()
        self.t.resetangle()
        self.t.turnleft()
        self.t.movebackward(100)
        self.t.turnleft()
        self.t.movebackward(100)
        self.t.turnright()
        self.t.unplay()
        self.assertEqual((oldx, oldy), (round(self.t.getx(), 1), round(self.t.gety(), 1)),
                         "Le retour en arrière a une erreur")


if __name__ == '__main__':
    unittest.main(verbosity=2)
