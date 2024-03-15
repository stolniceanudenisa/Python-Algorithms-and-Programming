def creeaza_prajitura(id_prajitura: int, nume, descriere, pret, calorii, an_introducere):
    '''

    :param id_prajitura:
    :param nume:
    :param descriere:
    :param pret:
    :param calorii:
    :param an_introducere:
    :return:
    '''
    return {
        'id': id_prajitura,
        'nume': nume,
        'desc': descriere,
        'pret': pret,
        'calorii': calorii,
        'an': an_introducere,
    }

def get_id(prajitura):
    '''
    Getter pentru id-ul prajiturii.
    :param prajitura: prajitura
    :return:id-ul prajiturii date ca parametru.
    '''
    return prajitura['id']


def get_nume(prajitura):
    '''

    :param prajitura:
    :return:
    '''
    return prajitura['nume']


def get_descriere(prajitura):
    return prajitura['desc']


def get_pret(prajitura):
    return prajitura['pret']


def get_calorii(prajitura):
    return prajitura['calorii']


def get_an_introducere(prajitura):
    return prajitura['an']


def get_str(prajitura):
    return f'Prajitura cu id-ul {get_id(prajitura)}, introdusa in anul: {get_an_introducere(prajitura)}, pretul: {get_pret(prajitura)}, caloriile: {get_calorii(prajitura)}, numele: {get_nume(prajitura)}, descrierea: {get_descriere(prajitura)}'