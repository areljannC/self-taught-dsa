from __future__ import annotations
from typing import Optional, List, Any

class Tree:
    def __init__(self,
                 label: str | int | float,
                 branches: Optional[List[Tree]] = None):
        self._label = label
        
        if branches is None:
            self._branches = []
        elif not isinstance(branches, List):
            raise TypeError('Branches must be an instance of List.')
        else:
            for branch in branches:
                if not isinstance(branch, Tree):
                    raise TypeError('A branch must be an instance of Tree.')
            self._branches = branches

    @property
    def label(self) -> str | int | float:
        return self._label

    @property
    def branches(self) -> List[Tree]:
        return self._branches

    def add_branch(self, branch: Tree) -> None:
        if not isinstance(branch, Tree):
            raise TypeError('A branch must be an instance of Tree.')
        self._branches.append(branch)

def is_leaf(tree: Tree) -> bool:
    return not tree.branches

# Test cases by ChatGPT o3-mini-high
def test_tree_leaf():
    """Test that a tree with no branches is considered a leaf."""
    t = Tree(4)
    assert t.label == 4, "Label should be 4"
    assert t.branches == [], "Leaf should have no branches"
    assert is_leaf(t), "A tree with no branches should be a leaf"

def test_tree_with_branches():
    """Test that a tree with branches is set up correctly."""
    t1 = Tree(2)
    t2 = Tree(5)
    t = Tree(4, [t1, t2])
    assert t.label == 4, "Label should be 4"
    assert t.branches == [t1, t2], "Branches should contain the two child trees"
    assert not is_leaf(t), "A tree with branches should not be a leaf"
    assert is_leaf(t1), "Child tree t1 should be a leaf"
    assert is_leaf(t2), "Child tree t2 should be a leaf"

def test_invalid_branches_not_list():
    """Test that passing a non-list to branches raises a TypeError."""
    try:
        Tree(4, "not a list")
    except TypeError:
        pass  # Expected
    else:
        assert False, "Expected TypeError when branches is not a list"

def test_invalid_branch_not_tree():
    """Test that passing a list with a non-Tree element raises a TypeError."""
    try:
        Tree(4, [5])
    except TypeError:
        pass  # Expected
    else:
        assert False, "Expected TypeError when a branch element is not a Tree"

def test_add_branch_empty():
    """Test adding a branch to a tree with no initial branches."""
    t = Tree(1)
    branch = Tree(2)
    t.add_branch(branch)
    # After adding, the branches list should contain only the new branch.
    assert t.branches == [branch], f"Expected branches to be [{branch}], got {t.branches}"

def test_add_branch_existing():
    """Test adding a branch to a tree that already has a branch."""
    branch1 = Tree(2)
    t = Tree(1, [branch1])
    branch2 = Tree(3)
    t.add_branch(branch2)
    # The branches list should now be [branch1, branch2].
    assert t.branches == [branch1, branch2], f"Expected branches to be [{branch1}, {branch2}], got {t.branches}"

def test_add_branch_invalid():
    """Test that adding a non-Tree value raises a TypeError."""
    t = Tree(1)
    try:
        t.add_branch(5)  # 5 is not a Tree instance.
    except TypeError:
        pass  # Expected behavior.
    else:
        assert False, "Expected TypeError when adding a non-Tree branch"

if __name__ == '__main__':
    try:
        test_tree_leaf()
        test_tree_with_branches()
        test_invalid_branches_not_list()
        test_invalid_branch_not_tree()
        test_add_branch_empty()
        test_add_branch_existing()
        test_add_branch_invalid()
        print('All test cases passed!')
    except:
       print('A test case failed.') 
