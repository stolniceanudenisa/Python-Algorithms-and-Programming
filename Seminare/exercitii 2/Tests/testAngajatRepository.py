from Domain.angajat import Angajat
from Repository.angajatRepository import AngajatRepository


def testadd_ang_repository():
    angajatRepository = AngajatRepository()
    angajat = Angajat("1", "ana")
    angajatRepository.add(angajat)

    angajati = angajatRepository.getAll()
    assert len(angajati) == 1
    assert angajatRepository.getById("1") is not None
    assert angajatRepository.getById("1").getNume() == "ana"

    try:
        angajatRepository.add(angajat)
        assert False
    except KeyError:
        ...


def testmodifica_ang_repository():
    angajatRepository = AngajatRepository()
    angajat = Angajat("1", "ana")
    angajatRepository.add(angajat)

    angajatNou1 = Angajat("1", "maria")
    angajatNou2 = Angajat("2", "ion")

    angajatRepository.modifica(angajatNou1)

    assert angajatRepository.getById("1").getNume() == "maria"

    try:
        angajatRepository.modifica(angajatNou2)
        assert False
    except KeyError:
        ...


def teststerge_ang_repository():
    angajatRepository = AngajatRepository()
    angajat = Angajat("1", "ana")
    angajatRepository.add(angajat)

    angajatRepository.sterge("1")
    assert len(angajatRepository.getAll()) == 0

    try:
        angajatRepository.sterge("1")
        assert False
    except KeyError:
        ...
