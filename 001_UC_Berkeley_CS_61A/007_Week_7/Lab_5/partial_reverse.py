'''
Implement the function partial_reverse which reverses a list starting from start until the end of the list.
This reversal should be in-place, meaning that the original list is modified.
Do not create a new list inside your function, even if you do not return it.
The partial_reverse function returns None.
'''

from typing import List

# Intuition: use 2 pointers to swap elements in the list
# Implementation: 2 pointers
# Time complexity: O(n)
# Space complexity: O(1)
def partial_reverse(s: List[int], start: int) -> None:
    lp, rp = start, len(s) - 1
    
    while lp < rp:
        s[lp], s[rp] = s[rp], s[lp]
        lp += 1
        rp -= 1

    return None

# Test cases
def test_partial_reverse():
    # Test Case 1: Given example
    a = [1, 2, 3, 4, 5, 6, 7]
    partial_reverse(a, 2)
    # After reversing from index 2, a should become [1, 2, 7, 6, 5, 4, 3]
    assert a == [1, 2, 7, 6, 5, 4, 3], f"Test Case 1a Failed: expected [1, 2, 7, 6, 5, 4, 3], got {a}"
    
    partial_reverse(a, 5)
    # Reversing from index 5 now should modify a to become [1, 2, 7, 6, 5, 3, 4]
    assert a == [1, 2, 7, 6, 5, 3, 4], f"Test Case 1b Failed: expected [1, 2, 7, 6, 5, 3, 4], got {a}"

    # Test Case 2: Reverse the entire list (start index 0)
    b = [10, 20, 30, 40, 50]
    partial_reverse(b, 0)
    # The entire list should be reversed.
    assert b == [50, 40, 30, 20, 10], f"Test Case 2 Failed: expected [50, 40, 30, 20, 10], got {b}"

    # Test Case 3: Start equals the length of the list (no change)
    c = [1, 2, 3]
    partial_reverse(c, 3)
    # Since start is at the end, the list should remain unchanged.
    assert c == [1, 2, 3], f"Test Case 3 Failed: expected [1, 2, 3], got {c}"

    # Test Case 4: Empty list
    d = []
    partial_reverse(d, 0)
    # An empty list remains empty.
    assert d == [], f"Test Case 4 Failed: expected [], got {d}"

    # Test Case 5: Single-element list (should remain unchanged)
    e = [5]
    partial_reverse(e, 0)
    assert e == [5], f"Test Case 5 Failed: expected [5], got {e}"

if __name__ == '__main__':
    try:
        test_partial_reverse()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
