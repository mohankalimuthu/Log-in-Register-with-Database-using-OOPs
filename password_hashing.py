class Hashing_:
    def __init__(self):
        self.max = 100

    def hashing_transfer(self,email,password):
        hash_idx = self.password_hashing(password)
        return [hash_idx,email]

    def password_hashing(self,password=None):
        val = 0
        for s in password:
            val+=ord(s)
        return val%self.max
