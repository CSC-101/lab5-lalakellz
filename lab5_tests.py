import data
import lab5
import unittest


# Write your test cases for each part below.
from lab5 import Time, time_add, is_descending


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
        self.assertTrue(is_descending([5.0, 4.0, 3.0, 2.0]))

    def test_descending_2(self):
        self.assertFalse([1.0, 2.0, 3.0])

    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
