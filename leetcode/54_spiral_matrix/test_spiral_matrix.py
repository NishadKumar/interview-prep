import unittest
import spiral_matrix

#please feel free to contribute more tests

class TestSpiralMatrix(unittest.TestCase):
    def test_spiral_matrix(self):

        self.assertEqual(spiral_matrix.spiral_order([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(spiral_matrix.spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7] )


if __name__ == '__main__':
    unittest.main()

