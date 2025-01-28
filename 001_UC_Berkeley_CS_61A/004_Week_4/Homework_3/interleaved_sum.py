"""
Write a function interleaved_sum, which takes in a number n and two one-argument functions: odd_func and even_func.
It applies odd_func to every odd number and even_func to every even number from 1 to n including n and returns the sum.

Implement this function without using any loops or directly testing if a number is odd or even -- no modulos (%) allowed!
Instead of checking whether a number is even or odd, start with 1, which you know is an odd number.

Hint: Introduce an inner helper function that takes an odd number k and computes an interleaved sum from k to n (including n).
"""

from typing import Callable

identity = lambda x: x
square = lambda x: x * x
triple = lambda x: x * 3

# Intuition: start from 1; use odd and even functions alternatively
# Time complexity: O(n) 
# Space complexity: O(n)
def interleaved_sum_v1(n: int, of: Callable[[int], int], ef: Callable[[int], int]) -> int:
    if n < 2: return n
    def odd_helper(k: int, f: Callable[[int], int]) -> int:
        return 0 if k > n else f(k) + odd_helper(k + 2, f)
    def even_helper(k: int, f: Callable[[int], int]) -> int:
        return 0 if k > n else f(k) + even_helper(k + 2, f)
    return odd_helper(1, of) + even_helper(2, ef)

# Intuition: ChatGPT 4o
# Implementation: improved version of v1
# Time complexity: O(n) 
# Space complexity: O(n)
def interleaved_sum_v2(n: int, of: Callable[[int], int], ef: Callable[[int], int]) -> int:
    def helper(k: int, f: Callable[[int], int])-> int:
        return 0 if k > n else f(k) + helper(k + 2, f)
    return helper(1, of) + helper(2, ef)

try:
    result, expectation = interleaved_sum_v1(5, identity, square), 29
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = interleaved_sum_v1(5, square, identity), 41
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = interleaved_sum_v1(4, triple, square), 32
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = interleaved_sum_v1(4, square, triple), 28
    assert result == expectation, f"Expected {expectation} but got {result}"

    result, expectation = interleaved_sum_v2(5, identity, square), 29
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = interleaved_sum_v2(5, square, identity), 41
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = interleaved_sum_v2(4, triple, square), 32
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = interleaved_sum_v2(4, square, triple), 28
    assert result == expectation, f"Expected {expectation} but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error.with_traceback())