"""
 Define the `countNum` function:
    Check if all input arguments are integers using a list comprehension and the isinstance function.
    Raise a TypeError if any input argument is not an integer.
    Raise a ValueError if the start value is greater than the end value or if the num value is negative.
    Initialize count to 0.
    Iterate over the range from start to end.
      Convert each number to a string and check if the string representation of num is contained within it.
      If found, increment count.
    Return count, representing the number of occurrences of num within the specified range.

 Define a function named run_tests to test the countNum function:
    Define a list of valid test cases, each containing the start, end, num, and expected output.
    Iterate over the valid test cases:
      Call the countNum function with the input parameters.
      Assert that the result matches the expected output.
      If an exception (TypeError or ValueError) occurs during the test, print "Test failed: <exception message>".
   
    Define a list of invalid test cases, each containing invalid input parameters.
    Iterate over the invalid test cases:
      Call the countNum function with the invalid input parameters.
      If the function does not raise an exception, print "Test failed: Function did not raise an exception for invalid input".
 If the script is run as the main program, call the run_tests function.
 Print "All tests passed successfully." at the end of the testing function.

"""

def countNum(start, end, num):
    
    if not all(isinstance(arg, int) for arg in [start, end, num]):
        raise TypeError("All inputs must be integers")
    if start > end:
        raise ValueError("Start value cannot be greater than end value")
    if num < 0:
        raise ValueError("Num value cannot be negative")
    
    count = 0
    for i in range(start, end + 1):  
        if str(num) in str(i):
            count += 1
    return count

def run_tests():
    tests = [
        (1, 5, 8, 0), 
        (1, 500, 2, 176),
        (-50, -5, 6, 5),
        (100, 1000, 42, 19),
        (1, 12, 1, 4),
        (5, 5, 5, 1)
    ]
    for test in tests:
        start, end, num, expected = test
        try:
            result = countNum(start, end, num)
            assert result == expected, f"Expected {expected}, but got {result}"
        except (TypeError, ValueError) as e:
            print(f"Test failed: {e}")

    
    invalid_tests = [
        
        (1.5, 9, 5),
        (1, 9.5, 5),
        (1, 9, 5.5),
        
        ('A', 9, 5),
        (1, 'A', 5),
        (1, 9, 'A'),
        
        (9, 1, 5),
        
        (1, 9, -5)
    ]
    for test in invalid_tests:
        start, end, num = test
        try:
            result = countNum(start, end, num)
            print("Test failed: Function did not raise an exception for invalid input:", test)
        except (TypeError, ValueError):
            pass  
    print("All tests passed successfully.")

if __name__ == "__main__":
    run_tests()
