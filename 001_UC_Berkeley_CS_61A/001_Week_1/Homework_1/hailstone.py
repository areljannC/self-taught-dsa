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
prints out the hailstone sequence starting at n,
and returns the number of steps in the sequence.
"""

# Implementation: intuition; very similar to FizzBuzz
# Time complexity: O(n)
# Space complexity: O(1)
def hailstone_v1(n: int) -> int:
  steps: int = 1
  while True:
    if n == 1: break
    if n % 2 == 0: n = n // 2
    else: n = (n * 3) + 1
    steps += 1
  return steps

# Implementation: ChatGPT 4o
# Time complexity: O(n)
# Space complexity: O(1)
def hailstone_v2(n: int) -> int:
  steps = 1
  while n != 1:
    if n % 2 == 0:
      n //= 2
    else:
      n = 3 * n + 1
    steps += 1
  return steps

try:
  result = hailstone_v1(10)
  assert result == 7, f"Expected 7 but got {result}"
  result = hailstone_v1(6)
  assert result == 9, f"Expected 9 but got {result}"
  result = hailstone_v1(1)
  assert result == 1, f"Expected 1 but got {result}"
  result = hailstone_v1(19)
  assert result == 21, f"Expected 21 but got {result}"
  result = hailstone_v1(7)
  assert result == 17, f"Expected 17 but got {result}"
  result = hailstone_v1(20)
  assert result == 8, f"Expected 8 but got {result}"
  result = hailstone_v1(27)
  assert result == 112, f"Expected 112 but got {result}"

  result = hailstone_v2(10)
  assert result == 7, f"Expected 7 but got {result}"
  result = hailstone_v2(6)
  assert result == 9, f"Expected 9 but got {result}"
  result = hailstone_v2(1)
  assert result == 1, f"Expected 1 but got {result}"
  result = hailstone_v2(19)
  assert result == 21, f"Expected 21 but got {result}"
  result = hailstone_v2(7)
  assert result == 17, f"Expected 17 but got {result}"
  result = hailstone_v2(20)
  assert result == 8, f"Expected 8 but got {result}"
  result = hailstone_v2(27)
  assert result == 112, f"Expected 112 but got {result}"

  print("All test cases passed!")
except AssertionError as error:
  print("A test case failed.")
  print(error)
