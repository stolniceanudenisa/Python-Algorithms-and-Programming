from domeniu.angajat import Angajat


def testAngajat():
    angajat = Angajat("1", "ana")

    assert angajat.getIdAngajat() == "1"
    assert angajat.getNume() == "ana"

def testAngajatSetteri():
    angajat = Angajat("1", "ana")

    angajat.setIdAngajat("2")
    assert angajat.getIdAngajat() == "2"

    angajat.setNume("paul")
    assert angajat.getNume() == "paul"