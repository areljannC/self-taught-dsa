"""
Let's write a function falling, which is a "falling" factorial that
takes two arguments, n and k, and returns the product of k consecutive
numbers, starting from n and working downwards.
When k is 0, the function should return 1.
"""

# intuition; problem mentions factorial which gives a hint that recursion is possible
# time: O(k)
# space: O(k)
def falling_v1(n, k):
    if k <= 0: return 1
    return n * falling_v1(n - 1, k - 1)

# intuition; problem can be solved iteratively if there's a recursive solution
# time: O(k)
# space: O(1)
def falling_v2(n, k):
    result = 1
    for i in range(k): result = result * (n - i)
    return result

try:
    result = falling_v1(6, 3)
    assert result == 120, f"Expected 120 but got {result}"
    result = falling_v1(4, 3)
    assert result == 24, f"Expected 24 but got {result}"
    result = falling_v1(4, 1)
    assert result == 4, f"Expected 4 but got {result}"
    result = falling_v1(4, 0)
    assert result == 1, f"Expected 1 but got {result}"

    result = falling_v2(6, 3)
    assert result == 120, f"Expected 120 but got {result}"
    result = falling_v2(4, 3)
    assert result == 24, f"Expected 24 but got {result}"
    result = falling_v2(4, 1)
    assert result == 4, f"Expected 4 but got {result}"
    result = falling_v2(4, 0)
    assert result == 1, f"Expected 1 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)