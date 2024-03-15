from domeniu import creeazaCarte, getCod, getTitlu, getAutor, getPret, setCod, setTitlu, setAutor, setPret
from operatii import adaugaCarte, modificaCarte, stergeCarte, cartiInIntervalPret, sumePreturiPerAutor, cautare, \
    mediePreturiPerAutor, ceaMaiScumpaCartePerAutor, sortareDupaPretDesc, reducerePretDupaAutor, cartiPeCategoriiPreturi


def testCreeazaCarte():
    carte = creeazaCarte(1, "ana", "bogdan", 23.5)
    assert getCod(carte) == 1
    assert getTitlu(carte) == "ana"
    assert getAutor(carte) == "bogdan"
    assert getPret(carte) == 23.5

def testSetteri():
    carte = creeazaCarte(1, "ana", "bogdan", 23.5)

    setCod(carte, 2)
    assert getCod(carte) == 2

    setTitlu(carte, "Ion")
    assert getTitlu(carte) == "Ion"

    setAutor(carte, "Popa")
    assert getAutor(carte) == "Popa"

    setPret(carte, 20.0)
    assert getPret(carte) == 20

def testAdaugaCarte():
    listaCarti = []
    cod = 1
    titlu = "ion"
    autor = "popa"
    pret = 23.1

    adaugaCarte(cod, titlu, autor, pret, listaCarti)

    assert(len(listaCarti) == 1)
    carte = listaCarti[0]
    assert getCod(carte) == 1
    assert getTitlu(carte) == "ion"
    assert getAutor(carte) == "popa"
    assert getPret(carte) == 23.1

def testModificaCarte():
    listaCarti = []
    titluNou = "flori"
    autorNou = "luci"
    pretNou = 20.0
    adaugaCarte(1, "ana", "bogdan", 23.5, listaCarti)
    adaugaCarte(2, "ion", "popa", 21.1, listaCarti)

    modificaCarte(1, titluNou, autorNou, pretNou, listaCarti)

    assert(len(listaCarti) == 2)

    assert(getCod(listaCarti[0]) == 1)
    assert (getTitlu(listaCarti[0]) == titluNou)
    assert (getAutor(listaCarti[0]) == autorNou)
    assert (getPret(listaCarti[0]) == pretNou)

    assert (getCod(listaCarti[1]) == 2)
    assert (getTitlu(listaCarti[1]) == "ion")
    assert (getAutor(listaCarti[1]) == "popa")
    assert (getPret(listaCarti[1]) == 21.1)

def testStergeCarte():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 23.5, listaCarti)
    adaugaCarte(2, "ion", "popa", 21.1, listaCarti)

    stergeCarte(2, listaCarti)

    assert(len(listaCarti) == 1)
    assert(getCod(listaCarti[0]) == 1)

def testCartiInIntervalPret():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 23.5, listaCarti)
    adaugaCarte(2, "ion", "popa", 21.1, listaCarti)
    adaugaCarte(3, "luci", "popescu", 24.1, listaCarti)

    rezultat = cartiInIntervalPret(22.2, 25.5, listaCarti)

    assert len(rezultat) == 2
    assert getCod(rezultat[0]) == 1
    assert getCod(rezultat[1]) == 3

def testSumaPreturiPerAutor():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 23.5, listaCarti)
    adaugaCarte(2, "ion", "popa", 21.1, listaCarti)
    adaugaCarte(3, "luci", "bogdan", 24.1, listaCarti)

    rezultat = sumePreturiPerAutor(listaCarti)

    assert(len(rezultat) == 2)
    assert(rezultat["bogdan"] == 47.6)
    assert(rezultat["popa"] == 21.1)

def testCautare():
    listaCarti = []
    adaugaCarte(111, "ana", "bogdan", 23.5, listaCarti)
    adaugaCarte(1, "luci", "bogdan", 24.1, listaCarti)
    adaugaCarte(2, "ion11", "popa", 21.1, listaCarti)
    adaugaCarte(3, "luci", "bogdan111", 24.1, listaCarti)
    adaugaCarte(4, "luci", "bogdan", 21114.1, listaCarti)

    rezultat = cautare("11", listaCarti)

    assert len(rezultat) == 4
    assert getCod(rezultat[0]) == 111
    assert getCod(rezultat[1]) == 2
    assert getCod(rezultat[2]) == 3
    assert getCod(rezultat[3]) == 4

def testMediePreturiPerAutor():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 20.0, listaCarti)
    adaugaCarte(2, "ion", "popa", 19.0, listaCarti)
    adaugaCarte(3, "luci", "bogdan", 10.0, listaCarti)

    rezultat = mediePreturiPerAutor(listaCarti)

    assert len(rezultat) == 2
    assert rezultat["bogdan"] == 15.0
    assert rezultat["popa"] == 19.0

def testCeaMaiScumpaCartePerAutor():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 20.0, listaCarti)
    adaugaCarte(2, "ion", "popa", 19.0, listaCarti)
    adaugaCarte(3, "luci", "bogdan", 10.0, listaCarti)

    rezultat = ceaMaiScumpaCartePerAutor(listaCarti)

    assert len(rezultat) == 2
    print(rezultat)
    assert getCod(rezultat['bogdan']) == 1
    assert getPret(rezultat['bogdan']) == 20.0
    assert getCod(rezultat['popa']) == 2
    assert getPret(rezultat['popa']) == 19.0


def testSortareDupaPretDesc():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 20.0, listaCarti)
    adaugaCarte(2, "ion", "popa", 29.0, listaCarti)
    adaugaCarte(3, "luci", "bogdan", 10.0, listaCarti)

    sortareDupaPretDesc(listaCarti)

    assert getCod(listaCarti[0]) == 2
    assert getCod(listaCarti[1]) == 1
    assert getCod(listaCarti[2]) == 3

def testReducerePretDupaAutor():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 20.0, listaCarti)
    adaugaCarte(2, "ion", "popa", 29.0, listaCarti)
    adaugaCarte(3, "luci", "bogdan", 10.0, listaCarti)

    reducerePretDupaAutor(10, "bogdan", listaCarti)

    assert getPret(listaCarti[0]) == 18
    assert getPret(listaCarti[1]) == 29
    assert getPret(listaCarti[2]) == 9

def testCartiPeCategoriiPreturi():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 49.0, listaCarti)
    adaugaCarte(2, "ion", "popa", 121.0, listaCarti)
    adaugaCarte(3, "luci", "bogdan", 13.0, listaCarti)

    rezultat = cartiPeCategoriiPreturi(listaCarti)

    assert len(rezultat) == 2
    assert getCod(rezultat[0][0]) == 1
    assert getCod(rezultat[0][1]) == 3
    assert getCod(rezultat[100][0]) == 2

def testAll():
    testCreeazaCarte()
    testSetteri()
    testAdaugaCarte()
    testModificaCarte()
    testStergeCarte()
    testCartiInIntervalPret()
    testSumaPreturiPerAutor()
    testCautare()
    testMediePreturiPerAutor()
    testCeaMaiScumpaCartePerAutor()
    testSortareDupaPretDesc()
    testReducerePretDupaAutor()
    testCartiPeCategoriiPreturi()