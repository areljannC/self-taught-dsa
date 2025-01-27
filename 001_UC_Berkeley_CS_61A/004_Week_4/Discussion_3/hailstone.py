"""
Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.

  1. Pick a positive integer n as the start.
  2. If n is even, divide it by 2.
  3. If n is odd, multiply it by 3 and add 1.
  4. Continue this process until n is 1.

The number n will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried -- nobody has ever proved that the sequence will terminate).
Analogously, a hailstone travels up and down in the atmosphere before eventually landing on earth.

This sequence of values of n is often called a Hailstone sequence.

Write a function that takes a single argument with formal parameter name n,
and returns the number of steps in the sequence.
"""

# Intuition: convert iterative solution from Week 1 to recursion
# Implementation: recursion
# Time complexity: O(n)
# Space complexity: O(1)
def hailstone(n: int) -> int:
    if n == 1: return 1
    return 1 + hailstone(n // 2 if n % 2 == 0 else (n * 3) + 1)

# Test cases
try:
    result = hailstone(10)
    assert result == 7, f"Expected 7 but got {result}"
    result = hailstone(6)
    assert result == 9, f"Expected 9 but got {result}"
    result = hailstone(1)
    assert result == 1, f"Expected 1 but got {result}"
    result = hailstone(19)
    assert result == 21, f"Expected 21 but got {result}"
    result = hailstone(7)
    assert result == 17, f"Expected 17 but got {result}"
    result = hailstone(20)
    assert result == 8, f"Expected 8 but got {result}"
    result = hailstone(27)
    assert result == 112, f"Expected 112 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)
