from unittest import TestCase

from lesson_03_functions import fibonacci


class TestFibLoop(TestCase):

    # check value
    def test_fib_loop(self):
        self.assertEqual(fibonacci.fib_loop(3), 2)

    # check TypeError
    def test_type(self):
        self.assertRaises(TypeError, fibonacci.fib_loop, 'sdf')

    def test_error(self):
        self.assertRaises(TypeError, fibonacci.fib_loop, None)

    # check Assertion = True
    def test_true(self):
        self.assertTrue(fibonacci.fib_loop, -1)

