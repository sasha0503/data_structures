import unittest
from bracket import is_balanced


class BracketTest(unittest.TestCase):

    def test_balanced(self):
        self.assertTrue(is_balanced('()([{}]){}'))
        self.assertTrue(is_balanced('(d)d(f[f{f}f]f)f{ff}'))
        self.assertFalse(is_balanced(')'))
        self.assertFalse(is_balanced(')('))
        self.assertFalse(is_balanced('(]'))
