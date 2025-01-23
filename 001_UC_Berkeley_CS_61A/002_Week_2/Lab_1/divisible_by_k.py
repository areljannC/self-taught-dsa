"""
Write a function that takes positive integers n and k.
It prints all positive integers less than or equal to n that are divisible by k from smallest to largest.
Then, it returns how many numbers were printed.
"""

# Intuition: start loop from k to n (inclusive) and increment by k
# Implementation: iteration
# Time complexity: O(n/k)
# Space complexity: O(1)
def divisible_by_k_v1(n: int, k: int) -> int:
    count = 0
    for i in range(k, n + 1, k):
        if i % k == 0:
            count += 1
            print(i)
    return count

# Intuition: if there's an iterative solution, there's a recursive solution
# Implementation: recursion
# Time complexity: O(n/k)
# Space complexity: O(n/k)
def divisible_by_k_v2(n: int, k: int) -> int:
    if n <= 0: return 0
    return (1 if n % k == 0 else 0) + divisible_by_k_v2(n - k, k)

# Test cases
try:
    result = divisible_by_k_v1(10, 2)
    assert result == 5, f"Expected 5 but got {result}"
    result = divisible_by_k_v1(3, 1)
    assert result == 3, f"Expected 3 but got {result}"
    result = divisible_by_k_v1(6, 7)
    assert result == 0, f"Expected 0 but got {result}"

    result = divisible_by_k_v2(10, 2)
    assert result == 5, f"Expected 5 but got {result}"
    result = divisible_by_k_v2(3, 1)
    assert result == 3, f"Expected 3 but got {result}"
    result = divisible_by_k_v2(6, 7)
    assert result == 0, f"Expected 0 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)