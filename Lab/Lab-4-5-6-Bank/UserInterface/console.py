from Domain.tranzactie import get_str, get_suma, get_tip, creeaza_tranzactie
from Logic.crud import read, update, delete_from_a_day, delete_between_a_period, delete_tranzactions_by_type, create
from Logic.elim_tranz_mai_mici_decat_suma import elim_tranz_mai_mici_decat_suma
from Logic.elimina_tranz_anumit_tip import elimina_tranz_anumit_tip
from Logic.sold_cont_la_o_data import sold_cont_la_o_data
from Logic.suma_totala_tranzactii_anumit_tip import suma_totala_tranzactii_anumit_tip
from Logic.tipareste_tranz_tip_ordonat_dupa_suma import tipareste_tranz_tip_ordonat_dupa_suma
from Logic.tipareste_tranzactii_de_un_anumit_tip import tipareste_tranzactii_de_un_anumit_tip
from Logic.tipareste_tranzactii_inainte_de_o_zi_mai_mari_decat_s import tranzactii_inainte_de_o_zi_mai_mari_decat_s
from Logic.tipareste_tranzactii_mai_mari_decat_o_suma_data import tranzactii_mai_mari_decat_o_suma_data
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print('1. Adaugari.')
    print('2. Stergeri.')
    print('3. Cautari.')
    print('4. Rapoarte.')
    print('5. Filtrare.')
    print('u. Undo.')
    print('r. Redo.')
    print('x. Exit ')


###############################################################################

def handle_show_all(tranzactii):
    '''
    Afiseaza toate tranzactiile efectuate.
    :param tranzactii: lista de tranzactii.
    :return: toate tranzactiile efectuate.
    '''
    for tranzactie in tranzactii:
        print(get_str(tranzactie))


def handle_show_details(tranzactii):
    '''
    Arata detaliile pentru o anumita tranzactie.
    :param tranzactii: lista de tranzactii.
    :return: detaliile unei tranzactii.
    '''
    ziua_tranzactie = int(input('Dati ziua in care a fost efectuata o tranzactie pentru care doriti detalii: '))
    tranzactie = read(tranzactii, ziua_tranzactie)
    print(f'Suma: {get_suma(tranzactie)}')
    print(f'Tipul tranzactiei: {get_tip(tranzactie)}')


###############################################################################


def handle_add(tranzactii, undo_list, redo_list):
    '''
    Interfata pentru adaugarea unei tranzactii.
    :param tranzactii: lista de tranzactii.
    :return: adaugarea in lista a unei tranzactii.
    '''
    try:
        ziua_tranzactie = int(input('Dati ziua efectuarii tranzactiei: '))
        if (ziua_tranzactie <= 0 or ziua_tranzactie > 31):
            raise ValueError(f"Reintroduceti ziua efectuarii tranzactiei.")
        suma_tranzactie = float(input('Dati suma tranzactiei: '))
        tip_tranzactie = input('Dati tipul tranzactiei: ')

        print('Adaugarea a fost efectuata cu succes.')
        return create(tranzactii, ziua_tranzactie, suma_tranzactie, tip_tranzactie,
                      undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)
    return tranzactii


def handle_update(tranzactii, undo_list, redo_list):
    '''
    Interfata pentru modificarea unei tranzactii.
    :param tranzactii: lista de tranzactii.
    :return: modificarea unei tranzactii din lista.
    '''
    try:
        ziua_tranzactie = int(input('Dati ziua efectuarii tranzactiei care se actualizeaza: '))
        suma_tranzactie = float(input('Dati noua suma a tranzactiei: '))
        tip_tranzactie = input('Dati noul tip de efectuare al tranzactiei: ')
        # return update(tranzactii, creeaza_tranzactie(ziua_tranzactie, suma_tranzactie, tip_tranzactie))
        new_tranzactie = creeaza_tranzactie(ziua_tranzactie, suma_tranzactie, tip_tranzactie)
        print('Modificarea a fost efectuata cu succes.')
        return update(tranzactii, new_tranzactie, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)

    return tranzactii


####################################################################################
# Stergeri

def handle_delete(tranzactii, undo_list, redo_list):
    '''
    Stergerea unei tranzactii din lista dupa ziua efectuarii tranzactiei.
    :param tranzactii: lista de tranzactii.
    :return: lista fara tranzactia stearsa.
    '''
    try:
        ziua_tranzactie = int(input('Dati ziua efectuarii tranzactiei care se va sterge: '))

        # tranzactii = delete_from_a_day(tranzactii, ziua_tranzactie)
        print('Stergerea a fost efectuata cu succes.')
        return delete_from_a_day(tranzactii, ziua_tranzactie, undo_list, redo_list)

    except ValueError as ve:
        print('Eroare:', ve)
    return tranzactii


def handle_delete_between_a_period(tranzactii, undo_list, redo_list):
    '''
    Șterge tranzacțiile dintr-o perioadă dată (se dă ziua de început și sfârșit).
    :param tranzactii: lista de tranzactii.
    :return: lista modificata cu tranzacțiile dintr-o perioadă dată sterse.
    '''
    try:
        ziua_tranzactie_inceput = int(input('Dati ziua de inceput a efectuarii tranzactiei: '))
        ziua_tranzactie_sfarsit = int(input('Dati ziua de sfarsit a efectuarii tranzactiei: '))
        tranzactii = delete_between_a_period(tranzactii, ziua_tranzactie_inceput, ziua_tranzactie_sfarsit, undo_list,
                                             redo_list)
        print('Stergerea a fost efectuata cu succes.')
        return tranzactii
    except ValueError as ve:
        print('Eroare', ve)
    return tranzactii


def handle_delete_tranzactions_by_type(tranzactii, undo_list, redo_list):
    '''
    Stergerea cheltuielilor dupa un anumit tip.
    :param tranzactii: lista de tranzactii.
    :return: lista modificata cu cheltuielilor de un anumit tip sterse.
    '''
    try:
        tip_tranzactie = str(input('Dati tipul de tranzactie: '))
        tranzactii = delete_tranzactions_by_type(tranzactii, tip_tranzactie, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes.')
        return tranzactii
        # return tranzactii
    except ValueError as ve:
        print('Eroare', ve)
    return tranzactii


####################################################################################
# Căutări

def handle_tranzactii_mai_mari_decat_o_suma_data(tranzactii):
    '''
    Tipărește tranzacțiile cu sume mai mari decât o sumă dată.
    :param tranzactii: lista de tranzactii.
    :return: tranzacțiile cu sume mai mari decât o sumă dată.
    '''
    try:
        suma_tranzactie = float(input('Dati suma pentru care cautati tranzactii mai mari: '))
        return tranzactii_mai_mari_decat_o_suma_data(tranzactii, suma_tranzactie)
    except ValueError as ve:
        print('Eroare', ve)
    return tranzactii


def handle_tranzactii_inainte_de_o_zi_mai_mari_decat_s(tranzactii):
    '''
    Tipărește toate tranzacțiile efectuate înainte de o zi și mai mari decât o sumă (se dă suma și ziua).
    :param tranzactii: lista de tranzactii.
    :return: toate tranzacțiile efectuate înainte de o zi și mai mari decât o sumă.
    '''
    try:
        ziua_tranzactie = int(input('Dati ziua pentru care se cauta tranzactia: '))
        new_tranzactii = handle_tranzactii_mai_mari_decat_o_suma_data(tranzactii)
        return tranzactii_inainte_de_o_zi_mai_mari_decat_s(new_tranzactii, ziua_tranzactie)
    except ValueError as ve:
        print('Eroare', ve)
    return tranzactii


def handle_tipareste_tranzactii_de_un_anumit_tip(tranzactii):
    '''
    Tipărește tranzacțiile de un anumit tip.
    :param tranzactii: lista de tranzactii.
    :return: lista cu tranzacțiile de un anumit tip.
    raise ValueError in caz ca tipul tranzactiei nu este 'intrare' sau 'iesire'.
    '''
    try:
        tip_tranzactie = input('Dati tipul tranzactiei: ')
        if not (tip_tranzactie == 'intrare' or tip_tranzactie == 'iesire'):
            raise ValueError('Tipul tranzactiei nu poate fi acesta. Reincercati.')
        return tipareste_tranzactii_de_un_anumit_tip(tranzactii, tip_tranzactie)
    except ValueError as ve:
        print('Eroare', ve)
    return tranzactii


###############################################################################

# Rapoarte

def handle_suma_totala_tranzactii_anumit_tip(tranzactii):
    '''
    Efectueaza suma totala a tranzactiilor de acelasi tip.
    :param tranzactii: lista de tranzactii.
    :return: suma.
    raise ValueError in caz ca tipul tranzactiei nu este 'intrare' sau 'iesire'.
    '''
    try:
        tip_tranzactie = input('Dati tipul tranzactiei: ')
        if not (tip_tranzactie == 'intrare' or tip_tranzactie == 'iesire'):
            raise ValueError('Tipul tranzactiei nu poate fi acesta. Reincercati.')
        return suma_totala_tranzactii_anumit_tip(tranzactii, tip_tranzactie)
    except ValueError as ve:
        print('Eroare', ve)


def handle_sold_cont_la_o_data(tranzactii):
    '''
    Soldul contului la o dată specificată.
    :param tranzactii: lista de tranzactii.
    :return: o lista cu tranzactii efectuate pana la o data.
    raise ValueError in caz ca ziua efectuarii tranzactiei nu este intre 1 si 31 inclusiv.
    '''
    try:
        ziua_tranzactie = int(input('Dati ziua pentru care se cauta soldul: '))
        if (ziua_tranzactie < 1 or ziua_tranzactie > 31):
            raise ValueError(
                'Ziua efectuarii tranzactiei nu poate fi aceasta. Se poate observa mai jos zilele care pot fi introduse.')
        return sold_cont_la_o_data(tranzactii, ziua_tranzactie)
    except ValueError as ve:
        print('Eroare', ve)
    return tranzactii


def handle_tipareste_tranz_tip_ordonat_dupa_suma(tranzactii):
    '''
    Tipărește toate tranzacțiile de un anumit tip ordonat după sumă.
    :param tranzactii: lista de tranzactii.
    :return: lista de tranzactii de un anumit tip, ordonata dupa suma.
    raise ValueError in caz ca tipul tranzactiei nu este 'intrare' sau 'iesire'.
    '''
    try:
        tip_tranzactie = input('Dati tipul tranzactiei: ')
        if not (tip_tranzactie == 'intrare' or tip_tranzactie == 'iesire'):
            raise ValueError(
                'Tipul tranzactiei nu poate fi acesta. Reincercati. Se poate observa mai jos care sunt tipurile disponibile.')
        return tipareste_tranz_tip_ordonat_dupa_suma(tranzactii, tip_tranzactie)
    except ValueError as ve:
        print('Eroare', ve)
    return tranzactii


###############################################################################
# Filtrare

def handle_elimina_tranz_anumit_tip(tranzactii):
    '''
    Elimină toate tranzacțiile de un anumit tip.
    :param tranzactii: lista de tranzactii.
    :return: lista de tranzactii modificata.
    raise ValueError in caz ca tipul tranzactiei nu este 'intrare' sau 'iesire'.
    '''
    try:
        tip_tranzactie = input('Dati tipul de tranzactie: ')
        if not (tip_tranzactie == 'intrare' or tip_tranzactie == 'iesire'):
            raise ValueError('Tipul tranzactiei nu poate fi acesta. Reincercati.')
        tranzactii = elimina_tranz_anumit_tip(tranzactii, tip_tranzactie)
        print('Stergerea a fost efectuata cu succes.')
        return tranzactii
    except ValueError as ve:
        print('Eroare', ve)
    return tranzactii


def handle_elim_tranz_mai_mici_decat_suma(tranzactii):
    '''
    Elimină toate tranzacțiile mai mici decât o sumă dată care au tipul specificat.
    :param tranzactii: lista de tranzactii.
    :return: lista de tranzactii modificata.
    raise ValueError in caz ca tipul tranzactiei nu este 'intrare' sau 'iesire'.
    '''
    try:
        tip_tranzactie = input('Dati tipul de tranzactie: ')
        if not (tip_tranzactie == 'intrare' or tip_tranzactie == 'iesire'):
            raise ValueError('Tipul tranzactiei nu poate fi acesta. Reincercati.')
        suma_tranzactie = float(input('Dati suma pentru care se cauta tranzactii mai mici: '))
        tranzactii = elim_tranz_mai_mici_decat_suma(tranzactii, tip_tranzactie, suma_tranzactie)
        print('Stergerea a fost efectuata cu succes.')
        return tranzactii
    except ValueError as ve:
        print('Eroare', ve)
    return tranzactii


###############################################################3


def Adaugare(tranzactii, undo_list, redo_list):
    while True:
        print('1. Adaugare tranzactie')
        print('2. Actualizare/modificare tranzactie')
        print('a. Afisare')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            tranzactii = handle_add(tranzactii, undo_list, redo_list)
        elif optiune == '2':
            tranzactii = handle_update(tranzactii, undo_list, redo_list)
        elif optiune == 'a':
            Afisarestr(tranzactii)
        elif optiune == 'b':
            return tranzactii
        else:
            print('Optiune invalida. Reincercati')


def Stergeri(tranzactii, undo_list, redo_list):
    while True:
        print('1. Șterge toate tranzacțiile de la ziua specificată.')
        print('2. Șterge tranzacțiile dintr-o perioadă dată (se dă ziua de început și sfârșit).')
        print('3. Șterge toate tranzacțiile de un anumit tip.')
        print('a. Afisare')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            tranzactii = handle_delete(tranzactii, undo_list, redo_list)
        elif optiune == '2':
            tranzactii = handle_delete_between_a_period(tranzactii, undo_list, redo_list)
        elif optiune == '3':
            tranzactii = handle_delete_tranzactions_by_type(tranzactii, undo_list, redo_list)
        elif optiune == 'a':
            Afisarestr(tranzactii)
        elif optiune == 'b':
            return tranzactii
        else:
            print('Optiune invalida. Reincercati.')


def Cautari(tranzactii):
    while True:
        print('1. Tipărește tranzacțiile cu sume mai mari decât o sumă dată.')
        print(
            '2. Tipărește toate tranzacțiile efectuate înainte de o zi și mai mari decât o sumă (se dă suma și ziua).')
        print('3. Tipărește tranzacțiile de un anumit tip.')
        print('a. Afisare')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            Afisarestr(handle_tranzactii_mai_mari_decat_o_suma_data(tranzactii))
        elif optiune == '2':
            Afisarestr(handle_tranzactii_inainte_de_o_zi_mai_mari_decat_s(tranzactii))
        elif optiune == '3':
            Afisarestr(handle_tipareste_tranzactii_de_un_anumit_tip(tranzactii))
        elif optiune == 'a':
            Afisarestr(tranzactii)
        elif optiune == 'b':
            return tranzactii
        else:
            print('Optiune invalida. Reincercati.')


def Rapoarte(tranzactii):
    while True:
        print('1. Suma totală a tranzacțiilor de un anumit tip.')
        print('2. Soldul contului la o dată specificată.')
        print('3. Tipărește toate tranzacțiile de un anumit tip, ordonat după sumă.')
        print('a. Afisare')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            print(handle_suma_totala_tranzactii_anumit_tip(tranzactii))
        elif optiune == '2':
            Afisarestr(handle_sold_cont_la_o_data(tranzactii))
        elif optiune == '3':
            Afisarestr(handle_tipareste_tranz_tip_ordonat_dupa_suma(tranzactii))
        elif optiune == 'a':
            handle_show_all(tranzactii)
        elif optiune == 'b':
            return tranzactii
        else:
            print('Optiune invalida. Reincercati')


def Filtrare(tranzactii):
    while True:
        print('1. Elimină toate tranzacțiile de un anumit tip.')
        print('2. Elimină toate tranzacțiile mai mici decât o sumă dată care au tipul specificat.')
        print('a. Afisare')
        print('b. Revenire')
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            tranzactii = handle_elimina_tranz_anumit_tip(tranzactii)
        elif optiune == '2':
            tranzactii = handle_elim_tranz_mai_mici_decat_suma(tranzactii)
        elif optiune == 'a':
            handle_show_all(tranzactii)
        elif optiune == 'b':
            return tranzactii
        else:
            print('Optiune invalida. Reincercati')


def Afisarestr(tranzactii):
    '''
    Afiseaza de tipul to_string
    :param tranzactii: lista de tranzactii
    :return:
    '''
    for tranzactie in tranzactii:
        print(get_str(tranzactie))
    return tranzactii


def handle_undo(tranzactii, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, tranzactii)
    if undo_result is not None:
        return undo_result
    return tranzactii


def handle_redo(tranzactii, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, tranzactii)
    if redo_result is not None:
        return redo_result
    return tranzactii


def run_ui1(tranzactii, undo_list, redo_list):
    while True:
        handle_show_all(tranzactii)
        show_menu()
        optiune = input('Optiunea aleasa: ')
        # if optiune == '1':
        # tranzactii = handle_crud(tranzactii)
        if optiune == '1':
            tranzactii = Adaugare(tranzactii, undo_list, redo_list)
        elif optiune == '2':
            tranzactii = Stergeri(tranzactii, undo_list, redo_list)
        elif optiune == '3':
            Cautari(tranzactii)
        elif optiune == '4':
            Rapoarte(tranzactii)
        elif optiune == '5':
            Filtrare(tranzactii)
        elif optiune == 'u':
            tranzactii = handle_undo(tranzactii, undo_list, redo_list)
        elif optiune == 'r':
            tranzactii = handle_redo(tranzactii, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')
    return tranzactii


##########################################


def handle_crud(tranzactii, undo_list, redo_list):
    while True:
        print('1. Adaugare tranzactie.')
        print('2. Actualizare tranzactie.')
        print('3. Șterge toate tranzacțiile de la ziua specificată.')
        print('4. Șterge tranzacțiile dintr-o perioadă dată (se dă ziua de început și sfârșit).')
        print('5. Șterge toate tranzacțiile de un anumit tip.')
        print('a. Afisare')
        print('d. Detalii tranzactie')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            tranzactii = handle_add(tranzactii, undo_list, redo_list)
        elif optiune == '2':
            tranzactii = handle_update(tranzactii, undo_list, redo_list)
        elif optiune == '3':
            tranzactii = handle_delete(tranzactii, undo_list, redo_list)
        elif optiune == '4':
            tranzactii = handle_delete_between_a_period(tranzactii, undo_list, redo_list)
        elif optiune == '5':
            tranzactii = handle_delete_tranzactions_by_type(tranzactii, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(tranzactii)
        elif optiune == 'd':
            handle_show_details(tranzactii)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return tranzactii

###############################################################################################
