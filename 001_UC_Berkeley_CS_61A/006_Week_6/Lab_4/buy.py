"""
Implement buy, which takes a list of required_fruits (strings), a dictionary prices (strings for key, positive integers for value), and a total_amount (integer).
It prints all the ways to buy some of each required fruit so that the total price equals total_amount.
You must include at least one of every fruit in required_fruit and cannot include any other fruits that are not in required_fruit.
"""

def buy(required_fruits, prices, total_amount):
    """
    Print ways to buy some of each fruit so that the sum of prices is amount.

    >>> prices = {'oranges': 4, 'apples': 3, 'bananas': 2, 'kiwis': 9}
    >>> buy(['apples', 'oranges', 'bananas'], prices, 12)
    [2 apples][1 orange][1 banana]
    >>> buy(['apples', 'oranges', 'bananas'], prices, 16)
    [2 apples][1 orange][3 bananas]
    [2 apples][2 oranges][1 banana]
    >>> buy(['apples', 'kiwis'], prices, 36)
    [3 apples][3 kiwis]
    [6 apples][2 kiwis]
    [9 apples][1 kiwi]
    """

    def add(fruits, amount, cart):
        if not fruits and amount == 0:
            print(cart)
        elif fruits and amount > 0:
            fruit = fruits[0]
            price = prices[fruit]
            for k in range(1, amount // price + 1):
                add(fruits[1:], amount - k * price, cart + display(fruit, k))

    add(required_fruits, total_amount, '')

def display(fruit, count):
    """
    Display a count of a fruit in square brackets.

    >>> display('apples', 3)
    '[3 apples]'
    >>> display('apples', 1)
    '[1 apple]'
    """
    assert count >= 1 and fruit[-1] == 's'
    if count == 1:
        fruit = fruit[:-1]  # Remove the plural 's'
    return '[' + str(count) + ' ' + fruit + ']'

prices = {'oranges': 4, 'apples': 3, 'bananas': 2, 'kiwis': 9}
buy(['apples', 'oranges', 'bananas'], prices, 12)
buy(['apples', 'oranges', 'bananas'], prices, 16)
buy(['apples', 'kiwis'], prices, 36)
