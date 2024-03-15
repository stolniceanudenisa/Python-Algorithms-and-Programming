'''
Problema 3. Cititi o lista de la tastatura. Afisati cea mai lunga subsecventa formata din numere palindrom.
Ex.: daca lista = [1, 3, 45, 103, 11211, 13431, 3, 9, 100, 2, 44], cea mai lunga subsecventa este: 11211, 13431, 3, 9
'''

#Cum vom proceda?
#1. Parcurgem lista si cautam primul numar palindrom. Cand l-am gasit, retinem pozitia lui din lista intr-o variabila.
#2. Pentru fiecare palindrom gasit, crestem lungimea subsecventei curente.
#3. Cand am gasit un numar care nu mai e palindrom ne oprim si verificam daca lungimea subsecventei curente este mai mare decat lungimea subsecventei maxime de pana acum.
#4. Daca este mai mare, lungimea subsecventei maxime primeste valoarea lungimii subsecventei curente.
#5. De asemenea, stocam si pozitia primului numar din subsecventa (cea pe care am retinut-o la punctul 2.) intr-o variabila.

#Vom folosi functiile citire_lista (seminar2/p4_citire_lista.py) si este_palindrom (seminar2/p1_functie_palindrom.py) scrise anterior


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


def gaseste_subsecventa1(lista_mea):
    '''
    Functie ce returneaza subsecventa de lungime maxima cu proprietatea ca numerele sunt palindromuri.
    Date intrare: lista_mea
    Date iesire: subsecventa de lungime maxima gasita
    '''

    lungime_maxima = 0  # la inceput, lungimea maxima a secventei de palindromuri este 0
    lungime_curenta = 0  # la fel e si lungimea secventei curente de palindromuri
    for i in range(0, len(lista_mea)):  # 1. Parcurgem lista si cautam primul numar palindrom. Cand l-am gasit, retinem pozitia lui din lista intr-o variabila.
        if este_palindrom(lista_mea[i]):
            if lungime_curenta == 0:  # daca acesta este primul element din secventa (secventa curenta avea pana acum lungime 0) retinem pozitia lui
                primul_element = i
            lungime_curenta += 1  # 2. Pentru fiecare palindrom gasit, crestem lungimea subsecventei curente.
        else:  # 3. Cand am gasit un numar care nu e palindrom ne oprim si verificam daca lungimea subsecventei curente este mai mare decat lungimea subsecventei maxime de pana acum.
            if lungime_curenta > lungime_maxima:
                lungime_maxima = lungime_curenta  # 4. Daca este mai mare, lungimea subsecventei maxime primeste valoarea lungimii subsecventei curente.
                pozitie_intiala = primul_element  # 5. De asemenea, stocam si pozitia primului numar din subsecventa (cea pe care am retinut-o la punctul 2.) intr-o noua variabila.
            lungime_curenta = 0  # reinitializam lungimea curenta cu 0 ca sa putem repeta pasii in cazul in care mai gasim subsecvente de palindromuri in lista

    # observati ca ne oprim din cresterea lungimii secventei atunci cand gasim un element nonpalindrom
    # dar e posibil ca subsecventa maxima sa nu mai fie urmata de un element nonpalindrom (de exemplu, daca e ultima subsecventa din lista)
    # trebuie sa tratam si acest caz, ca sa salvam in variabilele care ne descriu subsecventa maxima (pozitie_initiala si lungime_maxima) valorile obtinute

    # daca la finalul parcurgerii listei eram intr-o subsecventa de palindromuri lungime_curenta este > 0
    # si daca valoarea lungime_curenta > lungime_maxima inseamna ca ultima subsecventa e cea mai lunga si trebuie sa o retinem
    if lungime_curenta > 0 and lungime_curenta > lungime_maxima:
        lungime_maxima = lungime_curenta
        pozitie_intiala = primul_element

    if lungime_maxima == 0:
        return []
    else:
        # Acum, variabila pozitie_initiala are valoarea pozitiei de pe care incepe secventa de lungime maxima
        # Iar variabila lungime_maxima are valoarea lungimii subsecventei maxime
        # Vrem sa tiparim subsecventa maxima din lista, deci ne folosim de valorile acestea
        # Valoarea pozitiei finale este pozitia_initiala + lungime_maxima - 1
        # Returnam sublista dintre pozitia initiala si pozitia finala ca in fisierul seminar2/introducere_liste.py
        pozitie_finala = pozitie_intiala + lungime_maxima
        return lista_mea[pozitie_intiala: pozitie_finala]#se va returna sublista care merge pana la pozitie_finala-1


#Apelam functiile
lista_mea = citire_lista()
solutie = gaseste_subsecventa1(lista_mea)
print("Cea mai lunga subsecventa a listei care contine doar palindromuri este: ",solutie)
