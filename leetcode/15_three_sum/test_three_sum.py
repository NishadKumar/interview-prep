import unittest
import three_sum

#please feel free to contribute more tests

class TestThreeSum(unittest.TestCase):
    def test_three_sum(self):
        
        self.assertEqual(three_sum.three_sum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(three_sum.three_sum([0]), [])
        self.assertEqual(three_sum.three_sum([]), [])


if __name__ == '__main__':
    unittest.main()

