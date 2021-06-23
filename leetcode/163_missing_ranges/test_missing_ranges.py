import unittest
import missing_ranges

#please feel free to contribute more tests

class TestMissingRanges(unittest.TestCase):
    def test_missing_ranges(self):
        
        self.assertEqual(missing_ranges.find_missing_ranges([0,1,3,50,75], 0, 99), ["2","4->49","51->74","76->99"])
        self.assertEqual(missing_ranges.find_missing_ranges([], 1, 1), ["1"])
        self.assertEqual(missing_ranges.find_missing_ranges([], -3, -1), ["-3->-1"])
        self.assertEqual(missing_ranges.find_missing_ranges([-1], -1, -1), [])
        
if __name__ == '__main__':
    unittest.main()

