#!/usr/bin/python3
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    def empty(self):
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def one_item(self):
        test_list = [1]
        self.assertEqual(max_integer(test_list), 1)

    def end_is_max(self):
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(test_list), 5)

    def first_is_max(self):
        test_list = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(test_list), 5)

    def middle_is_max(self):
        test_list = [3, 4, 5, 2, 1]
        self.assertEqual(max_integer(test_list), 5)

    def one_negative(self):
        est_list = [3, 4, 5, 2, -1]
        self.assertEqual(max_integer(test_list), 5)

    def one_negative(self):
        test_list = [3, 4, 5, 2, -1]
        self.assertEqual(max_integer(test_list), 5)

    def all_negative(self):
        test_list = [-3, -4, -5, -2, -1]
        self.assertEqual(max_integer(test_list), -1)
