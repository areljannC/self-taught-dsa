'''
Implement repeated, which takes in an iterator t and an integer k greater than 1.
It returns the first value in t that appears k times in a row.

Important: Call next on t only the minimum number of times required. Assume that there is an element of t repeated at least k times in a row.
Hint: If you are receiving a StopIteration exception, your repeated function is calling next too many times.
'''

from typing import Iterator

def repeated(t: Iterator[int], k: int) -> int:
    count, num = 0, None
    
    while True:
        try:
            element = next(t)
            if num == None or num != element:
                num = element
                count = 1
            else:
                count += 1
                if count == k: break
        except StopIteration: break

    return num 


# Test cases
def test_repeated():
    # Test Case 1
    # Input: s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7]), k = 2
    # Expected: 9 (first value that appears 2 times in a row)
    s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    result = repeated(s, 2)
    expected = 9
    assert result == expected, f"Test 1 failed: expected {expected}, got {result}"

    # Test Case 2
    # Input: t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7]), k = 3
    # Expected: 8 (first value that appears 3 times in a row)
    t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    result = repeated(t, 3)
    expected = 8
    assert result == expected, f"Test 2 failed: expected {expected}, got {result}"

    # Test Case 3
    # Input: u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    # First call: k = 3, expected 2 (the first 3 elements are 3, 2, 2, so the first repeated 3 times is 2)
    u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    result = repeated(u, 3)
    expected = 2
    assert result == expected, f"Test 3a failed: expected {expected}, got {result}"
    # Second call on the same iterator: now the iterator has advanced,
    # the next 3 elements should be 2, 1, 4, 4, 5, 5, 5, and the first value that appears 3 times in a row is 5.
    result = repeated(u, 3)
    expected = 5
    assert result == expected, f"Test 3b failed: expected {expected}, got {result}"

    # Test Case 4
    # Input: v = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5]), k = 3
    # Expected: 2 (the first value that appears 3 times in a row is 2)
    v = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    result = repeated(v, 3)
    expected = 2
    assert result == expected, f"Test 4 failed: expected {expected}, got {result}"

if __name__ == '__main__':
    try:
        test_repeated()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
