#!/usr/bin/python3
"""
Unittests for max_integer([..]).

Test cases for the max_integer function covering various scenarios.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Define unittests for max_integer([..]).

    This class contains test cases to verify the behavior of the max_integer function
    under different conditions, including ordered and unordered lists, single-element lists,
    lists containing floats, strings, and empty lists.
    """

    def test_ordered_list(self):
        """
        Test max_integer with an ordered list of integers.

        Verifies that max_integer returns the correct maximum value from an ordered list.
        """
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """
        Test max_integer with an unordered list of integers.

        Checks if max_integer correctly identifies the maximum value in an unordered list.
        """
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """
        Test max_integer with a list where the max value is at the beginning.

        Validates that max_integer can handle a list where the maximum value is at the beginning.
        """
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """
        Test max_integer with an empty list.

        Checks if max_integer returns None when given an empty list.
        """
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_one_element_list(self):
        """
        Test max_integer with a list containing a single element.

        Verifies that max_integer correctly handles a list with a single element.
        """
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """
        Test max_integer with a list of floating-point numbers.

        Ensures that max_integer works correctly with a list of floating-point numbers.
        """
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """
        Test max_integer with a list containing both integers and floats.

        Checks if max_integer can handle a list with a mix of integers and floating-point numbers.
        """
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """
        Test max_integer with a string input.

        Verifies that max_integer correctly handles a string input by returning the maximum character.
        """
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """
        Test max_integer with a list of strings.

        Checks if max_integer can identify the maximum string based on lexicographical order.
        """
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """
        Test max_integer with an empty string.

        Validates that max_integer returns None when given an empty string.
        """
        self.assertIsNone(max_integer(""))

if __name__ == '__main__':
    unittest.main()
