"""
    An efficient data structure to support two operations
    1. Find the component to which an element belongs to.
       find(x) == find(y) <==> x and y in the same component
    2. Merge two components by allowing an edge to enable travelling between them.

    In reality, you can have many other ways to implement similar ideas depending on the problems. 
    This a general version for reference. 
"""
class UnionFind:
    def __init__(self, size: int):
        self.parent = []
        self.compontent_lengths = []
        for i in range(size):
            self.parent.append(i)
            self.compontent_lengths.append(1)

    def find(self, x: int):
        if x < 0 or x >= len(self.parent):
            raise ValueError('Invalid node position, cannot be larger than its parent length or smaller than 0')
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.compontent_lengths[x] < self.compontent_lengths[y]:
            x, y = y, x
        self.parent[y] = x
        self.compontent_lengths[x] += self.compontent_lengths[y]