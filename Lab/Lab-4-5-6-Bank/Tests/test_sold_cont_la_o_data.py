from Logic.crud import create
from Logic.sold_cont_la_o_data import sold_cont_la_o_data


def test_sold_cont_la_o_data():
    tranzactii = []
    tranzactii = create(tranzactii, 12, 200.234, 'intrare', [], [])
    tranzactii = create(tranzactii, 2, 1200.777, 'iesire', [], [])
    tranzactii = create(tranzactii, 31, 50.23, 'iesire', [], [])
    tranzactii = create(tranzactii, 4, 10000, 'intrare', [], [])
    tranzactii = create(tranzactii, 15, 100.50, 'intrare', [], [])
    tranzactii = create(tranzactii, 4, 4444, 'intrare', [], [])
    tranzactii = create(tranzactii, 26, 144.189, 'iesire', [], [])
    tranzactii = create(tranzactii, 7, 341121, 'iesire', [], [])
    tranzactii = create(tranzactii, 4, 1999.10, 'iesire', [], [])
    tranzactii = create(tranzactii, 8, 44121, 'iesire', [], [])
    tranzactii = create(tranzactii, 30, 3132, 'iesire', [], [])
    tranzactii = create(tranzactii, 4, 12.986, 'iesire', [], [])

    rezultat = sold_cont_la_o_data(tranzactii, 20)

    assert len(rezultat) == 9