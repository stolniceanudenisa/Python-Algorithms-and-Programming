from teste.test_domain import test_domain
from teste.test_repository import test_all_repository


def test_all():
    test_domain()
    test_all_repository()
    # test_all_service()