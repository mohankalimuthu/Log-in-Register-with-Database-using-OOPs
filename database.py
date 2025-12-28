class Database:
    def __init__(self):
        self.login_storage = [0]*200
        self.register_storage = {}

#    def input_transfer(self,fname,lname,email,password):
#        db_transfer_val = reg.hashing_transfer(email,password)
#        self.login_storage[db_transfer_val[0]] = db_transfer_val[1]
#        self.register_storage.update({db_transfer_val[0]:[fname,lname,email,db_transfer_val[0]]})

    def login_store(self,res):
        self.login_storage[res[0]] = res[1]
        print(self.login_storage)

    def reg_store(self,fname,lname,email,password):
        self.register_storage.update({password:[fname,lname,email,password]})
        print(self.register_storage)


db_ = Database()
#db_.input_transfer("mohan","kalimuthu","mohanmohan89057@gmail.com","8601")
#db_.input_transfer("abinaya","subramani","abisubramani8601@gmail.com","10688601")


