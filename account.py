#!usr/bin/env

class Account:

    def __init__(self, name, id, acct_type, acct_number, label, balance=0.00):
        self._owner_name = name
        self._owner_id = id
        self._acct_type = acct_type
        self._balance = balance
        self._acct_number = acct_number
        self._holdings = {}
        self._transactions = []
        self._label = label
        self._value = balance

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
        '''Getter for balance'''
        return self._balance

    @balance.setter
    def balance(self, new):
        self._balance += new

    @property
    def acct_number(self):
        return self._acct_number

    @property
    def holdings(self):
        return self._holdings

    @property
    def transactions(self):
        return self._transactions
    
    @property
    def label(self):
        return self._label
    
    @property
    def value(self):
        self._value = self.balance
        for holding in self._holdings.values():
            self._value += holding.shares * holding.stock.price
        return self._value

    def deposit(self):
        amt = self.get_amt("deposit")
        self._balance += amt

    def withdraw(self):
        amt = self.get_amt("withdraw")
        if amt > self.balance:
            print("Sorry, you do not have over-draft protection.")
        else:
            self._balance -= amt

    def get_amt(self, tran_type):
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
        return f"\tAccount Number:\t{self.acct_number}\n"\
               f"\tAccount Type:\t{self.acct_type}\n"\
               f"\tBalance:\t${self.balance:.2f}\n"\
               f"\tLabel:\t\t{self.label}\n"\
               f"\tCurrent Value:\t${self.value:.2f}\n"


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
        return f"\t\t{self.stock}\n"\
               f"\t\tShares:\t\t{self.shares}\n"\
               f"\t\tPurchase Price:\t${self.purchase_price:.2f}/share\n"


class Transaction:
    def __init__(self, timestamp, tran_type, price, memo):
        self._timestamp = timestamp
        self._tran_type = tran_type
        self._price = price
        self._memo = memo

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def tran_type(self):
        return self._tran_type

    @property
    def price(self):
        return self._price
    
    @property
    def memo(self):
        return self._memo

    def __str__(self):
        return f"\t\tTimestamp:\t{self.timestamp}\n"\
               f"\t\tTransaction:\t{self.tran_type}\n"\
               f"\t\tPrice:\t\t${self.price:.2f}\n"\
               f"\t\tMemo:\t\t{self.memo}\n"
