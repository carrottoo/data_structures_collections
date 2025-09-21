import heapq
from typing import Any, Union

"""
    An implementation of priority queue that allows user to remove an added item. 
    You can also implement it without using two helper sets. It is possible to do
    only by adding version control. Here we want to avoid adding same items twice,
    so two helper sets is preferred. 
"""
class RemovableHeapQ:
    def __init__(self):
        self.heap = []
        self.added = set()
        self.masked = set()

    def add(self, item: Any) -> None:
        if item not in self.added:
            heapq.heappush(self.heap, item)
            self.added.add(item)
        
        if item in self.masked:
            self.masked.remove(item)
    
    def remove(self, item: Any) -> None:
        self.masked.add(item)

    def pop(self) -> Union[Any, None]:
        while self.heap:
            top = heapq.heappop(self.heap)
            self.added.remove(top)
            if top not in self.masked:
                return top
        return None

    


