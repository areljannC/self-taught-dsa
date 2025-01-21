"""
Implement middle by writing a single return expression 
that evaluates to the value that is neither the largest or smallest 
among three different integers a, b, and c.

Hint: Try combining all the numbers and then taking away the ones you don't want to return.
"""

# intuition; sort the arguments and return the middle index
# time: O(1); 3 arguments will never change so this is a constant
# space: O(1)
def middle_v1(a: int, b: int, c: int) -> int:
    array: list[int] = [a, b, c]
    array.sort()
    return array[1]

# intuition; not scalable when there's more than 3 arguments
# time: O(1)
# space: O(1)
def middle_v2(a: int, b: int, c: int) -> int:
    if (a > b and a < c) or (a > c and a < b): return a
    if (b > a and b < c) or (b > c and b < a): return b
    if (c > a and c < b) or (c > b and c < a): return c

# ChatGPT 4o
# time: O(1)
# space: O(1)
def middle_v3(a: int, b: int, c: int) -> int:
    return a + b + c - max(a, b, c) - min(a, b, c)

try:
    result = middle_v1(3, 5, 4)
    assert result == 4, f"Expected 4 but got {result}"
    result = middle_v1(30, 5, 4)
    assert result == 5, f"Expected 5 but got {result}"
    result = middle_v1(3, 5, 40)
    assert result == 5, f"Expected 5 but got {result}"
    result = middle_v1(30, 5, 40)
    assert result == 30, f"Expected 30 but got {result}"

    result = middle_v2(3, 5, 4)
    assert result == 4, f"Expected 4 but got {result}"
    result = middle_v2(30, 5, 4)
    assert result == 5, f"Expected 5 but got {result}"
    result = middle_v2(3, 5, 40)
    assert result == 5, f"Expected 5 but got {result}"
    result = middle_v2(30, 5, 40)
    assert result == 30, f"Expected 30 but got {result}"

    result = middle_v3(3, 5, 4)
    assert result == 4, f"Expected 4 but got {result}"
    result = middle_v3(30, 5, 4)
    assert result == 5, f"Expected 5 but got {result}"
    result = middle_v3(3, 5, 40)
    assert result == 5, f"Expected 5 but got {result}"
    result = middle_v3(30, 5, 40)
    assert result == 30, f"Expected 30 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)