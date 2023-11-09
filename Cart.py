"""

Joseph Scruppi jps683
Cart class for group project
10/31/23

"""
import sqlite3
import sys
import Inventory

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

        for bookID in result:
            cursor.execute(f'SELECT Title Author FROM Inventory WHERE ISBN = {bookID[0]}')
            currentBook = cursor.fetchall() #assuming we get currentBook as a tuple or list
            print(currentBook) #will have to format the output once we get inventory db


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
            #print(f'Connected to {self.databaseName}!')
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
        
        return #NEED TO FIX
               #Interaction with Inventory class is not working 
        for temp in result:
            cartItem = temp[0] #ISBN as an int
            #update the inventory database accordingly:
            #!!CALL DECREASE STOCK FUNCTION HERE!!
            tmpInventory = Inventory()


            #remove row from table:
            cursor.execute(f'DELETE FROM {self.tableName} WHERE UserID = {userID} AND ISBN = {cartItem}')
            connection.commit()
            
myCart = Cart('cart.db', 'cart') #have to change the functions to user class fields instead of string literals







    
    