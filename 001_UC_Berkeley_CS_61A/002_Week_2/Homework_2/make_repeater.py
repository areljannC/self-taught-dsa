"""
Make Repeater Implement the function make_repeater that takes a one-argument function f and a positive integer n.
It returns a one-argument function, where make_repeater(f, n)(x) returns the value of f(f(...f(x)...)) in which f is applied n times to x.

For example, make_repeater(square, 3)(5) squares 5 three times and returns 390625, just like square(square(square(5))).
"""

from typing import Callable
from functools import reduce

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1

# Intuition: Stephen Curry these functions
# Implementation: call term n times
# Time complexity: O(n)
# Space complexity: O(1)
def make_repeater_v1(term: Callable[[int], int], n: int) -> Callable[[int], int]:
    def repeater(x: int) -> Callable[[int], int]:
        for _ in range(n): x = term(x)
        return x
    return repeater

# Intuition: ChatGPT 4o
# Implementation: use reduce if you want to be a functional programming pro
# Time complexity: O(n)
# Space complexity: O(1)
def make_repeater_v2(term: Callable[[int], int], n: int) -> Callable[[int], int]:
    return lambda term, n: lambda x: reduce(lambda acc, _: term(acc), range(n), x)

# Test cases
try:
    result = make_repeater_v1(increment, 3)(5)
    assert result == 8, f"Expected 8 but got {result}"
    result = make_repeater_v1(triple, 5)(1)
    assert result == 243, f"Expected 243 but got {result}"
    result = make_repeater_v1(square, 2)(5)
    assert result == 625, f"Expected 625 but got {result}"
    result = make_repeater_v1(square, 3)(5)
    assert result == 390625, f"Expected 390625 but got {result}"

    result = make_repeater_v1(increment, 3)(5)
    assert result == 8, f"Expected 8 but got {result}"
    result = make_repeater_v1(triple, 5)(1)
    assert result == 243, f"Expected 243 but got {result}"
    result = make_repeater_v1(square, 2)(5)
    assert result == 625, f"Expected 625 but got {result}"
    result = make_repeater_v1(square, 3)(5)
    assert result == 390625, f"Expected 390625 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)