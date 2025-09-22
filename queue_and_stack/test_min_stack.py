import unittest
from queue_and_stack.min_stack import MinStack

class TestMinStack(unittest.TestCase):

    def test_initial_state(self):
        """Tests the initial state of the MinStack."""
        stack = MinStack()
        self.assertIsNone(stack.top())
        self.assertIsNone(stack.getMin())

    def test_push_and_top(self):
        """Tests pushing elements and checking the top."""
        stack = MinStack()
        stack.push(5)
        self.assertEqual(stack.top(), 5)
        stack.push(10)
        self.assertEqual(stack.top(), 10)
        stack.push(2)
        self.assertEqual(stack.top(), 2)

    def test_pop(self):
        """Tests the pop functionality."""
        stack = MinStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.top(), 3)
        stack.pop()
        self.assertEqual(stack.top(), 2)
        stack.pop()
        self.assertEqual(stack.top(), 1)
        stack.pop()
        self.assertIsNone(stack.top())
        # Popping from an empty stack should not raise an error
        stack.pop() 
        self.assertIsNone(stack.top())

    def test_getMin_updates_correctly_on_push(self):
        """Tests if getMin returns the correct minimum as elements are pushed."""
        stack = MinStack()
        stack.push(10)
        self.assertEqual(stack.getMin(), 10)
        stack.push(5)
        self.assertEqual(stack.getMin(), 5)
        stack.push(12)
        self.assertEqual(stack.getMin(), 5)
        stack.push(3)
        self.assertEqual(stack.getMin(), 3)
        stack.push(3)
        self.assertEqual(stack.getMin(), 3)

    def test_getMin_updates_correctly_on_pop(self):
        """Tests if getMin returns the correct minimum as elements are popped."""
        stack = MinStack()
        stack.push(5)
        stack.push(3)
        stack.push(4)
        stack.push(1)
        stack.push(2)
        
        self.assertEqual(stack.getMin(), 1)
        stack.pop() # Pop 2
        self.assertEqual(stack.getMin(), 1)
        stack.pop() # Pop 1
        self.assertEqual(stack.getMin(), 3)
        stack.pop() # Pop 4
        self.assertEqual(stack.getMin(), 3)
        stack.pop() # Pop 3
        self.assertEqual(stack.getMin(), 5)
        stack.pop() # Pop 5
        self.assertIsNone(stack.getMin())

    def test_getMin_with_duplicate_minimums(self):
        """Tests getMin when the minimum value appears multiple times."""
        stack = MinStack()
        stack.push(5)
        stack.push(2)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.getMin(), 2)
        stack.pop() # Pop 3
        self.assertEqual(stack.getMin(), 2)
        stack.pop() # Pop 2
        self.assertEqual(stack.getMin(), 2)
        stack.pop() # Pop 2
        self.assertEqual(stack.getMin(), 5)


if __name__ == '__main__':
    unittest.main()