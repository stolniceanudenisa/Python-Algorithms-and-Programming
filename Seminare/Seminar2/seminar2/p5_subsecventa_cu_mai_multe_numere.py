'''
Problema 4. Cititi o lista de la tastatura. Afisati cea mai lunga subsecventa care respecta proprietatea ca intre oricare 3 numere consecutive, cel putin 2 sunt palindromuri.
Ex.: daca lista = [1, 3, 45, 103, 11211, 13431, 3, 9, 100, 2, 44], cea mai lunga subsecventa este: 103, 11211, 13431, 3, 9, 100, 2, 44
'''

#Implementam similar cu exercitiul precedent (din fisierul seminar2/p5_subsecventa_palindromuri.py)
#Vom folosi din nou functiile citire_lista si este_palindrom.
#Structura functiei gaseste_subsecventa va ramane la fel, doar ca in loc sa verificam proprietatea pe cate un numar din lista, il vom verifica pe cate 3.


def citire_lista():
    '''
    Functie care citeste o lista.
    Date intrare: -
    Date iesire: lista citita
    '''
    lista = []
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


#Apelam functiile
lista_mea = citire_lista()
solutie = gaseste_subsecventa2(lista_mea)
print("Cea mai lunga subsecventa a listei in care dintre 3 numere consecutive cel putin 2 sunt palindromuri este: ",solutie)