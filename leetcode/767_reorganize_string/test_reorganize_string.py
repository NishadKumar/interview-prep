import unittest
import reorganize_string

#please feel free to contribute more tests

class TestReorganizeString(unittest.TestCase):
    def test_reorganize_string(self):

        self.assertEqual(reorganize_string.reorganize_string("aab"), "aba")
        self.assertEqual(reorganize_string.reorganize_string("aaaaaba"), "")
        self.assertEqual(reorganize_string.reorganize_string("xxyz"), "xyxz")
        self.assertEqual(reorganize_string.reorganize_string("qqqqqq"), "")
        

if __name__ == '__main__':
    unittest.main()

