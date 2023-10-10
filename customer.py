#!usr/bin/env python3

import datetime


class Customer:
    unique_id = 1

    def __init__(self, name, zipcode):
        self._name = name
        self._id = self.unique_id
        self._zipcode = zipcode
        self._date_enrolled = datetime.date.today()
        self._accts = {}
        Customer.unique_id += 1

    @property
    def name(self):
        return self._name

    @property
    def zipcode(self):
        return self._zipcode

    @property
    def id(self):
        return self._id

    @property
    def accts(self):
        return self._accts

    @property
    def date_enrolled(self):
        return self._date_enrolled

    def show_accounts(self):
        for acct in self.accts.values():
            print(f"\tAccount Id:\t{acct.acct_number}\n"
                  f"\tType:\t{acct.acct_type}\n"
                  f"\tBalance:\t{acct.balance}\n")

    def __str__(self):
        return f"Name:\t\t{self._name}\n"\
               f"Customer ID:\t{self._id}\n"\
               f"Date Enrolled:\t{self._date_enrolled}\nAccounts:\n"
