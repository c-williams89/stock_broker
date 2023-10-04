#!usr/bin/env python3

class Interface:
    def __init__(self, menu_type, command_list):
        self._menu_type = menu_type
        self._command_dict = dict(enumerate(command_list, 1))

    def help(self):
        pass
        
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
        self.create_main_menu()

    def create_main_menu(self):
        '''Docstring'''
        new_cust = ("Create New Customer", None)
        find_cust = ("Find Customer", None)
        super().__init__("Main Menu", [new_cust, find_cust])

class CustDetailsMenu(Interface):
    '''Docstring'''
