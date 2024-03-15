from Domain.prajitura import get_pret, get_calorii


def raport_pret_calorii(prajitura):
    return get_pret(prajitura)/get_calorii(prajitura)


def get_ordonare_raport_pret_calorii(lst_prajituri):
    '''

    :param lst_prajituri:
    :return:
    '''
    return sorted(lst_prajituri, key=raport_pret_calorii)