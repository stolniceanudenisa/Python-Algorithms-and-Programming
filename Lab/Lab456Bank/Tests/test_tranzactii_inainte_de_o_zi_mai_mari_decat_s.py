from Logic.crud import create
from Logic.tipareste_tranzactii_inainte_de_o_zi_mai_mari_decat_s import tranzactii_inainte_de_o_zi_mai_mari_decat_s
from Logic.tipareste_tranzactii_mai_mari_decat_o_suma_data import tranzactii_mai_mari_decat_o_suma_data


def test_tranzactii_inainte_de_o_zi_mai_mari_decat_s():
    tranzactii = []
    tranzactii = create(tranzactii, 12, 234.90, 'intrare', [], [])
    tranzactii = create(tranzactii, 3, 999, 'iesire', [], [])
    tranzactii = create(tranzactii, 7, 12333, 'intrare', [], [])
    tranzactii = create(tranzactii, 13, 4342, 'iesire', [], [])
    tranzactii = create(tranzactii, 1, 10, 'intrare', [], [])
    tranzactii = create(tranzactii, 27, 10000, 'iesire', [], [])

    rezultat = tranzactii_inainte_de_o_zi_mai_mari_decat_s(tranzactii, 20)
    new_rezultat = tranzactii_mai_mari_decat_o_suma_data(rezultat, 200)

    assert len(new_rezultat) == 4