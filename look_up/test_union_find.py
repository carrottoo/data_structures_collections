import unittest
from look_up.union_find import UnionFind

class TestUnionFind(unittest.TestCase):

    def test_initialization(self):
        """Tests if the data structure is initialized correctly."""
        uf = UnionFind(10)
        # All elements should be their own parent
        self.assertEqual(uf.parent, list(range(10)))
        self.assertEqual(uf.compontent_lengths, [1] * 10)

    def test_find_initial_state(self):
        """Tests the find operation on a newly initialized structure."""
        uf = UnionFind(5)
        for i in range(5):
            self.assertEqual(uf.find(i), i)
            
    def test_simple_union(self):
        """Tests a basic union of two elements."""
        uf = UnionFind(5)
        uf.union(0, 1)

        self.assertEqual(uf.find(0), uf.find(1))
        self.assertNotEqual(uf.find(0), uf.find(2))

    def test_union_by_size(self):
        """Tests that the smaller tree is attached to the larger one."""
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(2, 3)
        
        self.assertEqual(uf.compontent_lengths[uf.find(0)], 2)
        self.assertEqual(uf.compontent_lengths[uf.find(2)], 2)
        
        uf.union(0, 2)

        root = uf.find(0)
        self.assertEqual(root, 0)
        
        self.assertEqual(uf.parent[2], 0)
        
        self.assertEqual(uf.compontent_lengths[root], 4)

    def test_union_of_same_set(self):
        """Tests that uniting elements already in the same set does nothing."""
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        
        root = uf.find(0)
        initial_size = uf.compontent_lengths[root]
        initial_parents = list(uf.parent)
        
        uf.union(0, 2)
        
        self.assertEqual(uf.compontent_lengths[root], initial_size)
        self.assertEqual(uf.parent, initial_parents)

    def test_path_compression(self):
        """Tests if path compression is working correctly."""
        uf = UnionFind(5)
        # Create a chain: 0 -> 1 -> 2 -> 3
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)
        
        # At this point, the parent of 3 might be 2.
        # After calling find(3), its parent should be compressed to the root (0).
        root = uf.find(3)
        self.assertEqual(root, 0)
        self.assertEqual(uf.parent[3], 0)

    def test_complex_unions(self):
        """Tests a more complex sequence of unions."""
        uf = UnionFind(10)
        uf.union(0, 2)
        uf.union(1, 3)
        uf.union(4, 6)
        uf.union(5, 7)
        uf.union(0, 3) # Merges sets {0, 2} and {1, 3}
        uf.union(4, 5) # Merges sets {4, 6} and {5, 7}
        uf.union(0, 4) # Merges the two large sets

        root = uf.find(0)
        for i in range(8):
            self.assertEqual(uf.find(i), root)
        
        # 8 and 9 are in their own sets
        self.assertNotEqual(uf.find(8), root)
        self.assertNotEqual(uf.find(9), root)
        self.assertEqual(uf.find(8), 8)
        self.assertEqual(uf.find(9), 9)

    def test_find_out_of_bounds_raises_error(self):
        """Tests that find() raises ValueError for out-of-bounds indices."""
        uf = UnionFind(10)
        
        with self.assertRaises(ValueError):
            uf.find(10)
            
        with self.assertRaises(ValueError):
            uf.find(-1)
            
        with self.assertRaises(ValueError):
            uf.find(100)

if __name__ == '__main__':
    unittest.main()