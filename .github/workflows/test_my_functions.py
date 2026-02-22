# test_my_functions.py
import unittest
from my_functions import add

class TestAdd(unittest.TestCase):
    """Test cases for the add function."""

    def test_add_positives(self):
        """Test the addition of two positive numbers."""
        result = add(1, 2)
        self.assertEqual(result, 3) #

    def test_add_negatives(self):
        """Test the addition of two negative numbers."""
        result = add(-1, -1)
        self.assertEqual(result, -2) #

    def test_add_zero(self):
        """Test the addition with zero."""
        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_add_float_and_int(self):
        """Test the addition of a float and an integer."""
        result = add(1.5, 2)
        self.assertEqual(result, 3.5)

    def test_add_string_fail(self):
        """Verify that adding strings raises a TypeError (if applicable to your function's intended behavior)."""
        # Example for testing if an exception is raised
        with self.assertRaises(TypeError): #
            add("a", "b")

if __name__ == '__main__':
    unittest.main() #
