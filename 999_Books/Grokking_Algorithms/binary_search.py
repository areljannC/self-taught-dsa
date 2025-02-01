# Time complexity: O(log n)
# Space complexity: O(1)
def binary_search(arr: list[int], x: int) -> int:
    lp, hp = 0, len(arr) - 1
    while lp <= hp:
        mp = (lp + hp) // 2
        if arr[mp] == x: return mp
        elif arr[mp] > x: hp = mp - 1
        else: lp = mp + 1
    return -1

# Test cases by ChatGPT 4o
try:
    # ✅ Basic Test Cases
    assert binary_search([1, 2, 3, 4, 5], 3) == 2, "Expected index 2"
    assert binary_search([10, 20, 30, 40, 50], 10) == 0, "Expected index 0"
    assert binary_search([10, 20, 30, 40, 50], 50) == 4, "Expected index 4"

    # ✅ Edge Cases
    assert binary_search([1], 1) == 0, "Expected index 0 (single element)"
    assert binary_search([], 3) == -1, "Expected -1 (empty list)"
    assert binary_search([1, 2, 3, 4, 5], 6) == -1, "Expected -1 (element not found)"
    assert binary_search([1, 3, 5, 7, 9], 2) == -1, "Expected -1 (element not found)"

    # ✅ Cases with Duplicate Values
    assert binary_search([1, 2, 2, 2, 3], 2) in [1, 2, 3], "Expected one of indices 1, 2, or 3"
    assert binary_search([5, 5, 5, 5, 5], 5) in [0, 1, 2, 3, 4], "Expected index between 0-4"

    # ✅ Large Input Test
    large_list = list(range(1000000))
    assert binary_search(large_list, 999999) == 999999, "Expected index 999999"
    assert binary_search(large_list, 0) == 0, "Expected index 0"
    assert binary_search(large_list, 500000) == 500000, "Expected index 500000"
    assert binary_search(large_list, 1000001) == -1, "Expected -1 (out of range)"
    
    print("All test cases passed!")
except AssertionError as error:
    print("A test case failed.")
    print(error.with_traceback())
