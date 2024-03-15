from Domain.client import Client


def test_client_getteri():
    client = Client('1', 'ion radu', '349873293')

    assert client.get_id_client() == '1'
    assert client.get_nume_client() == 'ion radu'
    assert client.get_cnp_client() == '349873293'


def test_client_setteri():
    client = Client('1', 'ion radu', '349873293')

    client.set_id_client('5')
    assert client.get_id_client() == '5'

    client.set_nume_client('gabriel alexandru')
    assert client.get_nume_client() == 'gabriel alexandru'

    client.set_cnp_client('3923874223')
    assert client.get_cnp_client() == '3923874223'
