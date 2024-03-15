from Logic.crud import create
from Logic.elim_tranz_mai_mici_decat_suma import elim_tranz_mai_mici_decat_suma


def test_elim_tranz_mai_mici_decat_suma():
    tranzactii = []
    tranzactii = create(tranzactii, 12, 234.90, 'intrare', [], [])
    tranzactii = create(tranzactii, 3, 999, 'iesire', [], [])
    tranzactii = create(tranzactii, 7, 12333, 'intrare', [], [])
    tranzactii = create(tranzactii, 13, 4342, 'iesire', [], [])
    tranzactii = create(tranzactii, 1, 10, 'intrare', [], [])
    tranzactii = create(tranzactii, 27, 10000, 'iesire', [], [])

    rezultat = elim_tranz_mai_mici_decat_suma(tranzactii, 'intrare', 1000)

    assert len(rezultat) == 3