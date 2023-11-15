
class User():

    #jps683 changed the constructors to work
    def __init__(self):
        self.databaseName = ''
        self.tableName = ''
        self.loggedin = False
        self.userID = ''
        
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedin = False
        self.userID = ''

    def Get_Usr(self):
        return self.User_ID

    def Get_Pas(self):
        return self.Password

    def is_admin(self):
        return self.admin

    def Get_address(self):
        return self.Address

    def Set_Usr(self, user):
        self.User_ID = user

    def Set_Pas(self, password):
        self.Password = password

    def Set_admin(self, admin):
        self.admin = admin

    def Set_address(self, address):
        self.Address = address

