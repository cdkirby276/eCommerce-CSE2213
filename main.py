"""
main class for group project

"""

import sqlite3
import sys
import Cart
import Inventory

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

    match(menuOption):
        case '1':
            print('Logging in')
        case '2':
            print('Logging out')
        case '3':
            print('Creating account')
        case _:
            print('Invalid menu option, please select again')



#when script is ran
if __name__ == '__main__':
    main()
