import unittest
import move_zeroes

#please feel free to contribute more tests

class TestMoveZeroesToBeginning(unittest.TestCase):
    def test_move_zeroes(self):
        
        self.assertEqual(move_zeroes.move_zeroes_beginning([0, 13, 5, 4, 0, 9, 0]), [0, 0, 0, 13, 5, 4, 9])
        self.assertEqual(move_zeroes.move_zeroes_beginning([]), [])
        self.assertEqual(move_zeroes.move_zeroes_beginning(None), None)
        self.assertEqual(move_zeroes.move_zeroes_beginning([0]), [0])
        self.assertEqual(move_zeroes.move_zeroes_beginning([3, 0]), [0, 3])
        
        
        
if __name__ == '__main__':
    unittest.main()

