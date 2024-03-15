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