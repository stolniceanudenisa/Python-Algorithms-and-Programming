from Domain.client import Client
from Repository.client_repository import ClientRepository


def test_client_repository():
    client_repo = ClientRepository()
    client = Client('1', 'ion popa', '84738132992')
    client_repo.add(client)

    clienti = client_repo.get_all()
    assert len(clienti) == 1
    assert client_repo.get_by_id('1') is not None
    assert client_repo.get_by_id('1').get_nume_client() == 'ion popa'
    assert client_repo.get_by_id('1').get_cnp_client() == '84738132992'

    try:
        client_repo.add(client)
        assert False  # exista deja clientul cu id '1'
    except KeyError:
        ...

    # ----------------------------------------

    client_repo.update(Client('1', 'marius radu', '23823124233'))
    assert client_repo.get_by_id('1').get_nume_client() == 'marius radu'
    assert client_repo.get_by_id('1').get_cnp_client() == '23823124233'

    try:
        client_repo.update(Client('9999', 'aaa', '2332234'))
        assert False  # nu exista clientul cu id 9999 pe care sa il modificam
    except KeyError:
        ...

    # ----------------------------------------

    client_repo.delete('1')
    assert len(client_repo.get_all()) == 0

    try:
        client_repo.delete('777')
        assert False  # nu exista clientul cu id 777 pe care sa il stergem
    except KeyError:
        ...

