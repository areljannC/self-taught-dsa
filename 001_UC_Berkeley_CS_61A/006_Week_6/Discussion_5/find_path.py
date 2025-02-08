"""
Implement find_path, which takes a tree t with unique labels and a value x.
It returns a list containing the labels of the nodes along a path from the root of t to a node labeled x.
If x is not a label in t, return None. Assume that the labels of t are unique.
"""

from tree import Tree
from typing import List

# Intuition: use recursion on an if-else statement
# Implementation: recursion
# Time complexity: O(n)
# Space complexity: O(n)
def find_path(t: Tree, x: str | int | float) -> List[str | int | float] | None:
    if not t: return None
    if t.label == x: return [t.label]
    for branch in t.branches:
        path = find_path(branch, x)
        if path: return [t.label] + path
    return None

# Test cases by ChatGPT o3-mini-high
def test_find_path_single_node():
    """
    Test a tree with a single node.
    If the target is the root label, the returned path should be [root_label].
    If not, it should return None.
    """
    t = Tree(3)
    assert find_path(t, 3) == [3], "Expected path [3] for target 3 in a single-node tree."
    assert find_path(t, 4) is None, "Expected None for target 4 in a single-node tree."

def test_find_path_simple_tree():
    """
    Build a simple tree:
            1
           / \
          2   3
             / \
            4   5
    Test various targets.
    """
    t = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])])
    
    # Test for a target in the left branch.
    assert find_path(t, 2) == [1, 2], "Expected path [1, 2] for target 2."
    
    # Test for targets in the right branch.
    assert find_path(t, 4) == [1, 3, 4], "Expected path [1, 3, 4] for target 4."
    assert find_path(t, 5) == [1, 3, 5], "Expected path [1, 3, 5] for target 5."
    
    # Test for a target that does not exist.
    assert find_path(t, 6) is None, "Expected None for target 6 which is not in the tree."

def test_find_path_complex_tree():
    """
    Build a more complex tree with string labels:
               'a'
             /     \
           'b'      'c'
          /        /   \
        'd'     'e'   'f'
                  |
                 'g'
    Test multiple paths.
    """
    t = Tree('a', [
        Tree('b', [Tree('d')]),
        Tree('c', [
            Tree('e', [Tree('g')]),
            Tree('f')
        ])
    ])
    
    # The root itself.
    assert find_path(t, 'a') == ['a'], "Expected path ['a'] for target 'a'."
    
    # A path down the left branch.
    assert find_path(t, 'd') == ['a', 'b', 'd'], "Expected path ['a', 'b', 'd'] for target 'd'."
    
    # Paths down the right branch.
    assert find_path(t, 'g') == ['a', 'c', 'e', 'g'], "Expected path ['a', 'c', 'e', 'g'] for target 'g'."
    assert find_path(t, 'f') == ['a', 'c', 'f'], "Expected path ['a', 'c', 'f'] for target 'f'."
    
    # Non-existent target.
    assert find_path(t, 'x') is None, "Expected None for target 'x' not found in the tree."

if __name__ == '__main__':
    try:
        test_find_path_single_node()
        test_find_path_simple_tree()
        test_find_path_complex_tree
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
