"""
Write a function that returns the number of unique digits in a positive integer.
"""

# Implementation: intuition; use an array to count digits
# Time complexity: O(n)
# Space complexity: O(1)
def unique_digits_v1(n: int) -> int:
    counter = [0] * 10
    while n > 0:
        counter[n % 10] += 1
        n //= 10

    unique = 0
    for i in range(len(counter)):
        if counter[i] >= 1: unique += 1

    return unique

# Implementation: ChatGPT 4o; use a set
# Time complexity: O(n)
# Space complexity: O(1)
def unique_digits_v2(n: int) -> int:
    unique = set()
    while n > 0:
        unique.add(n % 10) # Add the last digit to the set
        n //= 10           # Remove the last digit
    return len(unique)     # Return the number of unique digits

try:
    result = unique_digits_v1(8675309)
    assert result == 7, f"Expected 7 but got {result}"
    result = unique_digits_v1(13173131)
    assert result == 3, f"Expected 3 but got {result}"
    result = unique_digits_v1(101)
    assert result == 2, f"Expected 2 but got {result}"

    result = unique_digits_v2(8675309)
    assert result == 7, f"Expected 7 but got {result}"
    result = unique_digits_v2(13173131)
    assert result == 3, f"Expected 3 but got {result}"
    result = unique_digits_v2(101)
    assert result == 2, f"Expected 2 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)
