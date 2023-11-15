class User:
    def __init__(self, user_id, password, admin, address):
        self.User_ID = user_id
        self.Password = password
        self.admin = admin
        self.Address = address

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

