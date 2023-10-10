#!usr/bin/env python3

import json
import datetime
import os
from customer import Customer
from account import Account
from broker import Broker

class Bank:
    acct_unique_id = 1111
    customer_unique_id = 1
    _stock_list = {}
    def __init__(self):
        self._customer_list = {}
        with open('stock_data.json', 'r', encoding="utf-8") as stocks:
            stock_data = json.load(stocks)

        for ticker_symbol, data in stock_data.items():
            stock = Broker(ticker_symbol, data["Name"], data["Starting Share Price"],
                   data["Standard Deviation (%)"], data["Average Daily Change (%)"])
            Bank._stock_list.update({stock.ticker: stock})

    @property
    def customer_list(self):
        return self._customer_list

    def add_customer(self, new_customer: Customer):
        self._customer_list.update({new_customer.id: new_customer})

    def new_customer(self):
        for i in range(3):
            name = input("Please enter customer name: ")
            zip_code = input("Please enter customer zip code: ")
            customer = Customer(name, zip_code)

    def find_customer(self):
        search = input("Please enter customer ID or name: ")
        cust_matches = []
        if (search.isdigit()):
            curr_cust = self._customer_list.get(int(search))
            if (curr_cust is None):
                print(f"Customer ID {search} not found")
            return curr_cust
        else:
            for cust in self._customer_list.values():
                if (cust.name.find(search) != -1):
                    cust_matches.append(cust)
            if len(cust_matches) == 1:
                return cust_matches[0]
        print("Please select one of the matching customers:")
        for idx, cust in enumerate(cust_matches):
            print(f"{idx}: {cust.name}")
        selection = int(input("====> "))
        return cust_matches[selection]

    def new_account(self, acct_holder: Customer):
        # acct_holder.print_cust()
        print(acct_holder)
        acct_type = input("Please enter account type (regular or tax-free): ")
        balance = float(input("Please enter starting balance: "))
        new_acct = Account(acct_holder.name,
                           acct_holder.id,
                           acct_type,
                           Bank.acct_unique_id,
                           balance)
        Bank.acct_unique_id += 1
        acct_holder.accts.update({new_acct.acct_number: new_acct})
        return new_acct

    def select_account(self, acct_holder: Customer):
        selection = int(input("Please enter account number: "))
        acct = acct_holder.accts.get(selection)
        if (acct is None):
            print(f"Account {selection} does not exist")
        return acct

    def deposit(self, acct: Account, amt: float):
        pass

    def buy_stock(self, acct: Account):
        for stock in Bank._stock_list.values():
            print(stock)
        print("Please enter the symbol of stock to purchase.")
        selection = input("====> ")
        if (selection not in Bank._stock_list.keys()):
            print("Invalid stock selection")
        else:
            stock = Bank._stock_list.get(selection)
            print(f"How many shares of {stock.name} would you like to purchase?")
            shares = int(input("=====> "))
            purchase_price = shares * stock.price
            if (acct._balance < purchase_price):
                print("Insufficient funds")
            else:
                acct.withdraw(purchase_price)
                transaction = (datetime.datetime.now(),
                               "Purchase",
                               purchase_price)
                acct._transactions.append(transaction)
                holding = (stock, shares, purchase_price)
                # acct._holdings.append(holding)
                acct.holdings.update({selection : holding})

    def sell_stock(self, acct: Account):
        os.system("clear")
        acct.show_holdings()
        print("Please enter symbol of stock to sell.")
        selection = input("=====> ")
        if selection not in acct.holdings.keys():
            print("Not found")

    def __str__(self):
        for customer in self._customer_list:
            return f"Name: {customer._name}\nId: {customer._id}"