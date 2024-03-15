from Logic.crud import create
from Logic.elimina_tranz_anumit_tip import elimina_tranz_anumit_tip


def test_elimina_tranz_anumit_tip():
    tranzactii = []
    tranzactii = create(tranzactii, 12, 234, 'intrare', [], [])
    tranzactii = create(tranzactii, 3, 999, 'iesire', [], [])
    tranzactii = create(tranzactii, 7, 12333, 'intrare', [], [])
    tranzactii = create(tranzactii, 13, 4342, 'iesire', [], [])
    tranzactii = create(tranzactii, 1, 10, 'intrare', [], [])
    tranzactii = create(tranzactii, 27, 10000, 'iesire', [], [])

    tip_to_delete = 'intrare'
    deleted = elimina_tranz_anumit_tip(tranzactii, tip_to_delete)
    assert len(deleted) == 3
    assert len(deleted) != len(tranzactii)
