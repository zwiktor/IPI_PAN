import unittest
from domino import Domino

class TestDominoInstance(unittest.TestCase):



    def setUp(self):
        self.dominos = Domino(r'||//||\||/\|')


    def test_domino_atribute(self):
        self.assertTrue(hasattr(self.dominos, 'dominos'))
        self.assertEqual(self.dominos.dominos, r'||//||\||/\|')
        for dom in self.dominos.dominos:
            self.assertIn(dom, ['\\', '|', '/'])

    def test_domino_next_iteral(self):
        self.dominos.next_iteral()
        self.assertEqual(self.dominos.dominos, r'||///\\||/\|')

    def test_domino_previous_iteral(self):
        self.dominos.previous_iteral()
        self.assertEqual(self.dominos.dominos, r'||/|||\||/\|')


if __name__ == "__main__":
     unittest.main()