import unittest
import partition_3_parts

#please feel free to contribute more tests

class TestPartition3Parts(unittest.TestCase):
    def test_partition(self):
        
        self.assertEqual(partition_3_parts.partition_three_parts([0,2,1,-6,6,-7,9,1,2,0,1]), True)
        self.assertEqual(partition_3_parts.partition_three_parts([0,2,1,-6,6,7,9,-1,2,0,1]), False)
        self.assertEqual(partition_3_parts.partition_three_parts([3,3,6,5,-2,2,5,1,-9,4]), True)
        self.assertEqual(partition_3_parts.partition_three_parts([0,0,0,0]), True)
        
        
if __name__ == '__main__':
    unittest.main()

