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

    def viewInventory(self): #Displays all items in the inventory in some formatted way

        try:
            connection = sqlite3.connect("Inventory.db")
            print("Connected to Inventory.db")
            print()
        except:
            print("Failed to connect Inventory.db")
            print()
            sys.exit()

        
        #need to make cursor to call queries
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM inventory')

        result = cursor.fetchall()
        for item in result:
            print(f'{item[0]}. {item[1]} {item[2]} {item[3]} {item[4]} {item[5]} {item[6]}')
            




    def searchInventory(self, Title): #Asks for a *title*, checks the database to see if a result is returned on that name. If so, display all results. If not, the user is informed their search failed
        
        try:
            connection = sqlite3.connect("Inventory.db")
            print("Connected to Inventory.db")
        except:
            print("Failed to connect Inventory.db")
            sys.exit()
        
        #need to make cursor to call queries
        cursor = connection.cursor()



        cursor.execute('SELECT * FROM inventory')

        result = cursor.fetchall()

        i = 0

        for item in result:
            if(item[1] == Title):
                print(f'{item[0]}. {item[1]} {item[2]} {item[3]} {item[4]} {item[5]} {item[6]}')
                i += 1

        if (i == 0):
            print(f'Search for {Title} gave no Results')        

        quit

    def decreaseStock(self, ISBN): #Called with a single ISBN parameter and decreases the stock number in the appropriate database for the appropriate ISBN
        try:
            connection = sqlite3.connect("Inventory.db")
            print("Connected to Inventory.db")
            print()
        except:
            print("Failed to connect Inventory.db")
            print()
            sys.exit()
        
        #need to make cursor to call queries
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM inventory')

        result = cursor.fetchall()

        i = 0

        for item in result:
            if(item[0] == ISBN):
                stock = item[6] - 1
                cursor.execute(f'UPDATE inventory SET Stock = {stock} WHERE ISBN == {ISBN}')
                connection.commit()
                i += 1

        if (i == 0):
            print(f'Search for {ISBN} gave no Results')        


        quit


    """
    Getters / Setters: Appropriate traditional getters and setters for the class variables can
    be added to supplement the code
    """


myInventory = Inventory('Inventory.db', 'inventory') #have to change the functions to user class fields instead of string literals


myInventory.viewInventory()


myInventory.searchInventory("Example")

myInventory.decreaseStock("1")



    
    