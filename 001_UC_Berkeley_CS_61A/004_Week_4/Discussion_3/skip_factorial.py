"""
Define the base case for the skip_factorial function, which returns the product of every other positive integer, starting with n.
"""

# Intuition: base case is n <= 0
# Time complexity: O(n)
# Space complexity: O(n)
def skip_factorial(n: int) -> int:
    if n <= 1: return 1
    return n * skip_factorial(n - 2)

# Test cases by ChatGPT 4o
try:
    # Test 1: Base case for n = 0
    assert skip_factorial(0) == 1, "Expected 1 for skip_factorial(0)"

    # Test 2: Base case for n = 1
    assert skip_factorial(1) == 1, "Expected 1 for skip_factorial(1)"

    # Test 3: Small even n
    assert skip_factorial(6) == 48, "Expected 48 for skip_factorial(6)"  # 6 * 4 * 2

    # Test 4: Small odd n
    assert skip_factorial(5) == 15, "Expected 15 for skip_factorial(5)"  # 5 * 3 * 1

    # Test 5: Larger even n
    assert skip_factorial(8) == 384, "Expected 384 for skip_factorial(8)"  # 8 * 6 * 4 * 2

    # Test 6: Larger odd n
    assert skip_factorial(9) == 945, "Expected 945 for skip_factorial(9)"  # 9 * 7 * 5 * 3 * 1

    # Test 7: Edge case with n = 2
    assert skip_factorial(2) == 2, "Expected 2 for skip_factorial(2)"  # 2

    # Test 8: Edge case with n = 3
    assert skip_factorial(3) == 3, "Expected 3 for skip_factorial(3)"  # 3 * 1

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)