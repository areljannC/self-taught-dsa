"""
Return the result of fusing together the first n terms in a sequence and start.
The terms to be fused are term(1), term(2), ..., term(n).
The function fuse is a two-argument commutative & associative function.

accumulate has the following parameters:
    - fuse: a two-argument function that specifies how the current term is fused with the previously accumulated terms
    - start: value at which to start the accumulation
    - n: a non-negative integer indicating the number of terms to fuse
    - term: a single-argument function; term(i) is the ith term of the sequence

Implement accumulate, which fuses the first n terms of the sequence defined by term with the start value using the fuse function.
"""

from operator import add, mul
from typing import Callable

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1

# Intuition: gotta read the problem requirements carefully
# Implementation: iteration
# Time complexity: O(n)
# Space complexity: O(1)
def accumulate_v1(fuse: Callable[[int, int], int], start: int, n: int, term: Callable[[int], int]) -> int:
    total = start
    for i in range(1, n + 1): total = fuse(total, term(i))
    return total

# Intuition; why not try recursion?
# Implementation: recursion
# Time complexity: O(n)
# Space complexity: O(n)
def accumulate_v2(fuse: Callable[[int, int], int], start: int, n: int, term: Callable[[int], int]) -> int:
    if start > 0 and n <= 0: return start
    if n <= 1: return 1
    if start == 0: return fuse(term(n), accumulate_v2(fuse, 0, n - 1, term))
    return fuse(start, fuse(term(n), accumulate_v2(fuse, 0, n - 1, term)))

# Intuition: ChatGPT 4o; improvements for v2; instead of handling start, process it when n is 0
# Implementation: recursion
# Time complexity: O(n)
# Space complexity: O(n)
def accumulate_v3(fuse: Callable[[int, int], int], start: int, n: int, term: Callable[[int], int]) -> int:
    if n <= 0: return start
    return fuse(term(n), accumulate_v3(fuse, start, n - 1, term))

"""
Implement summation (from lecture) and product as one-line calls to accumulate.
Important: Both summation_using_accumulate and product_using_accumulate should be implemented with a single line of code starting with return.
"""
def summation_using_accumulate(n: int, term: Callable[[int], int]) -> int:
    return accumulate_v1(add, 0, n, term)

def product_using_accumulate(n: int, term: Callable[[int], int]) -> int:
    return accumulate_v1(mul, 1, n, term)

# Test cases
try:
    result = accumulate_v1(add, 0, 5, identity)
    assert result == 15, f"Expected 15 but got {result}"
    result = accumulate_v1(add, 11, 5, identity)
    assert result == 26, f"Expected 26 but got {result}"
    result = accumulate_v1(add, 11, 0, identity)
    assert result == 11, f"Expected 11 but got {result}"
    result = accumulate_v1(add, 11, 3, square)
    assert result == 25, f"Expected 25 but got {result}"
    result = accumulate_v1(mul, 2, 3, square)
    assert result == 72, f"Expected 72 but got {result}"
    result = accumulate_v1(lambda x, y: x + y + 1, 2, 3, square)
    assert result == 19, f"Expected 19 but got {result}"

    result = accumulate_v2(add, 0, 5, identity)
    assert result == 15, f"Expected 15 but got {result}"
    result = accumulate_v2(add, 11, 5, identity)
    assert result == 26, f"Expected 26 but got {result}"
    result = accumulate_v2(add, 11, 0, identity)
    assert result == 11, f"Expected 11 but got {result}"
    result = accumulate_v2(add, 11, 3, square)
    assert result == 25, f"Expected 25 but got {result}"
    result = accumulate_v2(mul, 2, 3, square)
    assert result == 72, f"Expected 72 but got {result}"
    result = accumulate_v2(lambda x, y: x + y + 1, 2, 3, square)
    assert result == 19, f"Expected 19 but got {result}"

    result = accumulate_v3(add, 0, 5, identity)
    assert result == 15, f"Expected 15 but got {result}"
    result = accumulate_v3(add, 11, 5, identity)
    assert result == 26, f"Expected 26 but got {result}"
    result = accumulate_v3(add, 11, 0, identity)
    assert result == 11, f"Expected 11 but got {result}"
    result = accumulate_v3(add, 11, 3, square)
    assert result == 25, f"Expected 25 but got {result}"
    result = accumulate_v3(mul, 2, 3, square)
    assert result == 72, f"Expected 72 but got {result}"
    result = accumulate_v3(lambda x, y: x + y + 1, 2, 3, square)
    assert result == 19, f"Expected 19 but got {result}"

    result = summation_using_accumulate(5, square)
    assert result == 55, f"Expected 55 but got {result}"
    result = summation_using_accumulate(5, triple)
    assert result == 45, f"Expected 45 but got {result}"

    result = product_using_accumulate(4, square)
    assert result == 576, f"Expected 576 but got {result}"
    result = product_using_accumulate(6, triple)
    assert result == 524880, f"Expected 524880 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)