"""
Write a function that takes in a number and determines if the digits contain two adjacent 8s.
"""

# Implementation: intuition; use modulo and division to "pop" the right digit
# Time complexity: O(n)
# Space complexity: O(1)
def double_eights_v1(n: int) -> bool:
    flag = False
    while n > 0:
        isEight = n % 10 == 8
        if flag and isEight: return True
        flag = True if isEight else False
        n //= 10
    return False

# Implementation: ChatGPT 4o
# Time complexity: O(n)
# Space complexity: O(n)
def double_eights_v2(n: int) -> bool:
    if n < 10:  # Base case: less than two digits
        return False
    if n % 10 == 8 and (n // 10) % 10 == 8:  # Check last two digits
        return True
    return double_eights_v2(n // 10)  # Recur with the number excluding the last digit

try:
    result = double_eights_v1(8)
    assert result == False, f"Expected False but got {result}"
    result = double_eights_v1(88)
    assert result == True, f"Expected True but got {result}"
    result = double_eights_v1(2882)
    assert result == True, f"Expected True but got {result}"
    result = double_eights_v1(880088)
    assert result == True, f"Expected True but got {result}"
    result = double_eights_v1(12345)
    assert result == False, f"Expected False but got {result}"
    result = double_eights_v1(80808080)
    assert result == False, f"Expected False but got {result}"

    result = double_eights_v2(8)
    assert result == False, f"Expected False but got {result}"
    result = double_eights_v2(88)
    assert result == True, f"Expected True but got {result}"
    result = double_eights_v2(2882)
    assert result == True, f"Expected True but got {result}"
    result = double_eights_v2(880088)
    assert result == True, f"Expected True but got {result}"
    result = double_eights_v2(12345)
    assert result == False, f"Expected False but got {result}"
    result = double_eights_v2(80808080)
    assert result == False, f"Expected False but got {result}"

    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error)