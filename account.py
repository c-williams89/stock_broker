#!usr/bin/env

class Account:

    def __init__(self, name, id, acct_type, acct_number, balance=0.00):
        self._owner_name = name
        self._owner_id = id
        self._acct_type = acct_type
        self._balance = balance
        self._acct_number = acct_number
        '''3-tuple: (stock, shares, purchase price)'''
        self._holdings = {}
        '''3-tuple: (Timestamp, purchase/sale, price)'''
        self._transactions = []

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def owner_id(self):
        return self._owner_id

    @property
    def acct_type(self):
        return self._acct_type

    @property
    def balance(self):
        return self._balance

    @property
    def acct_number(self):
        return self._acct_number

    @property
    def holdings(self):
        return self._holdings

    @property
    def transactions(self):
        return self._transactions

    def deposit(self, amt: float):
        self._balance += amt

    def withdraw(self, amt: float):
        self._balance -= amt

    def show_holdings(self):
        print("\tHoldings:")
        if len(self._holdings) == 0:
            print("None found")
        for holding in self._holdings.values():
            print(f"\t\t{holding.stock}\n"
                  f"\t\tShares: {holding.shares}\n"
                  f"\t\tPurchase Price: {holding.purchase_price}\n")
            # print(f"\t\t{holding[0]}\n"
            #       f"\t\tShares: {holding[1]}\n"\
            #       f"\t\tPurchase Price: {holding[2]}\n")

    def show_transactions(self):
        print("\tTransactions:")
        for transaction in self._transactions:
            print(f"\t\tTimestamp: {transaction[0]}\n"
                  f"\t\tTransaction: {transaction[1]}\n"
                  f"\t\tPrice: {transaction[2]}\n")

    def __str__(self):
        return f"\tAccount Number: {self._acct_number}\n"\
               f"\tAccount Type: {self._acct_type}\n"\
               f"\tBalance: {self._balance}\n"

class Holding:
    def __init__(self, stock, shares, purchase_price) -> None:
        self._stock = stock
        self._shares = shares
        self._purchase_price = purchase_price

    @property
    def stock(self):
        return self._stock
    
    @property
    def shares(self):
        return self._shares
    
    @property
    def purchase_price(self):
        return self._purchase_price
    
    def sell_shares(self, to_sell):
        self._shares -= to_sell

    def buy_shares(self, to_buy):
        self._shares += to_buy