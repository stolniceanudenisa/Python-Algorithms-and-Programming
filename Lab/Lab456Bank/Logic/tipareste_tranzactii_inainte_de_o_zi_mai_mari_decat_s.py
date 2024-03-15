from Domain.tranzactie import get_ziua, get_suma


def tranzactii_inainte_de_o_zi_mai_mari_decat_s(lst_tranzactii, ziua_tranzactie):
    '''
    Tipărește toate tranzacțiile efectuate înainte de o zi și mai mari decât o sumă (se dă suma și ziua)
    :param lst_tranzactii: lista de tranzactii
    :param ziua_ranzactie: ziua efectuarii tranzactiei
    :return: toate tranzacțiile efectuate înainte de o zi și mai mari decât o sumă
    '''
    rezultat = []
    for tranzactie in lst_tranzactii:
        if get_ziua(tranzactie) < ziua_tranzactie:
                rezultat.append(tranzactie)
    return rezultat








