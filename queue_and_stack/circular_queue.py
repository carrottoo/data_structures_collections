"""
    An implementation of circular queue. In reality, deque (built-in double - ended queue) is a 
    better choice in most cases.
"""

class CircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.tail:  # Queue is now empty
            self.queue[self.head] = None
            self.head = -1
            self.tail = -1
        else:
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.size == self.head 