#!usr/bin/env
'''Module for Account class'''
from typing import Dict, List


class Account:
    '''Account class'''
    def __init__(self,
                 name: str,
                 id: int,
                 acct_type: str,
                 acct_number: int,
                 label: str,
                 balance=0):
        self._owner_name = name
        self._owner_id = id
        self._acct_type = acct_type
        self._balance = balance
        self._acct_number = acct_number
        self._holdings: Dict[str, Holding] = {}
        self._transactions: List[Transaction] = []
        self._label = label
        self._value = balance

    @property
    def owner_name(self):
        '''Return account owner name'''
        return self._owner_name

    @property
    def owner_id(self):
        '''Return account owner id'''
        return self._owner_id

    @property
    def acct_type(self):
        '''Return account type'''
        return self._acct_type

    @property
    def balance(self):
        '''Return account balance case to float'''
        return float(self._balance / 100)

    @balance.setter
    def balance(self, new):
        self._balance += new

    @property
    def acct_number(self):
        '''Return account number'''
        return self._acct_number

    @property
    def holdings(self):
        '''Return account holdings dictionary'''
        return self._holdings

    @property
    def transactions(self):
        '''Return account transactions list'''
        return self._transactions

    @property
    def label(self):
        '''Return account label'''
        return self._label

    @property
    def value(self):
        '''Calculate and return account value to include holdings'''
        self._value = self.balance
        for holding in self._holdings.values():
            self._value += holding.shares * holding.stock.price
        return float(self._value)

    def deposit(self):
        '''Deposit money to account. For stock sales, can deposit positive or
        negative amount, based on whether sold at a loss or not.'''
        amt = self.get_amt("deposit")
        self._balance += int(amt * 100)
        print(f"Successfully deposited ${amt:.2f}")
        input("Press any key to continue.")

    def withdraw(self):
        '''Deduct from account balance. Used when withdrawing or purchasing
        stock.'''
        amt = self.get_amt("withdraw")
        if amt > self.balance:
            print("Sorry, you do not have over-draft protection.")
            input("Press any key to continue.")
        else:
            self._balance -= int(amt * 100)
            print(f"Succesfully withdrew ${amt:.2f}")
            input("Press anky key to continue.")

    def get_amt(self, tran_type):
        '''Helper function to get amount to deposit/withdraw'''
        amt = -1
        while amt < 0:
            try:
                amt = float(input(f"Please enter amount to {tran_type}. "))
                if amt < 0:
                    print(f"Value to {tran_type} must be non-negative.")
            except ValueError:
                print("Balance must be monetary value (xxx.xx)")
        return amt

    def show_holdings(self):
        '''Iterate and print current account holdings'''
        print("\tHoldings:")
        if len(self._holdings) == 0:
            print("\t\tNo Current Holdings")
        for holding in self._holdings.values():
            holding.stock.increment_price()
            print(holding)

    def show_transactions(self):
        '''Iterate and print current account transactions'''
        print("\tTransactions:")
        if len(self.transactions) == 0:
            print("\t\tNo transaction history")
        for transaction in self._transactions:
            print(transaction)

    def __str__(self):
        return f"\tAccount Number:\t{self.acct_number}\n"\
               f"\tAccount Type:\t{self.acct_type}\n"\
               f"\tBalance:\t${self.balance:.2f}\n"\
               f"\tLabel:\t\t{self.label}\n"\
               f"\tCurrent Value:\t${self.value:.2f}\n"


class Holding:
    '''Holdings class. Account objects have a dictionary of Holding objects'''
    def __init__(self, stock, shares, purchase_price) -> None:
        self._stock = stock
        self._shares = shares
        self._purchase_price = purchase_price

    @property
    def stock(self):
        '''Return holding stock object'''
        return self._stock

    @property
    def shares(self):
        '''Return number of shares'''
        return self._shares

    @property
    def purchase_price(self):
        '''Return purchase price cast to float'''
        return float(self._purchase_price / 100)

    def sell_shares(self, to_sell):
        '''Deduct number of sold shares from number of shares'''
        self._shares -= to_sell

    def buy_shares(self, to_buy):
        '''Add number of bought shares to number of shares'''
        self._shares += to_buy

    def __str__(self):
        return f"\t\t{self.stock}\n"\
               f"\t\tShares:\t\t{self.shares}\n"\
               f"\t\tPurchase Price:\t${self.purchase_price:.2f}/share\n"


class Transaction:
    '''Transaction class. Account objects have a list of transaction objects'''
    def __init__(self, timestamp, tran_type, price, memo):
        self._timestamp = timestamp
        self._tran_type = tran_type
        self._price = price
        self._memo = memo

    @property
    def timestamp(self):
        '''Return transaction timestamp'''
        return self._timestamp

    @property
    def tran_type(self):
        '''Return transaction type'''
        return self._tran_type

    @property
    def price(self):
        '''Return transaction price cast to float'''
        return float(self._price / 100)

    @property
    def memo(self):
        '''Return transaction memo'''
        return self._memo

    def __str__(self):
        return f"\t\tTimestamp:\t{self.timestamp}\n"\
               f"\t\tTransaction:\t{self.tran_type}\n"\
               f"\t\tPrice:\t\t${self.price:.2f}\n"\
               f"\t\tMemo:\t\t{self.memo}\n"
