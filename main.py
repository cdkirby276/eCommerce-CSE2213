"""
main class for group project

"""
from sys import exit
from Inventory import Inventory
from Cart import Cart
from userdata import User

def main():
    """
    Before Login state:
    User will be able to:
        -Login           
        -Create Account
        -Logout
    """
    #will create a user and pass it the db and table name for users
    current_user = User('user.db','User')


    #loop the prelogin state until someone logs in
    while(not(current_user.getLoggedIn())):
        #prompt user to start using the program
        print('Please input the correct command in order to do the following:\n(1)Login\n(2)Logout\n(3)Create Account')
        menuOption = input()

        match(menuOption):
            case '1':
                print('Logging in')
                current_user.login()
                mainMenu(current_user)
            case '2':
                print('Logging out')
                current_user.logout()
            case '3':
                print('Creating account')
                current_user.createAccount()
            case _:
                print('Invalid menu option, please select again\n')


"""
This is where we go once the user logs in
User can then:
    -logout
    -viewAccount info
    -view inventory info
    -view cart info
"""
def mainMenu(current_user):

    #loop through menu options as long as
    while(current_user.getLoggedIn()):
        #prompt user
        print('Please input the correct command in order to do the following:')
        print('(1)Logout\n(2)View Account Information\n(3)View Cart')
        menu_option = input()

        match(menu_option):
            case '1':
                current_user.logout() #user will logout
                break
            case '2':
                current_user.viewAccountInformation() #view user account information
                break
            case '3':

                temp_cart = Cart('cart.db', 'cart')
                temp_cart.viewCart(current_user.getUserID(), 'Inventory.db') #will view the user's "cart"
                break
            case _:
                print('Invalid menu option, please select again\n')
    
    #return to main once user logs out

"""
This is where we go when the use wants to view his/her cart
User will be able to:
    -Go back (to main menu)
    -View cart items
    -Add to cart
    -Remove from cart
    -Checkout

"""
def viewingCart(current_user):

    #make a temp cart
    temp_cart = Cart('cart.db','cart')
    temp_inventory = Inventory('Inventory.db', 'Inventory')
    while(True):
        #prompt user
        print('Please input the correct command in order to do the following:')
        print('(1)Return\n(2)View Cart Items\n(3)Add to cart\n(4)Remove from cart\n(5)Checkout')
        menu_option = input()

        match(menu_option):
            case '1':
                break #will break out of the loop and also return back to main menu
            case '2':
                temp_cart.viewCart(current_user.getUserID(),'Inventory.db') #displays what is in the cart
            case '3':
                #Prompts user to enter the ISBN that is displayed by viewInventory()
                #will then add that book to the cart
                print('What book would you like to add? (Please type ISBN#)')
                temp_inventory.viewInventory()
                temp_ISBN = input()
                temp_cart.addToCart(current_user.getUserID(), temp_ISBN)

            case '4':
                #show user what books they can remove
                print('What book would you like to remove? (Please type ISBN#)')
                temp_cart.viewCart(current_user.getUserID(), 'Inventory,db')
                temp_ISBN = input() #get ISBN selection from user
                
                #try to remove what user says
                temp_cart.removeFromCart(current_user.getUserID(), temp_ISBN)
                print()
            case '5':
                print('Checking out now')
                temp_cart.checkOut(current_user.getUserID()) #calls the checkout function and then breaks to main menu
                break
            case _:
                print('Invalid menu option, please select again:\n')
    
    #returns to main menu


#when script is ran
if __name__ == '__main__':
    main()
