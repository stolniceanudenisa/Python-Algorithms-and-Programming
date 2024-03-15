from Tests.test_domain_carte import test_carte_getteri, test_carte_setteri
from Tests.test_domain_client import test_client_getteri, test_client_setteri


def test_all():
    test_carte_getteri()
    test_carte_setteri()

    test_client_getteri()
    test_client_setteri()

    # test_carte_repository()
    # test_client_repository()

    # test_carte_service()
    # test_client_service()
