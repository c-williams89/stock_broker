#!usr/bin/env python3
'''Module for Customer class'''
import datetime
from typing import Dict


class Customer:
    '''Customer class'''

    def __init__(self, name: str, zipcode: int, unique_id: int) -> None:
        self._name = name
        self._zipcode = zipcode
        self._date_enrolled = datetime.date.today()
        self._accts: Dict = {}
        self._id = unique_id

    @property
    def name(self):
        '''Returns customer name'''
        return self._name

    @property
    def zipcode(self):
        '''Return customer zipcode'''
        return self._zipcode

    @property
    def id(self):
        '''Return customer ID'''
        return self._id

    @property
    def accts(self):
        '''Return customer account list'''
        return self._accts

    @property
    def date_enrolled(self):
        '''Return customer date enrolled'''
        return self._date_enrolled

    def show_accounts(self):
        '''Iterate and print customer accounts'''
        for acct in self.accts.values():
            print(f"\tAccount Id:\t{acct.acct_number}\n"
                  f"\tType:\t\t{acct.acct_type}\n"
                  f"\tBalance:\t{acct.balance}\n")

    def __str__(self):
        return f"Name:\t\t{self._name}\n"\
               f"Customer ID:\t{self._id}\n"\
               f"Date Enrolled:\t{self._date_enrolled}\nAccounts:\n"
