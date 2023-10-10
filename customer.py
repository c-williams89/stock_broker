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
    
    # def print_cust(self):
    #     print(f"Name:\t{self.name}\nID:\t{self.id}\n"\
    #           f"Date Enrolled:\t{self.date_enrolled}\n"\
    #           f"Accounts:\n",self._accts.keys())

    def __str__(self):
        nl = '\n'
        return f"Name:\t{self._name}\nID:\t{self._id}\n"\
               f"Date Enrolled:\t{self._date_enrolled}\nAccounts:\n"\
            #    f"\t{0xa.join(self._accts)}"
