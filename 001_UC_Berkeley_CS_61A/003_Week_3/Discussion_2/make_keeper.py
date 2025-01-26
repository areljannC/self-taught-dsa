"""
Implement make_keeper, which takes a positive integer n and returns a function f that takes as its argument another one-argument function cond.
When f is called on cond, it prints out the integers from 1 to n (including n) for which cond returns a true value when called on each of those integers.
Each integer is printed on a separate line.
"""

from typing import Callable

# Time complexity: O(n)
# Space complexity: O(1)
def make_keeper(n: int) -> Callable[[int], bool]:
    def f(cond: Callable[[int], bool]):
        for i in range(1, n + 1):
            if cond(i): print(i)
    return f

is_even = lambda x: x % 2 == 0
is_multiple_of_3 = lambda x: x % 3 == 0

# Test cases by ChatGPT 4o

keeper = make_keeper(10)

# Test 1: Print numbers from 1 to 10 that are even
print("Testing with is_even:")
keeper(is_even)
# Expected Output:
# 2
# 4
# 6
# 8
# 10

# Test 2: Print numbers from 1 to 10 that are multiples of 3
print("\nTesting with is_multiple_of_3:")
keeper(is_multiple_of_3)
# Expected Output:
# 3
# 6
# 9

# Test 3: Print numbers from 1 to 10 that are greater than 5
print("\nTesting with lambda x: x > 5:")
keeper(lambda x: x > 5)
# Expected Output:
# 6
# 7
# 8
# 9
# 10

# Test 4: No condition matches
print("\nTesting with lambda x: x > 20:")
keeper(lambda x: x > 20)
# Expected Output:
# (No output)