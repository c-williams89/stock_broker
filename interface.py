#!usr/bin/env python3
'''Module for Interface base class and menu sub-classes'''
import os
from bank import Bank
from typing import List


class Interface:
    '''Interface Base Class'''
    _curr_customer = None
    _bank = Bank()
    _curr_acct = None

    def __init__(self, menu_type: str, command_list: List) -> None:
        self._menu_type = menu_type
        self._command_dict = dict(enumerate(command_list, 1))

    def run(self, details):
        '''Controlling method to display menu and handle options'''
        while 1:
            print(f"{self._menu_type} Menu")
            if self._menu_type != "Main":
                print(f"{self._menu_type} Details:\n{details}")
                if self._menu_type == "Customer":
                    details.show_accounts()
                else:
                    details.show_holdings()
                    details.show_transactions()
            for option in self._command_dict.items():
                print(f"{option[0]}: {option[1][0]}")
            try:
                selection = int(input("=====> "))
            except ValueError:
                print("Invalid option selected")
            else:
                os.system("clear")
                func = self._command_dict.get(selection, None)
                if func is None:
                    print("Invalid Menu Option")
                elif func[1].__name__ == "back":
                    os.system("clear")
                    break
                else:
                    func[1]()

    def back(self):
        '''Method reference for sub-classes to control back-to option'''
        pass

    def quit_prgrm(self):
        '''Exits program'''
        exit()

    @property
    def curr_customer(self):
        '''Returns current customer being accessed'''
        return self._curr_customer

    @curr_customer.setter
    def curr_customer(self, new):
        self._curr_customer = new


class MainMenu(Interface):
    '''Class for Main Menu'''
    def __init__(self):
        self._customer_menu = CustomerMenu()
        new_cust = ("Create New Customer", self.get_cust_info)
        find_cust = ("Find Customer", self.find_cust)
        exit_prgrm = ("Exit Program", self.quit_prgrm)
        super().__init__("Main", [new_cust, find_cust, exit_prgrm])

    def get_cust_info(self):
        '''Gets customer informmation for new customer and adds to bank's
        customer list'''
        customer = super()._bank.new_customer()
        super()._bank.add_customer(customer)
        os.system("clear")
        Interface.curr_customer = customer
        self._customer_menu.run(Interface.curr_customer)

    def find_cust(self):
        '''Finds customer in bank customer list if they exist and calls
        customer menu with selected customer'''
        Interface.curr_customer = super()._bank.find_customer()
        if Interface.curr_customer is not None:
            self._customer_menu.run(Interface.curr_customer)


class CustomerMenu(Interface):
    '''Class for Customer Menu'''
    def __init__(self):
        select_acct = ("Select Account", self.account_select)
        create_acct = ("Create Account", self.account_create)
        back = ("Back to Main Menu", self.back)
        exit_prgrm = ("Exit Program", self.quit_prgrm)
        super().__init__("Customer", [select_acct,
                                      create_acct,
                                      back,
                                      exit_prgrm])
        self._acct_menu = AcctMenu()

    def account_select(self):
        '''Select account from current customer's account list'''
        Interface._curr_acct = super()._bank.select_account(
            super().curr_customer)
        if Interface._curr_acct is not None:
            print(f"Curr: {Interface._curr_acct}")
            self._acct_menu.run(Interface._curr_acct)

    def account_create(self):
        '''Create a new account for current customer'''
        Interface._curr_acct = super()._bank.new_account(super().curr_customer)
        self._acct_menu.run(Interface._curr_acct)


class AcctMenu(Interface):
    '''Class for Account Menu'''
    def __init__(self):
        deposit = ("Deposit", self.acct_depost)
        withdraw = ("Withdraw", self.acct_withdraw)
        buy = ("Buy Stock", self.stock_buy)
        sell = ("Sell Stock", self.stock_sell)
        back = ("Back to Customer Menu", self.back)
        exit_prgrm = ("Exit Program", self.quit_prgrm)
        super().__init__("Account", [deposit,
                                     withdraw,
                                     buy,
                                     sell,
                                     back,
                                     exit_prgrm])

    def acct_depost(self):
        '''Deposit funds'''
        super()._curr_acct.deposit()

    def acct_withdraw(self):
        '''Withdraw funds'''
        super()._curr_acct.withdraw()

    def stock_buy(self):
        '''Purchase stocks'''
        super()._bank.buy_stock(super()._curr_acct)

    def stock_sell(self):
        '''Sell stocks'''
        super()._bank.sell_stock(super()._curr_acct)
