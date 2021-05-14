import unittest
import course_schedule

#please feel free to contribute more tests

class TestCourseSchedule(unittest.TestCase):
    def test_can_finish(self):
        #when there are no cycles
        self.assertEqual(course_schedule.can_finish(2, [[1,0]]), True)
        self.assertEqual(course_schedule.can_finish(4, [[1,2],[2,3],[3,4]]), True)
        self.assertEqual(course_schedule.can_finish(5,[[2,3],[0,4],[4,1],[1,2]]), True)

        #when there are cycles
        self.assertEqual(course_schedule.can_finish(2, [[0,1],[1,0]]), False)
        self.assertEqual(course_schedule.can_finish(5, [[2,4],[0,4],[4,1],[1,2]]), False)
        

if __name__ == '__main__':
    unittest.main()

