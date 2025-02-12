'''
Define a function sprout_leaves that takes in a tree, t, and a list of leaves, leaves.
It produces a new tree that is identical to t, but where each old leaf node has new branches, one for each leaf in leaves.
'''

from tree import Tree, is_leaf
from typing import List

def sprout_leaves(t: Tree, leaves: List[Tree]) -> Tree:
    def find_leaves(root: Tree):
        if is_leaf(root):
            for leaf in leaves: root.add_branch(leaf)
        else:
            for branch in root.branches:
                find_leaves(branch)
    find_leaves(t)
    return t


# Test cases
def tree_to_tuple(t: Tree) -> tuple:
    return (t.label, [tree_to_tuple(b) for b in t.branches])

def test_sprout_leaves():
    # Test Case 1:
    # Original tree: 1 with two branches: 2 and 3.
    # After sprouting leaves [4, 5], each old leaf gets two new branches.
    # Expected tree:
    #  1
    #   ├─ 2
    #   │    ├─ 4
    #   │    └─ 5
    #   └─ 3
    #        ├─ 4
    #        └─ 5
    t1 = Tree(1, [Tree(2), Tree(3)])
    new1 = sprout_leaves(t1, [Tree(4), Tree(5)])
    expected1 = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(4), Tree(5)])])
    assert tree_to_tuple(new1) == tree_to_tuple(expected1), f"Test 1 failed: expected {tree_to_tuple(expected1)}, got {tree_to_tuple(new1)}"

    # Test Case 2:
    # Original tree: 1 with one branch 2 which itself has one branch 3.
    # After sprouting leaves [6, 1, 2], only the leaf 3 gets new branches.
    # Expected tree:
    #  1
    #   └─ 2
    #         └─ 3
    #              ├─ 6
    #              ├─ 1
    #              └─ 2
    t2 = Tree(1, [Tree(2, [Tree(3)])])
    new2 = sprout_leaves(t2, [Tree(6), Tree(1), Tree(2)])
    expected2 = Tree(1, [Tree(2, [Tree(3, [Tree(6), Tree(1), Tree(2)])])])
    assert tree_to_tuple(new2) == tree_to_tuple(expected2), f"Test 2 failed: expected {tree_to_tuple(expected2)}, got {tree_to_tuple(new2)}"

    # Test Case 3:
    # Original tree: A single-node tree 7.
    # After sprouting leaves [8, 9], 7 should get two new branches.
    # Expected tree: 7 with branches 8 and 9.
    t3 = Tree(7)
    new3 = sprout_leaves(t3, [Tree(8), Tree(9)])
    expected3 = Tree(7, [Tree(8), Tree(9)])
    assert tree_to_tuple(new3) == tree_to_tuple(expected3), f"Test 3 failed: expected {tree_to_tuple(expected3)}, got {tree_to_tuple(new3)}"

if __name__ == '__main__':
    try:
        test_sprout_leaves()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
