# Implementation: straight from the book
# Time complexity: O(n log n)
# Space complexity: O(n)
def quick_sort_v1(arr: list[int]) -> list[int]:
    if len(arr) < 2: return arr
    pivot = arr[0]
    lesser = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort_v1(lesser) + [pivot] + quick_sort_v2(greater)

# Implementation: improved by ChatGPT 4o
# Time complexity: O(n log n)
# Space complexity: O(n)
from random import randint
def quick_sort_v2(arr: list[int]) -> list[int]:
    if len(arr) < 2: return arr

    # select a random pivot
    pivot = arr[randint(0, len(arr) - 1)]

    # partition
    lesser = [i for i in arr if i < pivot]
    equal = [i for i in arr if i == pivot]
    greater = [i for i in arr if i > pivot]

    # divide and conquer
    return quick_sort_v2(lesser) + equal + quick_sort_v2(greater)

# Implementation: readability improvements; one-pass partitioning
# Time complexity: O(n log n)
# Space complexity: O(n)
from random import randint
def quick_sort_v3(arr: list[int]) -> list[int]:
    if len(arr) < 2: return arr

    # select a random pivot
    pivot = arr[randint(0, len(arr) - 1)]

    # partition
    lesser, equal, greater = [], [], []
    for i in arr:
        if i < pivot: lesser.append(i)
        if i == pivot: equal.append(i)
        if i > pivot: greater.append(i)

    # divide and conquer
    return quick_sort_v3(lesser) + equal + quick_sort_v3(greater)

# Test cases by ChatGPT 4o
try:
    assert quick_sort_v1([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9], "Expected [1, 1, 3, 4, 5, 9]"
    assert quick_sort_v1([10, 20, 5, 30, 40]) == [5, 10, 20, 30, 40], "Expected [5, 10, 20, 30, 40]"
    assert quick_sort_v1([100, 50, 25, 12, 6]) == [6, 12, 25, 50, 100], "Expected [6, 12, 25, 50, 100]"

    # ✅ Edge Cases
    assert quick_sort_v1([]) == [], "Expected [] (empty list case)"
    assert quick_sort_v1([1]) == [1], "Expected [1] (single element case)"
    assert quick_sort_v1([5, 5, 5, 5]) == [5, 5, 5, 5], "Expected [5, 5, 5, 5] (all elements same)"

    # ✅ Special Cases
    assert quick_sort_v1([-10, -1, -20, 0, 5]) == [-20, -10, -1, 0, 5], "Expected [-20, -10, -1, 0, 5] (negative numbers case)"
    assert quick_sort_v1([0, 0, 0, 1, 0]) == [0, 0, 0, 0, 1], "Expected [0, 0, 0, 0, 1] (zero-heavy list)"

    # ✅ Large Input Test
    large_list = list(range(100, 0, -1))  # [100, 99, ..., 1]
    assert quick_sort_v1(large_list) == list(range(1, 101)), "Expected sorted list from 1 to 100"

    print("All test cases passed! [quick_sort_v1]")
except AssertionError as error:
    print("A test case failed. [quick_sort_v1]")
    print(error.with_traceback())

try:
    assert quick_sort_v2([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9], "Expected [1, 1, 3, 4, 5, 9]"
    assert quick_sort_v2([10, 20, 5, 30, 40]) == [5, 10, 20, 30, 40], "Expected [5, 10, 20, 30, 40]"
    assert quick_sort_v2([100, 50, 25, 12, 6]) == [6, 12, 25, 50, 100], "Expected [6, 12, 25, 50, 100]"

    # ✅ Edge Cases
    assert quick_sort_v2([]) == [], "Expected [] (empty list case)"
    assert quick_sort_v2([1]) == [1], "Expected [1] (single element case)"
    assert quick_sort_v2([5, 5, 5, 5]) == [5, 5, 5, 5], "Expected [5, 5, 5, 5] (all elements same)"

    # ✅ Special Cases
    assert quick_sort_v2([-10, -1, -20, 0, 5]) == [-20, -10, -1, 0, 5], "Expected [-20, -10, -1, 0, 5] (negative numbers case)"
    assert quick_sort_v2([0, 0, 0, 1, 0]) == [0, 0, 0, 0, 1], "Expected [0, 0, 0, 0, 1] (zero-heavy list)"

    # ✅ Large Input Test
    large_list = list(range(100, 0, -1))  # [100, 99, ..., 1]
    assert quick_sort_v2(large_list) == list(range(1, 101)), "Expected sorted list from 1 to 100"

    print("All test cases passed! [quick_sort_v2]")
except AssertionError as error:
    print("A test case failed. [quick_sort_v2]")
    print(error.with_traceback())

try:
    assert quick_sort_v3([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9], "Expected [1, 1, 3, 4, 5, 9]"
    assert quick_sort_v3([10, 20, 5, 30, 40]) == [5, 10, 20, 30, 40], "Expected [5, 10, 20, 30, 40]"
    assert quick_sort_v3([100, 50, 25, 12, 6]) == [6, 12, 25, 50, 100], "Expected [6, 12, 25, 50, 100]"

    # ✅ Edge Cases
    assert quick_sort_v3([]) == [], "Expected [] (empty list case)"
    assert quick_sort_v3([1]) == [1], "Expected [1] (single element case)"
    assert quick_sort_v3([5, 5, 5, 5]) == [5, 5, 5, 5], "Expected [5, 5, 5, 5] (all elements same)"

    # ✅ Special Cases
    assert quick_sort_v3([-10, -1, -20, 0, 5]) == [-20, -10, -1, 0, 5], "Expected [-20, -10, -1, 0, 5] (negative numbers case)"
    assert quick_sort_v3([0, 0, 0, 1, 0]) == [0, 0, 0, 0, 1], "Expected [0, 0, 0, 0, 1] (zero-heavy list)"

    # ✅ Large Input Test
    large_list = list(range(100, 0, -1))  # [100, 99, ..., 1]
    assert quick_sort_v3(large_list) == list(range(1, 101)), "Expected sorted list from 1 to 100"

    print("All test cases passed! [quick_sort_v3]")
except AssertionError as error:
    print("A test case failed. [quick_sort_v3]")
    print(error.with_traceback())
