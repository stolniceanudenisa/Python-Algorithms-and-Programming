from domeniu import creeazaCarte, getAutor, getPret, getTitlu, getCod, setTitlu, setAutor, setPret


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
    found = False
    for carte in listaCarti:
        if getCod(carte) == cod:
            listaCarti.remove(carte)
            found = True
    if not found:
        raise ValueError("Nu exista nicio carte cu codul " + str(cod))

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

def cautare(cheie, listaCarti):
    '''
    cauta cartile ce contin cheia in cel putin una din proprietatile sale
    :param cheie:string
    :param listaCarti: lista de dicitonare de tipul carte
    :return: lista de dicitonare de tipul carte
    '''
    rezultat = []
    for carte in listaCarti:
        if cheie in str(getCod(carte)) \
            or cheie in getTitlu(carte) \
            or cheie in getAutor(carte) \
            or cheie in str(getPret(carte)):
            rezultat.append(carte)
    return rezultat

def mediePreturiPerAutor(listaCarti):
    '''
    determina media preturilor cartilor fiecarui autor
    :param listaCarti: lista de dicitonare de tipul carte
    :return: lista de dictionare ce contin drept chei numele autorilor
        si drept valori media preturilor cartilor lor
    '''
    preturi = {}
    for carte in listaCarti:
        autor = getAutor(carte)
        if autor in preturi:
            sumaAnterioara = preturi[autor][0]
            nrAnterior = preturi[autor][1]
            preturi[autor] = (sumaAnterioara + getPret(carte), nrAnterior + 1)
        else:
            preturi[autor] = (getPret(carte), 1)

    rezultat = {}
    for autor in preturi:
        rezultat[autor] = preturi[autor][0] / preturi[autor][1]
    return rezultat

def ceaMaiScumpaCartePerAutor(listaCarti):
    '''
    determina cea mai scumpa carte a fiecarui autor
    :param listaCarti: lista de dicitonare de tipul carte
    :return: un dictionar, continand drept chei numele autorilor
             si drept valori o carte
    '''
    rezultat = {}
    for carte in listaCarti:
        autor = getAutor(carte)
        pret = getPret(carte)
        if autor in rezultat:
            if pret > getPret(rezultat[autor]):
                rezultat[autor] = carte
        else:
            rezultat[autor] = carte
    return rezultat

def sortareDupaPretDesc(listaCarti):
    '''
    sorteaza cartile dupa pret, descrescator
    :param listaCarti: lista de dictionare de tipul carte
    :return:
    '''
    listaCarti.sort(key=lambda carte: getPret(carte),reverse=True)

def reducerePretDupaAutor(procent, autor, listaCarti):
    '''
    reduce pretul cartilor autorului dat cu un procent
    :param procent: numar intre 0 si 100
    :param autor: string
    :param listaCarti: lista de dictionare de tipul carte
    :return:
    '''
    if procent < 0 or procent > 100:
        raise ValueError("Procentul trebuie sa fie intre 0 si 100")
    for carte in listaCarti:
        if getAutor(carte) == autor:
            pretVechi = getPret(carte)
            pretNou = pretVechi - pretVechi*procent/100
            setPret(carte, pretNou)

def cartiPeCategoriiPreturi(listaCarti):
    '''
    grupeaza cartile dupa pret, din 50 in 50
    :param listaCarti: lista de dictionare de tipul carte
    :return: un dictionar avand drept chei limita inferioara a intervalului de pret
        (din 50 in 50) si drept valori o lista cu , cartile cuprinse in acel interval
    '''
    rezultat = {}
    for carte in listaCarti:
        limitaInferioaraInterval = 50*(getPret(carte)//50)
        if limitaInferioaraInterval in rezultat:
            rezultat[limitaInferioaraInterval].append(carte)
        else:
            rezultat[limitaInferioaraInterval] = [carte]
    return rezultat
