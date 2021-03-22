import unittest
from domino import Domino

class TestDominoInstance(unittest.TestCase):



    def setUp(self):
        self.dominos = Domino(r'//|||||\\\\|')

    def test_domino_atribute(self):
        self.assertEqual(self.dominos.dominos, '//|||||\\\\|')
        for dom in self.dominos.dominos:
            self.assertIn(dom, ['right', 'left', 'center'])

    def test_domino_next_iteral(self):
        self.assertEqual(self.dominos.next_iteral(self.dominos), r'///|||\\\\\|')

    def test_domino_previous_iteral(self):
        self.assertEqual(self.dominos.previous_iteral(), r'/|||||||\\\|')


if __name__ == "__main__":
     unittest.main()