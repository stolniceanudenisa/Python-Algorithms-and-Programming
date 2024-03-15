from Domain.tranzactie import get_ziua


def ordonare_ziua(tranzactie):
    return get_ziua(tranzactie)


def sold_cont_la_o_data(lst_tranzactii, ziua_tranzactie):
    '''
    Afiseaza toate tranzactiile efectuate pana la o zi data.
    :param lst_tranzactii: lista de tranzactii.
    :param ziua_tranzactie: ziua respectiva.
    :return: lista cu tranzactii efectuate pana la o zi data.
    '''
    rezultat = []
    for tranz in lst_tranzactii:
        if get_ziua(tranz) < ziua_tranzactie:
            rezultat.append(tranz)
    return sorted(rezultat, key=ordonare_ziua)