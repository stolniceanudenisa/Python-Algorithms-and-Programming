from Domain.tranzactie import get_tip


def tipareste_tranzactii_de_un_anumit_tip(lst_tranzactii, tip_tranzactie):
    '''
    Tipărește tranzacțiile de un anumit tip
    :param lst_tranzactii: lista de tranzactii
    :param tip_tranzactie: intrare/iesire
    :return: lista de tranzactii de un anumit tip
    '''
    rezultat = []
    for tranzactie in lst_tranzactii:
        if get_tip(tranzactie) == tip_tranzactie:
            rezultat.append(tranzactie)
    return rezultat
