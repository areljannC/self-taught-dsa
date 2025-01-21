"""
Write a function that takes an integer n that is greater than 1 
and returns the largest integer that is smaller than n and evenly divides n.

int: To check if b evenly divides a, use the expression a % b == 0, 
which can be read as, "the remainder when dividing a by b is 0."
"""

# Implementation: intuition; iterate from 1 to n and check if remainder is 0
# Time complexity: O(n)
# Space complexity: O(1)
def largest_factor_v1(n: int) -> int:
    lf = 1
    for i in range(1, n):
        f = n % i
        if f == 0 and i > lf: lf = i
    return lf

# Implementation: ChatGPT 4o
# Time complexity: O(n)
# Space complexity: O(1)
def largest_factor_v2(n: int) -> int:
    return max(b for b in range(1, n) if n % b == 0)

# Implementation: v1 by ChatGPT 4o; start from n - 1 and stop the loop right away when n % i == 0 instead of starting from 0
# Time complexity: O(n)
# Space complexity: O(1)
def largest_factor_v3(n: int) -> int:
    for i in range(n - 1, 0, -1):
        if n % i == 0: return i

try:
    result = largest_factor_v1(15)
    assert result == 5, f"Expected 5 but got {result}"
    result = largest_factor_v1(80)
    assert result == 40, f"Expected 40 but got {result}"
    result = largest_factor_v1(13)
    assert result == 1, f"Expected 1 but got {result}"

    result = largest_factor_v2(15)
    assert result == 5, f"Expected 5 but got {result}"
    result = largest_factor_v2(80)
    assert result == 40, f"Expected 40 but got {result}"
    result = largest_factor_v2(13)
    assert result == 1, f"Expected 1 but got {result}"

    result = largest_factor_v3(15)
    assert result == 5, f"Expected 5 but got {result}"
    result = largest_factor_v3(80)
    assert result == 40, f"Expected 40 but got {result}"
    result = largest_factor_v3(13)
    assert result == 1, f"Expected 1 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)