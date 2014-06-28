#!/usr/bin/python
#
# Copyright (c) 2013 Benjamin Geiger <begeiger@mail.usf.edu>

"""
Module-specific doc string.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function

import sys
if sys.version_info < (3, 0):
    input = raw_input

import unittest
import FuncProg

class TestPart1(unittest.TestCase):
    def setUp(self):
        self.f = lambda x: x * x
        self.g = lambda x: x + 1

    def test_no_application(self):
        out = FuncProg.repeat(self.f, 2, 0)
        self.assertEqual(2, out, "repeat with count of 0 should return input")

    def test_one_application(self):
        out = FuncProg.repeat(self.f, 2, 1)
        self.assertEqual(4, out, "repeat with count of 1 should return f(x)")

    def test_two_applications(self):
        out = FuncProg.repeat(self.f, 2, 2)
        self.assertEqual(16, out, "repeat with count of 2 should return f(f(x))")

    def test_many_applications(self):
        out = FuncProg.repeat(self.g, 2, 100)
        self.assertEqual(102, out, "repeat should work for high repeat counts")


class TestPart2(unittest.TestCase):
    def setUp(self):
        self.f1 = lambda x: x * x
        self.f2 = lambda x: x % 2 != 0

    def test_map_on_empty_list(self):
        out = FuncProg.my_map(self.f1, [])
        self.assertEqual([], out, "map over an empty list should return empty list")

    def test_map_on_single_element_list(self):
        out = FuncProg.my_map(self.f1, [2])
        self.assertEqual([4], out, "map over single element [x] should return [f(x)]")

    def test_map_on_multiple_element_list(self):
        out = FuncProg.my_map(self.f1, [1, 2, 3, 4, 5])
        self.assertEqual([1, 4, 9, 16, 25], out, "map over multiple elements should work")

    def test_filter_on_empty_list(self):
        out = FuncProg.my_filter(self.f2, [])
        self.assertEqual([], out, "filter over empty list should always return empty list")

    def test_filter_on_single_kept_element_list(self):
        out = FuncProg.my_filter(self.f2, [1])
        self.assertEqual([1], out, "filter over single element matching function should return that element")

    def test_filter_on_single_unkept_element_list(self):
        out = FuncProg.my_filter(self.f2, [2])
        self.assertEqual([], out, "filter over single element not matching function should return empty list")

    def test_filter_on_multiple_element_list(self):
        out = FuncProg.my_filter(self.f2, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual([1, 3, 5, 7, 9], out, "filter over multiple element list should work")


class TestPart3(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_input(self):
        even, odd = FuncProg.splitList([])

        self.assertEqual([], even, "splitList with empty input should return empty even list")
        self.assertEqual([], odd, "splitList with empty input should return empty odd list")

    def test_single_element_input(self):
        even, odd = FuncProg.splitList([1])

        self.assertEqual([1], even, "splitList with one-element input should return one-element even list")
        self.assertEqual([], odd, "splitList with one-element input should return empty odd list")

    def test_two_element_input(self):
        even, odd = FuncProg.splitList([1, 2])

        self.assertEqual([1], even, "splitList with two-element input should return one-element even list")
        self.assertEqual([2], odd, "splitList with two-element input should return one-element odd list")

    def test_many_element_input(self):
        even, odd = FuncProg.splitList([0, 1, 2, 3, 4, 5])

        self.assertEqual([0, 2, 4], even, "splitList should return even list with even elements")
        self.assertEqual([1, 3, 5], odd, "splitList should return odd list with odd elements")


if __name__ == "__main__":
    unittest.main()

# vim: set et sw=4 ts=4: