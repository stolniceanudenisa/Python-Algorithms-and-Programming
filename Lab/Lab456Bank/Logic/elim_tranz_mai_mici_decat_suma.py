from Domain.tranzactie import get_suma, get_tip


def elim_tranz_mai_mici_decat_suma(lst_tranzactii, tip_tranzactie, suma_tranzactie):
    '''
    Elimina tranzactiile mai mici decat o suma data care au tipul specificat.
    :param lst_tranzactii: lista de tranzactii
    :param suma_tranzactie:
    :return:
    '''
    rezultat = []
    for tranz in lst_tranzactii:
        if get_tip(tranz) == tip_tranzactie:
            if get_suma(tranz) > suma_tranzactie:
                rezultat.append(tranz)
        else:
            if get_suma(tranz) > suma_tranzactie:
                rezultat.append(tranz)
    return rezultat


