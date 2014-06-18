import random

class Customer:

    wallet = 1000
    bought = False

    def see(self,prev_customer):
        if prev_customer is not None:
            return prev_customer.bought
        else:
            return False

    def decide(self,price,prev_customer):
        if self.see(prev_customer):
            self.wtp = self.wtp + 10
        
        if self.wtp >= price:
            self.wallet = self.wallet - price
            self.bought = True
            #print "bought"
    
    def __init__(self):
        self.wtp = random.randint(0,100)
    

num_customer = 100
customers = []

for index in range(0,num_customer):
    customer = Customer()
    customers.append(customer)


price = 50
prev_customer = None

for customer in customers:
    
    customer.decide(price,prev_customer)

    prev_customer = customer








    

    
