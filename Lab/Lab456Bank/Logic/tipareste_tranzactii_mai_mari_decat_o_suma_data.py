from Domain.tranzactie import get_suma


def tranzactii_mai_mari_decat_o_suma_data(lst_tranzactii, suma_tranzactie):
    '''
    Gaseste tranzactiile mai mari decat o suma data.
    :param lst_tranzactii: lista de tranzactii
    :param suma_tranzactie: suma introdusa/scoasa
    :return: o lista cu tranzactiile mai mari decat o suma data
    '''
    rezultat = []
    for tranzactie in lst_tranzactii:
        if get_suma(tranzactie) > suma_tranzactie:
            rezultat.append(tranzactie)
    if len(rezultat) == 0:
        raise ValueError(f'Valoarea cheltuielii este prea mare.')
    return rezultat



