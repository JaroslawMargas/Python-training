from unittest import TestCase
from lesson_03_functions import collatz


class TestColCheck(TestCase):

    def test_string(self):
        self.assertRaises(TypeError, collatz.col_check, 'aoeu')

    def test_8(self):
        self.assertEqual(collatz.col_check(8), 4)

    def test_16(self):
        self.assertEqual(collatz.col_check(16), 8)
