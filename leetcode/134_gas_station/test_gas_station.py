import unittest
import gas_station

#please feel free to contribute more tests

class TestCourseSchedule2(unittest.TestCase):
    def test_gas_station(self):

        self.assertEqual(gas_station.can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]), 3)
        self.assertEqual(gas_station.can_complete_circuit([2,3,4], [3,4,3]), -1)

if __name__ == '__main__':
    unittest.main()

