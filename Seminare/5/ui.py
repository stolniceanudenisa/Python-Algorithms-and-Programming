from domeniu import toString
from operatii import adaugaCarte, modificaCarte, stergeCarte, stergeCartiDupaAutor, cartiInIntervalPret, cautare, \
    sumePreturiPerAutor, mediePreturiPerAutor, ceaMaiScumpaCartePerAutor, sortareDupaPretDesc, reducerePretDupaAutor, \
    cartiPeCategoriiPreturi


def printMenu():
    print("adauga {cod},{titlu},{autor},{pret}")
    print("modifica {cod},{titluNou},{autorNou},{pretNou}")
    print("sterge {cod}")
    print("sterge_autor {autor}")
    print("interval_pret {pretMin},{pretMax}")
    print("suma_preturi_per_autor")
    print("cautare {cheie}")
    print("medie_preturi_per_autor")
    print("cea_mai_scumpa_per_autor")
    print("sorteaza_pret_desc")
    print("reducere_pret {procent} (0-100), {autor}")
    print("interval_50")
    print("afiseaza")
    print("iesire")

def printCarti(listaCarti):
    for carte in listaCarti:
        print(toString(carte))

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
        titlu = parametri.split(',')[1]
        autor = parametri.split(',')[2]
        pret = parametri.split(',')[3]
        modificaCarte(cod, titlu, autor, pret, listaCarti)
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

def uiReducerePretDupaAutor(listaCarti, comanda):
    try:
        parametri = comanda.split()[1]
        procent =float(parametri.split(',')[0])
        autor = parametri.split(',')[1]
        reducerePretDupaAutor(procent, autor, listaCarti)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)

def uiCartiPeCategoriiPreturi(listaCarti):
    rezultat = cartiPeCategoriiPreturi(listaCarti)
    for interval in rezultat:
        print("Pentru intervalul [" + str(interval) + "-" + str(interval+50) + ") avem cartile:")
        printCarti(rezultat[interval])
        print()

def meniu():
    listaCarti = []
    while True:
        printMenu()
        comanda = input("Dati comanda: ")
        operatie = comanda.split()[0]
        if operatie == "adauga":
            uiAdaugaCarte(listaCarti, comanda)
        elif operatie == "modifica":
            uiModificaCarte(listaCarti, comanda)
        elif operatie == "sterge":
            uiStergeCarte(listaCarti, comanda)
        elif operatie == "sterge_autor":
            uiStergeCartiDupaAutor(listaCarti, comanda)
        elif operatie == "interval_pret":
            printCarti(uiCartiInIntervalPret(listaCarti, comanda))
        elif operatie == "suma_preturi_per_autor":
            print(sumePreturiPerAutor(listaCarti))
        elif operatie == "cautare":
            printCarti(uiCautare(listaCarti, comanda))
        elif operatie == "medie_preturi_per_autor":
            print(mediePreturiPerAutor(listaCarti))
        elif operatie == "cea_mai_scumpa_per_autor":
            print(ceaMaiScumpaCartePerAutor(listaCarti))
        elif operatie == "sorteaza_pret_desc":
            sortareDupaPretDesc(listaCarti)
        elif operatie == "reducere_pret":
            uiReducerePretDupaAutor(listaCarti, comanda)
        elif operatie == "interval_50":
            uiCartiPeCategoriiPreturi(listaCarti)
        elif operatie == "afiseaza":
            printCarti(listaCarti)
        elif operatie == "iesire":
            break
        else:
            print("Comanda gresita! Reincercati")