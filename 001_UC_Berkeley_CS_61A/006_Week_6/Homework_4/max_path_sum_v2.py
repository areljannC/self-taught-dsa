'''
Write a function that takes in a tree and returns the maximum sum of the values along any root-to-leaf path in the tree.
A root-to-leaf path is a sequence of nodes starting at the root and proceeding to some leaf of the tree.
You can assume the tree will have positive numbers for its labels.
'''

from tree import Tree, is_leaf
from typing import List

# Intuition: sum up the values returned from the recursion
# Implementation: recursion
# Time complexity: O(n)
# Space complexity: O(n)
def max_path_sum(root: Tree) -> int | float:
    if is_leaf(root): return root.label

    max_sum = None
    for branch in root.branches:
        branch_sum = max_path_sum(branch)
        if max_sum is None or branch_sum > max_sum:
            max_sum = branch_sum
    return root.label + max_sum

# Test cases by ChatGPT o3-mini-high
def test_max_path_sum_single_node():
    t = Tree(7)
    expected = 7
    result = max_path_sum(t)
    assert result == expected, f"Expected {expected}, got {result}"


def test_max_path_sum_simple():
    t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    expected = 11
    result = max_path_sum(t)
    assert result == expected, f"Expected {expected}, got {result}"


def test_max_path_sum_example_two():
    t2 = Tree(5, [Tree(4, [Tree(1), Tree(3)]), Tree(2, [Tree(10), Tree(3)])])
    expected = 17
    result = max_path_sum(t2)
    assert result == expected, f"Expected {expected}, got {result}"


def test_max_path_sum_deep_tree():
    left_subtree = Tree(3, [Tree(5, [Tree(7)])])
    right_subtree = Tree(4, [Tree(6, [Tree(8)])])
    t = Tree(2, [left_subtree, right_subtree])
    expected = 20
    result = max_path_sum(t)
    assert result == expected, f"Expected {expected}, got {result}"

if __name__ == '__main__':
    try:
        test_max_path_sum_single_node()
        test_max_path_sum_simple()
        test_max_path_sum_example_two()
        test_max_path_sum_deep_tree()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.')
       print(error)
