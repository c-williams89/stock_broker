#!usr/bin/env python3

from interface import MainMenu

if __name__ == "__main__":
    main_menu = MainMenu()
    try:
        main_menu.run(None)
    except KeyboardInterrupt:
        exit()
