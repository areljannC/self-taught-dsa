'''
Implement make_change, which takes a positive integer amount and a dictionary of coins.
The coins dictionary keys are positive integer denominations and its values are positive integer coin counts.
For example, {1: 4, 5: 2} represents four pennies and two nickels.
The make_change function returns a list of coins that sum to amount, where the count of any denomination k in the return value is at most coins[k].

If there are multiple ways to make change for amount, prefer to use as many of the smallest coins available and place the smallest coins first in the returned list.
'''
from typing import Dict, List

# Intuition: extract the coins & sort from least to greatest
# Implementation: interation
# Time complexity: O(n * m); n = coin type, m = coin type amount
# Space complexity: O(1)
def make_change(amount: int, coins: Dict[int, int]) -> List[int] | None:
    if not coins: return None

    # extract coins to a list & sort
    coins_list = []
    for coin in coins.keys():
        for i in range(coins[coin]):
            coins_list.append(coin)
    coins_list.sort()

    # add change to a list
    change = []
    for coin in coins_list:
        if amount - coin < 0: return None
        amount -= coin
        change.append(coin)
        if amount == 0: break

    return change if amount == 0 else None

# Test cases
def test_make_change():
    # Test 1: Using coins {2: 1}, amount = 2 -> should return [2]
    result = make_change(2, {2: 1})
    expected = [2]
    assert result == expected, f"Test 1 failed: expected {expected}, got {result}"

    # Test 2: Using coins {1: 2, 2: 1}, amount = 2 -> should return [1, 1]
    result = make_change(2, {1: 2, 2: 1})
    expected = [1, 1]
    assert result == expected, f"Test 2 failed: expected {expected}, got {result}"

    # Test 3: Using coins {1: 2, 2: 1}, amount = 4 -> should return [1, 1, 2]
    result = make_change(4, {1: 2, 2: 1})
    expected = [1, 1, 2]
    assert result == expected, f"Test 3 failed: expected {expected}, got {result}"

    # Test 4: Using coins {2: 1}, amount = 4 -> should return None (not enough coins)
    result = make_change(4, {2: 1})
    expected = None
    assert result == expected, f"Test 4 failed: expected {expected}, got {result}"

    # Prepare a coins dictionary for further tests.
    coins = {2: 2, 3: 2, 4: 3, 5: 1}

    # Test 5: Using coins, amount = 4 -> should return [2, 2]
    result = make_change(4, coins)
    expected = [2, 2]
    assert result == expected, f"Test 5 failed: expected {expected}, got {result}"

if __name__ == '__main__':
    try:
        test_make_change()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
