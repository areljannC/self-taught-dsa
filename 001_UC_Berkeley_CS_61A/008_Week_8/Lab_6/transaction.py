from __future__ import annotations

class Transaction:
    def __init__(self, id: int, before: int | float, after: int | float):
        self._id = id
        self._before = before
        self._after = after

    @property
    def id(self) -> int:
        return self._id

    def changed(self) -> bool:
        return self._before != self._after

    def report(self) -> str:
        if self.changed():
            if self._before > self._after:
                return f'{self._id}: decreased {self._before} -> {self._after}'
            return f'{self._id}: increased {self._before} -> {self._after}'
        return f'{self._id}: no change'

# Test cases by ChatGPT o3-mini-high
def test_transaction():
    # Test case 1: Transaction that resulted in a decrease.
    t1 = Transaction(3, 20, 10)
    expected_report1 = "3: decreased 20 -> 10"
    assert t1.report() == expected_report1, f"Expected '{expected_report1}', got '{t1.report()}'"
    assert t1.changed() is True, "Expected changed() to be True when before != after"
    assert t1.id == 3, f"Expected id 3, got {t1.id}"

    # Test case 2: Transaction that resulted in an increase.
    t2 = Transaction(4, 20, 50)
    expected_report2 = "4: increased 20 -> 50"
    assert t2.report() == expected_report2, f"Expected '{expected_report2}', got '{t2.report()}'"
    assert t2.changed() is True, "Expected changed() to be True when before != after"
    assert t2.id == 4, f"Expected id 4, got {t2.id}"

    # Test case 3: Transaction with no change.
    t3 = Transaction(5, 50, 50)
    expected_report3 = "5: no change"
    assert t3.report() == expected_report3, f"Expected '{expected_report3}', got '{t3.report()}'"
    assert t3.changed() is False, "Expected changed() to be False when before == after"
    assert t3.id == 5, f"Expected id 5, got {t3.id}"

if __name__ == '__main__':
    try:
        test_transaction()
        print('All test cases passed!')
    except:
       print('A test case failed.') 
