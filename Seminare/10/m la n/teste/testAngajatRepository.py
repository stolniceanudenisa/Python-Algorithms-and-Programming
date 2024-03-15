from domeniu.angajat import Angajat
from repository.repository import Repository


def testAdaugaAngajatRepository():
    angajatRepository = Repository()
    angajat = Angajat("1", "ana")

    angajatRepository.adauga(angajat)

    angajati = angajatRepository.getAll()
    assert len(angajati) == 1
    assert angajati[0].getIdAngajat() == "1"

    try:
        angajatRepository.adauga(angajat)
        assert False
    except KeyError:
        ...

def testModificaAngajatRepository():
    angajatRepository = Repository()
    angajat = Angajat("1", "ana")
    angajatNou1 = Angajat("1", "paul")
    angajatNou2 = Angajat("2", "ion")
    angajatRepository.adauga(angajat)

    angajatRepository.modifica(angajatNou1)

    angajati = angajatRepository.getAll()
    assert angajati[0].getNume() == "paul"

    try:
        angajatRepository.modifica(angajatNou2)
        assert False
    except KeyError:
        ...

def testStergeAngajatRepository():
    angajatRepository = Repository()
    angajat = Angajat("1", "ana")
    angajatRepository.adauga(angajat)

    angajatRepository.sterge("1")

    assert len(angajatRepository.getAll()) == 0

    try:
        angajatRepository.sterge("!")
        assert False
    except KeyError:
        ...