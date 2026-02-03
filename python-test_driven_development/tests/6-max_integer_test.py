#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_one_item(self):
        test_list = [1]
        self.assertEqual(max_integer(test_list), 1)

    def test_end_is_max(self):
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(test_list), 5)

    def test_first_is_max(self):
        test_list = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(test_list), 5)

    def test_middle_is_max(self):
        test_list = [3, 4, 5, 2, 1]
        self.assertEqual(max_integer(test_list), 5)

    def test_one_negative(self):
        est_list = [3, 4, 5, 2, -1]
        self.assertEqual(max_integer(test_list), 5)

    def test_one_negative(self):
        test_list = [3, 4, 5, 2, -1]
        self.assertEqual(max_integer(test_list), 5)

    def test_all_negative(self):
        test_list = [-3, -4, -5, -2, -1]
        self.assertEqual(max_integer(test_list), -1)
