from password_hashing import Hashing_
from database import Database
class UserInput:

    def __init__(self,hasher,databaser):
        self.hasher = hasher
        self.databaser = databaser

    def get_input(self):
        fname = str(input("enter your first name:"))
        lname = str(input("enter your last name:"))
        mail = str(input("enter your mail:"))
        password = str(input("enter your password:"))
        self.hash_pipeline(fname,lname,mail,password)



    def hash_pipeline(self,fname,lname,mail,password):
        res = self.hasher.hashing_transfer(mail,password)
        self.login_pipeline(res)
        self.reg_pipeline(fname, lname, mail, res[0])

    def login_pipeline(self,data):
        self.databaser.login_store(data)

    def reg_pipeline(self,fname,lname,mail,password):
        self.databaser.reg_store(fname,lname,mail,password)


hash_tool = Hashing_()
database_tool = Database()
UI = UserInput(hash_tool,database_tool)
UI.get_input()