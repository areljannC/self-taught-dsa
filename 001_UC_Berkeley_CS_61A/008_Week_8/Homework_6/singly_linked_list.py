from __future__ import annotations

class Node:
    def __init__(self, value: int, next_node: Node | None = None):
        self._value = value
        self._next_node = None if not next_node else next_node

    @property
    def value(self) -> int:
        return self._value

    @property
    def next_node(self) -> Node | None:
        return self._next_node

    def set_value(self, value: int) -> None:
        self._value = value

    def set_next_node(self, next_node: Node | None) -> None:
        self._next_node = next_node

class SinglyLinkedList:
    def __init__(self):
        self._guard_head_node = Node(0)
        self._size = 0
    
    def is_empty(self) -> bool:
        return self._size < 1

    @property
    def size(self) -> str:
        if self.is_empty(): return 'Linked list is empty.'
        return f'Linked list contains {self._size} nodes.'

    def at_head(self) -> str:
        if self.is_empty(): return 'Linked list is empty.'
        return f'Head node value is {self._guard_head_node.next_node.value}.'

    def at(self, index: int) -> str:
        if self.is_empty(): return 'Linked list is empty.'
        if index < 0 or index >= self._size: return 'Invalid index.'

        current_node, i = self._guard_head_node.next_node, 0
        while i != index:
            current_node = current_node.next_node
            i += 1

        return f'Node value at index {index} is {current_node.value}.'

    def get_head_node(self) -> Node | None:
        return self._guard_head_node.next_node

    def add_node(self, node: Node) -> None:
        current_node = self._guard_head_node
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.set_next_node(node) 
        self._size += 1

# Test cases
def test_singly_linked_list_empty():
    """Test the behavior of an empty linked list."""
    ll = SinglyLinkedList()
    assert ll.is_empty() is True, "Expected an empty list to return True for is_empty()"
    assert ll.size == "Linked list is empty.", f"Expected size 'Linked list is empty.', got {ll.size}"
    assert ll.at_head() == "Linked list is empty.", f"Expected at_head() to return 'Linked list is empty.', got {ll.at_head()}"


def test_singly_linked_list_add_node():
    """Test adding a single node to the linked list."""
    ll = SinglyLinkedList()
    node1 = Node(10)
    ll.add_node(node1)
    # After adding one node, the list is no longer empty.
    assert ll.is_empty() is False, "Expected list to be non-empty after adding a node."
    # Note: our implementation increments _size by 1 on each add_node call.
    expected_size = "Linked list contains 1 nodes."
    assert ll.size == expected_size, f"Expected size '{expected_size}', got '{ll.size}'"
    expected_head = "Head node value is 10."
    assert ll.at_head() == expected_head, f"Expected head '{expected_head}', got '{ll.at_head()}'"


def test_singly_linked_list_at_index():
    """Test retrieving nodes at various indices."""
    ll = SinglyLinkedList()
    # Add several nodes.
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    ll.add_node(node1)
    ll.add_node(node2)
    ll.add_node(node3)
    # With three nodes added (each add increases _size by 1), the size should be:
    expected_size = "Linked list contains 3 nodes."
    assert ll.size == expected_size, f"Expected size '{expected_size}', got '{ll.size}'"
    # The head node should be the first added node (value 10)
    expected_head = "Head node value is 10."
    assert ll.at_head() == expected_head, f"Expected head '{expected_head}', got '{ll.at_head()}'"
    # Test retrieval by index:
    # Index 0 should be node1 with value 10.
    expected_index0 = "Node value at index 0 is 10."
    assert ll.at(0) == expected_index0, f"Expected '{expected_index0}', got '{ll.at(0)}'"
    # Index 1 should be node2 with value 20.
    expected_index1 = "Node value at index 1 is 20."
    assert ll.at(1) == expected_index1, f"Expected '{expected_index1}', got '{ll.at(1)}'"
    # Index 2 should be node3 with value 30.
    expected_index2 = "Node value at index 2 is 30."
    assert ll.at(2) == expected_index2, f"Expected '{expected_index2}', got '{ll.at(2)}'"
    # Index 3 is out of range.
    expected_invalid = "Invalid index."
    assert ll.at(3) == expected_invalid, f"Expected '{expected_invalid}', got '{ll.at(3)}'"

if __name__ == '__main__':
    try:
        test_singly_linked_list_empty()
        test_singly_linked_list_add_node()
        test_singly_linked_list_at_index()
        print('All test cases passed!')
    except AssertionError as error:
        print('A test case failed.')
        print(error)
