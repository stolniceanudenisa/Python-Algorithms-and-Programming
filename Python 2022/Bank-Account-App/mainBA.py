from datetime import date
from cmdUI import account_console
from menuUI import account_menu
from tests import *

# THE MAIN
def run_bank_account_app():
    today = date.today()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("W E L C O M E   T O   T H E   M O N T H L Y   B A N K   A C C O U N T   M A N A G E R !")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Current year & month are: {}/{}.\nCurrent day is {}.".format(
        today.year, today.month, today.day))
    UI = input("Choose your USER INTERFACE! Insert:\n1 for menu-based | 2 for command-based -> ")
    while True:
        try:
            UI = int(UI)
            if UI!=1 and UI!=2:
                raise ValueError()
            break
        except ValueError:
            print("There is no other UI.")
            UI = input("Press 1 or 2: ")
    if UI == 1:
        account_menu()
    else:
        account_console()

'''
    Program entry point
'''
run_all_tests()
run_bank_account_app()