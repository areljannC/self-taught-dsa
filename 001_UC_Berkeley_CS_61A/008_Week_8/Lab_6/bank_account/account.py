from __future__ import annotations
from transaction import Transaction

class Account:
    _interest = 0.02

    def __init__(self, holder: str) -> None:
        self._balance = 0.0
        self._holder = holder
        self._transactions = []

    @property
    def balance(self) -> int | float:
        return self._balance

    @property
    def holder(self) -> str:
        return self._holder

    def deposit(self, amount: int | float) -> int | float:
        assert amount > 0.0, 'Amount must be greater than 0.0.'
        
        new_balance = self._balance + amount
        transaction = Transaction(len(self._transactions), self._balance, new_balance)
        self._transactions.append(transaction)
        self._balance = new_balance
        return self._balance

    def withdraw(self, amount: int | float) -> int | float:
        assert amount > 0.0, 'Amount must be greater than 0.0.'
        assert self._balance > amount, 'Insufficient balance.'

        new_balance = self._balance - amount
        transaction = Transaction(len(self._transactions), self._balance, new_balance)
        self._transactions.append(transaction)
        self._balance = new_balance
        return self._balance

class CheckingAccount(Account):
    _interest = 0.01
    _withdraw_charge = 1.0

    def withdraw(self, amount: int | float) -> int | float:
        return Account.withdraw(self, amount + self._withdraw_charge)

class SavingsAccount(Account):
    _deposit_charge = 2

    def deposit(self, amount: int | float) -> int | float:
        return Account.deposit(self, amount - self._deposit_charge)

# Test cases by ChatGPT o3-mini-high
def test_account_deposit_withdraw():
    # Create a basic Account.
    a = Account("Alice")
    assert a.holder == "Alice", "Holder should be 'Alice'."
    assert a.balance == 0.0, "Initial balance should be 0.0."

    # Deposit money.
    a.deposit(100)
    assert a.balance == 100, f"Balance should be 100 after deposit, got {a.balance}"

    # Withdraw money.
    a.withdraw(50)
    assert a.balance == 50, f"Balance should be 50 after withdrawal, got {a.balance}"

    # Test deposit with a negative amount (should raise an AssertionError).
    try:
        a.deposit(-10)
    except AssertionError:
        pass
    else:
        assert False, "Depositing a negative amount should raise an AssertionError."

    # Test withdrawing a negative amount.
    try:
        a.withdraw(-10)
    except AssertionError:
        pass
    else:
        assert False, "Withdrawing a negative amount should raise an AssertionError."

    # Test withdrawing more than the balance.
    try:
        a.withdraw(100)
    except AssertionError:
        pass
    else:
        assert False, "Withdrawing more than the balance should raise an AssertionError."

def test_checking_account_withdraw():
    # Create a CheckingAccount.
    c = CheckingAccount("Bob")
    # Deposit money (using the inherited deposit method).
    c.deposit(100)
    # Withdraw 50; CheckingAccount charges $1 extra.
    # So the actual withdrawal amount is 50 + 1 = 51.
    c.withdraw(50)
    expected_balance = 100 - 51  # 49
    assert abs(c.balance - expected_balance) < 1e-6, f"Expected balance {expected_balance} in CheckingAccount, got {c.balance}"

    # Test insufficient funds.
    try:
        c.withdraw(100)
    except AssertionError:
        pass
    else:
        assert False, "Withdrawing more than available should raise an AssertionError in CheckingAccount."

def test_savings_account_deposit():
    # Create a SavingsAccount.
    s = SavingsAccount("Carol")
    # Deposit money. SavingsAccount charges $2 on deposit.
    # So depositing 100 should add 98 to the balance.
    s.deposit(100)
    expected_balance = 98
    assert abs(s.balance - expected_balance) < 1e-6, f"Expected balance {expected_balance} in SavingsAccount, got {s.balance}"

    # Test deposit with a negative amount.
    try:
        s.deposit(-10)
    except AssertionError:
        pass
    else:
        assert False, "Depositing a negative amount should raise an AssertionError in SavingsAccount."

    # Test withdrawing money works as normal.
    s.withdraw(50)
    expected_balance = 98 - 50  # 48
    assert abs(s.balance - expected_balance) < 1e-6, f"Expected balance {expected_balance} after withdrawal, got {s.balance}"

def test_account_transactions():
    # Test basic Account deposit and withdrawal.
    a = Account("Alice")
    # Initially, balance is 0 and no transactions exist.
    assert a.balance == 0.0, "Initial balance should be 0.0"
    assert len(a._transactions) == 0, "Initial transaction history should be empty"

    # Deposit 100.
    new_balance = a.deposit(100)
    assert new_balance == 100, "Balance should be 100 after deposit"
    assert a.balance == 100, "Balance property should be 100 after deposit"
    # A transaction should be recorded.
    assert len(a._transactions) == 1, "There should be one transaction after a deposit"
    t0 = a._transactions[0]
    assert t0.id == 0, "First transaction should have id 0"
    assert t0._before == 0, "Before deposit, balance was 0"
    assert t0._after == 100, "After deposit, balance should be 100"
    assert t0.changed() is True, "Transaction should indicate a change"

    # Withdraw 30.
    new_balance = a.withdraw(30)
    assert new_balance == 70, "Balance should be 70 after withdrawal"
    assert a.balance == 70, "Balance property should be 70 after withdrawal"
    assert len(a._transactions) == 2, "There should be two transactions after a withdrawal"
    t1 = a._transactions[1]
    assert t1.id == 1, "Second transaction should have id 1"
    assert t1._before == 100, "Before withdrawal, balance was 100"
    assert t1._after == 70, "After withdrawal, balance should be 70"
    assert t1.changed() is True, "Transaction should indicate a change"

    # Attempt to withdraw more than balance.
    try:
        a.withdraw(100)
    except AssertionError:
        pass
    else:
        assert False, 'Insufficent balance'
    assert len(a._transactions) == 2, "No new transaction should be recorded for unsuccessful withdrawal"

def test_checking_account_transactions():
    # Create a CheckingAccount (withdrawals incur an extra charge of $1).
    c = CheckingAccount("Bob")
    # Deposit 100.
    c.deposit(100)
    assert c.balance == 100, "After deposit, balance should be 100"
    assert len(c._transactions) == 1, "One transaction expected after deposit"
    t0 = c._transactions[0]
    assert t0.id == 0, "Deposit transaction should have id 0"
    assert t0._after == 100, "After deposit, balance should be 100"

    # Withdraw 30: effective withdrawal = 30 + 1 (charge) = 31.
    new_balance = c.withdraw(30)
    expected_balance = 100 - 31  # 69
    assert new_balance == expected_balance, f"Expected balance {expected_balance}, got {new_balance}"
    assert c.balance == expected_balance, "Balance property should match expected balance"
    assert len(c._transactions) == 2, "Two transactions expected after withdrawal"
    t1 = c._transactions[1]
    assert t1.id == 1, "Withdrawal transaction should have id 1"
    assert t1._before == 100, "Before withdrawal, balance was 100"
    assert t1._after == expected_balance, f"After withdrawal, balance should be {expected_balance}"

def test_savings_account_transactions():
    # Create a SavingsAccount (deposits incur a charge of $2).
    s = SavingsAccount("Carol")
    # Deposit 100: effective deposit = 100 - 2 = 98.
    new_balance = s.deposit(100)
    expected_balance = 98
    assert new_balance == expected_balance, f"Expected balance {expected_balance}, got {new_balance}"
    assert s.balance == expected_balance, "Balance property should be updated correctly"
    assert len(s._transactions) == 1, "One transaction expected after deposit"
    t0 = s._transactions[0]
    assert t0.id == 0, "Deposit transaction should have id 0"
    assert t0._before == 0, "Initial balance before deposit was 0"
    assert t0._after == expected_balance, f"After deposit, balance should be {expected_balance}"

    # Withdraw 50 normally.
    new_balance = s.withdraw(50)
    expected_balance -= 50  # 98 - 50 = 48
    assert new_balance == expected_balance, f"Expected balance {expected_balance} after withdrawal, got {new_balance}"
    assert s.balance == expected_balance, "Balance property should reflect the withdrawal"
    assert len(s._transactions) == 2, "Two transactions expected after withdrawal"
    t1 = s._transactions[1]
    assert t1.id == 1, "Withdrawal transaction should have id 1"
    assert t1._before == 98, "Before withdrawal, balance was 98"
    assert t1._after == expected_balance, f"After withdrawal, balance should be {expected_balance}"

if __name__ == '__main__':
    try:
        test_account_deposit_withdraw()
        test_checking_account_withdraw()
        test_savings_account_deposit()
        test_account_transactions()
        test_checking_account_transactions()
        test_savings_account_transactions()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error.withtrackback())
