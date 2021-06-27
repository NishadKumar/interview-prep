import unittest
import minimum_knight_moves

#please feel free to contribute more tests

class TestMinimumKnightMoves(unittest.TestCase):
    def test_minumum_knight_moves(self):
        
        self.assertEqual(minimum_knight_moves.min_moves(2, 1), 1)
        self.assertEqual(minimum_knight_moves.min_moves(5,5), 4)
        
if __name__ == '__main__':
    unittest.main()

