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

    def __str__(self):
        return f"Name:\t{self._name}\nID:\t{self._id}\n"\
               f"Date:\t{self._date_enrolled}\nAccounts:\n"\
               f"\t{(acct for acct in self._accts.values())}"
