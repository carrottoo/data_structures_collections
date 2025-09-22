import unittest
from queue_and_stack.circular_queue import CircularQueue

class TestCircularQueue(unittest.TestCase):

    def test_initialization(self):
        """Tests the initial state of the queue."""
        q = CircularQueue(3)
        self.assertTrue(q.isEmpty())
        self.assertFalse(q.isFull())
        self.assertEqual(q.Front(), -1)
        self.assertEqual(q.Rear(), -1)
        self.assertEqual(q.size, 3)

    def test_enQueue_and_deQueue_single_element(self):
        """Tests adding and then removing a single element."""
        q = CircularQueue(5)
        self.assertTrue(q.enQueue(10))
        self.assertFalse(q.isEmpty())
        self.assertEqual(q.Front(), 10)
        self.assertEqual(q.Rear(), 10)
        
        self.assertTrue(q.deQueue())
        self.assertTrue(q.isEmpty())
        self.assertEqual(q.Front(), -1)

    def test_fill_queue_to_capacity(self):
        """Tests enQueue until the queue is full."""
        q = CircularQueue(3)
        self.assertTrue(q.enQueue(1))
        self.assertTrue(q.enQueue(2))
        self.assertTrue(q.enQueue(3))
        
        self.assertTrue(q.isFull())
        self.assertEqual(q.Front(), 1)
        self.assertEqual(q.Rear(), 3)
        
        self.assertFalse(q.enQueue(4))
        self.assertEqual(q.Rear(), 3)

    def test_deQueue_from_empty_queue(self):
        """Tests that deQueue on an empty queue fails."""
        q = CircularQueue(2)
        self.assertFalse(q.deQueue())

        q.enQueue(1)
        q.deQueue()
        self.assertFalse(q.deQueue())

    def test_circular_behavior(self):
        """Tests the core circular functionality of the queue."""
        q = CircularQueue(3)

        q.enQueue(1)
        q.enQueue(2)
        q.enQueue(3)
        self.assertTrue(q.isFull())
        self.assertEqual(q.Front(), 1)

        self.assertTrue(q.deQueue())
        self.assertFalse(q.isFull())
        self.assertEqual(q.Front(), 2)

        self.assertTrue(q.enQueue(4))
        self.assertTrue(q.isFull())
        self.assertEqual(q.Front(), 2) 
        self.assertEqual(q.Rear(), 4)  

    def test_front_and_rear_updates(self):
        """Tests if Front and Rear pointers update correctly."""
        q = CircularQueue(4)
        q.enQueue(10) # F: 10, R: 10
        self.assertEqual(q.Front(), 10)
        self.assertEqual(q.Rear(), 10)
        
        q.enQueue(20) # F: 10, R: 20
        self.assertEqual(q.Front(), 10)
        self.assertEqual(q.Rear(), 20)
        
        q.deQueue() # F: 20, R: 20
        self.assertEqual(q.Front(), 20)
        self.assertEqual(q.Rear(), 20)
        
        q.enQueue(30) # F: 20, R: 30
        q.enQueue(40) # F: 20, R: 40
        self.assertEqual(q.Front(), 20)
        self.assertEqual(q.Rear(), 40)

    def test_edge_case_size_one(self):
        """Tests the queue with the smallest possible size."""
        q = CircularQueue(1)
        self.assertTrue(q.isEmpty())
        
        self.assertTrue(q.enQueue(99))
        self.assertTrue(q.isFull())
        self.assertEqual(q.Front(), 99)
        self.assertEqual(q.Rear(), 99)
        
        self.assertFalse(q.enQueue(100))
        
        self.assertTrue(q.deQueue())
        self.assertTrue(q.isEmpty())
        self.assertFalse(q.deQueue())


if __name__ == '__main__':
    unittest.main()