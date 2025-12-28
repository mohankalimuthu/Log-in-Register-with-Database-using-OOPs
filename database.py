class Database:
    def __init__(self):
        self.login_storage = [0]*200
        self.register_storage = {}

    def login_store(self,res):
        self.login_storage[res[0]] = res[1]
        print(self.login_storage)

    def reg_store(self,fname,lname,email,password):
        self.register_storage.update({password:[fname,lname,email,password]})
        print(self.register_storage)


db_ = Database()


