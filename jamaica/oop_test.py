class Myunsoo:

    def goto_school(self):
        self.location = "School"
        self.wallet = self.wallet - 1000
        
    def __init__(self,location,wallet,age):
        
        self.location = location
        self.wallet = wallet
        self.age = age

myunsoo = Myunsoo(location = "Taejun", wallet = 2000,age = 40)

print myunsoo.location

myunsoo.goto_school()

print myunsoo.location



