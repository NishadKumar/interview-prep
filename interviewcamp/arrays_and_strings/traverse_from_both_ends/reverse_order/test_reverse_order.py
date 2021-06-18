import unittest
import reverse_order

#please feel free to contribute more tests

class TestReverseOrder(unittest.TestCase):
    def test_reverse_traverse_array(self):
        
        self.assertEqual(reverse_order.reverse_order_array([]), [])
        self.assertEqual(reverse_order.reverse_order_array(None), None)
        self.assertEqual(reverse_order.reverse_order_array([1, 3, 5, 7]), [7, 5, 3, 1])
        self.assertEqual(reverse_order.reverse_order_array([0, 0, 0]), [0, 0, 0])
        self.assertEqual(reverse_order.reverse_order_array([5]), [5])
        
        
if __name__ == '__main__':
    unittest.main()

