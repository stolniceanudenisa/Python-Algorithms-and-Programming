from functions import *
from validation import valid_day
from datetime import date
import copy

def menu_info():
    print("\n---------------------- MENU BASED USER INTERFACE -------------------------")
    print("""NB! # <value> is amount of money (positive integer)
    # <type> can be either 'in' (into the account), or 'out' (from the account)
    # press 'i' to see this information again\n""")

def print_menu():
    print("""Press:
    1  to add a transaction for today              
    2  to add a transaction for another day
    3  to remove all transactions from a day
    4  to remove all transactions between two days
    5  to remove all 'in' or 'out' transactions
    6  to modify the value of a transaction 
    7  to list all transactions                                           
    8  to list 'in' or 'out' transactions                           
    9  to list transactions compared to a value
    10 to see the balance on a day
    11 to see the total amount from 'in' or 'out' transactions
    12 to see the maximum 'in' or 'out' transaction on a day
    13 to filter 'in' or 'out' transactions
    14 to filter 'in' or 'out' transactions having an amount of money smaller than a value 
    u  to undo
    x  to exit / close the application\n""")

def read_value(s): #checks if the input is an integer
    x = input(s)
    while True:
        try:
            x = int(x)
            if x < 0:
                raise ValueError
            return x
        except ValueError:
            print("invalid value!")
            x = input(s)

def read_day(s):
    x = input(s)
    while True:
        try:
            if not valid_day(x):
                raise ValueError("This day doesn't exist!")
            return int(x)
        except Exception as ex:
            print(ex)
            x = input(s)

def read_type():
    x = input("Insert type (in or out): ")
    while True:
        try:
            if x not in ('in','out'):
                raise ValueError("Incorrect type!")
            return x
        except Exception as ex:
            print(ex)
            x = input("Insert type (in or out): ")

def read_operator():
    x = input("Insert operator (<,=,>): ")
    while True:
        try:
            if x not in ('<','=','>'):
                raise ValueError("Incorrect operator!")
            return x
        except Exception as ex:
            print(ex)
            x = input("Insert operator (<,=,>): ")

def option1(trList):
    t_type = read_type()
    t_value = read_value("Insert transaction value: ")
    t_description = '_'.join(input("Insert description: ").split())
    append_transaction(date.today().day,t_type,t_value,t_description,trList)

def option2(trList):
    t_day = read_day("Insert day: ")
    t_type = read_type()
    t_value = read_value("Insert transaction value: ")
    t_description = '_'.join(input("Insert description: ").split())
    append_transaction(t_day, t_type, t_value, t_description, trList)

def option3(trList):
    t_day = read_day("Insert day: ")
    remove_day(t_day,trList)

def option4(trList):
    t_day1 = read_day("Insert the first day: ")
    t_day2 = read_day("Insert the second day: ")
    remove_between_days(t_day1,t_day2,trList)

def option5(trList):
    t_type = read_type()
    remove_type(t_type,trList)

def option6(trList):
    t_day = read_day("Insert the day of the transaction you want to modify: ")
    t_type = read_type()
    t_description = input("Insert the description of the transaction you want to modify\n(use '_' as space if it has more than one word): ")
    t_value = read_value("Insert the new value: ")
    replace_value(t_day,t_type,t_description,t_value,trList)

def option7(trList):
    list_all(trList)

def option8(trList):
    t_type = read_type()
    list_type(t_type,trList)

def option9(trList):
    t_operator = read_operator()
    t_value = read_value("Insert the value for comparision: ")
    list_compared_to_value(t_operator,t_value,trList)

def option10(trList):
    t_day = read_day("Insert day: ")
    list_balance_day(t_day,trList)

def option11(trList):
    t_type = read_type()
    print_sum_of_type(t_type,trList)

def option12(trList):
    t_type = read_type()
    t_day = read_day("Insert the day for which to show the maximum: ")
    print_max_specific_transaction(t_type,t_day,trList)

def option13(trList):
    t_type = read_type()
    filter_type(t_type,trList)

def option14(trList):
    t_type = read_type()
    t_value = read_value("Insert the maximum value: ")
    filter_type_value(t_type,t_value,trList)

def account_menu():
    # the transactions repository:
    transactions = [{'d': 1, 't': 'in', 'v': 420, 'des': 'initial_money'},
                    {'d': 2, 't': 'out', 'v': 90, 'des': 'grocery'},
                    {'d': 3, 't': 'in', 'v': 80, 'des': 'sp_service'},
                    {'d': 10, 't': 'out', 'v': 100, 'des': 'cash'},
                    {'d': 11, 't': 'in', 'v': 200, 'des': 'weed'},
                    {'d': 13, 't': 'out', 'v': 22, 'des': 'ice_cream'},
                    {'d': 13, 't': 'in', 'v': 33, 'des': 'luck'},
                    {'d': 15, 't': 'in', 'v': 420, 'des': 'weed2'},
                    {'d': 22, 't': 'in', 'v': 222, 'des': 'birthday'},
                    {'d': 22, 't': 'out', 'v': 100, 'des': 'surprise_MDFK'}]
    TrnStack = [[]]
    menu_info()
    options = {1: option1,
               2: option2,
               3: option3,
               4: option4,
               5: option5,
               6: option6,
               7: option7,
               8: option8,
               9: option9,
               10: option10,
               11: option11,
               12: option12,
               13: option13,
               14: option14}
    print_menu()
    while True:
        option = input("Insert your option | Press 'm' to see the menu -> ")
        try:
            if option == 'x':
                exit()
            elif option == 'u':
                undo(TrnStack, transactions)
            elif option == 'm':
                print_menu()
            elif option == 'i':
                menu_info()
            else:
                if option.isdigit() and 0 < int(option) < 15:
                    option = int(option)
                else:
                    raise ValueError("Please choose an existing option. Press 'm' to see the options.")
                # if the transactions are about to be modified, append a copy of them to the stack
                if option in (1,2,3,4,5,6,13,14):
                    TrnStack.append(copy.deepcopy(transactions))
                # call the function of the chosen option
                options[option](transactions)
        except Exception as ex:
            print(ex)