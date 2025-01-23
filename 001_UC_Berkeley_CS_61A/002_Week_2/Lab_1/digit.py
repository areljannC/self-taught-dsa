"""
Implement digit, which takes positive integers n and k and has only a single return statement as its body.
It returns the digit of n that is k positions to the left of the rightmost digit (the one's digit).
If k is 0, return the rightmost digit.
If there is no digit of n that is k positions to the left of the rightmost digit, return 0.

Hint: Use // and % and the built-in pow function to isolate a particular digit of n.
"""

# Intuition: didn't read the hint
# Time complexity: O(k)
# Space complexity: O(1)
def digits_v1(n: int, k: int) -> int:
    if n < 0 or k < 0: return -1
    t = 0
    for _ in range(k + 1):
        t = n % 10
        n = n // 10
    return t

# Intuition: ChatGPT 4o; prompted with the hint
# Time complexity: O(log k); pow() causes log k time
# Space complexity: O(1)
def digits_v2(n: int, k: int) -> int:
    if k < 0: return 0
    p = pow(10, k) # raise 10 to the power of k; shift k to the right
    r = n // p # remove the last k digits of n
    return r % 10 # return the rightmost digit of the number

# Test cases
try:
    result = digits_v1(3579, 2)
    assert result == 5, f"Expected 5 but got {result}"
    result = digits_v1(3579, 0)
    assert result == 9, f"Expected 9 but got {result}"
    result = digits_v1(3579, 10)
    assert result == 0, f"Expected 0 but got {result}"

    result = digits_v2(3579, 2)
    assert result == 5, f"Expected 5 but got {result}"
    result = digits_v2(3579, 0)
    assert result == 9, f"Expected 9 but got {result}"
    result = digits_v2(3579, 10)
    assert result == 0, f"Expected 0 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)
