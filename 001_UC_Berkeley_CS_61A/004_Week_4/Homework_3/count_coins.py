"""
Given a positive integer total, a set of coins makes change for total if the sum of the values of the coins is total.
Here we will use standard US Coin values: 1, 5, 10, 25.

For example, the following sets make change for 15:

- 15 1-cent coins

- 10 1-cent
- 1 5-cent coins

- 5 1-cent
- 2 5-cent coins

- 5 1-cent
- 1 10-cent coins

- 3 5-cent coins

- 1 5-cent
- 1 10-cent coin

Thus, there are 6 ways to make change for 15.
Write a recursive function count_coins that takes a positive integer total and returns the number of ways to make change for total using coins.
"""

# Constants
CENT = 1
NICKEL = 5
DIME = 10
QUARTER = 25

# Helpers
def next_larger_coin(coin: int) -> int | None:
    if coin == CENT: return NICKEL
    if coin == NICKEL: return DIME
    if coin == DIME: return QUARTER
    return None

def next_smaller_coin(coin: int) -> int | None:
    if coin == QUARTER: return DIME
    if coin == DIME: return NICKEL
    if coin == NICKEL: return CENT
    return None

# Intuition: based off of these solutions:
# - https://www.learncs.site/docs/curriculum-resource/cs61a/homework/sol-hw03
# - https://martinlwx.github.io/en/hw03-of-cs61a-of-ucb/
# Implementation: start from the largest coin; QUARTER
# Time complexity: O(n)
# Space complexity: O(n)
def count_coins_nsc(change: int) -> int:
    def counter(total: int, coin: int) -> int:
        if total == 0: return 1
        if total < 0 or coin == None: return 0
        return counter(total - coin, coin) + counter(total, next_smaller_coin(coin))
    return counter(change, QUARTER)


# Intuition: based off of the solution above
# Implementation: start from the smallest coin; CENT
# Time complexity: O(n)
# Space complexity: O(n)
def count_coins_nlc(change: int) -> int:
    def counter(total: int, coin: int) -> int:
        if total == coin: return 1
        if total < 0 or coin == None: return 0
        return counter(total - coin, coin) + counter(total, next_larger_coin(coin))
    return counter(change, CENT)

# Test cases
try:
    assert next_larger_coin(CENT) == NICKEL, f"Expected {NICKEL} for next_larger_coin({CENT})"
    assert next_larger_coin(NICKEL) == DIME, f"Expected {DIME} for next_larger_coin({NICKEL})"
    assert next_larger_coin(DIME) == QUARTER, f"Expected {QUARTER} for next_larger_coin({DIME})"
    assert next_larger_coin(QUARTER) == None, f"Expected {None} for next_larger_coin({QUARTER})"

    assert next_smaller_coin(QUARTER) == DIME, f"Expected {DIME} for next_smaller_coin({QUARTER})"
    assert next_smaller_coin(DIME) == NICKEL, f"Expected {NICKEL} for next_smaller_coin({DIME})"
    assert next_smaller_coin(NICKEL) == CENT, f"Expected {CENT} for next_smaller_coin({NICKEL})"
    assert next_smaller_coin(CENT) == None, f"Expected {None} for next_smaller_coin({CENT})"

    result, expectation = count_coins_nsc(15), 6
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = count_coins_nsc(10), 4
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = count_coins_nsc(20), 9
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = count_coins_nsc(100), 242
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = count_coins_nsc(200), 1463
    assert result == expectation, f"Expected {expectation} but got {result}"

    result, expectation = count_coins_nlc(15), 6
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = count_coins_nlc(10), 4
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = count_coins_nlc(20), 9
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = count_coins_nlc(100), 242
    assert result == expectation, f"Expected {expectation} but got {result}"
    result, expectation = count_coins_nlc(200), 1463
    assert result == expectation, f"Expected {expectation} but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error.with_traceback())