"""
Write a recursive function num_eights that takes a positive integer n and returns the number of times the digit 8 appears in n.
"""

# Intuition: base case is 0
# Time complexity: O(n)
# Space complexity: O(n)
def num_eights(n: int) -> int:
    if n <= 0: return 0
    return (1 if n % 10 == 8 else 0) + num_eights(n // 10)

try:
    result = num_eights(3)
    assert result == 0, f"Expected 0 but got {result}"
    result = num_eights(8)
    assert result == 1, f"Expected 1 but got {result}"
    result = num_eights(88888888)
    assert result == 8, f"Expected 8 but got {result}"
    result = num_eights(2638)
    assert result == 1, f"Expected 1 but got {result}"
    result = num_eights(86380)
    assert result == 2, f"Expected 2 but got {result}"
    result = num_eights(12345)
    assert result == 0, f"Expected 0 but got {result}"
    result = num_eights(8782089)
    assert result == 3, f"Expected 0 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error.with_traceback())