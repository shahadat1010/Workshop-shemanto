"""
Check if all parameters start, end, and num are integers.
    If any parameter is not an integer, raise a TypeError with the message "All parameters must be integers".
Check if the start parameter is less than or equal to the end parameter.
    If start is greater than end, raise a ValueError with the message "Start must be less than or equal to end".
Check if the num parameter is non-negative.
    If num is negative, raise a ValueError with the message "Num must be non-negative".
Initialize a variable count to 0 to count the occurrences of num.
Iterate over the range from start to end .
    Convert each number to a string and check if the string representation of num is contained within it.
    If found, increment the count variable.
Return the final value of count, which represents the number of occurrences of num within the specified range from start to end.
"""


def countNum(start, end, num):
    if not all(isinstance(x, int) for x in [start, end, num]):
        raise TypeError("All parameters must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    if num < 0:
        raise ValueError("Input must be non-negative")

    count = 0
    for i in range(start, end + 1):
        if str(num) in str(i):
            count += 1
    return count
