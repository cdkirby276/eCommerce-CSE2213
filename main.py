"""
main class for group project

"""

from Inventory import Inventory
from Cart import Cart
from userdata import User

def main():
    """

        Before Login state:
        User will be able to:
            Login
            Create Account
            Logout
        
    """

    #prompt user to start using the program
    print('Please input the correct command in order to do the following:\n(1)Login\n(2)Logout\n(3)Create Account')
    menuOption = input()

    #will create a user and pass it the db and table name for users
    #currernt_user = User('user.db','User')
    current_user = User()
    temp_loginstate = False


    #loop the prelogin state until someone logs in
    while(not current_user.getLoggedIn()):
        match(menuOption):
            case '1':
                print('Logging in')
                #current_user.login()
                mainMenu(current_user)
            case '2':
                print('Logging out')
                #current_user.logout()
            case '3':
                print('Creating account')
            case _:
                print('Invalid menu option, please select again')


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
                print('Invalid menu option, please select again')
    
        

    #return to main once user logs out
    return 

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
    #returns to main menu
    return 


#when script is ran
if __name__ == '__main__':
    main()
