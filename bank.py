#!usr/bin/env python3

import json
import datetime
import os
from typing import Dict, Union
from customer import Customer
from account import Account, Holding, Transaction
from broker import Stock


class Bank:
    acct_unique_id = 1111
    customer_unique_id = 1
    _stock_list: Dict[str, Stock] = {}

    def __init__(self):
        self._customer_list = {}
        with open('stock_data.json', 'r', encoding="utf-8") as stocks:
            stock_data = json.load(stocks)

        for ticker_symbol, data in stock_data.items():
            stock = Stock(ticker_symbol,
                          data["Name"],
                          data["Starting Share Price"],
                          data["Standard Deviation (%)"],
                          data["Average Daily Change (%)"])
            Bank._stock_list.update({stock.ticker: stock})

    @property
    def customer_list(self):
        return self._customer_list

    def add_customer(self, new_customer: Customer):
        self._customer_list.update({new_customer.id: new_customer})

    def new_customer(self):
        name = input("Please enter customer name: ")
        try:
            zip_code = int(input("Please enter customer zip code: "))
        except ValueError:
            print("Invalid zip code")
            return None
        else:
            customer = Customer(name, zip_code)
        return customer

    def find_customer(self) -> Union[Customer, None]:
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
                    print("Found a match")
                    cust_matches.append(cust)
            if len(cust_matches) == 0:
                print(f"No matches found for '{search}'")
                return None
            if len(cust_matches) == 1:
                return cust_matches[0]
        print("Please select one of the matching customers:")
        for idx, cust in enumerate(cust_matches):
            print(f"{idx}: {cust.name}")
        selection = -1
        while selection not in range(len(cust_matches)):
            try:
                selection = int(input("=====> "))
            except ValueError:
                print("Invalid option")
        return cust_matches[selection]

    def new_account(self, acct_holder: Customer):
        print(acct_holder)
        acct_type = input("Please enter account type (regular or tax-free): ")
        label = input("Please enter label for account (optional): ")
        os.system("clear")
        new_acct = Account(acct_holder.name,
                           acct_holder.id,
                           acct_type,
                           Bank.acct_unique_id,
                           label)
        Bank.acct_unique_id += 1
        acct_holder.accts.update({new_acct.acct_number: new_acct})
        return new_acct

    def select_account(self, acct_holder: Customer):
        try:
            selection = int(input("Please enter account number: "))
        except ValueError:
            print("Account ID must be a number")
            return None
        acct = acct_holder.accts.get(selection)
        if acct is None:
            print(f"Account {selection} does not exist")
        return acct

    def buy_stock(self, acct: Account):
        for stock in Bank._stock_list.values():
            stock.increment_price()
            print(stock)
        print(f"Current Account Balance: ${acct.balance:.2f}")
        print("Please enter the symbol of stock to purchase.")
        selection = input("====> ")
        if (selection not in Bank._stock_list.keys()):
            print("Invalid stock selection")
        else:
            stock = Bank._stock_list[selection]
            print(f"How many shares of {stock.name} "
                  f"would you like to purchase?")
            while 1:
                try:
                    shares = int(input("=====> "))
                    if shares < 1:
                        print("Stock purchases must be in positive integers.")
                    else:
                        break
                except ValueError:
                    print("Stock purchases must be in whole numbers.")
            purchase_price = shares * stock.price
            if acct.balance < purchase_price:
                print("Insufficient funds")
            else:
                acct.balance = -purchase_price
                dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                memo = input("Optional: Enter memo for this transaction. ")
                os.system("clear")
                transaction = Transaction(dt,
                                          "Purchase",
                                          int(purchase_price * 100),
                                          memo)
                acct.transactions.append(transaction)
                holding = Holding(stock, shares, int(stock.price * 100))
                tmp = acct.holdings.get(selection)
                if tmp is not None:
                    tmp.buy_shares(shares)
                else:
                    acct.holdings.update({selection: holding})

    def sell_stock(self, acct: Account):
        os.system("clear")
        acct.show_holdings()
        print("Please enter symbol of stock to sell.")
        selection = input("=====> ")
        holding = acct.holdings.get(selection)
        if holding is None:
            print("Not found")
        else:
            print("How many shares would you like to sell?")
            shares = 0
            while shares < 1:
                try:
                    shares = int(input("=====> "))
                    if shares < 1:
                        print("Stock sales must be in positive integers")
                except ValueError:
                    print("Stock sales must be in whole numbers.")

            if shares > holding.shares:
                print("Too many shares.")
            else:
                holding.sell_shares(shares)
                revenue = holding.stock.price * shares
                acct.balance = revenue
                dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                memo = input("Optional: Enter memo for this transaction. ")
                os.system("clear")
                transaction = Transaction(dt,
                                          "Sell",
                                          int(revenue * 100),
                                          memo)
                acct.transactions.append(transaction)
                if holding.shares == 0:
                    acct.holdings.pop(holding.stock.ticker)

    def __str__(self):
        for customer in self._customer_list:
            return f"Name: {customer._name}\nId: {customer._id}"
