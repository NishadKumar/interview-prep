import unittest
import merge_intervals

#please feel free to contribute more tests

class TestMergeIntervals(unittest.TestCase):
    def test_merge(self):
        
        self.assertEqual(merge_intervals.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(merge_intervals.merge([[1,4],[4,5]]), [[1,5]])


if __name__ == '__main__':
    unittest.main()

