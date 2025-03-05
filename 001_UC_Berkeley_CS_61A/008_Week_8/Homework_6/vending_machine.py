'''
Create a class called VendingMachine that represents a vending machine for some product.
A VendingMachine object returns strings describing its interactions.
'''
class VendingMachine:
    NO_PRODUCT_IN_STOCK = 'Nothing left to vend. Please restock.'
    
    def __init__(self, product: str, price: int | float): 
        self._product = product
        self._price = price
        self._stock = 0
        self._funds = 0

    def vend(self) -> str:
        if self._stock <= 0:
            return self.NO_PRODUCT_IN_STOCK
        if self._funds < self._price:
            return f'Please add ${self._price - self._funds} more funds.'
        
        change = self._funds - self._price
        self._funds = 0
        self._stock -= 1

        if change == 0:
            return f'Here is your {self._product}.'
        return f'Here is your {self._product} and ${change} change.'

    def add_funds(self, funds: int | float) -> str:
        if self._stock <= 0:
            return f'{self.NO_PRODUCT_IN_STOCK} Here is your ${funds}.'
        self._funds += funds
        return f'Current balance: ${self._funds}'
    
    def restock(self, amount: int) -> str:
        if amount < 1:
            return 'Restock amount must be 1 or more.'
        self._stock += amount
        return f'Current {self._product} stock: {self._stock}'

# Test cases
def test_vending_machine():
    # Test with candy machine:
    v = VendingMachine('candy', 10)
    
    # Initially, no stock so vend() should return a restock message.
    result = v.vend()
    expected = 'Nothing left to vend. Please restock.'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # Add funds when no stock: funds returned.
    result = v.add_funds(15)
    expected = 'Nothing left to vend. Please restock. Here is your $15.'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # Restock the machine with 2 candies.
    result = v.restock(2)
    expected = 'Current candy stock: 2'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # Try to vend without enough funds.
    result = v.vend()
    expected = 'Please add $10 more funds.'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # Add funds.
    result = v.add_funds(7)
    expected = 'Current balance: $7'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # Still not enough funds to vend.
    result = v.vend()
    expected = 'Please add $3 more funds.'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # Add more funds.
    result = v.add_funds(5)
    expected = 'Current balance: $12'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # Vend the candy; expect change since balance is over price.
    result = v.vend()
    expected = 'Here is your candy and $2 change.'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # After vend, add funds again.
    result = v.add_funds(10)
    expected = 'Current balance: $10'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # Vend the candy; now exactly enough funds.
    result = v.vend()
    expected = 'Here is your candy.'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # With no stock left, adding funds returns the funds.
    result = v.add_funds(15)
    expected = 'Nothing left to vend. Please restock. Here is your $15.'
    assert result == expected, f"Expected: {expected}, got: {result}"

    # Test with soda machine:
    w = VendingMachine('soda', 2)
    
    # Restock soda.
    result = w.restock(3)
    expected = 'Current soda stock: 3'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # Restock again.
    result = w.restock(3)
    expected = 'Current soda stock: 6'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # Add funds for soda.
    result = w.add_funds(2)
    expected = 'Current balance: $2'
    assert result == expected, f"Expected: {expected}, got: {result}"
    
    # Vend soda.
    result = w.vend()
    expected = 'Here is your soda.'
    assert result == expected, f"Expected: {expected}, got: {result}"

if __name__ == '__main__':
    try:
        test_vending_machine()
        print('All test cases passed!')
    except AssertionError as error:
        print('A test case failed.')
        print(error)
