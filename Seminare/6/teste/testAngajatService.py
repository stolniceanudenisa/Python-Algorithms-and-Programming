from repository.angajatRepository import AngajatRepository
from service.AngajatService import AngajatService


def testAdaugaAngajatService():
    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)
    angajatService.adauga("1", "ana")

    angajati = angajatService.getAllAngajati()
    assert len(angajati) == 1
    assert angajati[0].getIdAngajat() == "1"

    try:
        angajatService.adauga("1", "ion")
        assert False
    except KeyError:
        ...

def testModificaAngajatService():
    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)
    angajatService.adauga("1", "ana")

    angajatService.modifica("1", "paul")

    angajati = angajatService.getAllAngajati()
    assert angajati[0].getNume() == "paul"

    try:
        angajatService.modifica("2", "ion")
        assert False
    except KeyError:
        ...

def testStergeAngajatService():
    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)
    angajatService.adauga("1", "ana")

    angajatService.sterge("1")

    angajati = angajatService.getAllAngajati()
    assert len(angajati) == 0

    try:
        angajatService.sterge("1")
        assert False
    except KeyError:
        ...