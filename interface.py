#!usr/bin/env python3

import os
from customer import Customer
from bank import Bank

class Interface:
    _curr_customer = None
    _bank = Bank()
    def __init__(self, menu_type, command_list):
        self._menu_type = menu_type
        self._command_dict = dict(enumerate(command_list, 1))

    def run(self):
        print(self._menu_type)
        while 1:
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
        super().__init__("Main Menu", [new_cust, find_cust, exit_prgrm])

    def get_cust_info(self):
        '''Docstring'''
        name = input("Please enter customer name: ")
        zip_code = input("Please enter customer zip code: ")
        customer = Customer(name, zip_code)
        super()._bank.add_customer(customer)
        os.system("clear")
        print(customer)
        Interface.curr_customer = customer
        self._customer_menu.run()

    def find_cust(self):
        pass

class CustomerMenu(Interface):
    '''Docstring'''
    def __init__(self):
        '''Docstring'''
        select_acct = ("Select Account", self.get_curr)
        create_acct = ("Create Account", self.create_account)
        back = ("Back to Main Menu", self.back)
        exit_prgrm = ("Exit Program", exit)
        super().__init__("Customer Account Options", [select_acct, create_acct, back, exit_prgrm])
    
    def create_account(self):
        super()._bank.new_account(super().curr_customer)

    def get_curr(self):
        print(f"Current customer: {Interface.curr_customer.name}")

class AcctMenu(Interface):
    '''Docstring'''
    def __init__(self):
        '''Docstring'''
        self.create_acct_menu()

    def create_acct_menu(self):
        pass
