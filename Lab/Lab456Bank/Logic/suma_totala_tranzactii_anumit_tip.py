from Domain.tranzactie import get_tip, get_suma


def suma_totala_tranzactii_anumit_tip(lst_tranzactii, tip_tranzactie):
    '''
    Suma totală a tranzacțiilor de un anumit tip
    :param lst_tranzactii: lista de tranzactii
    :param tip_tranzactie: intrare sau iesire
    :return: suma totală a tranzacțiilor de un anumit tip
    '''
    suma = 0
    for tranzactie in lst_tranzactii:
        if get_tip(tranzactie) == tip_tranzactie:
            suma = suma + get_suma(tranzactie)
    return suma