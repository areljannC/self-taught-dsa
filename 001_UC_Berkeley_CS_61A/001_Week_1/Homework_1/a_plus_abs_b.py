"""
Python's operator module contains two-argument functions such as add 
and sub for Python's built-in arithmetic operators.

For example, add(2, 3) evalutes to 5, just like the expression 2 + 3.

Without calling abs(), create a function that adds two numbers.
"""

# Implementation: intuition; multiply -1 to a negative number to make it a positive
# Time complexity: O(1)
# Space complexity: O(1)
def a_plus_abs_b_v1(a, b):
  sum = a
  sum += b * -1 if b < 0 else b
  return sum

# Implementation: ChatGPT 4o
# Time complexity: O(1)
# Space complexity: O(1)
def a_plus_abs_b_v2(a, b):
  return a + (b if b >= 0 else -b)

# Test Cases
try:
  assert a_plus_abs_b_v1(2, 3) == 5
  assert a_plus_abs_b_v1(2, -3) == 5
  assert a_plus_abs_b_v1(-1, 4) == 3
  assert a_plus_abs_b_v1(-1, -4) == 3
  assert a_plus_abs_b_v2(2, 3) == 5
  assert a_plus_abs_b_v2(2, -3) == 5
  assert a_plus_abs_b_v2(-1, 4) == 3
  assert a_plus_abs_b_v2(-1, -4) == 3
  print("All test cases passed!")
except AssertionError:
  print("A test case failed.")