'''
Define a generator function yield_paths which takes in a tree t, a value value, and returns a generator object which yields each path from the root of t to a node that has label value.

Each path should be represented as a list of the labels along that path in the tree.
You may yield the paths in any order.
'''

from tree import Tree
from typing import List

def yield_paths(t: Tree, value: int) -> List[int]:
    if t.label == value:
        yield [t.label]  
    for branch in t.branches:
        for path in yield_paths(branch, value):
            yield [t.label] + path

# Test cases
def test_yield_paths():
    # Test Case 1: A tree with two distinct paths to a node with label 5.
    # Construct t1 as described:
    # t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    t1 = Tree(1, [
        Tree(2, [
            Tree(3),
            Tree(4, [Tree(6)]),
            Tree(5)
        ]),
        Tree(5)
    ])
    # For value 6, there is a unique path [1, 2, 4, 6].
    gen6 = yield_paths(t1, 6)
    path6 = next(gen6)
    expected_path6 = [1, 2, 4, 6]
    assert path6 == expected_path6, f"Test Case 1a Failed: Expected {expected_path6}, got {path6}"
    
    # For value 5, there are two paths: one from the left branch and one direct from the root.
    # Expected paths: [1, 2, 5] and [1, 5]
    gen5 = yield_paths(t1, 5)
    paths5 = list(gen5)
    expected_paths5 = [[1, 2, 5], [1, 5]]
    assert sorted(paths5) == sorted(expected_paths5), f"Test Case 1b Failed: Expected {expected_paths5}, got {paths5}"
    
    # Test Case 2: A nested tree.
    # Construct t2 = Tree(0, [Tree(2, [t1])])
    t2 = Tree(0, [Tree(2, [t1])])
    # For value 2 in t2, there are two paths:
    # - Directly from the root: [0, 2]
    # - A deeper one coming from t1: [0, 2, 1, 2]
    gen2 = yield_paths(t2, 2)
    paths2 = list(gen2)
    expected_paths2 = [[0, 2], [0, 2, 1, 2]]
    assert sorted(paths2) == sorted(expected_paths2), f"Test Case 2 Failed: Expected {expected_paths2}, got {paths2}"

if __name__ == '__main__':
    try:
        test_yield_paths()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
