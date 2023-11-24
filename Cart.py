"""

Joseph Scruppi jps683
Cart class for group project
10/31/23

"""
import sqlite3
import sys
from Inventory import Inventory

class Cart():

    #zero contructor
    def __init__(self):
        self.databaseName = ''
        self.tableName = ''
    #paramaterized constructor
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
    
    """
    Displays all the books in the user's cart (table row)
    uses the inventory database to do so
    """
    def viewCart(self, userID, inventoryDatabase):
        #find all instances in cart.db that match the userID
        try:
            connection = sqlite3.connect(self.databaseName)
        except:
            print("Failed to connect cart database")
            sys.exit()
        
        #need to make cursor to call queries
        cursor = connection.cursor()
        
        #get all the book ISBN that match our user 
        cursor.execute(f'SELECT ISBN FROM {self.tableName} WHERE UserID = {userID}')

        #gives us all the book primary keys that are in our user's cart
        result = cursor.fetchall() #:: gives us a list of tuples

        #connect to inventory database
        try:
            connection = sqlite3.connect(inventoryDatabase)
        except:
            print("Failed to connect to the inventory")
            sys.exit()
        cursor = connection.cursor()

        counter = 1;
        for bookID in result:#looping through our matching userIDs
            cursor.execute(f'SELECT Title, Author, ISBN FROM Inventory WHERE ISBN = {bookID[0]}')
            currentBook = cursor.fetchall() #gives us a list of tuples (Title, Author)

            """
            Formating view cart to the following:
            #. Title by Author (ISBN)

            """
            tmp = list(currentBook[0])#convert currentBook's title author to list

            #output in format to console
            print(f'{counter}. ', end='')
            print(f'{tmp[0]} by {tmp[1]} ({tmp[2]})')

            counter = counter+1

        print()#newline for spacing



    """
    Adds another row to the cart table
    """
    def addToCart(self, userID, ISBN):
        try:
            connection = sqlite3.connect(self.databaseName)
        except:
            print("Failed to connect")
            sys.exit()


        cursor = connection.cursor()

        #inserting another row into cart.db 
        #want the userID and ISBN to match the function parameters
        cursor.execute(f"INSERT INTO {self.tableName}(UserID, ISBN, Quantity) VALUES({userID}, {ISBN}, 1)")

        connection.commit()
        
    """
    Removes an entry from the cart table that matches the userID given to the function from main
    """
    def removeFromCart(self, userID, ISBN):
        try:
            connection = sqlite3.connect(self.databaseName)
        except:
            print("Failed to connect")
            sys.exit()

        
        cursor = connection.cursor()
        #need to delete from cart.db
        cursor.execute(f"DELETE FROM {self.tableName} WHERE UserId = {userID} AND ISBN = {ISBN}")

        connection.commit()

    """
    Removes all the times that match the userID and updates the inventory database based on the amount of books sold in the users cart

    """
    def checkOut(self, userID):
        #connect to the cart database
        try:
            connection = sqlite3.connect(self.databaseName)
        except:
            print("Failed to connect")
            sys.exit()
        
        #select all the ISBNs that the user has in their cart
        cursor = connection.cursor()
        cursor.execute(f'SELECT ISBN FROM {self.tableName} WHERE UserID = {userID}')
        result = cursor.fetchall() #gives us a list of tuples
         
        tmpInventory = Inventory('Inventory.db', 'inventory')
        for temp in result:
            cartItem = temp[0] #ISBN as an int must convert to a string
            #update the inventory database accordingly:
            tmpInventory.decreaseStock(cartItem)

            #remove row from table:
            cursor.execute(f'DELETE FROM {self.tableName} WHERE UserID = {userID} AND ISBN = {cartItem}')
            connection.commit()