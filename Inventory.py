"""

Cameron Kirby CDK76
Inventory class for E-commerse group project
11/8/23

"""



import sqlite3
import sys

class Inventory():

    #zero contructor
    def __init__(self):
        self.databaseName = ''
        self.tableName = ''

    #paramaterized constructor
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
    
    """

    Start of functions

    """

    def viewInventory(): #Displays all items in the inventory in some formatted way
        try:
            connection = sqlite3.connect("Inventory.db")
            print("Connected to Inventory.db")
        except:
            print("Failed to connect Inventory.db")
            sys.exit()
        
        #need to make cursor to call queries
        cursor = connection.cursor()

        cursor.execute(f'SELECT ISBN FROM {self.tableName}')

        result = cursor.fetchall()
        print(type(result[0]))
        print(result[0][0])


        quit


    def searchInventory(): #Asks for a *title*, checks the database to see if a result is returned on that name. If so, display all results. If not, the user is informed their search failed
        try:
            connection = sqlite3.connect("Inventory.db")
            print("Connected to Inventory.db")
        except:
            print("Failed to connect Inventory.db")
            sys.exit()
        
        #need to make cursor to call queries
        cursor = connection.cursor()

        quit

    def decreaseStock(ISBN): #Called with a single ISBN parameter and decreases the stock number in the appropriate database for the appropriate ISBN
        try:
            connection = sqlite3.connect("Inventory.db")
            print("Connected to Inventory.db")
        except:
            print("Failed to connect Inventory.db")
            sys.exit()
        
        #need to make cursor to call queries
        cursor = connection.cursor()

        quit


    """
    Getters / Setters: Appropriate traditional getters and setters for the class variables can
    be added to supplement the code
    """



myInventory = Inventory('Inventory.db', 'inventory') #have to change the functions to user class fields instead of string literals
myInventory.viewInventory






    
    