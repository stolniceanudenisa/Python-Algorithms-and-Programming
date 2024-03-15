"""
    Command validation
"""
def valid_day(d):
    # checks if parameter 'd' (str or int) is a valid_day in a month
    if type(d) == str and not d.isdigit():
        return False
    d = int(d)
    if d < 1 or d > 31:
        return False
    return True

def valid_add(command):
    if len(command) >= 4 and command[1].isdigit() and command[2] in ('in','out'):
        return 1
    return 0

def valid_insert(command):
    if len(command) >= 5 and valid_day(command[1]) and command[2].isdigit() and command[3] in ('in', 'out'):
        return 2
    return 0

def valid_remove(command):
    n = len(command)
    if n == 2:
        if valid_day(command[1]):
            return 3
        if command[1] in ('in','out'):
            return 5
    if n==4 and command[2] == 'to' and valid_day(command[1]) and valid_day(command[3]):
        return 4
    return 0

def valid_replace(command):
    if len(command) == 6 and valid_day(command[1]) and command[2] in ('in', 'out') and command[4] == 'with' and command[5].isdigit():
        return 6
    return 0

def valid_list(command):
    n = len(command)
    if n == 1: return 7
    if n == 2 and command[1] in ('in','out'):
        return 8
    if n == 3:
        if command[1] in ('<', '=', '>') and command[2].isdigit():
            return 9
        if command[1] == 'balance' and valid_day(command[2]):
            return 10
    return 0

def valid_sum(command):
    if len(command) == 2 and command[1] in ('in','out'):
        return 11
    return 0

def valid_max(command):
    if len(command) == 3 and command[1] in ('in','out') and valid_day(command[2]):
        return 12
    return 0

def valid_filter(command):
    if len(command) == 2 and command[1] in ('in','out'):
        return 13
    if len(command) == 3 and command[1] in ('in','out') and command[2].isdigit():
        return 14
    return 0

def valid(command):
    """
    Function that checks if the input command is valid.
    :param command: command - list of strings that represent every element from the command
    :return: the number of the command if it's valid
    raise ValueError if the given command isn't valid
    """
    cmds =  {'add': valid_add,
            'insert': valid_insert,
            'remove': valid_remove,
            'replace': valid_replace,
            'list': valid_list,
            'sum': valid_sum,
            'max': valid_max,
            'filter': valid_filter}
    if not len(command):
        raise ValueError("Command has no elements.")
    if command[0] in cmds:
        cmd = cmds[command[0]](command)
        if not cmd:
            raise ValueError("Incorrect command! Try again")
        return cmd
    else: raise ValueError("Command doesn't exist!")