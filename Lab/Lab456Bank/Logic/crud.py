'''
1. Adăugare de noi tranzacții
• adaugă tranzacție (se dă ziua, suma, tipul)
• actualizare tranzacție (se dă ziua, suma, tipul)

2. Ștergere.
• Șterge toate tranzacțiile de la ziua specificată
• Șterge tranzacțiile dintr-o perioadă dată (se dă ziua de început și sfârșit)
• Șterge toate tranzacțiile de un anumit tip

3. Căutări.
• Tipărește tranzacțiile cu sume mai mari decât o sumă dată
• Tipărește toate tranzacțiile efectuate înainte de o zi și mai mari decât o
sumă (se dă suma și ziua)
• Tipărește tranzacțiile de un anumit tip
'''

from Domain.tranzactie import creeaza_tranzactie, get_ziua, get_tip


def create(lst_tranzactii, ziua_tranzactie: int, suma_tranzactie: float, tip_tranzactie,
           undo_list: list, redo_list: list):
    '''

    :param lst_tranzactii: lista de tranzactii
    :param ziua_tranzactie: ziua in care a fost efectuata tranzactia
    :param suma_tranzactie: suma introdusa
    :param tip_tranzactie: tipul tranzactiei
    :param undo_list:
    :param redo_list:
    :return: crearea unei tranzactii cu parametrii de mai sus
    '''

    tranzactie = creeaza_tranzactie(ziua_tranzactie, suma_tranzactie, tip_tranzactie)

    undo_list.append(lst_tranzactii)
    redo_list.clear()

    return lst_tranzactii + [tranzactie]


def read(lst_tranzactii, ziua_tranzactie: int = None):
    '''
    Citeste o tranzactie din 'baza de date'.
    :param lst_tranzactii: lista de tranzactii.
    :param ziua_tranzactie: ziua in care a fost efectuata tranzactia
    :return: - tranzactia facuta in ziua ziua_tranzactie, daca exista.
            - lista cu toate tranzactiile, daca ziua_tranzactie = None.
            - None, daca nu exista tranzactie facuta in ziua_tranzactie.
    '''
    if not ziua_tranzactie:
        return lst_tranzactii

    tranzactie_cu_ziua = None
    for tranzactie in lst_tranzactii:
        if get_ziua(tranzactie) == ziua_tranzactie:
            tranzactie_cu_ziua = tranzactie

    if tranzactie_cu_ziua:
        return tranzactie_cu_ziua
    return None


def update(lst_tranzactii, new_tranzactie, undo_list, redo_list):
    '''
    Actualizeaza o tranzactie.
    :param lst_tranzactii: lista de tranzactii.
    :param new_tranzactie: tranzactia care se va actualiza.
    #:param undo_list:
    #:param redo_list:
    :param undo_list:
    :param redo_list:
    :return: o lista actualizata cu tranzactii.
    '''
    new_tranzactii = []

    for tranzactie in lst_tranzactii:
        if get_ziua(tranzactie) != get_ziua(new_tranzactie):
            new_tranzactii.append(tranzactie)
        else:
            new_tranzactii.append(new_tranzactie)

    undo_list.append(lst_tranzactii)
    redo_list.clear()

    return new_tranzactii




def delete_from_a_day(lst_tranzactii, ziua_tranzactie, undo_list, redo_list):
    '''
    Șterge toate tranzacțiile de la ziua specificată.
    :param lst_tranzactii: lista de tranzactii.
    :param ziua_tranzactie: ziua din care se sterg toate tranzactiile.
    :param undo_list:
    :param redo_list:
    :return: o lista de tranzactii din care s-au sters diverse tranzactii efectuate intr-o anumita zi.
    '''

    if read(lst_tranzactii, ziua_tranzactie) is None:
        raise ValueError(f'Nu exista o tranzactie facuta in ziua {ziua_tranzactie} pe care sa o stergem.')

    new_tranzactii = []
    for tranzactie in lst_tranzactii:
        if get_ziua(tranzactie) != ziua_tranzactie:
            new_tranzactii.append(tranzactie)

    undo_list.append(lst_tranzactii)
    redo_list.clear()

    return new_tranzactii


def delete_between_a_period(lst_tranzactii, ziua_tranzactie_inceput, ziua_tranzactie_sfarsit, undo_list, redo_list):
    '''
    Șterge tranzacțiile dintr-o perioadă dată (se dă ziua de început și sfârșit)
    :param lst_tranzactii: lista de tranzactii.
    :param ziua_tranzactie_inceput:
    :param ziua_tranzactie_sfarsit:
    :return:
    '''
    new_tranzactii = []
    for tranzactie in lst_tranzactii:
        if get_ziua(tranzactie) < ziua_tranzactie_inceput or get_ziua(tranzactie) > ziua_tranzactie_sfarsit:
            new_tranzactii.append(tranzactie)
        else:
            pass

    undo_list.append(lst_tranzactii)
    redo_list.clear()

    return new_tranzactii


def delete_tranzactions_by_type(lst_tranzactii, tip_tranzactie, undo_list, redo_list):
    '''
    Șterge toate tranzacțiile de un anumit tip
    :param lst_tranzactii: lista de tranzactie
    :param tip_tranzactie: intrare / iesire
    :return:  lista cu tranzactiile de un anumit tip sterse
    '''
    new_tranzactii = []
    for tranzactie in lst_tranzactii:
        if get_tip(tranzactie) != tip_tranzactie:
            new_tranzactii.append(tranzactie)

    undo_list.append(lst_tranzactii)
    redo_list.clear()

    return new_tranzactii
