"""
Implement close, which takes a list of numbers s and a non-negative integer k.
It returns how many of the elements of s are within k of their index.
That is, the absolute value of the difference between the element and its index is less than or equal to k.

Implement close, which takes a list of numbers s and a non-negative integer k.
It returns how many of the elements of s are within k of their index.
That is, the absolute value of the difference between the element and its index is less than or equal to k.
"""

# Time complexity: O(n)
# Space complexity: O(1)
def close(s: list[int], k: int) -> int:
    count = 0
    for i in range(len(s)):
        if abs(s[i] - i) <= k: count += 1
    return count

# Test cases
t = [6, 2, 4, 3, 5]
try:
    result, expectation = close(t, 0), 1
    assert result == expectation, f"Expected {expectation} but got {result}."

    result, expectation = close(t, 1), 3
    assert result == expectation, f"Expected {expectation} but got {result}."

    result, expectation = close(t, 2), 4
    assert result == expectation, f"Expected {expectation} but got {result}."

    result, expectation = close(list(range(10)), 0), 10
    assert result == expectation, f"Expected {expectation} but got {result}."

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)
