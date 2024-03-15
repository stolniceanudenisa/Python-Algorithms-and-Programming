from Domain.tranzactie import get_suma, get_tip


def ordonare_suma(tranzactie):
    return get_suma(tranzactie)


def tipareste_tranz_tip_ordonat_dupa_suma(lst_tranzactii, tip_tranzactie):
    '''
    Tipărește toate tranzacțiile efectuate înainte de o zi și mai mari decât o sumă
    :param lst_tranzactii: lista de tranzactii
    :param tip_tranzactie: tipul tranzactiei
    :return: toate tranzacțiile efectuate înainte de o zi și mai mari decât o sumă
    '''
    rezultat = []
    for tranzactie in lst_tranzactii:
        if get_tip(tranzactie) == tip_tranzactie:
            rezultat.append(tranzactie)
    return sorted(rezultat, key=ordonare_suma)
