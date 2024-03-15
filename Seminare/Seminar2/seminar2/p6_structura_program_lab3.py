'''
Structura programului pentru Lab3.
'''


def program():
    '''
    Functia principala a programului.
    Date intrare: -
    Date iesire: -
    '''
    ruleaza = True
    while ruleaza == True:
        meniul_meu = meniu()
        print(meniul_meu)
        comanda = int(input("Introduceti comanda:"))
        if comanda == 1:
            lista_mea = citire_lista()
        elif comanda == 2:
            subsecventa1 = gaseste_subsecventa1(lista_mea)
            print(subsecventa1)
        elif comanda == 3:
            subsecventa2 = gaseste_subsecventa2(lista_mea)
            print(subsecventa2)
        elif comanda == 4:
            #iesim din program oprind executarea while-ului
            ruleaza = False


def meniu():
    '''
    Functie care construieste meniul si il returneaza.
    Date intrare: -
    Date iesire: meniu
    '''
    meniul_meu = ""
    meniul_meu = meniul_meu + "\n MENIU \n" #observati ca am folosit \n (inseamna sfarsit de linie (Enter) si ne va alinia meniul mai frumos)
    meniul_meu = meniul_meu + "1. Citire lista \n"
    meniul_meu = meniul_meu + "2. Verificare proprietate 1 \n"
    meniul_meu = meniul_meu + "3. Verificare proprietate 2 \n"
    meniul_meu = meniul_meu + "4. Iesire \n"
    return meniul_meu

def citire_lista():
    '''
    Functie care citeste o lista.
    Date intrare: -
    Date iesire: lista citita
    '''
    lista = [] #initializam lista cu o lista vida. Pe masura ce citim valori de la tastatura, le vom introduce in lista
    lungime_lista = int(input("Introduceti lungimea listei citite:"))
    for i in range(0, lungime_lista):
        element = int(input("Introduceti un element in lista:"))
        lista.append(element)
    return lista


def este_palindrom(numar):
    '''
    Functie care verifica daca numarul n dat este palindrom.
    Date intrare: numar (numarul pe care vrem sa il verificam)
    Date iesire: True, daca n e palindrom
                 False, altfel
    '''
    if numar == invers(numar):
        return True
    else:
        return False


def invers(numar):
    '''
    Functie care calculeaza inversul unui numar.
    Date intrare: numar (numarul caruia ii calculam inversul)
    Date iesire: inversul numarului
    '''
    invers_curent = 0
    while numar != 0:
        ultima_cifra = numar % 10
        invers_curent = invers_curent * 10 + ultima_cifra
        numar = numar//10
    return invers_curent


def numara_palindromuri_pe_lista(lista):
    '''
    Functie care numara cate din elementele listei date sunt palindromuri.
    Date intrare: lista
    Date iesire: numarul de palindromuri
    '''
    palindromuri = 0
    for i in range(0, len(lista)):
        if este_palindrom(lista[i]):
            palindromuri += 1
    return palindromuri


def gaseste_subsecventa1(lista_mea):
    '''
    Functie ce returneaza subsecventa de lungime maxima cu proprietatea ca numerele sunt palindromuri.
    Date intrare: lista_mea
    Date iesire: subsecventa de lungime maxima gasita
    '''
    lungime_maxima = 0
    lungime_curenta = 0
    for i in range(0, len(lista_mea)):
        if este_palindrom(lista_mea[i]):
            if lungime_curenta == 0:
                primul_element = i
            lungime_curenta += 1
        else:
            if lungime_curenta > lungime_maxima:
                lungime_maxima = lungime_curenta
                pozitie_intiala = primul_element
            lungime_curenta = 0

    if lungime_curenta > 0 and lungime_curenta > lungime_maxima:
        lungime_maxima = lungime_curenta
        pozitie_intiala = primul_element

    if lungime_maxima == 0:
        return []
    else:
        pozitie_finala = pozitie_intiala + lungime_maxima
        return lista_mea[pozitie_intiala: pozitie_finala]


def gaseste_subsecventa2(lista_mea):
    '''
    Functie ce returneaza subsecventa de lungime maxima cu proprietatea ca cel putin 2 din 3 numere consecutive sunt palindromuri.
    Date intrare: lista_mea
    Date iesire: subsecventa de lungime maxima gasita
    '''
    lungime_maxima = 0
    lungime_curenta = 0
    if len(lista_mea) < 3:
        return [] #daca lista e prea scurta, nu putem efectua verificarea si returnam o subsecventa vida
    else:
        for i in range(0, len(lista_mea)-2):#vom verifica intotdeauna numarul curent si urmatoarele 2 numere dupa el, de aceea parcurgem lista pana la lungime-3
            if numara_palindromuri_pe_lista(lista_mea[i:i+3]) >= 2:
                if lungime_curenta == 0:
                    primul_element = i
                lungime_curenta += 1
            else:
                if lungime_curenta > lungime_maxima:
                    lungime_maxima = lungime_curenta
                    pozitie_intiala = primul_element
                lungime_curenta = 0
        if lungime_curenta > 0 and lungime_curenta > lungime_maxima:
            lungime_maxima = lungime_curenta
            pozitie_intiala = primul_element

        if lungime_maxima == 0:
            return [] #daca nu gasim nicio subsecventa cu proprietatea dorita, returnam o subsecventa vida
        else:
            return lista_mea[pozitie_intiala : pozitie_intiala+lungime_maxima+2]

#Ca sa folosim functia, trebuie sa o apelam!
program()