"""
For a given integer, the digit distance is the sum of the absolute differences between consecutive digits.

The digit distance of 6 is 0. The digit distance of 61 is 5, as the absolute value of 6 - 1 is 5.
The digit distance of 71253 is 12 (6 + 1 + 3 + 2).

Write a function that determines the digit distance of a given positive integer.
"""

# Intuition: use % and // to get the first and second digits and recurse; base case is n <= 9
# Time complexity: O(n)
# Space complexity: O(n)
def digit_distance(n: int) -> int:
    if n <= 9: return 0
    return abs((n // 10 % 10) - (n % 10)) + digit_distance(n // 10)

try:
    result, expectation = digit_distance(3), 0
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = digit_distance(777), 0
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = digit_distance(314), 5
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = digit_distance(31415926535), 32
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = digit_distance(3464660003), 16
    assert result == expectation, f"Expected {expectation} but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error.with_traceback())