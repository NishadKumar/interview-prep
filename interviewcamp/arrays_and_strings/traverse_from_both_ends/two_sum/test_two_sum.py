import unittest
import two_sum

#please feel free to contribute more tests

class TestTwoSum(unittest.TestCase):
    def test_two_sum_target(self):
        
        self.assertEqual(two_sum.two_sum_target([], 1), [])
        self.assertEqual(two_sum.two_sum_target(None, 5), None)
        self.assertEqual(two_sum.two_sum_target([1, 3, 5, 9], 8), [3, 5])
        self.assertEqual(two_sum.two_sum_target([1, 3, 5, 7], 9), [-1, -1])
        
if __name__ == '__main__':
    unittest.main()

