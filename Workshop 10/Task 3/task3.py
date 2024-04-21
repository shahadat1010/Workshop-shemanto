"""
 Define the `countNum` function:
    Check if all input arguments are integers using a list comprehension and the isinstance function.
    Raise a TypeError if any input argument is not an integer.
    Raise a ValueError if the start value is greater than the end value or if the num value is negative.
    Initialize count to 0.
    Iterate over the range from start to end .
      Convert each number to a string and check if the string representation of `num` is contained within it.
      If found, increment count.
    Return count, representing the number of occurrences of num within the specified range.

 Define a list of invalid test cases, each containing:
    start, end, num: Input parameters for the countNum function with at least one invalid input.
   
 For each invalid test case:
    Attempt to execute the `countNum` function with the provided input parameters.
    If the function executes successfully without raising an exception:
      Print "Test Case Passed: No exception raised".
    If the function raises a TypeError or ValueError:
      Print "Test Case Failed: <Exception Type> - <Exception Message>".

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
invalid_test_cases = [
    {"start": 1.5, "end": 9, "num": 5},
    {"start": 1, "end": 9.5, "num": 5},
    {"start": 1, "end": 9, "num": 5.5},
    {"start": 'A', "end": 9, "num": 5},
    {"start": 1, "end": 'A', "num": 5},
    {"start": 1, "end": 9, "num": 'A'},
    {"start": 9, "end": 1, "num": 5},
    {"start": 1, "end": 9, "num": -5}
]
for i, test_case in enumerate(invalid_test_cases):
    try:
        start = test_case["start"]
        end = test_case["end"]
        num = test_case["num"]
        result = countNum(start, end, num)
        print(f"Test Case {i+1} Passed: No exception raised")
    except (TypeError, ValueError) as e:
        print(f"Test Case {i+1} Failed: {type(e).__name__} - {e}")
