import unittest
from unittest.mock import patch
from stack import Stack, input_stacks


class StackTest(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.stack, [])

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.stack, [1])
        stack.push(2)
        self.assertEqual(stack.stack, [1, 2])
        stack.push(3)
        self.assertEqual(stack.stack, [1, 2, 3])

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)


class InputTest(unittest.TestCase):
    def test_input(self):
        stack_even = Stack()
        stack_odd = Stack()
        with patch('builtins.input', return_value='q'):
            input_stacks(stack_even, stack_odd)
            self.assertEqual(stack_even.stack, [])
            self.assertEqual(stack_odd.stack, [])
        with patch('builtins.input', side_effect=['1', '1.5', 'm', '2', '3', 'q']):
            input_stacks(stack_even, stack_odd)
            self.assertEqual(stack_even.stack, [2])
            self.assertEqual(stack_odd.stack, [1, 3])


if __name__ == '__main__':
    unittest.main()
