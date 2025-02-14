'''
Write a generator function merge that takes in two infinite generators a and b
that are in increasing order without duplicates and returns a generator that has
all the elements of both generators, in increasing order, without duplicates.
'''

from typing import Generator

def merge(a: Generator[int, None, None], b: Generator[int, None, None]) -> Generator[int, None, None]:
   a_res, b_res = next(a), next(b)
   while True:
        if a_res < b_res:
            yield a_res
            a_res = next(a)
        elif a_res > b_res:
            yield b_res
            b_res = next(b)
        else:
            yield a_res
            a_res, b_res = next(a), next(b)

# Test cases
def test_merge():
    # Helper generator: yields an arithmetic sequence starting at start with step.
    def sequence(start, step):
        while True:
            yield start
            start += step

    # Test 1: Provided example.
    # a: 2, 5, 8, 11, 14, 17, ...
    # b: 3, 5, 7, 9, 11, 13, ...
    # Expected merged: 2, 3, 5, 7, 8, 9, 11, 13, 14, 15, ...
    a = sequence(2, 3)
    b = sequence(3, 2)
    merged = merge(a, b)
    expected1 = [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    result1 = [next(merged) for _ in range(10)]
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"

    # Test 2: Merge even and odd sequences.
    def even_seq():
        n = 2
        while True:
            yield n
            n += 2

    def odd_seq():
        n = 1
        while True:
            yield n
            n += 2

    a = even_seq()  # 2, 4, 6, 8, 10, ...
    b = odd_seq()   # 1, 3, 5, 7, 9, ...
    merged = merge(a, b)
    # Expected merged: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...
    expected2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result2 = [next(merged) for _ in range(10)]
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"

    # Test 3: Merge multiples of 3 and multiples of 5.
    def mult_seq(n):
        i = 1
        while True:
            yield n * i
            i += 1

    a = mult_seq(3)  # 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, ...
    b = mult_seq(5)  # 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, ...
    merged = merge(a, b)
    # Expected merged sequence:
    # 3, 5, 6, 9, 10, 12, 15, 18, 20, 21, ... (note: 15, 30, ... appear only once)
    expected3 = [3, 5, 6, 9, 10, 12, 15, 18, 20, 21]
    result3 = [next(merged) for _ in range(10)]
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"

if __name__ == '__main__':
    try:
        test_merge()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
