import unittest
import reverse_traversal

#please feel free to contribute more tests

class TestReverseTraversal(unittest.TestCase):
    def test_reverse_traversal(self):
        
        self.assertEqual(reverse_traversal.reverse_traversal_array([0, 2, 1, -1, -1]), [0, 0, 2, 2, 1])
        self.assertEqual(reverse_traversal.reverse_traversal_array([0, -1]), [0,0])
        self.assertEqual(reverse_traversal.reverse_traversal_array([1, 3, 5, 7]), [1, 3, 5, 7])
        self.assertEqual(reverse_traversal.reverse_traversal_array([2, 4, 6, 8, -1, -1, -1, -1]), [2, 2, 4, 4, 6, 6, 8, 8])
        self.assertEqual(reverse_traversal.reverse_traversal_array([]), [])
        self.assertEqual(reverse_traversal.reverse_traversal_array(None), None)
        
if __name__ == '__main__':
    unittest.main()

