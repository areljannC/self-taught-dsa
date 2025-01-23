"""
The fizzbuzz function takes a positive integer n and prints out a single line for each integer from 1 to n.

For each i:
- If i is divisible by both 3 and 5, print fizzbuzz.
- If i is divisible by 3 (but not 5), print fizz.
- If i is divisible by 5 (but not 3), print buzz.
- Otherwise, print the number i.
"""

# Intuition: bro... c'mon... it's fizzbuzz
# Time complexity: O(n)
# Space complexity: O(1)
def fizzbuzz_v1(n: int) -> int:
    if n <= 0: return
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0: print("fizzbuzz")
        elif i % 3 == 0: print("fizz")
        elif i % 5 == 0: print("buzz")
        else: print(i)

# Intuition: make booleans into variables
# Time complexity: O(n)
# Space complexity: O(1)
def fizzbuzz_v2(n: int) -> int:
    if n <= 0: return

    def isFizz(i: int) -> bool: return i % 3 == 0
    def isBuzz(i: int) -> bool: return i % 5 == 0

    for i in range(1, n + 1):
        if isFizz(i) and isBuzz(i): print("fizzbuzz")
        elif isFizz(i): print("fizz")
        elif isBuzz(i): print("buzz")
        else: print(i)

fizzbuzz_v1(16)
fizzbuzz_v2(16)