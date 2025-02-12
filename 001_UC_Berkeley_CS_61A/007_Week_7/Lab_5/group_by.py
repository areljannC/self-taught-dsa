'''
Write a function that takes in a list s and a function fn and returns a dictionary.

The values of the dictionary are lists of elements from s.
Each element e in a list should be constructed such that fn(e) is the same for all elements in that list.
The key for each value should be fn(e).
For each element e in s, check the value that calling fn(e) returns, and add e to the corresponding group.
'''

from typing import List, Callable, Dict

def group_by(s: List[int], fn: Callable[[int], int]) -> Dict[int, List[int]]:
    grouped = {}

    for i in s:
        key = fn(i)
        if key in grouped: grouped[key].append(i) 
        else: grouped[key] = [i]

    return grouped

# Test cases
def test_group_by():
    # Test Case 1: Provided example with integer division by 10.
    result = group_by([12, 23, 14, 45], lambda p: p // 10)
    expected = {1: [12, 14], 2: [23], 4: [45]}
    assert result == expected, f"Test 1 Failed: Expected {expected}, got {result}"

    # Test Case 2: Provided example using square of numbers.
    result = group_by(range(-3, 4), lambda x: x * x)
    expected = {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    assert result == expected, f"Test 2 Failed: Expected {expected}, got {result}"

    # Test Case 3: Empty list should return an empty dictionary.
    result = group_by([], lambda x: x)
    expected = {}
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"

    # Test Case 4: Group elements by their identity.
    result = group_by([1, 1, 2, 2, 3, 3], lambda x: x)
    expected = {1: [1, 1], 2: [2, 2], 3: [3, 3]}
    assert result == expected, f"Test 4 Failed: Expected {expected}, got {result}"

    # Test Case 5: Group by the remainder modulo 2.
    result = group_by([1, 2, 3, 4, 5], lambda x: x % 2)
    expected = {1: [1, 3, 5], 0: [2, 4]}
    assert result == expected, f"Test 5 Failed: Expected {expected}, got {result}"

if __name__ == '__main__':
    try:
        test_group_by()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
