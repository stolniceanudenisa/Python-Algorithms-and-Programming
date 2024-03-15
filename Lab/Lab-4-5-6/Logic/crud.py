from Domain.prajitura import creeaza_prajitura, get_id


def create(lst_prajituri, id_prajitura: int, nume, descriere, pret, calorii, an_introducere):
    '''

    :param lst_prajituri:
    :param id_prajitura:
    :param nume:
    :param descriere:
    :param pret:
    :param calorii:
    :param an_introducere:
    :return: o noua lista formata din lst_prajituri si noua prajitura adaguata.
    '''

    if read(lst_prajituri, id_prajitura) is not None:
        raise ValueError(f'Exista deja o prajitura cu id-ul {id_prajitura}')

    prajitura = creeaza_prajitura(id_prajitura, nume, descriere, pret, calorii, an_introducere)
    #lst_prajituri.append(prajitura)
    return lst_prajituri + [prajitura]


def read(lst_prajituri, id_prajitura: int = None):
    '''
    Citeste o prajitura din "baza de date".
    :param lst_prajituri: lista de prajituri
    :param id_prajitura: id-ul prajiturii dorite.
    :return: - prajitura cu id-ul id_prajitura, daca exista
            - lista cu toate prajiturile daca id_prajitura = None
            - None, caca nu exista o prajitura cu id_prajitura
    '''

    if not id_prajitura:
        return lst_prajituri

    prajtura_cu_id = None
    for prajitura in lst_prajituri:
        if get_id(prajitura) == id_prajitura:
            prajtura_cu_id = prajitura

    if prajtura_cu_id:
        return prajtura_cu_id
    return None



def update(lst_prajituri, new_prajitura):
    '''
    Actualizeaza o prajitura.
    :param lst_prajituri: lista de prajituri.
    :param prajitura: prajitura care se va actualiza - id-ul trebuie sa fie existent.
    :return: o lista cu prajitura actualizata.
    '''

    #lst_prajituri=[p1:(1, ecler),p2: (2,amandina)], prajitura=(2, lavacake)
    new_prajituri = []

    if read(lst_prajituri, get_id(new_prajitura)) is None:
        raise ValueError(f'Nu exista o prajitura cu id-ul {get_id(new_prajitura)} care sa se actualizeze.')

    for prajitura in lst_prajituri:
        if get_id(prajitura) != get_id(new_prajitura):
            new_prajituri.append(prajitura)
        else:
            new_prajituri.append(new_prajitura)
    return new_prajituri


def delete(lst_prajituri, id_prajitura: int):
    '''

    :param lst_prajituri:
    :param id_prajitura:
    :return: o lista de prajituri fara id-ul id_prajitura.
    '''

    if read(lst_prajituri, id_prajitura) is None:
        raise ValueError(f'Nu exista o prajitura cu id-ul {id_prajitura} pe care sa o stergem.')

    new_prajituri = []

    for prajitura in lst_prajituri:
        if get_id(prajitura) != id_prajitura:
            new_prajituri.append(prajitura)
    return new_prajituri



