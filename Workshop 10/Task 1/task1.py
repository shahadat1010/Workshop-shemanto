"""
Define the countNum function:
  Initialize a variable count to 0.
  Iterate over the range from start to end (inclusive).
    Convert each number to a string and check if the string representation of num is contained within it.
    If found, increment the count variable.
  Return the final value of count, representing the number of occurrences of num within the specified range.
Define a list of test cases, each containing:
    start, end, num: The input parameters for the countNum function.
     expected_output: The expected output of the function for the given input.
Iterate over each test case:
  Extract the input parameters and the expected output from the test case.
  Call the countNum function with the input parameters and store the result.
  Print the details of the test case, including input values, expected output, and actual output.
  Check if the actual output matches the expected output:
    If they match, print "Test Result: Passed".
    If they don't match, print "Test Result: Failed".
"""

def countNum(start, end, num):
    count = 0
    for i in range(start, end + 1):
        if str(num) in str(i):
            count += 1
    return count
test_cases = [
    {"start": 1, "end": 5, "num": 8, "expected_output": 0},
    {"start": 1, "end": 500, "num": 2, "expected_output": 176},
    {"start": -50, "end": -5, "num": 6, "expected_output": 5},
    {"start": 100, "end": 1000, "num": 42, "expected_output": 19},
    {"start": 1, "end": 12, "num": 1, "expected_output": 4},
    {"start": 5, "end": 5, "num": 5, "expected_output": 1}
]
for i, test_case in enumerate(test_cases):
    start = test_case["start"]
    end = test_case["end"]
    num = test_case["num"]
    expected_output = test_case["expected_output"]
    result = countNum(start, end, num)
    print(f"Test Case {i+1}:")
    print(f"Input: start = {start}, end = {end}, num = {num}")
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {result}")
    print("Test Result:", "Passed" if result == expected_output else "Failed")
    print()
