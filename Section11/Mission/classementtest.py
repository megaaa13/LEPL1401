import unittest
from classement import Classement


class TestClassement(unittest.TestCase):
    def setUp(self):
        self.c = Classement()

    def test_init(self):
        self.assertEqual(self.c.size(), 0, "Mauvaise initiation")

    def test_add_limit(self):
        with self.assertRaises(ValueError):
            n = 0
            while True:
                n += 1
                self.c.add(n)

    def test_add(self):
        self.c.add(1)
        self.assertEqual(self.c.size(), 1, "Taille mal prise en compte")

    def test_get(self):
        """
        Même problème que dans orderedlinkedlist :
        J'utilise des méthodes de classes qui ne seront pas importées dans inginious,
        le code ne passerait pas...
        """
        pass

    def test_str(self):
        """idem..."""
        pass
