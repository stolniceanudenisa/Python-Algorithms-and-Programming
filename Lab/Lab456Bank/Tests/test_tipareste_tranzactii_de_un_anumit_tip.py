from Logic.crud import create
from Logic.tipareste_tranzactii_de_un_anumit_tip import tipareste_tranzactii_de_un_anumit_tip


def test_tipareste_tranzactii_de_un_anumit_tip():
    tranzactii = []
    tranzactii = create(tranzactii, 12, 234.90, 'intrare', [], [])
    tranzactii = create(tranzactii, 3, 999, 'iesire', [], [])
    tranzactii = create(tranzactii, 7, 12333, 'intrare', [], [])
    tranzactii = create(tranzactii, 13, 4342, 'iesire', [], [])
    tranzactii = create(tranzactii, 1, 10, 'intrare', [], [])
    tranzactii = create(tranzactii, 27, 10000, 'iesire', [], [])

    rezultat = tipareste_tranzactii_de_un_anumit_tip(tranzactii, 'intrare')

    assert len(rezultat) == 3