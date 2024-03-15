from Repository.client_repository import ClientRepository
from Service.client_service import ClientService


def test_client_service():
    client_repo = ClientRepository()
    client_service = ClientService(client_repo)

    # test client service add
    client_service.add_client('1', 'mihai munteanu', '38293924')
    clienti = client_service.get_all_clienti()

    assert len(clienti) == 1
    assert clienti[0].get_id_client() == '1'
    assert clienti[0].get_nume_client() == 'mihai munteanu'
    assert clienti[0].get_cnp_client() == '38293924'

    try:
        client_service.add_client('1', 'aaa', 'bbbb')
        assert False  # exista deja un client cu id-ul '1'
    except KeyError:
        ...

    # test client service update
    client_service.add_client('2', 'ion marin', '345232142')
    client_service.update_client('2', 'ana maria', '24542546')
    clienti = client_service.get_all_clienti()
    assert clienti[1].get_nume_client() == 'ana maria'
    assert clienti[1].get_cnp_client() == '24542546'

    try:
        client_service.update_client('5555', 'aaa', 'aaaa')
        assert False  # nu exista clientul cu id-ul '5555' care sa se updateze
    except KeyError:
        ...

    # test client service delete
    client_service.delete_client('2')
    clienti = client_service.get_all_clienti()
    assert len(clienti) == 1

    client_service.delete_client('1')
    assert len(client_service.get_all_clienti()) == 0

    try:
        client_service.delete_client('999')
        assert False  # nu exista clientul cu id '999' care sa se stearga
    except KeyError:
        ...
