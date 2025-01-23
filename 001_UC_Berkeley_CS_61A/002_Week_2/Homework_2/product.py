"""
Write a function called product that returns the product of the
first n terms of a sequence. Specifically, product takes in an
integer n and term, a single-argument function that determines a sequence.

(That is, term(i) gives the ith term of the sequence.)
product(n, term)should return term(1) * ... * term(n).
"""

from operator import mul

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1

# Implementation: intuition; not sure... this one seems pretty straightforward
# Time complexity: O(n)
# Space complexity: O(1)
def product_v1(n: int, term: int) -> int:
    product = 1
    for i in range(1, n + 1): product = mul(product, term(i))
    return product

# Implementation: ChatGPT 4o
# Time complexity: O(n)
# Space complexity: O(1)
def product_v2(n: int, term: int) -> int:
    if n == 0: return 1
    return term(n) * product_v1(n - 1, term)

try:
    result = product_v1(3, identity)
    assert result == 6, f"Expected 6 but got {result}"
    result = product_v1(5, identity)
    assert result == 120, f"Expected 120 but got {result}"
    result = product_v1(3, square)
    assert result == 36, f"Expected 36 but got {result}"
    result = product_v1(5, square)
    assert result == 14400, f"Expected 14400 but got {result}"
    result = product_v1(3, increment)
    assert result == 24, f"Expected 24 but got {result}"
    result = product_v1(3, triple)
    assert result == 162, f"Expected 162 but got {result}"

    result = product_v2(3, identity)
    assert result == 6, f"Expected 6 but got {result}"
    result = product_v2(5, identity)
    assert result == 120, f"Expected 120 but got {result}"
    result = product_v2(3, square)
    assert result == 36, f"Expected 36 but got {result}"
    result = product_v2(5, square)
    assert result == 14400, f"Expected 14400 but got {result}"
    result = product_v2(3, increment)
    assert result == 24, f"Expected 24 but got {result}"
    result = product_v2(3, triple)
    assert result == 162, f"Expected 162 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)