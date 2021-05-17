import unittest
import course_schedule_2

#please feel free to contribute more tests

class TestCourseSchedule2(unittest.TestCase):
    def test_find_order(self):

        self.assertEqual(course_schedule_2.find_order(2, [[1,0]]), [0,1])
        self.assertEqual(course_schedule_2.find_order(4, [[1,0],[2,0],[3,1],[3,2]]), [0,1,2,3])
        self.assertEqual(course_schedule_2.find_order(1, []), [0])


if __name__ == '__main__':
    unittest.main()

