from Domain.prajitura import get_pret


def suma_pe_fiecare_an(lst_prajituri):
    '''

    :param lst_prajituri:
    :return:
    '''
    result = {}  # result[x] = prajitura cu nr max de calorii din anul x
    for prajitura in lst_prajituri:
        an = get_an_introducere(prajitura)
        calorii = get_calorii(prajitura)
        if an not in result:
            result[an] = pret[prajitura]
        else:  # sau elif
                result[an] += get_pret(prajitura)
    return result