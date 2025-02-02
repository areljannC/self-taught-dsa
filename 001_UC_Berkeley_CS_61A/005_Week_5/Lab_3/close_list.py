"""
Implement close_list, which takes a list of numbers s and a non-negative integer k.
It returns a list of the elements of s that are within k of their index.
That is, the absolute value of the difference between the element and its index is less than or equal to k.
"""
# Time complexity: O(n)
# Space complexity: O(n)
def close_list(s: list[int], k: int) -> list[int]:
    close = []
    for i in range(len(s)):
        if abs(s[i] - i) <= k: close.append(s[i])
    return close

# Test cases
t = [6, 2, 4, 3, 5]
try:
    result, expectation = close_list(t, 0), [3]
    assert result == expectation, f"Expected {expectation} but got {result}."

    result, expectation = close_list(t, 1), [2, 3, 5]
    assert result == expectation, f"Expected {expectation} but got {result}."

    result, expectation = close_list(t, 2), [2, 4, 3, 5]
    assert result == expectation, f"Expected {expectation} but got {result}."

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)
