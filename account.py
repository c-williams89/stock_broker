#!usr/bin/env

class Account:
    unique_id = 1111
    def __init__(self, name, id, acct_type, balance=0.00):
        self._owner_name = name
        self._owner_id = id
        self._acct_type = acct_type
        self._balance = balance
        self._acct_number = self.unique_id
        Account.unique_id += 1

    def __str__(self):
        return f"Account Type: {self._acct_type}\n"\
               f"Account Number: {self._acct_number}\n"\
               f"Balance: {self._balance}"