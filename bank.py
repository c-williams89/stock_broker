#!usr/bin/env python3

from customer import Customer

class Bank:
    def __init__(self):
        self._customer_list = []

    @property 
    def customer_list(self):
        return self._customer_list
    
    def add_customer(self, new_customer):
        self._customer_list.append(new_customer)

    
    def new_customer(self):
        for i in range(3):
            name = input("Please enter customer name: ")
            zip_code = input("Please enter customer zip code: ")
            customer = Customer(name, zip_code)
            self._customer_list.append(customer)

    def __str__(self):
        for customer in self._customer_list:
            return f"Name: {customer._name}\nId: {customer._id}"