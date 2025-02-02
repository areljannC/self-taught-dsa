"""
Implement the function squares, which takes in a list of positive integers.
It returns a list that contains the square roots of the elements of the original list that are perfect squares.
Use a list comprehension.
"""

from math import sqrt

# Time complexity: O(n)
# Space complexity: O(n)
def squares(s: list[int]) -> list[int]:
    perfect = []
    for x in s:
        r = int(sqrt(x))
        if r ** 2 == x: perfect.append(r)
    return perfect

# Test cases
seq1 = [8, 49, 8, 9, 2, 1, 100, 102]
seq2 = [500, 30]

try:
    result, expectation = squares(seq1), [7, 3, 1, 10]
    assert result == expectation, f"Expected {expectation} but got {result}."

    result, expectation = squares(seq2), []
    assert result == expectation, f"Expected {expectation} but got {result}."

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)
