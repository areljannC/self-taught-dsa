"""
Implement swipe, which prints the digits of argument n, one per line, first backward then forward.
The left-most digit is printed only once.
Do not use while or for or str.
(Use recursion, of course!)
"""

# Intuition: print n as recursion happens
# Time complexity: O(n)
# Space complexity: O(n)
def swipe(n: int) -> None:
    if n <= 0: return
    print(n)
    swipe(n // 10)
    print(n)

swipe(505)