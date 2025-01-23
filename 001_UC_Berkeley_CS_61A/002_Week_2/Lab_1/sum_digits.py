"""
Write a function that takes in a nonnegative integer and sums its digits.
(Using floor division and modulo might be helpful here!)
"""

# Intuition: use division and modulo to "pop" the right digit
# Implemetation: iteration
# Time complexity: O(n)
# Space complexity: O(1)
def sum_digits_v1(n: int) -> int:
    sum = 0
    while n > 0: sum, n = sum + n % 10, n // 10
    return sum

# Intuition; if there's an iterative solution, there's a recursive solution
# Implementation: recursion
# Time complexity: O(n)
# Space complexity: O(n)
def sum_digits_v2(n: int) -> int:
    if n == 0: return 0
    return (n % 10) + sum_digits_v2(n // 10)

# Test cases
try:
    result = sum_digits_v1(10)
    assert result == 1, f"Expected 1 but got {result}"
    result = sum_digits_v1(4224)
    assert result == 12, f"Expected 12 but got {result}"
    result = sum_digits_v1(1234567890)
    assert result == 45, f"Expected 45 but got {result}"
    result = sum_digits_v1(123)
    assert result == 6, f"Expected 6 but got {result}"

    result = sum_digits_v2(10)
    assert result == 1, f"Expected 1 but got {result}"
    result = sum_digits_v2(4224)
    assert result == 12, f"Expected 12 but got {result}"
    result = sum_digits_v2(1234567890)
    assert result == 45, f"Expected 45 but got {result}"
    result = sum_digits_v2(123)
    assert result == 6, f"Expected 6 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)