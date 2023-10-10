#!usr/bin/env

class Account:

    def __init__(self, name, id, acct_type, acct_number, balance=0.00):
        self._owner_name = name
        self._owner_id = id
        self._acct_type = acct_type
        self._balance = balance
        self._acct_number = acct_number
        self._holdings = []
        self._transactions = []

    @property
    def acct_number(self):
        return self._acct_number
    
    def deposit(self, amt: float):
        self._balance += amt

    def withdraw(self, amt: float):
        self._balance -= amt

    def show_holdings(self):
        for holding in self._holdings:
            print(f"\t{holding[0]}\n"
                  f"\tShares: {holding[1]}\n"\
                  f"\tPurchase Price: {holding[2]}")

    def __str__(self):
        return f"\tAccount Number: {self._acct_number}\n"\
               f"\tAccount Type: {self._acct_type}\n"\
               f"\tBalance: {self._balance}\n\n"\
               f"\tHoldings:\n{self.show_holdings()}"