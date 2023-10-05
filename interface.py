#!usr/bin/env python3

import os
from customer import Customer
from bank import Bank

class Interface:
    # TODO: Have base class hold all three menus so each menu can call super().'menu' to go back
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
        # os.system("clear")
        pass

class MainMenu(Interface):
    '''Docstring'''
    def __init__(self):
        self._bank = Bank()
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
        self._bank.add_customer(customer)
        os.system("clear")
        print(customer)
        self._customer_menu.run()

    def find_cust(self):
        pass

class CustomerMenu(Interface):
    '''Docstring'''
    def __init__(self):
        '''Docstring'''
        select_acct = ("Select Account", None)
        create_acct = ("Create Account", None)
        back = ("Back to Main Menu", self.back)
        exit_prgrm = ("Exit Program", exit)
        super().__init__("Customer Account Options", [select_acct, create_acct, back, exit_prgrm])

    # def back(self):
    #     pass

class AcctMenu(Interface):
    '''Docstring'''
    def __init__(self):
        '''Docstring'''
        self.create_acct_menu()

    def create_acct_menu(self):
        pass
