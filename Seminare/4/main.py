# domeniu ------------------------

def creeazaCarte(cod, titlu, autor, pret):
    '''
    creaza un dicitonar de tipul carte
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
    return "cod: " + str(getCod(carte)) + ", titlu: " + getTitlu(carte) + \
        ", autor: " + getAutor(carte) + ", pret: " + str(getPret(carte))

# operatii ---------------
def adaugaCarte(cod, titlu, autor, pret, listaCarti):
    '''
    adauga o carte intr-o lista de carti
    :param cod: nr. intreg
    :param titlu: string
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
    :param listaCarti: lista de carti
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
            i -= 1
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

def sumaPreturiPerAutor(listaCarti):
    '''
    determina suma preturilor cartilor fiecarui autor
    :param listaCarti: lista de dicitonare de tip carte
    :return: un dicitonar continand drept chei numele autorilor
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

def cautare(cheie, listaCarti):
    '''
    cauta cartile care contin in proprietatile lor o cheie de cautare
    :param cheie: string
    :param listaCarti: lista de dictionare de tipul carte
    :return: lista de dictionare de tipul carte
    '''
    rezultat = []
    for carte in listaCarti:
        if cheie in str(getCod(carte)) \
            or cheie in getTitlu(carte)\
            or cheie in getAutor(carte)\
            or cheie in str(getPret(carte)):
            rezultat.append(carte)
    return rezultat

def mediePreturiPerAutor(listaCarti):
    '''
    calculeaza media preturilor cartilor fiecarui autor
    :param listaCarti: lista de dictionare de tipul carte
    :return: un dictionar avand drept chei numele autorilor
        si drept valori media aritmetica a preturilor cartilor lor
    '''
    preturi = {}
    for carte in listaCarti:
        autor = getAutor(carte)
        pret = getPret(carte)
        if autor in preturi:
            sumaAnterioara = preturi[autor][0]
            nrAnterior = preturi[autor][1]
            preturi[autor] = (sumaAnterioara + pret, nrAnterior + 1)
        else:
            preturi[autor] = (pret, 1)
    rezultat = {}
    for autor in preturi:
        rezultat[autor] = preturi[autor][0] / preturi[autor][1]
    return rezultat

def ceaMaiScumpaPerAutor(listaCarti):
    '''
    determina cea mai scumpa carte a fiecarui autor
    :param listaCarti: lista de dictionare de tipul carte
    :return: un dictionar avand drept chei numele autorilor
        si drept valori cele mai scumpe carti ale lor
    '''
    rezultat = {}
    for carte in listaCarti:
        autor = getAutor(carte)
        if autor in rezultat:
            pretMax = getPret(rezultat[autor])
            if getPret(carte) > pretMax:
                rezultat[autor] = carte
        else:
            rezultat[autor] = carte
    return rezultat

# ui
def printMenu():
    print("adauga {cod},{titlu},{autor},{pret}")
    print("modifica {cod},{titluNou},{autorNou},{pretNou}")
    print("sterge {cod}")
    print("sterge_autor {autor}")
    print("interval_pret {pretMin}, {pretMax}")
    print("suma_preturi_per_autor")
    print("cautare {cheie}")
    print("medie_preturi_per_autor")
    print("cea_mai_scumpa_per_autor")
    print("afiseaza")
    print("iesire")

def uiAdaugaCarte(listaCarti, comanda):
    try:
        parametri = comanda.split()[1]
        cod = int(parametri.split(',')[0])
        titlu = parametri.split(',')[1]
        autor = parametri.split(',')[2]
        pret = float(parametri.split(',')[3])
        adaugaCarte(cod, titlu, autor, pret, listaCarti)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)

def uiModificaCarte(listaCarti, comanda):
    try:
        parametri = comanda.split()[1]
        cod = int(parametri.split(',')[0])
        titluNou = parametri.split(',')[1]
        autorNou = parametri.split(',')[2]
        pretNou = float(parametri.split(',')[3])
        modificaCarte(cod, titluNou, autorNou, pretNou, listaCarti)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)

def uiStergeCarte(listaCarti, comanda):
    try:
        cod = int(comanda.split()[1])
        stergeCarte(cod, listaCarti)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)

def uiStergeCartiDupaAutor(listaCarti, comanda):
    try:
        autor = comanda.split()[1]
        stergeCartiDupaAutor(autor, listaCarti)
    except IndexError as e:
        print(e)

def uiCartiInIntervalPret(listaCarti, comanda):
    try:
        parametri = comanda.split()[1]
        pretMin = float(parametri.split(',')[0])
        pretMax = float(parametri.split(',')[1])
        return cartiInIntervalPret(pretMin, pretMax, listaCarti)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)

def uiCautare(listaCarti, comanda):
    try:
        cheie = comanda.split()[1]
        return cautare(cheie, listaCarti)
    except IndexError as e:
        print(e)

def printCarti(listaCarti):
    for carte in listaCarti:
        print(toString(carte))

# teste
def testCreeazaCarte():
    carte = creeazaCarte(1, "ana", "bogdan", 23.6)

    assert(getCod(carte) == 1)
    assert(getTitlu(carte) == "ana")
    assert(getAutor(carte) == "bogdan")
    assert(getPret(carte) == 23.6)

def testAdaugaCarte():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 23.6, listaCarti)
    adaugaCarte(2, "ion", "pop", 21.1, listaCarti)

    assert len(listaCarti) == 2
    assert(getCod(listaCarti[0]) == 1)
    assert(getTitlu(listaCarti[0]) == "ana")
    assert(getAutor(listaCarti[0]) == "bogdan")
    assert(getPret(listaCarti[0]) == 23.6)
    assert(getCod(listaCarti[1]) == 2)
    assert(getTitlu(listaCarti[1]) == "ion")
    assert(getAutor(listaCarti[1]) == "pop")
    assert(getPret(listaCarti[1]) == 21.1)

def testModificaCarte():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 23.6, listaCarti)
    adaugaCarte(2, "ion", "pop", 21.1, listaCarti)

    modificaCarte(1, "luci", "popescu", 19.9, listaCarti)

    assert len(listaCarti) == 2
    assert len(listaCarti) == 2
    assert (getCod(listaCarti[0]) == 1)
    assert (getTitlu(listaCarti[0]) == "luci")
    assert (getAutor(listaCarti[0]) == "popescu")
    assert (getPret(listaCarti[0]) == 19.9)
    assert (getCod(listaCarti[1]) == 2)
    assert (getTitlu(listaCarti[1]) == "ion")
    assert (getAutor(listaCarti[1]) == "pop")
    assert (getPret(listaCarti[1]) == 21.1)

def testStergeCarte():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 23.6, listaCarti)
    adaugaCarte(2, "ion", "pop", 21.1, listaCarti)

    stergeCarte(2, listaCarti)

    assert len(listaCarti) == 1
    assert getCod(listaCarti[0]) == 1

def testCartiInIntervalPret():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 23.6, listaCarti)
    adaugaCarte(2, "ion", "pop", 21.1, listaCarti)
    adaugaCarte(3, "ion", "pop", 24.9, listaCarti)

    rezultat = cartiInIntervalPret(22.5, 25.5, listaCarti)

    assert(len(rezultat) == 2)
    assert(getCod(rezultat[0]) == 1)
    assert (getCod(rezultat[1]) == 3)

def testSumaPreturiPerAutor():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 23.6, listaCarti)
    adaugaCarte(2, "ion", "pop", 21.1, listaCarti)
    adaugaCarte(3, "ion", "pop", 24.9, listaCarti)

    rezultat = sumaPreturiPerAutor(listaCarti)
    assert len(rezultat) == 2
    assert rezultat["bogdan"] == 23.6
    assert rezultat["pop"] == 46.0

def testCautare():
    listaCarti = []
    adaugaCarte(11, "ana", "bogdan", 23.6, listaCarti)
    adaugaCarte(1, "ana", "bogdan", 23.6, listaCarti)
    adaugaCarte(2, "ion111", "pop", 21.1, listaCarti)
    adaugaCarte(3, "ion", "p11op", 24.9, listaCarti)
    adaugaCarte(4, "ion", "pop", 24111.9, listaCarti)

    rezultat = cautare("11", listaCarti)

    assert len(rezultat) == 4
    assert getCod(rezultat[0]) == 11
    assert getCod(rezultat[1]) == 2
    assert getCod(rezultat[2]) == 3
    assert getCod(rezultat[3]) == 4

def testMediePreturiPerAutor():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 14.0, listaCarti)
    adaugaCarte(2, "ion", "pop", 20.0, listaCarti)
    adaugaCarte(3, "ion", "pop", 10.0, listaCarti)

    rezultat = mediePreturiPerAutor(listaCarti)

    assert len(rezultat) == 2
    assert rezultat["bogdan"] == 14.0
    assert rezultat['pop'] == 15.0

def testCeaMaiScumpaPerAutor():
    listaCarti = []
    adaugaCarte(1, "ana", "bogdan", 14.0, listaCarti)
    adaugaCarte(2, "ion", "pop", 20.0, listaCarti)
    adaugaCarte(3, "ion", "pop", 10.0, listaCarti)

    rezultat = ceaMaiScumpaPerAutor(listaCarti)

    assert len(rezultat) == 2
    assert getCod(rezultat["bogdan"]) == 1
    assert getPret(rezultat["bogdan"]) == 14.0
    assert getCod(rezultat["pop"]) == 2
    assert getPret(rezultat["pop"]) == 20.0

def testAll():
    testCreeazaCarte()
    testAdaugaCarte()
    testModificaCarte()
    testStergeCarte()
    testCartiInIntervalPret()
    testSumaPreturiPerAutor()
    testCautare()
    testMediePreturiPerAutor()
    testCeaMaiScumpaPerAutor()

def main():
    testAll()
    listaCarti = []
    while True:
        printMenu()
        comanda = input("Dati comanda: ")
        operatiune = comanda.split()[0]
        if operatiune == "adauga":
            uiAdaugaCarte(listaCarti, comanda)
        elif operatiune == "modifica":
            uiModificaCarte(listaCarti, comanda)
        elif operatiune == "sterge":
            uiStergeCarte(listaCarti, comanda)
        elif operatiune == "sterge_autor":
            uiStergeCartiDupaAutor(listaCarti, comanda)
        elif operatiune == "interval_pret":
            printCarti(uiCartiInIntervalPret(listaCarti, comanda))
        elif operatiune == "suma_preturi_per_autor":
            print(sumaPreturiPerAutor(listaCarti))
        elif operatiune == "cautare":
            printCarti(uiCautare(listaCarti, comanda))
        elif operatiune == "medie_preturi_per_autor":
            print(mediePreturiPerAutor(listaCarti))
        elif operatiune == "cea_mai_scumpa_per_autor":
            print(ceaMaiScumpaPerAutor(listaCarti))
        elif operatiune == "afiseaza":
            printCarti(listaCarti)
        elif operatiune == "iesire":
            break
        else: print("Comanda gresita, reincercati")


main()