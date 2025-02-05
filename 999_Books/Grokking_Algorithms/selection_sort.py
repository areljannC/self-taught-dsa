# Time complexity: O(n)
# Space complexity: O(1)
def get_smallest_index(arr: list[int]) -> int | None:
    if len(arr) <= 0: return None
    smallest, smallest_index = arr[0], 0
    for i in range(1, len(arr)):
        if arr[i] < smallest: smallest, smallest_index = arr[i], i
    return smallest_index

# Time complexity: O(n^2)
# Space complexity: O(n)
def selection_sort_v1(arr: list[int]) -> list[int]:
   new_arr = []
   for i in range(len(arr)):
       smallest_index = get_smallest_index(arr)
       new_arr.append(arr.pop(smallest_index))
   return new_arr

# Time complexity: O(n^2)
# Space complexity: O(1)
def selection_sort_v2(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] >= arr[j]: arr[i], arr[j] = arr[j], arr[i]
    return arr

# Test cases by ChatGPT 4o
try:
    assert get_smallest_index([3, 1, 4, 1, 5]) == 1  # Smallest at index 1
    assert get_smallest_index([10, 20, 5, 30, 40]) == 2  # Smallest at index 2
    assert get_smallest_index([100]) == 0  # Single element case
    assert get_smallest_index([]) is None  # Empty list case
    assert get_smallest_index([-10, -20, 0, 5, -30]) == 4  # Negative numbers case

    print("All test cases passed! [get_smallest_index]")
except AssertionError as error:
    print("A test case failed. [get_smallest_index]")
    print(error.with_traceback())

try:
    assert selection_sort_v1([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9], "Expected [1, 1, 3, 4, 5, 9]"
    assert selection_sort_v1([10, 20, 5, 30, 40]) == [5, 10, 20, 30, 40], "Expected [5, 10, 20, 30, 40]"
    assert selection_sort_v1([100, 50, 25, 12, 6]) == [6, 12, 25, 50, 100], "Expected [6, 12, 25, 50, 100]"

    # ✅ Edge Cases
    assert selection_sort_v1([]) == [], "Expected [] (empty list case)"
    assert selection_sort_v1([1]) == [1], "Expected [1] (single element case)"
    assert selection_sort_v1([5, 5, 5, 5]) == [5, 5, 5, 5], "Expected [5, 5, 5, 5] (all elements same)"

    # ✅ Special Cases
    assert selection_sort_v1([-10, -1, -20, 0, 5]) == [-20, -10, -1, 0, 5], "Expected [-20, -10, -1, 0, 5] (negative numbers case)"
    assert selection_sort_v1([0, 0, 0, 1, 0]) == [0, 0, 0, 0, 1], "Expected [0, 0, 0, 0, 1] (zero-heavy list)"

    # ✅ Large Input Test
    large_list = list(range(100, 0, -1))  # [100, 99, ..., 1]
    assert selection_sort_v1(large_list) == list(range(1, 101)), "Expected sorted list from 1 to 100"

    print("All test cases passed! [selection_sort_v1]")
except AssertionError as error:
    print("A test case failed. [selection_sort_v1]")
    print(error.with_traceback())

try:
    assert selection_sort_v2([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9], "Expected [1, 1, 3, 4, 5, 9]"
    assert selection_sort_v2([10, 20, 5, 30, 40]) == [5, 10, 20, 30, 40], "Expected [5, 10, 20, 30, 40]"
    assert selection_sort_v2([100, 50, 25, 12, 6]) == [6, 12, 25, 50, 100], "Expected [6, 12, 25, 50, 100]"

    # ✅ Edge Cases
    assert selection_sort_v2([]) == [], "Expected [] (empty list case)"
    assert selection_sort_v2([1]) == [1], "Expected [1] (single element case)"
    assert selection_sort_v2([5, 5, 5, 5]) == [5, 5, 5, 5], "Expected [5, 5, 5, 5] (all elements same)"

    # ✅ Special Cases
    assert selection_sort_v2([-10, -1, -20, 0, 5]) == [-20, -10, -1, 0, 5], "Expected [-20, -10, -1, 0, 5] (negative numbers case)"
    assert selection_sort_v2([0, 0, 0, 1, 0]) == [0, 0, 0, 0, 1], "Expected [0, 0, 0, 0, 1] (zero-heavy list)"

    # ✅ Large Input Test
    large_list = list(range(100, 0, -1))  # [100, 99, ..., 1]
    assert selection_sort_v2(large_list) == list(range(1, 101)), "Expected sorted list from 1 to 100"

    print("All test cases passed! [selection_sort_v2]")
except AssertionError as error:
    print("A test case failed. [selection_sort_v2]")
    print(error.with_traceback())
