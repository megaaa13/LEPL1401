import unittest
from orderedlinkedlist import OrderedLinkedList


class TestOrderedList(unittest.TestCase):

    def setUp(self):
        self.o = OrderedLinkedList()

    def test_init(self):
        self.assertEqual((self.o.size(), self.o.first()), (0, None), "Mauvaise initialisation")

    def test_modif_size_and_first(self):
        self.o.dec_size()
        self.assertEqual(self.o.size(), -1, "Mauvais dec")
        self.o.inc_size()
        self.assertEqual(self.o.size(), 0, "Mauvais inc")
        self.o.set_first(23)
        self.assertEqual(self.o.first(), 23, "Mauvais set first")
        self.o.set_first(None)

    def test_add(self):
        self.o.add(1)
        self.assertEqual(self.o.first(), OrderedLinkedList.Node(1))
        self.o.add(4)
        self.o.add(3)
        self.o.add(0.5)
        self.o.add_to_end(0.1)
        self.assertEqual(self.o.first(), OrderedLinkedList.Node(0.5))

    def test_remove(self):
        """
        Je n'ai aucune idée de comment réaliser les tests ici,
        sachant que la méthode
        ne peut fonctionner qu'avec le programme de la course...
        (je dois comparer des coureurs, donc appeler des attributs de résultats...)
        """
        pass

    def test_get(self):
        """idem"""
        pass
