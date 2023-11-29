"""
This program will test the interaction between the Cart class and Inventory class
Since one of our group members did not complete the user class
Group 9

"""

from Cart import Cart
from Inventory import Inventory


test_cart = Cart('cart.db', 'cart')
test_inv = Inventory('Inventory.db', 'Inventory')

#testing inventory
print('Viewing Inventory')
test_inv.viewInventory()

#testing viewCart
print('View cart test')
test_cart.viewCart('999', 'Inventory.db')

#test checkout
print('Checkout Test')
test_cart.checkOut('999')

#show that we checked out user 999
print('2nd View cart test')
test_cart.viewCart('999', 'Inventory.db')