'''
Introducere recursivitate
'''
"""
O functie recursiva este o functie care se apeleaza pe ea insasi.
Pentru ca ea sa nu se apeleze la infinit, este important sa avem o conditie de oprire.

REGULI:

0. Nu citim/tiparim in functiile recursive.
1. Functiile recursive pe care le folosim vor returna intotdeauna o valoare.
2. Inainte sa scriem orice functie recursiva, scriem modelul matematic recursiv pentru ea.
3. Daca lucram cu liste, vom avea acces doar la inceputul listei L[0] si de acolo vom accesa si restul listei L[1:]
"""

def factorial(n):
    '''
    Functie ce calculeaza n! (n factorial)
    Model matematic recursiv:
                    |1, daca n == 0 sau n == 1
    factorial(n) =  |
                    |n * factorial(n-1), altfel
    :param n:
    :return: n!
    '''
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

n = 6
n_factorial = factorial(n)
print(n, "factorial este:",  n_factorial)

def cmmdc(a, b):
    '''
    Functie care calculeaza recursiv cel mai mare divizor comum al numerelor a si b
    Model matematic recursiv:
                     |a, daca a == b  <- aceasta este conditia de oprire: cand ne vom afla pe ramura aceasta nu vom mai apela functia cmmdc, deci recursivitatea se va opri
        cmmdc(a,b) = |cmmdc(a-b, b), daca a > b
                     |cmmdc(a, b-a), daca b > a

    :param a:
    :param b:
    :return:
    '''
    if a == b:
        return a
    if a > b:
        return cmmdc(a-b, b)
    if b > a:
        return cmmdc(a, b-a)

#apelam functia cmmdc(a,b) cu valori concrete pentru parametrii a si b
a = 8
b = 22
valoare = cmmdc(a,b)
print("CMMDC al numerelor", a, "si", b, "este:", valoare)


def fibonacci(pozitie):
    '''
    Functie ce returneaza numarul de pe o pozitie data din Sirul lui Fibonacci.

    Sirul lui Fibonacci incepe cu valorile 0 si 1, apoi continua prin formarea fiecarui element urmator ca suma celor doua elemente anterioare.
    ex. 0, 1, 1(este 0+1), 2(este 1+1), 3(este 1+2), 5(este 2+3), 8(este 3+5), 13(este 5+8), 21(este 8+13), 34(este 13+21), ...

    Observam ca avem nevoie de doua numere anterioare (doi pasi anteriori) pentru a calcula valoarea urmatorului numar din sir.

    Model matematic recursiv:
                         |0, daca pozitie == 1
    fibonacci(pozitie) = |1, daca pozitie == 2
                         |fibonacci(pozitie-2) + fibonacci(pozitie-1), altfel

    :param pozitie: pozitia numarului pe care vrem sa il returnam
    :return: numarul de pe pozitia data din sirul lui Fibonacci
    '''
    if pozitie == 1:
        return 0
    if pozitie == 2:
        return 1
    if pozitie > 2:
        return fibonacci(pozitie-2) + fibonacci(pozitie-1)

pozitie = 5
fib = fibonacci(pozitie)
print("Al", pozitie, "-lea numar din Sirul lui Fibonacci este:", fib)

def lungime_lista(L):
    '''
    Functie ce calculeaza recursiv lungimea unei liste.
    Model matematic recursiv:
        Se da lista L = [el_1, ..., el_n]
                                              |0, daca L == []
        lungime_lista( [el_1, ..., el_n] ) =  |
                                              |1 + lungime_lista( [el_2, ..., el_n] ), altfel

    :param lista_mea:
    :return: lungimea listei
    '''
    if len(L) == 0:
        return 0
    else:
        return 1 + lungime_lista(L[1:])

lista1 = [20,30,40,10]
lungime = lungime_lista(lista1)
print("Lungimea listei", lista1, "este:", lungime)


def suma_lista(L):
    '''
    Functie ce calculeaza recursiv suma elementelor unei liste.
    Model matematic recursiv:
        Se da lista L = [el_1, ..., el_n]
                                           |0, daca L == []
        suma_lista( [el_1, ..., el_n] ) =  |
                                           |el_1 + suma_lista( [el_2, ..., el_n] ), altfel

    :param L:
    :return: suma elementelor listei
    '''
    if len(L) == 0:
        return 0
    return L[0] + suma_lista(L[1:])

def produs_lista(L):
    '''
    Functie ce calculeaza recursiv produsul elementelor unei liste.
    Model matematic recursiv:
        Se da lista L = [el_1, ..., el_n]
                                             |0, daca L = []
        produs_lista( [el_1, ..., el_n] ) =  |el_1, daca L are un singur element
                                             |el_1 * produs_lista( [el_2, ..., el_n] ), altfel

    :param L:
    :return: produsul elementelor listei
    '''
    if len(L) == 0:
        return 0
    if len(L) == 1:
        return L[0]
    return L[0] * produs_lista(L[1:])

lista2 = [1,2,3,4,5]
suma = suma_lista(lista2)
print("Suma listei", lista2, "este:", suma)
produs = produs_lista(lista2)
print("Produsul listei", lista2, "este:", produs)


def minim_lista(L):
    '''
    Functie ce returneaza valoarea minima dintr-o lista data.
    Model matematic recursiv:
        Se da lista L = [el_1, ..., el_n]
                                            |None, daca L = []
        minim_lista( [el_1, ..., el_n] ) =  |el_1, daca L are un singur element
                                            |el_1, daca L are mai multe elemente si el_1 < decat minim_lista( [el_2, ..., el_n] )
                                            |minim_lista( [el_2, ..., el_n] ), altfel

    :param L:
    :return: valoarea minima din lista
    '''
    if len(L) == 0:
        return None
    if len(L) == 1:
        return L[0]
    if len(L) > 1:
        if L[0] < minim_lista(L[1:]):
            return L[0]
        else:
            return minim_lista(L[1:])

def maxim_lista(L):
    '''
    Functie ce returneaza valoarea maxima dintr-o lista data.
    Model matematic recursiv:
        Se da lista L = [el_1, ..., el_n]
                                            |None, daca L = []
        maxim_lista( [el_1, ..., el_n] ) =  |el_1, daca L are un singur element
                                            |el_1, daca L are mai multe elemente si el_1 > decat maxim_lista( [el_2, ..., el_n] )
                                            |maxim_lista( [el_2, ..., el_n] ), altfel

    :param L:
    :return: valoarea maxima din lista
    '''
    if len(L) == 0:
        return None
    if len(L) == 1:
        return L[0]
    if len(L) > 1:
        if L[0] > maxim_lista(L[1:]):
            return L[0]
        else:
            return maxim_lista(L[1:])


lista3 = [1,2,3,5,-9,10]
minim = minim_lista(lista3)
print("Minimul listei", lista3, "este:", minim)
maxim = maxim_lista(lista3)
print("Maximul listei", lista3, "este:", maxim)


def cmmdc_lista(L):
    '''
    Functie ce returneaza cel mai mare divizor comun al numerelor dintr-o lista data.
    Model matematic recursiv:
                                             |None, daca L == []
    cmmdc_lista( [el_1, el_2, ..., el_n] ) = |el_1, daca L are un singur element
                                             |cmmdc(el_1, el_2), daca L are doua elemente
                                             |cmmdc( el_1, cmmdc_lista( [el_2, ..., el_n] ) ), altfel
    :param L:
    :return:
    '''
    if len(L) == 0:
        return None
    if len(L) == 1:
        return L[0]
    if len(L) == 2:
        return cmmdc(L[0], L[1])
    return cmmdc(L[0], cmmdc_lista(L[1:]))

lista4 = [12,24,14,6,8]
cmmdc_lista4 = cmmdc_lista(lista4)
print("CMMDC al elementelor din lista", lista4, "este:", cmmdc_lista4)