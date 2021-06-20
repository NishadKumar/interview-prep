import unittest
import move_zeroes_end

#please feel free to contribute more tests

class TestMoveZeroesToEnd(unittest.TestCase):
    def test_move_zeroes(self):
        
        self.assertEqual(move_zeroes_end.move_zeroes([0, 13, 5, 4, 0, 9, 0]), [13, 5, 4, 9, 0, 0, 0])
        self.assertEqual(move_zeroes_end.move_zeroes([]), [])
        self.assertEqual(move_zeroes_end.move_zeroes(None), None)
        self.assertEqual(move_zeroes_end.move_zeroes([0]), [0])
        self.assertEqual(move_zeroes_end.move_zeroes([0, 3]), [3, 0])
        
        
        
if __name__ == '__main__':
    unittest.main()

