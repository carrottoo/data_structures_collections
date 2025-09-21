import unittest
from priority_queue.removable_heap import RemovableHeapQ

class TestRemovableHeapQ(unittest.TestCase):
    def setUp(self):
        self.removable_heapq = RemovableHeapQ()

    def test_add_and_pop_single_item(self):
        """Tests adding one item and then popping it."""
        self.removable_heapq.add(10)
        self.assertEqual(self.removable_heapq.pop(), 10)
        self.assertIsNone(self.removable_heapq.pop())

    def test_add_multiple_items_and_pop_in_order(self):
        """Tests if items are popped in correct min-heap (ascending) order."""
        items = [5, 1, 9, 3, 7]
        for item in items:
            self.removable_heapq.add(item)
        
        popped_items = []
        while (item := self.removable_heapq.pop()) is not None:
            popped_items.append(item)
        
        self.assertEqual(popped_items, sorted(items))

    def test_add_duplicate_item(self):
        """Tests that adding a duplicate item has no effect on the heap's contents."""
        self.removable_heapq.add(5)
        self.removable_heapq.add(3)
        self.removable_heapq.add(5)  # This duplicate should be ignored
  
        self.assertEqual(len(self.removable_heapq.heap), 2)
        self.assertEqual(self.removable_heapq.pop(), 3)
        self.assertEqual(self.removable_heapq.pop(), 5)
        self.assertIsNone(self.removable_heapq.pop())

    def test_pop_from_empty_heap(self):
        """Tests that popping from an empty heap returns None."""
        self.assertIsNone(self.removable_heapq.pop())

    def test_remove_item_from_middle(self):
        """Tests removing an item from the middle and ensuring it's not popped."""
        self.removable_heapq.add(5)
        self.removable_heapq.add(1)
        self.removable_heapq.add(9)
        
        self.removable_heapq.remove(5) # Mask the middle element
        
        self.assertEqual(self.removable_heapq.pop(), 1)
        self.assertEqual(self.removable_heapq.pop(), 9)
        self.assertIsNone(self.removable_heapq.pop())

    def test_remove_top_item(self):
        """Tests removing the smallest (top) item before popping."""
        self.removable_heapq.add(5)
        self.removable_heapq.add(1)
        self.removable_heapq.add(9)
        
        self.removable_heapq.remove(1) # Mask the top element
        
        self.assertEqual(self.removable_heapq.pop(), 5)
        self.assertEqual(self.removable_heapq.pop(), 9)
        self.assertIsNone(self.removable_heapq.pop())

    def test_remove_nonexistent_item(self):
        """Tests that removing an item that was never added doesn't cause an error."""
        self.removable_heapq.add(10)
        self.removable_heapq.remove(99) # This should not raise an error
        self.assertEqual(self.removable_heapq.pop(), 10)
        self.assertIsNone(self.removable_heapq.pop())

    def test_re_add_removed_item(self):
        """Tests that re-adding a removed (masked) item makes it available again."""
        self.removable_heapq.add(5)
        self.removable_heapq.add(1)
        
        self.removable_heapq.remove(1)
        self.assertEqual(self.removable_heapq.pop(), 5, "Popped 5, as 1 was removed")
        
        self.removable_heapq.add(1) # Add 1 back, which unmasks it
        self.assertEqual(self.removable_heapq.pop(), 1, "Popped 1 after re-adding it")
        self.assertIsNone(self.removable_heapq.pop())

    def test_complex_sequence_of_operations(self):
        """Tests a mixed sequence of add, remove, and pop to check state management."""
        self.removable_heapq.add(10)
        self.removable_heapq.add(20)
        self.removable_heapq.add(5)
        
        # Current items: {5, 10, 20}
        self.removable_heapq.remove(5)  # Mask 5
        self.removable_heapq.add(30)
        self.removable_heapq.add(15)
        
        # Pop should skip 5 and return 10
        self.assertEqual(self.removable_heapq.pop(), 10)
        
        self.removable_heapq.remove(30) # Mask 30
        self.removable_heapq.add(5)     # Unmask 5 by adding it back
        
        # Pop should now return 5
        self.assertEqual(self.removable_heapq.pop(), 5)
        self.assertEqual(self.removable_heapq.pop(), 15)
        
        self.removable_heapq.add(30)    # Unmask 30 by adding it back
        
        # Pop should skip the initially added 20, then pop 30
        self.assertEqual(self.removable_heapq.pop(), 20)
        self.assertEqual(self.removable_heapq.pop(), 30)
        self.assertIsNone(self.removable_heapq.pop())


if __name__ == "__main__":
    unittest.main()