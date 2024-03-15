
# getters & setters

def get_day(transaction):
    return transaction['d']

def get_type(transaction):
    return transaction['t']

def get_value(transaction):
    return transaction['v']

def get_description(transaction):
    return transaction['des']

def set_day(transaction, new_day):
    transaction['d'] = new_day

def set_type(transaction, new_type):
    transaction['t'] = new_type

def set_value(transaction, new_value):
    transaction['v'] = new_value

def set_description(transaction, new_descr):
    transaction['des'] = new_descr


'''
    Functions used by the commands / menu options
'''

def create_transaction(t_day,t_type,t_value,t_des):
    # Function that creates a transaction as a dictionary
    return {'d': t_day, 't': t_type, 'v': t_value, 'des': t_des}

def append_transaction(t_day,t_type,t_value,t_des,trList):
    # Function that adds the new transaction at the end of the transaction list
    trList.append(create_transaction(t_day,t_type,t_value,t_des))

def type_sum(t_type,t_day,trList):
    """
    Function that computes the sum of the values of the transactions
    with a certain type that happened on or before a given day
    :param t_type: str - 'in' or 'out' - the type we are searching for
    :param t_day: int - the day that acts as a upper limit
    :param trList: list - contains all the transactions up to this point
    :return: t_sum (int) if we could find transactions that meet the conditions, -1 otherwise
    """
    t_sum = 0
    ok = 0
    for tr in trList:
        if get_day(tr) <= t_day and get_type(tr) == t_type:
            t_sum += get_value(tr) ; ok=1
    if ok:
        return t_sum
    return -1

def compute_balance(trList, t_day):
    """
    Function that computes the account balance in a specific valid_day.
    :param trList: list - contains all the transactions up to this point
    :param t_day: int - the valid_day for which we calculate the balance
    :return: sum_in - sum_out (int) - the balance in the 't_day'
    """
    sum_in = type_sum('in',t_day,trList)
    if sum_in == -1: sum_in = 0
    sum_out = type_sum('out',t_day,trList)
    if sum_out == -1: sum_out = 0
    return sum_in - sum_out

def compute_max_transaction(s_type,s_day,trList):
    """
    Function that computes the maximum value of the transaction with a given day and type
    :param s_type: str - 'in' or 'out'
    :param s_day: int - the day that the transaction must have
    :param trList: list - contains all the transactions up to this point
    :return: maxi - int - the maximum value/amount of money
    """
    maxi = -1
    for tr in trList:
        if get_type(tr) == s_type and get_day(tr) == s_day and get_value(tr) > maxi:
            maxi = get_value(tr)
    return maxi

def remove_day(s_day,trList):
    """
    Function that removes the transactions from a given day from the list
    :param s_day: int - the day we are looking for
    :param trList: list - contains all the transactions up to this point
    :return: nothing; trList will be updated
    """
    n = len(trList)
    i = 0
    deleted = 0
    while i < n:
        if get_day(trList[i]) == s_day:
            deleted += 1
        else:
            trList[i-deleted] = trList[i]
        i += 1
    del trList[n-deleted : n]

def remove_type(s_type,trList):
    """
    Function that removes the transactions with a given type from the list
    :param s_type: str - the type we are looking for
    :param trList: list - contains all the transactions up to this point
    :return: nothing; trList will be updated
    """
    n = len(trList)
    i = 0
    deleted = 0
    while i < n:
        if get_type(trList[i]) == s_type:
            deleted += 1
        else:
            trList[i - deleted] = trList[i]
        i += 1
    del trList[n - deleted: n]

def remove_between_days(day1,day2,trList):
    """
    Function that removes from the list the transactions that occurred between 2 given days
    :param day1: int - the first day
    :param day2: int - the second day
    :param trList: list - contains all the transactions up to this point
    :return: nothing; trList will be updated
    """
    n = len(trList)
    i = 0
    deleted = 0
    while i < n:
        if day1 <= get_day(trList[i]) <= day2:
            deleted += 1
        else:
            trList[i - deleted] = trList[i]
        i += 1
    del trList[n - deleted: n]

def remove_bigger_value(value, trList):
    """
    Function that removes the transactions with a value bigger or equal to a given value
    :param value: int - the given value used for comparision
    :param trList: list - contains all the transactions up to this point
    :return: nothing; trList will be updated
    """
    n = len(trList)
    i = 0
    deleted = 0
    while i < n:
        if get_value(trList[i]) >= value:
            deleted += 1
        else:
            trList[i - deleted] = trList[i]
        i += 1
    del trList[n - deleted: n]

def replace_value(s_day,s_type,s_description,newValue,trList):
    """
    Function that modifies the value of a specified transaction
    :param s_day: int - the day we are looking for
    :param s_type: str - the type we are looking for
    :param s_description: str - the description we are looking for
    :param newValue: int - the new value to set
    :param trList: list - contains all the transactions up to this point
    :return: nothing; the transaction will be updated
    :raise Exception: if the given transaction was not found
    """
    ok = 0
    for tr in trList:
        if get_description(tr) == s_description and get_type(tr) == s_type and get_day(tr) == s_day:
            ok = 1
            set_value(tr, newValue)
    if not ok:
        raise Exception("The transaction you want to modify doesn't exist.")

def filter_type(t_type, trList):
    """
    Function that removes the transactions that have a different type from the given one
    :param t_type: str - the given type to filter
    :param trList: list - contains all the transactions up to this point
    :return: nothing; trList will be updated
    """
    s_type = 'out'
    if t_type == 'out':
        s_type = 'in'
    remove_type(s_type, trList)

def filter_type_value(t_type, t_value, trList):
    """
    Function that removes the transactions that have a different type from the given one
    and the value bigger or equal to the given one
    :param t_type: str - the given type to filter
    :param t_value: int - the maximum allowed value
    :param trList: list - contains all the transactions up to this point
    :return: nothing; trList will be updated
    """
    s_type = 'out'
    if t_type == 'out':
        s_type = 'in'
    remove_type(s_type, trList)
    remove_bigger_value(t_value, trList)

#THE UNDO
def undo(TrnStack, trList):
    """
    Function that can undo the add, insert, remove, replace, filter commands
    :param TrnStack: list - has a copy of the transactions list at every modification
    :param trList: the list of transactions
    :return: nothing. The trList will be reversed to its previous state.
    """
    # The transaction list is cleared
    trList.clear()
    n = len(TrnStack)
    if not n:
        raise Exception("You have reached the beginning. You cannot undo anymore.")
    # The transaction list is reversed by assigning the transactions of the last list saved in the stack
    for tr in TrnStack[n-1]:
        trList.append(tr)
    # After the transaction is reversed to its previous state, the last list from the stack is removed
    TrnStack.pop()

################################ OUTPUT FUNCTIONS FOR BOTH UIs ###################################

def list_all(trList):
    # lists all transactions
    if not len(trList):
        raise Exception("There are no transactions.")
    print("The transactions from this month are: ")
    i = 0
    for tr in trList:
        i+=1
        print("{}) Day: {}, type: {}, value: {}, description: {}.".format(i, tr['d'], tr['t'], tr['v'], tr['des']))

def list_type(s_type, trList):
    # lists 'in' or 'out' transactions
    if not len(trList):
        raise Exception("There are no transactions.")
    print("The '{}' transactions from this month are: ".format(s_type))
    i = 0
    for tr in trList:
        if tr['t'] == s_type:
            i+=1
            print("{}) Day: {}, value: {}, description: {}.".format(i,tr['d'], tr['v'], tr['des']))
    if not i:
        raise Exception("None.")

def list_balance_day(s_day, trList):
    # prints the balance on a day
    if not len(trList):
        raise Exception("There are no transactions.")
    print("The account balance is {} RON on day {}.".format(compute_balance(trList, s_day), s_day))

def list_compared_to_value(operator,value,trList):
    # lists transactions compared to a value
    if not len(trList):
        raise Exception("There are no transactions.")
    if operator == '=': operator += '='
    i = 0
    for tr in trList:
        if eval('{}{}{}'.format(tr['v'], operator, value)):
            i+=1
            print("{}) Day: {}, type: {}, value: {}, description: {}.".format(i,tr['d'], tr['t'], tr['v'], tr['des']))
    if not i:
        raise Exception("None.")

def print_sum_of_type(s_type, trList):
    # prints the total amount from 'in' or 'out' transactions
    t_sum = type_sum(s_type, 31, trList)
    if t_sum == -1:
        raise Exception("There are no transactions of this type.")
    print("The total amount from {} transactions is {} RON.".format(s_type, t_sum))

def print_max_specific_transaction(s_type,s_day,trList):
    # prints the maximum 'in' or 'out' transaction on a day
    maxi = compute_max_transaction(s_type, s_day, trList)
    if maxi == -1:
        raise Exception("There are no transactions of this type in this day.")
    print("The maximum '{}' transaction on day {} is {} RON.".format(s_type, s_day, maxi))