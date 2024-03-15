from Domain.angajat import Angajat


def testAngajatGetteri():
    angajat = Angajat("1", "ana")

    assert angajat.getIdAngajat() == "1"
    assert angajat.getNume() == "ana"


def testAngajatSetteri():
    angajat = Angajat("1", "ana")

    angajat.setIdAngajat("2")
    assert angajat.getIdAngajat() == "2"

    angajat.setNume("maria")
    assert angajat.getNume() == "maria"
