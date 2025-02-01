"""
Implement print_if, which takes a list s and a one-argument function f.
It prints each element x of s for which f(x) returns a true value.
"""

from typing import Callable

# Time complexity: O(n) 
# Space complexity: O(n) 
def print_if(s: list[int], f: Callable[[int], bool]):
    for x in s:
        if f(x): print(x)

print_if([3, 4, 5, 6], lambda x: x > 4)
