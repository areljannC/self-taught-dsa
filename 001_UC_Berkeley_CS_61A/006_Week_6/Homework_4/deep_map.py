'''
Write a function deep_map that takes a list s and a one-argument function f.
s may be a nested list, one that contain other lists. deep_map modifies s by replacing each element within s or any of the lists it contains with the result of calling f on that element.
deep_map returns None and should not create any new lists.
'''

from typing import Callable, List

# Intuition: use recursion and check if second argument type is a list
# Time complexity: O(n)
# Space complexity: O(1); in-place modification
def deep_map(f: Callable[[int | float], int | float], s: List[int | float]):
    n = len(s)
    if n < 1: return
    for i in range(n):
        if isinstance(s[i], List): deep_map(f, s[i])
        else: s[i] = f(s[i])

# Test cases by ChatGPT o3-mini-high
def test_deep_map():
    # Test 1: Square all numbers in a nested list.
    six = [1, 2, [3, [4], 5], 6]
    deep_map(lambda x: x * x, six)
    expected = [1, 4, [9, [16], 25], 36]
    assert six == expected, f"Test 1 failed: expected {expected}, got {six}"

    # Test 2: Check in-place modification (no new sublists should be created).
    s = [3, [1, [4, [1]]]]
    s1 = s[1]
    s2 = s1[1]
    s3 = s2[1]
    deep_map(lambda x: x + 1, s)
    expected = [4, [2, [5, [2]]]]
    assert s == expected, f"Test 2 failed: expected {expected}, got {s}"
    # Ensure the original sublist objects remain unchanged (same identity)
    assert s1 is s[1], "Test 2 failed: s1 is not s[1]"
    assert s2 is s1[1], "Test 2 failed: s2 is not s1[1]"
    assert s3 is s2[1], "Test 2 failed: s3 is not s2[1]"

    # Test 3: Applying an identity function should leave the list unchanged.
    t = [10, [20, [30]]]
    expected = [10, [20, [30]]]
    deep_map(lambda x: x, t)
    assert t == expected, f"Test 3 failed: expected {expected}, got {t}"

    # Test 4: An empty list should remain empty.
    empty = []
    deep_map(lambda x: x * 2, empty)
    assert empty == [], f"Test 4 failed: expected [], got {empty}"

if __name__ == '__main__':
    try:
        test_deep_map()
        print('All test cases passed!')
    except AssertionError as error:
        print('A test case failed.')
        print(error)   
