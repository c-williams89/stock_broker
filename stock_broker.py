#!usr/bin/env python3

from interface import MainMenu
from bank import Bank

if __name__ == "__main__":
    main_menu = MainMenu()
    bank = Bank()
    main_menu.run(None)