from Domain.carte_validator import CarteValidator
from Repository.carte_file_repository import CarteFileRepository
# from Repository.carte_repository import CarteRepository
from Service.carte_service import CarteService


def test_carte_service():
    carte_repo = CarteFileRepository()
    carte_validator = CarteValidator()
    carte_service = CarteService(carte_repo, carte_validator)

    # test carte service add
    carte_service.add_carte('1', 'morometii', 'roman', 'marin preda')
    carti = carte_service.get_all_carti()
    assert len(carti) == 1
    assert carti[0].get_id_carte() == '1'
    assert carti[0].get_titlu_carte() == 'morometii'
    assert carti[0].get_descriere_carte() == 'roman'
    assert carti[0].get_autor_carte() == 'marin preda'

    try:
        carte_service.add_carte('1', 'aaa', 'bbbb', 'ccc')
        assert False
    except KeyError:
        ...

    # test carte service update
    carte_service.add_carte('2', 'iona', 'teatru', 'marin sorescu')
    carte_service.update_carte('2', 'ciresarii', 'roman', 'ct chirita')
    carti = carte_service.get_all_carti()
    assert carti[1].get_titlu_carte() == 'ciresarii'
    assert carti[1].get_descriere_carte() == 'roman'
    assert carti[1].get_autor_carte() == 'ct chirita'

    try:
        carte_service.update_carte('7', 'aaa', 'aaaa', 'aaaa')
        assert False  # nu exista inca cartea cu id '7' care sa se modifica
    except KeyError:
        ...

    # test carte service delete
    carte_service.delete_carte('2')
    carti = carte_service.get_all_carti()
    assert len(carti) == 1

    carte_service.delete_carte('1')
    assert len(carte_service.get_all_carti()) == 0

    try:
        carte_service.delete_carte('999')
        assert False  # nu exista cartea cu id '999' care sa se stearga
    except KeyError:
        ...

    # test carte service cautari dupa id, titlu, descriere, autor
