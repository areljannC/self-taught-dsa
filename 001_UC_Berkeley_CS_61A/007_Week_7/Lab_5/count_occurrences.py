'''
Implement count_occurrences, which takes an iterator t, an integer n, and a value x.
It returns the number of elements equal to x that appear in the first n elements of t.

Important: Call next on t exactly n times. Assume there are at least n elements in t.
'''

from typing import Iterator, List 

def count_occurrences(t: Iterator[int], n: int, x: int) -> int:
    count = 0
    for _ in range(n):
        if next(t) == x: count += 1
    return count

# Test cases
def test_count_occurrences():
    # Test Case 1:
    # Input: [10, 9, 10, 9, 9, 10, 8, 8, 8, 7]
    # n = 10, x = 9
    # Expected: 3 occurrences of 9 in the first 10 elements.
    s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    result = count_occurrences(s, 10, 9)
    expected = 3
    assert result == expected, f"Test Case 1 Failed: expected {expected}, got {result}"
    
    # Test Case 2:
    # Input: [10, 9, 10, 9, 9, 10, 8, 8, 8, 7]
    # n = 3, x = 10
    # Expected: 2 occurrences of 10 in the first 3 elements.
    t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    result = count_occurrences(t, 3, 10)
    expected = 2
    assert result == expected, f"Test Case 2 Failed: expected {expected}, got {result}"
    
    # Test Case 3:
    # Input: [3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    # First call: n = 1, x = 3. The first element is 3.
    # Expected: 1 occurrence.
    u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    result = count_occurrences(u, 1, 3)
    expected = 1
    assert result == expected, f"Test Case 3a Failed: expected {expected}, got {result}"
    
    # Second call on the same iterator:
    # Now u is advanced by one element; the next 3 elements are 2, 2, 2.
    # Call: n = 3, x = 2, expected count is 3.
    result = count_occurrences(u, 3, 2)
    expected = 3
    assert result == expected, f"Test Case 3b Failed: expected {expected}, got {result}"
    
    # Now, the iterator should have advanced 1 + 3 = 4 elements.
    # The remaining elements should be: [1, 2, 1, 4, 4, 5, 5, 5].
    remaining = list(u)
    expected_remaining = [1, 2, 1, 4, 4, 5, 5, 5]
    assert remaining == expected_remaining, f"Test Case 3c Failed: expected remaining {expected_remaining}, got {remaining}"
    
    # Test Case 4:
    # Input: [4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5]
    # n = 6, x = 6.
    # First 6 elements: [4, 1, 6, 6, 7, 7] → there are 2 occurrences of 6.
    v = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    result = count_occurrences(v, 6, 6)
    expected = 2
    assert result == expected, f"Test Case 4 Failed: expected {expected}, got {result}"

if __name__ == '__main__':
    try:
        test_count_occurrences()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
