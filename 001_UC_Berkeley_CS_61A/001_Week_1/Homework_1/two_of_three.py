"""
Write a function that takes three positive numbers as arguments and returns the sum of the squares of the two smallest numbers.
Use only a single line for the body of the function.

Hint: Consider using the max or min function.
"""

from operator import pow

# Implementation: intuition; do "sum magic" to get the second lowest value
# by adding all values and subtracting the max and min values to it
# Time complexity: O(1)
# Space complexity: O(1)
def two_of_three_v1(i, j, k):
  return (pow(min(i, j, k), 2)) + (pow((i + j + k) - max(i, j, k) - min(i, j, k), 2))

# Implementation: ChatGPT 4o
# Time complexity: O(1)
# Space complexity: O(1)
def two_of_three_v2(i, j, k):
  return i**2 + j**2 + k**2 - max(i, j, k)**2

# Test Cases
try:
  assert two_of_three_v1(1, 2, 3) == 5
  assert two_of_three_v1(5, 3, 1) == 10
  assert two_of_three_v1(10, 2, 8) == 68
  assert two_of_three_v1(5, 5, 5) == 50
  assert two_of_three_v2(1, 2, 3) == 5
  assert two_of_three_v2(5, 3, 1) == 10
  assert two_of_three_v2(10, 2, 8) == 68
  assert two_of_three_v2(5, 5, 5) == 50
  print("All test cases passed!")
except AssertionError:
  print("A test case failed.")