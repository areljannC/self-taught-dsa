"""
Implement has_path, which takes a Tree t and a list p.
It returns whether there is a path from the root of t with labels p.
For example, t1 has a path from its root with labels [3, 5, 6] but not [3, 4, 6] or [5, 6].
"""

from tree import Tree
from typing import List

# Intuition: use recursion on an if-else statement
# Implementation: recursion
# Time complexity: O(n)
# Space complexity: O(n)
def has_path(t: Tree, p: List[Tree]) -> bool:
    if not t or not p: return False  # base case: t or p is empty
    if t.label != p[0]: return False # base case: t does not match p
    if len(p) == 1: return True      # base case: found a match when len of p is 1
    for branch in t.branches:        # check each branch
        if has_path(branch, p[1:]): return True # recurse on the if-else statement
    return False

# Test cases by ChatGPT o3-mini-high
def test_has_path_valid():
    """
    Test that a valid path is found.
    For t1: [3, 5, 6] should be a valid path.
    """
    # Build the tree t1:
    #        3
    #       / \
    #      5   4
    #     /
    #    6
    t1 = Tree(3, [Tree(5, [Tree(6)]), Tree(4)])
    
    assert has_path(t1, [3, 5, 6]) == True, "Expected path [3, 5, 6] to be found in t1."

def test_has_path_invalid_structure():
    """
    Test that a non-existent path returns False.
    For t1, [3, 4, 6] should not be found.
    """
    t1 = Tree(3, [Tree(5, [Tree(6)]), Tree(4)])
    
    assert has_path(t1, [3, 4, 6]) == False, "Expected path [3, 4, 6] not to be found in t1."

def test_has_path_not_from_root():
    """
    Test that a path that does not start at the root returns False.
    For t1, [5, 6] should not be a valid path since it doesn't start at the root.
    """
    t1 = Tree(3, [Tree(5, [Tree(6)]), Tree(4)])
    
    assert has_path(t1, [5, 6]) == False, "Expected path [5, 6] not to be found because it doesn't start at the root."

def test_has_path_single_node():
    """
    Test a tree with a single node.
    The path should only be valid if it matches the root label exactly.
    """
    t2 = Tree(3)
    
    assert has_path(t2, [3]) == True, "Expected path [3] to be found in a single-node tree."
    assert has_path(t2, [4]) == False, "Expected path [4] not to be found in a single-node tree."
    # Also test that an empty path is not valid.
    assert has_path(t2, []) == False, "Empty path should return False."

if __name__ == '__main__':
    try:
        test_has_path_valid()
        test_has_path_invalid_structure()
        test_has_path_not_from_root()
        test_has_path_single_node()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
