import unittest
import smallest_common_region

#please feel free to contribute more tests

class TestSmallestCommonRegion(unittest.TestCase):
    def test_smallest_common_region(self):
        
        self.assertEqual(smallest_common_region.find_smallest_region([  ["Earth","North America","South America"],
                                                                        ["North America","United States","Canada"],
                                                                        ["United States","New York","Boston"],
                                                                        ["Canada","Ontario","Quebec"],
                                                                        ["South America","Brazil"]], "Quebec", "New York"), "North America")
        self.assertEqual(smallest_common_region.find_smallest_region([  ["Earth", "North America", "South America"],
                                                                        ["North America", "United States", "Canada"],
                                                                        ["United States", "New York", "Boston"],
                                                                        ["Canada", "Ontario", "Quebec"],
                                                                        ["South America", "Brazil"]], "Canada", "Quebec"), "Canada")
        
if __name__ == '__main__':
    unittest.main()

