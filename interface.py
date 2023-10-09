#!usr/bin/env python3

import os
from customer import Customer
from bank import Bank

class Interface:
    _curr_customer = None
    _bank = Bank()
    _curr_acct = None

    back = ("Back to Main Menu", None)

    def __init__(self, menu_type, command_list):
        self._menu_type = menu_type
        self._command_dict = dict(enumerate(command_list, 1))

    def run(self, details):
        while 1:
            print(f"{self._menu_type} Menu")
            if (self._menu_type != "Main"):
                print(f"{self._menu_type} Details:\n{details}")
            for option in self._command_dict.items():
                print(f"{option[0]}: {option[1][0]}")
            selection = int(input("=====> "))
            func = self._command_dict.get(selection, self._command_dict.get(0))[1]
            if func.__name__ == "back":
                os.system("clear")
                break
            else:
                func()

    def back(self):
        pass

    @property
    def curr_customer(self):
        return self._curr_customer
    
    @curr_customer.setter
    def curr_customer(self, new):
        self._curr_customer = new

class MainMenu(Interface):
    '''Docstring'''
    def __init__(self):
        self._customer_menu = CustomerMenu()
        new_cust = ("Create New Customer", self.get_cust_info)
        find_cust = ("Find Customer", self.find_cust)
        exit_prgrm = ("Exit Program", exit)
        super().__init__("Main", [new_cust, find_cust, exit_prgrm])

    def get_cust_info(self):
        '''Docstring'''
        name = input("Please enter customer name: ")
        zip_code = input("Please enter customer zip code: ")
        customer = Customer(name, zip_code)
        super()._bank.add_customer(customer)
        os.system("clear")
        Interface.curr_customer = customer
        self._customer_menu.run(Interface.curr_customer)

    def find_cust(self):
        Interface.curr_customer = super()._bank.find_customer()
        self._customer_menu.run(Interface.curr_customer)


class CustomerMenu(Interface):
    '''Docstring'''
    def __init__(self):
        '''Docstring'''
        select_acct = ("Select Account", self.get_curr)
        create_acct = ("Create Account", self.create_account)
        back = ("Back to Main Menu", self.back)
        exit_prgrm = ("Exit Program", exit)
        super().__init__("Customer", [select_acct,
                                      create_acct,
                                      back,
                                      exit_prgrm])

    def get_curr(self):
        Interface._curr_acct = super()._bank.select_account(super().curr_customer)
        if (Interface._curr_acct != None):
            self._acct_menu = AcctMenu()
            self._acct_menu.run(Interface._curr_acct)

    def create_account(self):
        super()._bank.new_account(super().curr_customer)

class AcctMenu(Interface):
    '''Docstring'''
    def __init__(self):
        '''Docstring'''
        deposit = ("Deposit", self.acct_depost)
        withdraw = ("Withdraw", self.acct_withdraw)
        buy = ("Buy Stock", None)
        sell = ("Sell Stock", None)
        back = ("Back to Main Menu", self.back)
        exit_prgrm = ("Exit Program", exit)
        super().__init__("Account", [deposit,
                                             withdraw,
                                             buy,
                                             sell,
                                             back,
                                             exit_prgrm])

    def acct_depost(self):
        amt = float(input("Please enter the amount to deposit: "))
        super()._curr_acct.deposit(amt)

    def acct_withdraw(self):
        amt = float(input("Please enter amount to withdraw: "))
        super()._curr_acct.withdraw(amt)
