"""
Write a function, count_partitions(n, m), that returns the number of different partitions of n using parts up to m.
This function has a simple solution as a tree-recursive function, based on the following observation:

The number of ways to partition n using integers up to m equals:
    - the number of ways to partition n-m using integers up to m
    - the number of ways to partition n using integers up to m-1
"""

# Not part of Week 3 - Homework 3 but just want to understand how this recursive function works.
def count_partitions(n: int, m: int) -> int:
    if n == 0: return 1
    if n < 0 or m == 0: return 0
    return count_partitions(n - m, m) + count_partitions(n, m - 1)

# Intuition: try to implement memoization using a dictionary with tuple keys
def count_partitions_memo_v1(n: int, m: int) -> int:
    memo = dict()
    def partition(j: int, k: int) -> int:
        if memo.get((j, k)): return memo.get((j, k))
        if j == 0:
            memo[(j, k)] = 1
            return 1
        if j < 0 or k == 0:
            memo[(j, k)] = 0
            return 0
        return partition(j - k, k) + partition(j, k - 1)
    return partition(n, m)

# Intuition: ChatGPT 4o
# Implementation: improved version of v1 with my own unreadable style
def count_partitions_memo_v2(n: int, m: int) -> int:
    memo = dict()
    def partition(j: int, k: int) -> int:
        tk = (j, k)
        if tk in memo: return memo[tk]
        if j == 0: return 1
        if j < 0 or k == 0: return 0
        memo[tk] = partition(j - k, k) + partition(j, k - 1)
        return memo[tk]
    return partition(n, m)


try:
    result, expectation = count_partitions(6, 4), 9
    assert result == expectation, f"Expected {expectation} but got {result}"

    result, expectation = count_partitions_memo_v1(6, 4), 9
    assert result == expectation, f"Expected {expectation} but got {result}"

    result, expectation = count_partitions_memo_v2(6, 4), 9
    assert result == expectation, f"Expected {expectation} but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error.with_traceback())