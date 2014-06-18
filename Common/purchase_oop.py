import random

class Customer:

    bought = False

    def see(self,prev_customer):
        if prev_customer.bought == True:
            self.wtp = self.wtp + 10

    def __init__(self):
        self.wtp = random.randint(0,100)
    

MAX_CUSTOMER = 100

for price in range(0,100):

    total_purchase = 0
    customers = []

    ##make customers
    for customer_id in range(0,MAX_CUSTOMER):
        customer = Customer()
        customers.append(customer)
        

    ##buy!!

    prev_customer = None

    for customer in customers:

        #print "before:",customer.wtp
        
        if prev_customer is not None:
            customer.see(prev_customer)

        if customer.wtp > price:
            ##buy
            customer.bought = True
            total_purchase = total_purchase + 1

        #print "after", customer.wtp

        prev_customer = customer
        
    print price, price*total_purchase
