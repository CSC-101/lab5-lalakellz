import data
import lab5
import unittest


# Write your test cases for each part below.
from lab5 import Time, time_add, is_descending, largest_between, furthest_from_origin, Point


class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add(self):
        time1 = Time(1, 20, 30)
        time2 = Time(2, 10, 25)
        result = time_add(time1, time2)
        self.assertEqual(result, Time(3, 30, 55))

    def test_time_add_2(self):
        time1 = Time(1, 45, 50)
        time2 = Time(2, 20, 15)
        result = time_add(time1, time2)
        self.assertEqual(result, Time(4, 6, 5))

    # Part 4
    def test_descending(self):
        nums = [5.0, 4.0, 3.0, 2.0, 1.0]
        result = is_descending(nums)
        self.assertTrue(result)

    def test_descending_2(self):
        nums = [1.0, 2.0, 3.0]
        result = is_descending(nums)
        self.assertFalse(result)

    # Part 5
    def test_large(self):
        nums = [1, 3, 5, 7, 9]
        result = largest_between(nums, 1, 3)
        self.assertEqual(result, 3)

    def test_large_2(self):
        nums = [1, 3, 5, 7, 9]
        result = largest_between(nums, 3, 1)
        self.assertIsNone(result)

    def test_large_3(self):
        numbers = [1, 3, 5, 7, 9]
        result = largest_between(numbers, -5, 10)
        self.assertEqual(result, 4)

    # Part 6
    def test_furthest(self):
        points = [Point(1, 1), Point(3, 4), Point(6, 8)]
        result = furthest_from_origin(points)
        self.assertEqual(result, 2)

    def test_furthest_2(self):
        points = []
        result = furthest_from_origin(points)
        self.assertIsNone(result)



if __name__ == '__main__':
    unittest.main()
