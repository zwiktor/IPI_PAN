import unittest
from domino import Domino


class TestDomino(unittest.TestCase):

    def setUp(self):
        self.dominoes = Domino(r'||//||\||/\|')

    def test_domino_attribute(self):
        self.assertTrue(hasattr(self.dominoes, 'dominoes'))
        self.assertEqual(self.dominoes.dominoes, r'||//||\||/\|')
        for dom in self.dominoes.dominoes:
            self.assertIn(dom, ['\\', '|', '/'])

    def test_domino_next_iteration(self):
        self.dominoes.next_position_of_dominoes()
        self.assertEqual(self.dominoes.dominoes, r'||///\\||/\|')

    def test_domino_previous_iteration(self):
        self.dominoes.previous_position_of_dominoes()
        self.assertEqual(self.dominoes.dominoes, r'||/|||\||/\|')


if __name__ == "__main__":
    unittest.main()
