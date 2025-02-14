'''
Write a generator function that yiels the elements of the hailstone sequence starting at number n.
After reaching the end of the hailstone sequence, the generator should yield the value 1 indefinitely.

  1. Pick a positive integer n as the start.
  2. If n is even, divide it by 2.
  3. If n is odd, multiply it by 3 and add 1.
  4. Continue this process until n is 1.
'''

def infinite_hailstone(n: int) -> int:
    while n != 1:
        yield n
        if n % 2 == 0: n = n // 2
        else: n = (n * 3) + 1 
    while n == 1: yield n

# Test cases
def test_infinite_hailstone():
    # Create a hailstone generator starting at 10.
    hail_gen = infinite_hailstone(10)
    # According to the problem statement, the first 10 yielded values should be:
    expected_first_10 = [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    actual_first_10 = [next(hail_gen) for _ in range(10)]
    assert actual_first_10 == expected_first_10, \
        f"Test Failed: Expected first 10 values {expected_first_10}, got {actual_first_10}"
    
    # After those 10 values, the next call should yield 1 (since 1 is yielded infinitely)
    next_value = next(hail_gen)
    assert next_value == 1, f"Test Failed: Expected next value to be 1, got {next_value}"

if __name__ == '__main__':
    try:
        test_infinite_hailstone()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
