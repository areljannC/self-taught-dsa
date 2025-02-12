'''
Write a function which takes in a list s, a value before, and a value after.
It inserts after just after each value equal to before in s. It returns s.

Important: No new lists should be created or returned.
'''

from typing import List

# Intuition: count the occurence of before and append that amount to the list
# Implementation: use 2 pointers starting from the end of the list
# Time complexity: O(n)
# Space complexity: O(1)
def insert_items(s: List[int], before: int, after: int):
    ep = len(s) - 1
    s.extend([None] * s.count(before))
    ap = len(s) - 1
    
    while ep >= 0:
        if s[ep] == before:
            s[ap] = after
            s[ap - 1] = s[ep]
            ap = ap - 1
        else:
            s[ap] = s[ep]
        ep, ap = ep - 1, ap - 1

    return s

# Test cases
def test_insert_items():
    # Test Case 1
    test_s = [1, 5, 8, 5, 2, 3]
    new_s = insert_items(test_s, 5, 7)
    # Expected modification in-place: [1, 5, 7, 8, 5, 7, 2, 3]
    assert new_s == [1, 5, 7, 8, 5, 7, 2, 3], f"Expected [1, 5, 7, 8, 5, 7, 2, 3], got {new_s}"
    # Check that the original list was modified in place.
    assert new_s is test_s, "Expected new_s is test_s (in-place modification)"

    # Test Case 2
    double_s = [1, 2, 1, 2, 3, 3]
    double_s = insert_items(double_s, 3, 4)
    # Expected: [1, 2, 1, 2, 3, 4, 3, 4]
    assert double_s == [1, 2, 1, 2, 3, 4, 3, 4], f"Expected [1, 2, 1, 2, 3, 4, 3, 4], got {double_s}"

    # Test Case 3
    large_s = [1, 4, 8]
    large_s2 = insert_items(large_s, 4, 4)
    # Expected: [1, 4, 4, 8]
    assert large_s2 == [1, 4, 4, 8], f"Expected [1, 4, 4, 8], got {large_s2}"

    large_s3 = insert_items(large_s2, 4, 6)
    # Expected: [1, 4, 6, 4, 6, 8]
    assert large_s3 == [1, 4, 6, 4, 6, 8], f"Expected [1, 4, 6, 4, 6, 8], got {large_s3}"
    # Check in-place modification: large_s3 should be the same object as large_s.
    assert large_s3 is large_s, "Expected large_s3 is large_s (in-place modification)"

if __name__ == '__main__':
    try:
        test_insert_items()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
