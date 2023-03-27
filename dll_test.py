import unittest
from dll import DoublyLinkedList, Node, swap_k


class NodeTest(unittest.TestCase):

    def test_node(self):
        node = Node(1)
        self.assertEqual(node.value, 1)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)


class DllTest(unittest.TestCase):

    def test_init(self):
        dll = DoublyLinkedList()
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

    def test_append(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        self.assertEqual(dll.head.value, 1)
        self.assertEqual(dll.tail.value, 2)
        self.assertEqual(dll.head.next.value, 2)
        self.assertEqual(dll.head.prev, None)
        self.assertEqual(dll.tail.prev.value, 1)
        self.assertEqual(dll.tail.next, None)

    def test_prepend(self):
        dll = DoublyLinkedList()
        dll.prepend(1)
        dll.prepend(2)
        self.assertEqual(dll.head.value, 2)
        self.assertEqual(dll.tail.value, 1)
        self.assertEqual(dll.head.next.value, 1)
        self.assertEqual(dll.head.prev, None)
        self.assertEqual(dll.tail.prev.value, 2)
        self.assertEqual(dll.tail.next, None)

    def test_remove_success(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.remove(2)
        self.assertEqual(dll.head.value, 1)
        self.assertEqual(dll.tail.value, 3)
        self.assertEqual(dll.head.next.value, 3)
        self.assertEqual(dll.head.prev, None)
        self.assertEqual(dll.tail.prev.value, 1)
        self.assertEqual(dll.tail.next, None)

    def test_remove_head(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.remove(1)
        self.assertEqual(dll.head.value, 2)
        self.assertEqual(dll.tail.value, 3)
        self.assertEqual(dll.head.next.value, 3)
        self.assertEqual(dll.head.prev, None)
        self.assertEqual(dll.tail.prev.value, 2)
        self.assertEqual(dll.tail.next, None)

    def test_remove_tail(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.remove(3)
        self.assertEqual(dll.tail.value, 2)
        self.assertEqual(dll.tail.next, None)

    def test_remove_fail(self):
        dll = DoublyLinkedList()
        with self.assertRaises(ValueError):
            dll.remove(2)
        dll.append(1)
        with self.assertRaises(ValueError):
            dll.remove(2)

    def test_find(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll.find(1), None)
        dll.append(1)
        self.assertEqual(dll.find(1), 0)
        self.assertEqual(dll.find(4), None)

    def test_swap_neighbors_success(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.swap_neighbors(2)
        self.assertEqual(dll.find(2), 1)
        self.assertEqual(dll.head.value, 3)
        self.assertEqual(dll.tail.value, 1)
        self.assertEqual(dll.head.next.value, 2)
        self.assertEqual(dll.head.prev, None)
        self.assertEqual(dll.tail.prev.value, 2)
        self.assertEqual(dll.tail.next, None)
        self.assertEqual(dll.head.next.next.value, 1)
        self.assertEqual(dll.head.next.prev.value, 3)

    def test_swap_neighbors_fail(self):
        dll = DoublyLinkedList()
        with self.assertRaises(ValueError):
            dll.swap_neighbors(1)
        dll.append(1)
        dll.append(2)
        dll.append(3)
        with self.assertRaises(ValueError):
            dll.swap_neighbors(1)
        with self.assertRaises(ValueError):
            dll.swap_neighbors(3)
        with self.assertRaises(ValueError):
            dll.swap_neighbors(4)

    def test_split_success(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        idx = dll.find(2)
        dll1, dll2 = dll.split(idx)
        self.assertEqual(dll.head.value, 1)
        self.assertEqual(dll1.tail.value, 2)
        self.assertEqual(dll2.head.value, 3)
        self.assertEqual(dll1.tail.next, None)
        self.assertEqual(dll1.head.prev, None)
        self.assertEqual(dll2.tail.next, None)
        self.assertEqual(dll2.head.prev, None)
        self.assertEqual(len(dll1), 2)
        self.assertEqual(len(dll2), 1)

    def test_split_fail(self):
        dll = DoublyLinkedList()
        with self.assertRaises(ValueError):
            dll.split(1)
        dll.append(1)
        with self.assertRaises(ValueError):
            dll.split(1)
        dll.append(2)
        with self.assertRaises(ValueError):
            dll.split(2)
        with self.assertRaises(ValueError):
            dll.split(3)

    def test_str(self):
        dll = DoublyLinkedList()
        self.assertEqual(str(dll), "")
        dll.append(1)
        self.assertEqual(str(dll), "[1]")
        dll.append(2)
        self.assertEqual(str(dll), "[1, 2]")

    def test_merge(self):
        dll1 = DoublyLinkedList()
        dll1.append(1)
        dll1.append(2)
        dll2 = DoublyLinkedList()
        dll2.append(3)
        dll2.append(4)
        dll1 += dll2
        self.assertEqual(dll1.head.value, 1)
        self.assertEqual(dll1.tail.value, 4)
        self.assertEqual(dll1.head.next.value, 2)
        self.assertEqual(dll1.head.prev, None)
        self.assertEqual(dll1.tail.prev.value, 3)
        self.assertEqual(dll1.tail.next, None)
        self.assertEqual(dll1.head.next.next.value, 3)
        self.assertEqual(dll1.tail.prev.prev.value, 2)
        self.assertEqual(len(dll1), 4)

    def test_copy(self):
        import copy
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll_copy = copy.copy(dll)
        self.assertEqual(dll.head.value, dll_copy.head.value)
        self.assertEqual(dll.tail.value, dll_copy.tail.value)
        self.assertEqual(dll.head.next.value, dll_copy.head.next.value)
        self.assertEqual(dll.head.prev, dll_copy.head.prev)
        self.assertEqual(dll.tail.next, dll_copy.tail.next)
        self.assertEqual(dll.head.prev, None)
        self.assertEqual(dll.tail.next, None)
        self.assertEqual(len(dll), len(dll_copy))

    def test_len(self):
        dll = DoublyLinkedList()
        self.assertEqual(len(dll), 0)
        dll.append(1)
        self.assertEqual(len(dll), 1)
        dll.append(2)
        self.assertEqual(len(dll), 2)


class SwapKTest(unittest.TestCase):
    def test_swap_k_success(self):
        a = DoublyLinkedList()
        a.append(1)
        a.append(3)
        a.append(1)

        b = DoublyLinkedList()
        b.append(1)
        b.append(2)
        b.append(1)

        swap_k(a, b, 1)
        self.assertEqual(a.head.value, 1)
        self.assertEqual(a.tail.value, 1)
        self.assertEqual(a.head.next.value, 2)
        self.assertEqual(a.head.prev, None)
        self.assertEqual(a.tail.next, None)

        self.assertEqual(b.head.value, 1)
        self.assertEqual(b.tail.value, 1)
        self.assertEqual(b.head.next.value, 3)
        self.assertEqual(b.head.prev, None)
        self.assertEqual(b.tail.next, None)

    def test_swap_k_fail(self):
        a = DoublyLinkedList()
        a.append(1)
        a.append(2)

        b = DoublyLinkedList()
        b.append(1)
        b.append(2)
        b.append(3)

        with self.assertRaises(ValueError):
            swap_k(a, b, -1)
        with self.assertRaises(ValueError):
            swap_k(a, b, 2)
        with self.assertRaises(ValueError):
            swap_k(a, b, 3)


if __name__ == '__main__':
    unittest.main()
