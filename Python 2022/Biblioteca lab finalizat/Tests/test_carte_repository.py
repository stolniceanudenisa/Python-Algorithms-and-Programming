from Domain.carte import Carte
from Repository.carte_repository import CarteRepository


def test_carte_repository():
    carte_repo = CarteRepository()
    carte = Carte('1', 'ion', 'roman', 'lvr')
    carte_repo.add(carte)

    carti = carte_repo.get_all()
    assert len(carti) == 1
    assert carte_repo.get_by_id('1') is not None
    assert carte_repo.get_by_id('1').get_titlu_carte() == 'ion'
    assert carte_repo.get_by_id('1').get_descriere_carte() == 'roman'
    assert carte_repo.get_by_id('1').get_autor_carte() == 'lvr'

    try:
        carte_repo.add(carte)
        assert False  # exista deja cartea cu id '1'
    except KeyError:
        ...

    # ----------------------------------------

    carte_repo.update(Carte('1', 'eeee', 'ffff', 'gggg'))
    assert carte_repo.get_by_id('1').get_titlu_carte() == 'eeee'
    assert carte_repo.get_by_id('1').get_descriere_carte() == 'ffff'
    assert carte_repo.get_by_id('1').get_autor_carte() == 'gggg'

    try:
        carte_repo.update(Carte('9999', 'aa', 'bb', 'cc'))
        assert False  # nu exista cartea cu id 9999 pe care sa o modificam
    except KeyError:
        ...

    # ----------------------------------------

    carte_repo.delete('1')
    assert len(carte_repo.get_all()) == 0

    try:
        carte_repo.delete('777')
        assert False  # nu exista cartea cu id 777 pe care sa o stergem
    except KeyError:
        ...
