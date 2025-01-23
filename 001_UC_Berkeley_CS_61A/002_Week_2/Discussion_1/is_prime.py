"""
Write a function that returns True if a positive integer n is a prime number and False otherwise.

A prime number n is a number that is not divisible by any numbers other than 1 and n itself.
For example, 13 is prime, since it is only divisible by 1 and 13, but 14 is not, since it is divisible by 1, 2, 7, and 14.

Use the % operator: x % y returns the remainder of x when divided by y.
"""

# Implementation: intuition; use a for-loop until the half point of an odd number
# Time complexity: O(sqrt(n))
# Space complexity: O(1)
def is_prime_v1(n: int) -> bool:
    if n == 2: return True
    if n <= 1 or n % 2 == 0: return False

    for i in range(2, (n // 2) + 1):
        if n % i == 0 and i != n: return False

    return True

# Implementation: ChatGPT 4o
# Time complexity: O(n/2)
# Space complexity: O(1)
def is_prime_v2(n: int) -> bool:
    if n <= 1:  # 1 and below are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # Eliminate even numbers greater than 2
        return False

    # Check divisors from 3 to sqrt(n), skipping even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

try:
    result = is_prime_v1(2)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v1(4)
    assert result == False, f"Expected False but got {result}"
    result = is_prime_v1(3)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v1(5)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v1(9)
    assert result == False, f"Expected False but got {result}"
    result = is_prime_v1(11)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v1(15)
    assert result == False, f"Expected False but got {result}"
    result = is_prime_v1(17)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v1(1)
    assert result == False, f"Expected False but got {result}"
    result = is_prime_v1(23)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v1(25)
    assert result == False, f"Expected False but got {result}"
    result = is_prime_v1(29)
    assert result == True, f"Expected True but got {result}"

    result = is_prime_v2(2)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v2(4)
    assert result == False, f"Expected False but got {result}"
    result = is_prime_v2(3)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v2(5)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v2(9)
    assert result == False, f"Expected False but got {result}"
    result = is_prime_v2(11)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v2(15)
    assert result == False, f"Expected False but got {result}"
    result = is_prime_v2(17)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v2(1)
    assert result == False, f"Expected False but got {result}"
    result = is_prime_v2(23)
    assert result == True, f"Expected True but got {result}"
    result = is_prime_v2(25)
    assert result == False, f"Expected False but got {result}"
    result = is_prime_v2(29)
    assert result == True, f"Expected True but got {result}"

    print("All test cases passed!")
except  AssertionError as error:
    print("A test case failed.")
    print(error)