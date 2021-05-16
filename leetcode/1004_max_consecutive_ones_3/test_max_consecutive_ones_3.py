import unittest
import max_consecutive_ones_3

#please feel free to contribute more tests

class TestMaxConsecutiveOnes(unittest.TestCase):
    def test_longest_ones(self):
        
        self.assertEqual(max_consecutive_ones_3.longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2), 6)
        self.assertEqual(max_consecutive_ones_3.longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10)


if __name__ == '__main__':
    unittest.main()

