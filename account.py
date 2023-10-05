#!usr/bin/env

class Account:
    # unique_id = 1111
    def __init__(self, name, id, acct_type, acct_number, balance=0.00):
        self._owner_name = name
        self._owner_id = id
        self._acct_type = acct_type
        self._balance = balance
        # self._acct_number = self.unique_id
        self._acct_number = acct_number
        # Account.unique_id += 1

    @property
    def acct_number(self):
        return self._acct_number

    def __str__(self):
        return f"\tAccount Number: {self._acct_number}\n"\
               f"\tAccount Type: {self._acct_type}\n"\
               f"\tBalance: {self._balance}\n"