#!usr/bin/env python3

from customer import Customer
from account import Account

class Bank:
    def __init__(self):
        self._customer_list = []

    @property 
    def customer_list(self):
        return self._customer_list
    
    def add_customer(self, new_customer: Customer):
        self._customer_list.append(new_customer)

    
    def new_customer(self):
        for i in range(3):
            name = input("Please enter customer name: ")
            zip_code = input("Please enter customer zip code: ")
            customer = Customer(name, zip_code)
            self._customer_list.append(customer)

    def new_account(self, acct_holder: Customer):
        print(acct_holder)
        acct_type = input("Please enter account type (regular or tax-free): ")
        balance = float(input("Please enter starting balance: "))
        new_acct = Account(acct_holder.name,
                           acct_holder.id,
                           acct_type,
                           balance)
        acct_holder.accts.append(new_acct)
        print(acct_holder)
        for acct in acct_holder.accts:
            print(acct)

    def select_account(self, acct_holder: Customer):
        pass

    def __str__(self):
        for customer in self._customer_list:
            return f"Name: {customer._name}\nId: {customer._id}"