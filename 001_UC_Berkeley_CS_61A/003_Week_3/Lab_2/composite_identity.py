"""
Write a function that takes in two single-argument functions, f and g, and returns another function that has a single parameter x.
The returned function should return True if f(g(x)) is equal to g(f(x)) and False otherwise.
You can assume the output of g(x) is a valid input for f and vice versa.
"""

from typing import Callable

# Not much problem solving here, this lab seems to be
# more or so about learning HoCs and how to write them.
def composite_identity(f: Callable[[int], int], g: Callable[[int], int]) -> Callable[[int], bool]:
    return lambda x: f(g(x)) == g(f(x))

# Test cases by ChatGPT 40
try:
    # Test 1: Simple identity functions
    f = lambda x: x
    g = lambda x: x

    result = composite_identity(f, g)(5)
    assert result == True, f"Expected True but got {result}"

    # Test 2: Commutative functions
    f = lambda x: x + 2
    g = lambda x: x * 3

    result = composite_identity(f, g)(5)  # f(g(x)) = f(15) = 17, g(f(x)) = g(7) = 21
    assert result == False, f"Expected False but got {result}"

    # Test 3: Functions that are commutative for all inputs
    f = lambda x: x ** 2
    g = lambda x: abs(x)

    result = composite_identity(f, g)(-3)  # f(g(x)) = f(3) = 9, g(f(x)) = g(9) = 9
    assert result == True, f"Expected True but got {result}"

    # Test 4: Non-commutative functions
    f = lambda x: x + 1
    g = lambda x: x - 1

    result = composite_identity(f, g)(10)  # f(g(x)) = f(9) = 10, g(f(x)) = g(11) = 10
    assert result == True, f"Expected True but got {result}"

    # Test 5: Edge case with constant functions
    f = lambda x: 42
    g = lambda x: 0

    result = composite_identity(f, g)(100)  # f(g(x)) = f(0) = 42, g(f(x)) = g(42) = 0
    assert result == False, f"Expected False but got {result}"

    # Test 6: Commutative custom logic
    f = lambda x: x ** 3
    g = lambda x: x ** (1 // 3)

    result = composite_identity(f, g)(8)  # f(g(x)) = f(2) = 8, g(f(x)) = g(8) = 2
    assert result == True, f"Expected True but got {result}"

    # Test 7: Functions with non-commutative behavior for some inputs
    f = lambda x: x * 2
    g = lambda x: x + 5

    result = composite_identity(f, g)(2)  # f(g(x)) = f(7) = 14, g(f(x)) = g(4) = 9
    assert result == False, f"Expected False but got {result}"

    result = composite_identity(f, g)(0)  # f(g(x)) = f(5) = 10, g(f(x)) = g(0) = 5
    assert result == False, f"Expected False but got {result}"

    # Test 8: Functions with float outputs
    f = lambda x: x / 2
    g = lambda x: x + 3

    result = composite_identity(f, g)(6)  # f(g(x)) = f(9) = 4.5, g(f(x)) = g(3) = 6
    assert result == False, f"Expected False but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error.with_traceback())