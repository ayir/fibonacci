from django.test import TestCase
from app.utils import fibonacci_calculation


class FibonacciTest(TestCase):

    def test_negative_number(self):
        """
        Calling fibonacci at a negative number should raise an index error.
        """
        with self.assertRaises(IndexError):
            fibonacci_calculation(-2)

    def test_zero_length(self):
        """
        Calling fibonacci(0) should return a 0.
        """
        self.assertEqual(fibonacci_calculation(0),0)

    def test_positive_numbers(self):
        """
        Calling fibonacci with a positive number should return a
        """
        self.assertEqual(fibonacci_calculation(5), 5)
        self.assertEqual(fibonacci_calculation(7),13)

    def test_not_a_number(self):
        with self.assertRaises(TypeError):
            fibonacci_calculation("Hii")