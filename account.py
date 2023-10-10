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
            print("\t\tNo Current Holdings")
        for holding in self._holdings.values():
            holding.stock.increment_price()
            print(holding)

    def show_transactions(self):
        print("\tTransactions:")
        if len(self.transactions) == 0:
            print("\t\tNo transaction history")
        for transaction in self._transactions:
            print(transaction)

    def __str__(self):
        return f"\tAccount Number: {self._acct_number}\n"\
               f"\tAccount Type: {self._acct_type}\n"\
               f"\tBalance: ${self._balance:.2f}\n"

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

    def __str__(self):
        return f"\t\tStock: {self.stock}\n"\
               f"\t\tShares: {self.shares}\n"\
               f"\t\tPurchase Price: ${self.purchase_price:.2f}/share\n"
    

class Transaction:
    def __init__(self, timestamp, tran_type, price):
        self._timestamp = timestamp
        self._tran_type = tran_type
        self._price = price

    @property
    def timestamp(self):
        return self._timestamp
    
    @property
    def tran_type(self):
        return self._tran_type
    
    @property
    def price(self):
        return self._price
    
    def __str__(self):
        return f"\t\tTimestamp:\t{self.timestamp}\n"\
               f"\t\tTransaction:\t{self.tran_type}\n"\
               f"\t\tPrice:\t${self.price:.2f}\n"