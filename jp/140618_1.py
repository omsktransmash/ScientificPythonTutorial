class Ex:
    age = 40
    wallet = 2000

    def goto_school(self): #method
        self.location = "School"
        self.wallet = self.wallet - 1000
    def __init__(self,location,wallet,age):
        self.location = "House"
        self.wallet = wallet
        self.age= age

ex = Ex(location = "Seoul", wallet = 2000, age = 20) #??

print ex.location

ex.goto_school()

print ex.location
