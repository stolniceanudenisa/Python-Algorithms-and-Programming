from Domain.tranzactie import get_tip


def elimina_tranz_anumit_tip(lst_tranzactii, tip_tranzactie):
    '''
    Elimină toate tranzacțiile de un anumit tip
    :param lst_tranzactii: lista de tranzactii
    :param tip_tranzactie: tipul tranzactiei
    :return: o lista nou cu tranzactiile eliminate
    '''
    tranzactii = []
    for tranz in lst_tranzactii:
        if get_tip(tranz) != tip_tranzactie:
            tranzactii.append(tranz)
    return tranzactii
