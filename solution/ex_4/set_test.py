import unittest
from set import Set


class SetTest(unittest.TestCase):
    def test_init(self):
        test_set = Set()
        self.assertIsInstance(test_set.items, set)

    def test_init_with_items(self):
        test_set = Set([1, 2, 3])
        self.assertEqual(test_set.items, {1, 2, 3})
        test2_set = Set([3, 2, 1])
        self.assertEqual(test_set.items, test2_set.items)

    def test_complement(self):
        test_set = Set([3, 4, 5])
        other_set = Set([3, 4, 5, 6, 7])
        self.assertEqual(test_set.complement(other_set), Set([6, 7]))
        self.assertEqual(other_set.complement(test_set), Set([]))

    def test_union(self):
        test_set = Set([3, 4, 5])
        other_set = Set([3, 4, 5, 6, 7])
        self.assertEqual(test_set.union(other_set), Set([3, 4, 5, 6, 7]))
        self.assertEqual(other_set.union(test_set), Set([3, 4, 5, 6, 7]))

    def test_intersection(self):
        test_set = Set([3, 4, 5])
        other_set = Set([3, 4, 5, 6, 7])
        self.assertEqual(test_set.intersection(other_set), Set([3, 4, 5]))
        self.assertEqual(other_set.intersection(test_set), Set([3, 4, 5]))
        other_set = Set([1, 2])
        self.assertEqual(test_set.intersection(other_set), Set([]))
        self.assertEqual(other_set.intersection(test_set), Set([]))

    def test_difference(self):
        test_set = Set([3, 4, 5])
        other_set = Set([3, 4, 5, 6, 7])
        self.assertEqual(test_set.difference(other_set), Set([]))
        self.assertEqual(other_set.difference(test_set), Set([6, 7]))

    def test_symmetric_difference(self):
        test_set = Set([1, 2, 3, 4, 5])
        other_set = Set([3, 4, 5, 6, 7])
        self.assertEqual(test_set.symmetric_difference(other_set), Set([1, 2, 6, 7]))
        self.assertEqual(other_set.symmetric_difference(test_set), Set([1, 2, 6, 7]))

    def test_str(self):
        test_set = Set([1, 2, 3, 4, 5])
        self.assertEqual(str(test_set), "{1, 2, 3, 4, 5}")

    def test_str_empty(self):
        test_set = Set()
        self.assertEqual(str(test_set), "{}")


if __name__ == '__main__':
    unittest.main()
