from Logic.crud import create
from Logic.suma_totala_tranzactii_anumit_tip import suma_totala_tranzactii_anumit_tip


def test_suma_totala_tranzactii_anumit_tip():
    tranzactii = []
    tranzactii = create(tranzactii, 12, 1, 'intrare', [], [])
    tranzactii = create(tranzactii, 3, 999, 'iesire', [], [])
    tranzactii = create(tranzactii, 7, 2, 'intrare', [], [])
    tranzactii = create(tranzactii, 13, 4342, 'iesire', [], [])
    tranzactii = create(tranzactii, 1, 3, 'intrare', [], [])
    tranzactii = create(tranzactii, 27, 4, 'iesire', [], [])

    rez =  suma_totala_tranzactii_anumit_tip(tranzactii, 'intrare')
    assert rez == 6