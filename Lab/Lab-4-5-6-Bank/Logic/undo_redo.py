def do_undo(undo_list: list, redo_list: list, current_list: list):
    '''
    Creeaza o lista de undo ce retine lista inainte sa fie modificata
    :param undo_list: Lista de undo
    :param redo_list: Lista de redo
    :param current_list: Lista curenta
    :return: lista de undo, daca s-a modificat ceva in lista, altfel retunreaza None
    '''

    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()

    return None


def do_redo(undo_list: list, redo_list: list, current_list: list):
    '''
    Creeaza o lista de redo care anuleaza un undo
    :param undo_list: Lista de undo
    :param redo_list: Lista de redo
    :param current_list: Lista curenta
    :return: lista care este echivalenta cu lista de undo, care a modificat lista initiala, altfel retunreaza None
    '''

    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo

    return None
