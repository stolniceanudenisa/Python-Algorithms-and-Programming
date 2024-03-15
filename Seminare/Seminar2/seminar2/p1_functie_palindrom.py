'''
Recapitulare functii.
Functiile sunt explicate in acest proiect, in fisierul seminar1/functii.py
Recititi acel fisier pentru notiuni introductive.
'''

'''
Vrem sa rezolvam probleme folosind functii.

Problema 1. Scrieti o functie care verifica daca un numar n dat este palindrom. Testati aceasta functie.

Un numar este palindrom daca este egal cu inversul sau.
Ex. numere care SUNT palindrom: 121, 54845, 9889, 1001, 2, 55
Ex. numere care NU SUNT palindrom: 3231, 21, 345, 100, 64
'''

def este_palindrom(numar):
    '''
    Functie care verifica daca numarul n dat este palindrom.
    Date intrare: numar (numarul pe care vrem sa il verificam)
    Date iesire: True, daca n e palindrom
                 False, altfel
    '''
    if numar == invers(numar): #ne amintim ca o functie trebuie sa aiba O SINGURA RESPONSABILITATE, deci functia este_palindrom va verifica doar daca numarul e egal cu inversul sau. Inversul il vom calcula folosind o alta functie.
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


def test_este_palindrom():
    '''
    Functie care testeaza functia este_palindrom.
    Produce eroare de tip AssertionError daca testele esueaza.
    '''
    assert(este_palindrom(131) == True)
    assert(este_palindrom(14) != True)
    assert(este_palindrom(211) == False)
    assert(este_palindrom(8) != False)
    print("Functia este_palindrom a trecut toate testele!")


def test_invers():
    '''
    Functie care testeaza functia invers.
    Produce eroare de tip AssertionError daca testele esueaza.
    '''
    assert(invers(131) == 131)
    assert(invers(211) == 112)
    assert(invers(8) == 8)
    assert(invers(14) != 14)
    # daca facem o asertiune gresita (falsa), primim eroare si executia se opreste aici. Decomentati linia urmatoare si observati ce sa intampla
    #assert (invers(91) == 91)
    print("Functia invers a trecut toate testele!")


#Nu uitam, TREBUIE SA APELAM FUNCTIILE pentru a le folosi in program!
test_invers()
test_este_palindrom()