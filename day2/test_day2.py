#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from day2.day2 import PasswordChecker
import os.path


class Day2TestCase(unittest.TestCase):
    def setUp(self):
        self._day2 = PasswordChecker(
            os.path.join(os.path.abspath(os.path.dirname(__file__)), "test_data.txt")
        )
