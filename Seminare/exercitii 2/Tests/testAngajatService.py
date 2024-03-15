from Repository.angajatRepository import AngajatRepository
from Service.angajatService import AngajatService


def testadaugaAngajat_service():
    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)

    angajatService.adaugaAngajat("1", "ana")
    angajati = angajatService.getAllAngajati()
    assert len(angajati) == 1
    assert angajati[0].getIdAngajat() == "1"
    assert angajati[0].getNume() == "ana"

    try:
        angajatService.adaugaAngajat("1", "ana")
        assert False
    except KeyError:
        ...


def testmodificaAngajat_service():
    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)
    angajatService.adaugaAngajat("1", "ana")

    angajatService.modificaAngajat("1", "maria")

    angajati = angajatService.getAllAngajati()
    assert angajati[0].getNume() == "maria"

    try:
        angajatService.modificaAngajat("2", "ion")
        assert False
    except KeyError:
        ...


def teststergeAngajat_service():
    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)
    angajatService.adaugaAngajat("1", "ana")

    angajatService.stergeAngajat("1")
    angajati = angajatService.getAllAngajati()

    assert len(angajati) == 0

    try:
        angajatService.stergeAngajat("1")
        assert False
    except KeyError:
        ...
