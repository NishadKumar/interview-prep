import unittest
import find_pivot_index

#please feel free to contribute more tests

class TestFindPivotIndex(unittest.TestCase):
    def test_find_pivot_index(self):

        self.assertEqual(find_pivot_index.pivot_index([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(find_pivot_index.pivot_index([1, 2, 3]), -1)
        self.assertEqual(find_pivot_index.pivot_index([2, 1, -1]), 0)
        

if __name__ == '__main__':
    unittest.main()

