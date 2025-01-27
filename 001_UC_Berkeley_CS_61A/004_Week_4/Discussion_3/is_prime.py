"""
Implement is_prime that takes an integer n greater than 1.
It returns True if n is a prime number and False otherwise. 
"""

# Intuition: ChatGPT 4o
# Time complexity: O(n)
# Space complexity: O(n)
def is_prime_v1(n: int) -> bool:
    # Base case for n = 1
    if n <= 1:
        return False

    def helper(i: int) -> bool:
        # Base case: If i reaches n, no divisors were found, so n is prime
        if i == n:
            return True
        # Check if i divides n
        if n % i == 0:
            return False
        # Recursive case: Check the next divisor
        return helper(i + 1)
    
    # Start checking divisors from 2
    return helper(2)

# Intuition: ChatGPT 4o
# Implementation: improved version of v1
# Time complexity: O(log n)
# Space complexity: O(log n)
def is_prime_v2(n: int) -> bool:
    # Base case for n = 1
    if n <= 1:
        return False

    def helper(i: int) -> bool:
        # Base case: If i * i > n, no divisors were found, so n is prime
        if i * i > n:
            return True
        # Check if i divides n
        if n % i == 0:
            return False
        # Recursive case: Check the next divisor
        return helper(i + 1)
    
    # Start checking divisors from 2
    return helper(2)

# Test cases
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
    print(error.with_traceback())