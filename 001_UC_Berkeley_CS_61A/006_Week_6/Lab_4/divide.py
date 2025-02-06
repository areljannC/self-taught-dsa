"""
Implement divide, which takes two lists of positive integers quotients and divisors.
It returns a dictionary whose keys are the elements of quotients.
For each key q, its corresponding value is a list of all the elements of divisors that can be evenly divided by q.
"""

# Time complexity: O(n * m)
# Space complexity: O(m)
def divide(quotients: list[int], divisors: list[int]) -> dict[int, list[int]]:
    dictionary = {}
    for quotient in quotients:
        if quotient not in dictionary:
            dictionary[quotient] = [divisor for divisor in divisors if divisor % quotient == 0]
    return dictionary

# Test cases
try:
    result = divide([3, 4, 5], [8, 9, 10, 11, 12])
    expectation = {3: [9, 12], 4: [8, 12], 5: [10]}
    assert result == expectation, f"Expected {expectation} but got {result}."

    result = divide(range(1, 5), range(20, 25))
    expectation = {1: [20, 21, 22, 23, 24], 2: [20, 22, 24], 3: [21, 24], 4: [20, 24]}
    assert result == expectation, f"Expected {expectation} but got {result}."

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)
