from random import randint

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

# Implementation: Lomuto's partition scheme 
# Time complexity: O(n log n)
# Space complexity: O(1)
# Legend:
#   - lp: left pointer
#   - rp: right pointer
#   - ap: anchor pointer
#   - ep: explorer pointer
def quick_sort_lomuto(arr: list[int]) -> list[int]:
    if len(arr) < 1: return arr

    def quick_sort(arr: list[int], lp: int, rp: int):
        if lp >= rp: return
        pivot_index = partition(arr, lp, rp) # get pivot index
        quick_sort(arr, lp, pivot_index - 1) # partition left side
        quick_sort(arr, pivot_index + 1, rp) # partition right side

    def partition(arr: list[int], lp: int, rp: int) -> int:
        # choose a random pivot and move it to the right
        pivot_index = randint(lp, rp)
        arr[pivot_index], arr[rp] = arr[rp], arr[pivot_index]

        pivot = arr[rp] # pivot is right-most element
        ap = lp - 1     # anchor pointer starts before left pointer

        # move elements less than pivot to the left using:
        #   - anchor pointer: move elements here
        #   - explorer pointer: find elements less than pivot
        for ep in range(lp, rp):
            if arr[ep] < pivot:
                ap += 1
                arr[ap], arr[ep] = arr[ep], arr[ap]

        ap += 1 # anchor pointer + 1 is the new pivot index
        arr[ap], arr[rp] = arr[rp], arr[ap] # move pivot element to its proper place
        return ap

    quick_sort(arr, 0, len(arr) - 1)
    return arr

# Implementation: Hoare's partition scheme 
# Time complexity: O(n log n)
# Space complexity: O(1)
# Legend:
#   - lp: left pointer
#   - rp: right pointer
#   - ap: anchor pointer
#   - ep: explorer pointer
def quick_sort_hoare(arr: list[int]) -> list[int]:
    if len(arr) < 1: return arr

    def quick_sort(arr: list[int], lp: int, rp: int):
        if lp >= rp: return
        pivot_index = partition(arr, lp, rp) # get pivot index
        quick_sort(arr, lp, pivot_index)     # partition left side
        quick_sort(arr, pivot_index + 1, rp) # partition right side

    def partition(arr: list[int], lp: int, rp: int) -> int:
        # choose a random pivot and move it to the left
        pivot_index = randint(lp, rp)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[lp] = arr[lp], arr[pivot_index]

        # use another set of left and right pointers that starts out of bounds
        lp2, rp2 = lp - 1, rp + 1
        while True:
            # look for a value >= to the pivot
            lp2 += 1
            while arr[lp2] < pivot: lp2 += 1
            
            # look for a value <= to the pivot
            rp2 -= 1
            while arr[rp2] > pivot: rp2 -= 1

            # return the new pivot index when left and right pointers have crossed
            if lp2 >= rp2: return rp2

            # move the values to their proper sides of the pivot
            arr[lp2], arr[rp2] = arr[rp2], arr[lp2]

    quick_sort(arr, 0, len(arr) - 1)
    return arr

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

try:
    assert quick_sort_lomuto([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9], "Expected [1, 1, 3, 4, 5, 9]"
    assert quick_sort_lomuto([10, 20, 5, 30, 40]) == [5, 10, 20, 30, 40], "Expected [5, 10, 20, 30, 40]"
    assert quick_sort_lomuto([100, 50, 25, 12, 6]) == [6, 12, 25, 50, 100], "Expected [6, 12, 25, 50, 100]"

    # ✅ Edge Cases
    assert quick_sort_lomuto([]) == [], "Expected [] (empty list case)"
    assert quick_sort_lomuto([1]) == [1], "Expected [1] (single element case)"
    assert quick_sort_lomuto([5, 5, 5, 5]) == [5, 5, 5, 5], "Expected [5, 5, 5, 5] (all elements same)"

    # ✅ Special Cases
    assert quick_sort_lomuto([-10, -1, -20, 0, 5]) == [-20, -10, -1, 0, 5], "Expected [-20, -10, -1, 0, 5] (negative numbers case)"
    assert quick_sort_lomuto([0, 0, 0, 1, 0]) == [0, 0, 0, 0, 1], "Expected [0, 0, 0, 0, 1] (zero-heavy list)"

    # ✅ Large Input Test
    large_list = list(range(100, 0, -1))  # [100, 99, ..., 1]
    assert quick_sort_lomuto(large_list) == list(range(1, 101)), "Expected sorted list from 1 to 100"

    print("All test cases passed! [quick_sort_lomuto]")
except AssertionError as error:
    print("A test case failed. [quick_sort_lomuto]")
    print(error.with_traceback())

try:
    assert quick_sort_hoare([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9], "Expected [1, 1, 3, 4, 5, 9]"
    assert quick_sort_hoare([10, 20, 5, 30, 40]) == [5, 10, 20, 30, 40], "Expected [5, 10, 20, 30, 40]"
    assert quick_sort_hoare([100, 50, 25, 12, 6]) == [6, 12, 25, 50, 100], "Expected [6, 12, 25, 50, 100]"

    # ✅ Edge Cases
    assert quick_sort_hoare([]) == [], "Expected [] (empty list case)"
    assert quick_sort_hoare([1]) == [1], "Expected [1] (single element case)"
    assert quick_sort_hoare([5, 5, 5, 5]) == [5, 5, 5, 5], "Expected [5, 5, 5, 5] (all elements same)"

    # ✅ Special Cases
    assert quick_sort_hoare([-10, -1, -20, 0, 5]) == [-20, -10, -1, 0, 5], "Expected [-20, -10, -1, 0, 5] (negative numbers case)"
    assert quick_sort_hoare([0, 0, 0, 1, 0]) == [0, 0, 0, 0, 1], "Expected [0, 0, 0, 0, 1] (zero-heavy list)"

    # ✅ Large Input Test
    large_list = list(range(100, 0, -1))  # [100, 99, ..., 1]
    assert quick_sort_hoare(large_list) == list(range(1, 101)), "Expected sorted list from 1 to 100"

    print("All test cases passed! [quick_sort_hoare]")
except AssertionError as error:
    print("A test case failed. [quick_sort_hoare]")
    print(error.with_traceback())
