"""
Implement find_digit, which takes in a positive integer k and returns a function that takes in a positive integer x and returns the kth digit from the right of x.
If x has fewer than k digits, it returns 0.

For example, in the number 4567, 7 is the 1st digit from the right,
6 is the 2nd digit from the right, and the 5th digit from the right
is 0 (since there are only 4 digits).
"""

from typing import Callable

# Time complexity: O(n)
# Space complexity: O(1)
def find_digit(k: int) -> Callable[[int], int]:
    def finder(x: int) -> int:
        pop = 0
        for _ in range(k): pop, x = x % 10, x // 10
        return pop
    return finder

# Test cases by ChatGPT 4o
try:
    # Create a function that finds the 1st digit from the right
    get_1st_digit = find_digit(1)

    # Test 1: Get the 1st digit from the right
    result = get_1st_digit(4567)  # 7 is the 1st digit from the right
    assert result == 7, f"Expected 7 but got {result}"

    # Create a function that finds the 2nd digit from the right
    get_2nd_digit = find_digit(2)

    # Test 2: Get the 2nd digit from the right
    result = get_2nd_digit(4567)  # 6 is the 2nd digit from the right
    assert result == 6, f"Expected 6 but got {result}"

    # Create a function that finds the 5th digit from the right
    get_5th_digit = find_digit(5)

    # Test 3: Get the 5th digit from the right (number has fewer than 5 digits)
    result = get_5th_digit(4567)  # 5th digit does not exist, so it should return 0
    assert result == 0, f"Expected 0 but got {result}"

    # Test 4: Get the 3rd digit from the right for a smaller number
    get_3rd_digit = find_digit(3)
    result = get_3rd_digit(12)  # Number has only 2 digits, so the 3rd digit is 0
    assert result == 0, f"Expected 0 but got {result}"

    # Test 5: Get the 1st digit from the right for a single-digit number
    result = get_1st_digit(9)  # 9 is the 1st digit from the right
    assert result == 9, f"Expected 9 but got {result}"

    # Test 6: Get the 10th digit from the right for a large number
    get_10th_digit = find_digit(10)
    result = get_10th_digit(1234567890)  # 10th digit is 1
    assert result == 1, f"Expected 1 but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)