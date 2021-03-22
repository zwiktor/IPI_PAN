import unittest
from domino import Domino

class TestDominoInstance(unittest.TestCase):
    def setUp(self):
        self.initial_dominos = Domino('\\\|||//|/\\|/')

    def test_domino_atribute(self):
        self.assertEqual(self.initial_dominos.dominos, '\\\|||//|/\\|/')


if __name__ == "__main__":
     unittest.main()