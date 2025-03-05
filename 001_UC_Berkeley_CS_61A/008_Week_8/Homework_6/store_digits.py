'''
Write a function store_digits that takes in an integer n and returns a linked list where each element of the list is a digit of n.
'''
from __future__ import annotations
from singly_linked_list import Node, SinglyLinkedList

def store_digits(n: int) -> Node | None:
    sll, digits = SinglyLinkedList(), []

    while n != 0:
        digits.append(n % 10)
        n = n // 10
    for i in range(len(digits) - 1, -1, -1):
        sll.add_node(Node(digits[i]))

    return sll.get_head_node()

# Test cases
def linked_list_to_list(head: Node | None) -> list:
    """Helper function to convert a linked list starting at head into a Python list."""
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next_node
    return result


def test_store_digits():
    # Test case 1: Single digit number.
    head1 = store_digits(1)
    result1 = linked_list_to_list(head1)
    expected1 = [1]
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"

    # Test case 2: A multi-digit number (2345).
    head2 = store_digits(2345)
    result2 = linked_list_to_list(head2)
    expected2 = [2, 3, 4, 5]
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"

    # Test case 3: Another multi-digit number (876).
    head3 = store_digits(876)
    result3 = linked_list_to_list(head3)
    expected3 = [8, 7, 6]
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"

    # Test case 4: A number ending with 0 (2450).
    head4 = store_digits(2450)
    result4 = linked_list_to_list(head4)
    expected4 = [2, 4, 5, 0]
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"

if __name__ == '__main__':
    try:
        test_store_digits()
        print('All test cases passed!')
    except AssertionError as error:
        print('A test case failed.')
        print(error)
