import random

MAX_CUSTOMER = 100

for price in range(0,100):

    bought = 0
    customers = []

    for customer_id in range(0,MAX_CUSTOMER):
        customer = {}
        customer['wtp'] = random.randint(0,100)
        customers.append(customer)


    for customer in customers:
        if customer['wtp'] > price:
            bought = bought + 1
        

    print price, price*bought
    #print customers
