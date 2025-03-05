'''
Implement a function two_list that takes in two lists and returns a linked list.
The first list contains the values that we want to put in the linked list, and the second list contains the number of each corresponding value.
Assume both lists are the same size and have a length of 1 or greater.
Assume all elements in the second list are greater than 0.
'''
from __future__ import annotations
from typing import List
from singly_linked_list import Node, SinglyLinkedList

def two_list(a: List[int], b: List[int]) -> Node:
    ssl = SinglyLinkedList()

    for value, count in zip(a, b):
        for _ in range(count):
            ssl.add_node(Node(value))

    return ssl.get_head_node()

# Test cases
def linked_list_to_list(head: Node | None) -> list:
    """Convert a linked list starting at head into a Python list of values."""
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next_node
    return result


def test_two_list():
    # Test Case 1:
    # a = [1, 3] and b = [1, 1] should yield a linked list representing [1, 3]
    a = [1, 3]
    b = [1, 1]
    head = two_list(a, b)
    result = linked_list_to_list(head)
    expected = [1, 3]
    assert result == expected, f"Test 1 failed: expected {expected}, got {result}"

    # Test Case 2:
    # a = [1, 3, 2] and b = [2, 2, 1] should yield [1, 1, 3, 3, 2]
    a = [1, 3, 2]
    b = [2, 2, 1]
    head = two_list(a, b)
    result = linked_list_to_list(head)
    expected = [1, 1, 3, 3, 2]
    assert result == expected, f"Test 2 failed: expected {expected}, got {result}"

    # Test Case 3:
    # Single element repeated: a = [7] and b = [3] should yield [7, 7, 7]
    a = [7]
    b = [3]
    head = two_list(a, b)
    result = linked_list_to_list(head)
    expected = [7, 7, 7]
    assert result == expected, f"Test 3 failed: expected {expected}, got {result}"

    # Test Case 4:
    # More complex case:
    # a = [2, 5, 9] and b = [2, 1, 2] should yield [2, 2, 5, 9, 9]
    a = [2, 5, 9]
    b = [2, 1, 2]
    head = two_list(a, b)
    result = linked_list_to_list(head)
    expected = [2, 2, 5, 9, 9]
    assert result == expected, f"Test 4 failed: expected {expected}, got {result}"

if __name__ == '__main__':
    try:
        test_two_list()
        print('All test cases passed!')
    except AssertionError as error:
        print('A test case failed.')
        print(error)
