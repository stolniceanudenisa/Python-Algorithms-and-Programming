# domeniu ----------------------------
def creeazaCarte(cod, titlu, autor, pret):
    '''
    creeaza un dictionar de tipul carte
    :param cod: nr. intreg
    :param titlu: string
    :param autor: string
    :param pret: float
    :return: un dicitonar de tipul carte
    '''
    return {
        "cod": cod,
        "titlu": titlu,
        "autor": autor,
        "pret": pret
    }

def getCod(carte):
    return carte["cod"]

def getTitlu(carte):
    return carte["titlu"]

def getAutor(carte):
    return carte["autor"]

def getPret(carte):
    return carte["pret"]

def setCod(carte, cod):
    carte["cod"] = cod

def setTitlu(carte, titlu):
    carte["titlu"] = titlu

def setAutor(carte, autor):
    carte["autor"] = autor

def setPret(carte, pret):
    carte["pret"] = pret

def toString(carte):
    return "Cod: " + str(getCod(carte)) + ", titlu: " + getTitlu(carte) + \
           ", autor: " + getAutor(carte) + ", pret: " + str(getPret(carte))

# operatii ------------------
def adaugaCarte(cod, titlu, autor, pret, listaCarti):
    '''
    adauga o carte in lista
    :param cod: nr. intreg
    :param titlu: stirng
    :param autor: string
    :param pret: float
    :param listaCarti: lista de dictionare de tipul carte
    :return:
    '''
    carte = creeazaCarte(cod, titlu, autor, pret)
    listaCarti.append(carte)

def modificaCarte(cod, titluNou, autorNou, pretNou, listaCarti):
    '''
    modifica o carte dupa cod
    :param cod: nr. intreg
    :param titluNou: string
    :param autorNou: string
    :param pretNou: float
    :param listaCarti: lista de dictionare de tip carte
    :return: 
    '''
    for carte in listaCarti:
        if getCod(carte) == cod:
            setTitlu(carte, titluNou)
            setAutor(carte, autorNou)
            setPret(carte, pretNou)

def stergeCarte(cod, listaCarti):
    '''
    sterge o carte dupa cod
    :param cod: nr. intreg
    :param listaCarti: lista de dictionare de tipul carte
    :return:
    '''
    for carte in listaCarti:
        if getCod(carte) == cod:
            listaCarti.remove(carte)

def stergeCartiDupaAutor(autor, listaCarti):
    i = 0
    while i < len(listaCarti):
        if getAutor(listaCarti[i]) == autor:
            listaCarti.pop(i)
            i = i - 1
        i += 1

def cartiInIntervalPret(pretMin, pretMax, listaCarti):
    '''
    gaseste cartile cuprinse intr-un interval de pret dat
    :param pretMin: float
    :param pretMax: float
    :param listaCarti: lista de dictionare de tip carte
    :return: lista de dictionare de tip carte
    '''
    rezultat = []
    for carte in listaCarti:
        if pretMin < getPret(carte) < pretMax:
            rezultat.append(carte)
    return rezultat

def sumePreturiPerAutor(listaCarti):
    '''
    calculeaza suma peturilor cartilor fiecarui autor
    :param listaCarti: lista de dictionare de tipul carte
    :return: un dicitonar, continand drept chei numele autorilor
             si drept valori suma preturilor cartilor lor
    '''
    rezultat = {}
    for carte in listaCarti:
        autor = getAutor(carte)
        pret = getPret(carte)
        if autor in rezultat:
            rezultat[autor] += pret
        else:
            rezultat[autor] = pret
    return rezultat

# UI
def printMenu():
    print("1. Adauga carte")
    print("2. Modifica carte")
    print("3. Sterge carte")
    print("4. Sterge toate cartile unui autor")
    print("5. Afiseaza cartile cuprinse intr-un interval de pret")
    print("6. Afiseaza suma preturilor cartilor fiecarui autor")
    print("a. Afiseaza carti")
    print("x. Iesire")

def printCarti(listaCarti):
    for carte in listaCarti:
        print(toString(carte))

def uiAdaugaCarte(listaCarti):
    cod = int(input("Dati codul numeric al cartii (unic): "))
    titlu = input("Dati titlul cartii: ")
    autor = input("Dati autorul cartii: ")
    pret = float(input("Dati pretul cartii: "))
    adaugaCarte(cod, titlu, autor, pret, listaCarti)

def uiModificaCarte(listaCarti):
    cod = int(input("Dati codul numeric al cartii de modificat: "))
    titlu = input("Dati noul titl al cartii: ")
    autor = input("Dati noul autorul al cartii: ")
    pret = float(input("Dati noul pret al cartii: "))
    modificaCarte(cod, titlu, autor, pret, listaCarti)

def uiStergeCarte(listaCarti):
    cod = int(input("Dati codul cartii de sters: "))
    stergeCarte(cod, listaCarti)

def uiStergeCartiDupaAutor(listaCarti):
    autor = input("Dati autorul caruia vreti sa ii stergeti cartile: ")
    stergeCartiDupaAutor(autor, listaCarti)

def uiCartiInIntervalPret(listaCarti):
    pretMin = float(input("Dati pretul minim: "))
    pretMax = float(input("Dati pretul maxim: "))
    return cartiInIntervalPret(pretMin, pretMax, listaCarti)

# teste ----------------

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

def testAll():
    testCreeazaCarte()
    testSetteri()
    testAdaugaCarte()
    testModificaCarte()
    testStergeCarte()
    testCartiInIntervalPret()
    testSumaPreturiPerAutor()

def main():
    testAll()
    listaCarti = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            uiAdaugaCarte(listaCarti)
        elif optiune == "2":
            uiModificaCarte(listaCarti)
        elif optiune == "3":
            uiStergeCarte(listaCarti)
        elif optiune == "4":
            uiStergeCartiDupaAutor(listaCarti)
        elif optiune == "5":
            printCarti(uiCartiInIntervalPret(listaCarti))
        elif optiune == "6":
            print(sumePreturiPerAutor(listaCarti))
        elif optiune == "a":
            printCarti(listaCarti)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")

main()
