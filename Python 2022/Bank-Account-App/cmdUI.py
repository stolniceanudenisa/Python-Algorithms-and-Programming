from functions import *
from validation import valid
from datetime import date
import copy

def info():
    print("""   
NB! # <value> is amount of money (positive integer)
    # <type> can be either 'in' (into the account), or 'out' (from the account)
    # use '_' as space in 'replace' if description is more than one word
Therefore, the commands for transactions are:

1)  add <value> <type> <description>                - adds to the current day a <type> transaction of <value> with <description>
2)  insert <day> <value> <type> <description>       - insert to <valid_day> a <type> transaction of <value> with <description>
3)  remove <day>                                    - remove all transactions from <day>
4)  remove <start day> to <end day>                 - removes all transactions between <start day> and <end day>
5)  remove <type>                                   - remove all the <type> transactions from the current month
6)  replace <day> <type> <description> with <value> - replace the amount for the <type> transaction having the <description> from <day> with <value>
7)  list                                            – write the entire list of transactions
8)  list <type>                                     – write all the <type> transactions
9)  list [<,=,>] <value>                            - write all transactions having an amount of money <,=,> <value>
10) list balance <day>                              - computes the account’s balance on <valid_day>
11) sum <type>                                      - write the total amount from <type> transactions
12) max <type> <day>                                - write the maximum <type> transaction on <valid_day>
13) filter <type>                                   - keep only <type> transactions
14) filter <type> <value>                           - keep only <type> transactions having an amount of money smaller than <value>
15) undo                                            - the last operation that has modified program data will be reversed
16) exit                                            - to close the application
17) info                                            - show this information again.\n""")

def cmd1_add(command,trList):
    """
    Function that adds a transaction given by the command to the 'transactions' list.
    :param command: list of strings that represent every element from the add/insert command
    :param trList: - list - contains all the transactions up to this point
    :return: nothing. A new transaction will be added at the end of the transaction list
    """
    # add <value> <type> <description>
    t_day = date.today().day
    t_value = int(command[1])
    t_type = command[2]
    t_des = "_".join(command[3:])
    append_transaction(t_day, t_type, t_value, t_des, trList)

def cmd2_insert(command,trList):
    # insert <day> <value> <type> <description>
    t_day = int(command[1])
    t_value = int(command[2])
    t_type = command[3]
    t_des = "_".join(command[4:])
    append_transaction(t_day, t_type, t_value, t_des, trList)

def cmd3_remove(command,trList):
    """
    :param command: list that contains the elements of remove command in str format
    :param trList: list that contains all the transactions up to this point
    """
    # remove <day>
    remove_day(int(command[1]), trList)

def cmd4_remove(command,trList):
    # remove <start day> to <end day>
    day1 = int(command[1])
    day2 = int(command[3])
    remove_between_days(day1, day2, trList)

def cmd5_remove(command,trList):
    # remove <type>
    remove_type(command[1], trList)

def cmd6_replace(command,trList):
    # replace <day> <type> <description> with <value>
    replace_value(int(command[1]), command[2], command[3], int(command[5]), trList)

def cmd7_list(command,trList):
    """
    :param command: list - contains the elements of the command in str format
    :param trList: list - contains all the transactions up to this point
    :output: prints the transactions selected with the 'list' command
    """
    if command[0] != 'list': raise ValueError("Wrong command!")
    # list
    list_all(trList)

def cmd8_list(command,trList):
    # list <type>
    list_type(command[1], trList)

def cmd9_list(command,trList):
    # list [<,=,>] <value>
    list_compared_to_value(command[1], command[2], trList)

def cmd10_list(command,trList):
    # list balance <day>
    list_balance_day(int(command[2]), trList)

def cmd11_sum(command,trList):
    # sum <type>
    print_sum_of_type(command[1], trList)

def cmd12_max(command,trList):
    # max <type> <day>
    print_max_specific_transaction(command[1], int(command[2]), trList)

def cmd13_filter(command,trList):
    # filter <type>
    filter_type(command[1], trList)

def cmd14_filter(command,trList):
    # filter <type> <value>
    filter_type_value(command[1], int(command[2]), trList)

def account_console():
    """
    The main function that runs the account console.
    """
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
                    {'d': 22, 't': 'out', 'v': 100, 'des': 'surprise_motherF'}]
    numbered_commands = {1: cmd1_add, # add <value> <type> <description>
                         2: cmd2_insert, # insert <day> <value> <type> <description>
                         3: cmd3_remove, # remove <day>
                         4: cmd4_remove, # remove <start day> to <end day>
                         5: cmd5_remove, # remove <type>
                         6: cmd6_replace, # replace <day> <type> <description> with <value>
                         7: cmd7_list, # list
                         8: cmd8_list, # list <type>
                         9: cmd9_list, # list [<,=,>] <value>
                         10: cmd10_list, # list balance <day>
                         11: cmd11_sum, # sum <type>
                         12: cmd12_max, # max <type> <day>
                         13: cmd13_filter, # filter <type>
                         14: cmd14_filter # filter <type> <value>
                         }
    TrnStack = [[]]
    print("\n------------------- COMMAND BASED USER INTERFACE -------------------")
    print("Type 'info' to learn more about this console.")
    while True:
        cmd = input("SCM\Bank Transaction>")
        try:
            if cmd == 'exit':
                exit()
            elif cmd == 'undo':
                undo(TrnStack, transactions)
            elif cmd == 'info':
                info()
            else:
                command = cmd.split()
                # if the command is correct, validation returns its unique number; otherwise valid sends an exception
                valid_cmd_nr = valid(command)
                # if the transactions are about to be modified, append a copy of them to the stack
                if command[0] in ('add','insert','remove','replace','filter'):
                    TrnStack.append(copy.deepcopy(transactions))
                # call the function for the written command by using the command number specified by the validation
                numbered_commands[valid_cmd_nr](command,transactions)
        except Exception as ex:
            print(ex)