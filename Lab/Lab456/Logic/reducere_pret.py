from Domain.prajitura import get_nume, get_pret, creeaza_prajitura, get_descriere, get_calorii, get_an_introducere, \
    get_id


def reducere_pret_pentru_nume(lst_prajituri, continut_nume, procentaj):
    '''

    :param lst_prajituri:
    :param continut_nume:
    :param procentaj: intre 0 si 100
    :return:
    '''

    if not (0 <= procentaj <= 100):
        raise ValueError('Procentajul trebuie sa fie intre 0 si 100 inclusiv.')
    if continut_nume == '':
        raise ValueError('Textul cautat nu poate fi gol!')

    result = []
    for prajitura in lst_prajituri:
        if continut_nume in get_nume(prajitura):
            pret_nou = ( procentaj / 100 ) * get_pret(prajitura)
            result.append(creeaza_prajitura(
                get_id(prajitura),
                get_nume(prajitura),
                get_descriere(prajitura),
                pret_nou,
                get_calorii(prajitura),
                get_an_introducere(prajitura)
            ))
        else:
            result.append(prajitura)
    return result