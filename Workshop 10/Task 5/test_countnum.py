"""
Import the unittest module and the countnum module.
Define a test class named TestCountNum that extends unittest.TestCase.
Inside the test class, define two test methods:
   test_boundary_edge_cases: This method tests the function countNum with boundary and edge cases, asserting that the results match the expected values.
   test_invalid_input_cases: This method tests the function countNum with invalid input cases, asserting that the function raises the appropriate exceptions.
In each test method, use assertions to compare the actual output of the countNum function with the expected output or to check if the function raises the expected exceptions.
Use the unittest.main() function to run the test suite when the script is executed directly.
"""

import unittest
import countnum

class TestCountNum(unittest.TestCase):
    def test_boundary_edge_cases(self):
        self.assertEqual(countnum.countNum(1, 5, 8), 0) 
        self.assertEqual(countnum.countNum(1, 500, 2), 176)
        self.assertEqual(countnum.countNum(-50, -5, 6), 5)
        self.assertEqual(countnum.countNum(100, 1000, 42), 19)
        self.assertEqual(countnum.countNum(1, 12, 1), 4)
        self.assertEqual(countnum.countNum(5, 5, 5), 1)

    def test_invalid_input_cases(self):
        self.assertRaises(TypeError, countnum.countNum, 1.5, 9, 5)
        self.assertRaises(TypeError, countnum.countNum, 1, 9.5, 5)
        self.assertRaises(TypeError, countnum.countNum, 1, 9, 5.5)
        self.assertRaises(TypeError, countnum.countNum, 'A', 9, 5)
        self.assertRaises(TypeError, countnum.countNum, 1, 'A', 5)
        self.assertRaises(TypeError, countnum.countNum, 1, 9, 'A')
        self.assertRaises(ValueError, countnum.countNum, 9, 1, 5)
        self.assertRaises(ValueError, countnum.countNum, 1, 9, -5)

if __name__ == '__main__':
    unittest.main()
