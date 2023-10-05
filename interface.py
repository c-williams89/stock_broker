#!usr/bin/env python3

from customer import Customer

class Interface:
    # TODO: Have base class hold all three menus so each menu can call super().'menu' to go back
    def __init__(self, menu_type, command_list):
        self._menu_type = menu_type
        self._command_dict = dict(enumerate(command_list, 1))
        # self._main_menu = None
        
    def display_menu(self):
        print(self._menu_type)
        for option in self._command_dict.items():
            print(f"{option[0]}: {option[1][0]}")
        selection = int(input("=====> "))
        func = self._command_dict.get(selection, self._command_dict.get(0))[1]
        func()

class MainMenu(Interface):
    '''Docstring'''
    def __init__(self):
        new_cust = ("Create New Customer", self.get_cust_info)
        find_cust = ("Find Customer", self.find_cust)
        exit_prgrm = ("Exit Program", exit)
        super().__init__("Main Menu", [new_cust, find_cust, exit_prgrm])

    def get_cust_info(self):
        for i in range(4):
            name = input("Please enter customer name: ")
            zip_code = input("Please enter customer zip code: ")
            customer = Customer(name, zip_code)
            print(customer)
        print("Successfully created new customer")

    def find_cust(self):
        pass

class CustAcctDetailsMenu(Interface):
    '''Docstring'''
    def __init__(self):
        '''Docstring'''
        self.create_cust_acct_details_menu()

    def create_cust_acct_details_menu(self):
        '''Docstring'''
        select_acct = ("Select Account", None)
        create_acct = ("Create Account", None)
        back = ("Back to Main Menu", None)
        exit_prgrm = ("Exit Program", exit)
        super().__init__("Customer Account Options", [select_acct, create_acct, back, exit_prgrm])

class AcctMenu(Interface):
    '''Docstring'''
    def __init__(self):
        '''Docstring'''
        self.create_acct_menu()

    def create_acct_menu(self):
        pass
