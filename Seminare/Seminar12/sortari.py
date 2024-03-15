def interclasare(A, pozitie_stanga, pozitie_delimitare, pozitie_dreapta):
    '''
    Functie ce interclaseaza in ordine crescatoare elementele din 2 subliste (tot crescatoare) ale unei liste date.
    Ex.: A = [1,2,3,10,0,2,5,6,8,10,12]
        pozitie_stanga = 0
        pozitie_delimitare = 3
        pozitie_dreapta = 10
        => A = [0,1,2,2,3,5,6,8,10,10,12]
    Daca notam len(A)=N, atunci si len(a1)+len(a2)=N, unde a1 si a2 sunt cele doua subsecvente ale listei A.
    Ambele subsecvente vor fi parcurse pana la capat.
    Asadar se vor efectua len(a1)+len(a2)= N pasi

    :param A: lista continand doua subliste ordonate crescator
    :return:
    '''
    #delimitam cele doua subliste ordonate crescator ale listei A, impartindu-le in doua liste: a1 si a2
    a1 = A[pozitie_stanga:pozitie_delimitare+1]
    a2 = A[pozitie_delimitare+1:pozitie_dreapta+1]

    i = 0 #cu i parcurgem prima sublista a listei A: pe a1
    j = 0 #cu j parcurgem a doua sublista a listei A: pe a2
    k = pozitie_stanga #cu k parcurgem lista A

    #se va iesi din acest while cand vom ajunge la capatul uneia dintre liste (a1 sau a2)
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            A[k] = a1[i]
            i = i + 1
        else:
            A[k] = a2[j]
            j = j + 1
        k = k + 1

    #chiar daca am terminat de executat while-ul, se poate ca in una din listele a1 sau a2 (nu stim in care)
    #sa mai fi ramas elemente. Trebuie sa le adaugam si pe ele:

    #daca atunci cand am terminat de parcurs lista a2 mai exista inca elemente in lista a1, le vom adauga in lista A
    while i < len(a1):
        A[k] = a1[i]
        i = i + 1
        k = k + 1

    #daca atunci cand am terminat de parcurs lista a1 mai exista inca elemente in lista a2, le vom adauga in lista A
    while j < len(a2):
        A[k] = a2[j]
        j = j + 1
        k = k + 1

A = [1,2,3,10,0,2,5,6,8,10,12]
print("Lista initiala este:", A)
interclasare(A, 0, 3, 10)
print("Dupa interclasare, lista devine:", A)


def bubble_sort(lista):
    '''
    Functie ce aplica metoda bulelor pentru a sorta o lista data.
    Aceasta metoda implica parcurgerea unei liste si compararea elementelor din ea, pe rand, doua cate doua.
    Daca doua elemente consecutive nu sunt ordonate crescator, atunci trebuie sa le interschimbam.
    Marcam faptul ca am gasit doua elemente care nu erau ordonate dand variabilei se_fac_schimbari valoarea True.
    In acest caz, procesul se va repeta.
    Atunci cand vom termina de parcurs lista fara ca sa mai fie nevoie sa interschimbam valori ordonate gresit
    (valoarea lui se_fac_schimbari ramane False) inseamna ca lista e ordonata si nu mai trebuie sa repetam procesul.

    Daca len(lista)=N:
    Observati ca chiar si in cel mai bun caz (in care lista este ordonata corect de la inceput si nu trebuie sa facem nicio interschimbare)
    lista tot va trebui sa fie parcursa o data ca sa verificam daca ordinea e corecta.
    Deci tot vom avea de parcurs N elemente = N pasi.

    In cel mai rau caz (de exemplu, cand lista e ordonata descrescator),
    va trebui sa facem: N-1 + N-2 + ... + 1 = N(N-1)/2 interschimbari.
    Lista va fi parcursa (prin intermediul for-ului) de fiecare data pana la sfarsit = N-1 pasi
    Iar aceasta parcurgere se va repeta de N ori (prin intermediul while-ului).
    Deci in cel mai rau caz vom avea N(N-1)/2 interschimbari si N(N-1) parcurgeri

    :param lista: lista pe care vrem sa o sortam
    :return:
    '''
    se_fac_schimbari = True
    while se_fac_schimbari == True:
        se_fac_schimbari = False
        for i in range(1, len(lista)):
            if lista[i-1] > lista[i]:
                variablia_auxiliara = lista[i-1]
                lista[i-1] = lista[i]
                lista[i] = variablia_auxiliara
                se_fac_schimbari = True

lista1 = [10,23,2,15,2,556,5,1]
print("\nLista initiala este:", lista1)
bubble_sort(lista1)
print("Dupa sortare prin metoda bulelor, lista devine:", lista1)


def insertion_sort(lista):
    '''
    Functie ce aplica sortarea prin insertie pentru a sorta o lista data.

    Daca len(lista)=N:
    In cel mai bun caz, lista e ordonata crescator si nu se intra niciodata in while, deci vom face N-1 pasi.
    In cel mai rau caz, se va intra in while pentru fiecare valoare a lui i din for, atunci cand lista e descrescatoare.
    Parcurgem indicii din lista de la 1 la N-1 (for-ul cu i):
    Pentru i = 1: while-ul se repeta o data.
    Apoi   i = 2: while-ul se repeta de 2 ori.
    ...
    Apoi   i = N-1: while-ul se repeta de N-1 ori.
    In total, repetarile vor avea loc de 1 + 2 + ... + N-1 = N*(N-1)/2 ori = N*(N-1)/2 pasi.

    :param lista: lista pe care vrem sa o sortam
    :return:
    '''
    for i in range(1, len(lista)):
        index = i-1
        urmatorul_element = lista[i]
        while index >= 0 and urmatorul_element < lista[index]:
            lista[index+1] = lista[index]
            index = index - 1
        lista[index+1] = urmatorul_element


lista2 = [10,23,2,15,2,556,5,1]
print("\nLista initiala este:", lista2)
insertion_sort(lista2)
print("Dupa sortare prin insertie, lista devine:", lista2)


def selection_sort(lista):
    '''
    Functie ce aplica metoda sortarii prin selectie pentru a sorta o lista data.

    Daca len(lista)=N:
    Parcurgem indicii din lista folosind i de la 0 la N-2 (in for-ul cu i).
    Pentru i = 0: for-ul cu j face (N-1) - (0+1) + 1  = N-1 pasi.
    Apoi   i = 1: for-ul de la j face (N-1) - (1+1) + 1 = N-2 pasi
    ...
    Apoi   i = N-2: for-ul de la j face (N-1) - (N-2+1) + 1 = 1 pas

    In total se vor face: N-1 + N-2 + ... + 1 = N(N-1)/2 pasi.

    :param lista: lista pe care vrem sa o sortam
    :return:
    '''
    for i in range(0, len(lista)-1):
        index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[index]:
                index = j
        if i < index:
            variabila_auxiliara = lista[i]
            lista[i] = lista[index]
            lista[index] = variabila_auxiliara

lista3 = [10,23,2,15,2,556,5,1]
print("\nLista initiala este:", lista3)
selection_sort(lista3)
print("Dupa sortare prin selectie, lista devine:", lista3)


def merge_sort(pozitie_stanga, pozitie_dreapta, lista):
    '''
    Functie ce sorteaza o lista prin metoda interclasarii.
    Impartim lista in 2 subliste (fiecare avand aproximativ jumatate din lungimea listei initiale)
    Cand sublistele pe care le-am tot despartit ajung sa aiba lungime=1 (adica un singur element),
    interclasam valorile din aceste subliste pe rand, 2 cate 2.
    La final vom avea lista sortata.

    Daca len(lista)=N:
    La fiecare pas, lista se va imparti in doua liste de lungime N/2 pana cand vom avea N liste de lungime 1.
    Impartirea unei liste in jumatate la fiecare pas presupune log2(N) pasi.
    Pentru ca aceasta impartire (log2(N) pasi) a unei listei in subliste se face de N ori,
    pana cand fiecare sublista are lungime=1, algoritmul merge_sort vom efectua N*log2(N) pasi.

    :param pozitie_stanga:
    :param pozitie_dreapta:
    :param lista:
    :return:
    '''
    if pozitie_stanga < pozitie_dreapta:
        mijloc = (pozitie_stanga + pozitie_dreapta) // 2
        merge_sort(pozitie_stanga, mijloc, lista)
        merge_sort(mijloc+1, pozitie_dreapta, lista)
        interclasare(lista, pozitie_stanga, mijloc, pozitie_dreapta)


lista4 = [10,23,2,15,2,556,5,1]
print("\nLista initiala este:", lista4)
pozitie_stanga = 0
pozitie_dreapta = len(lista4)-1
merge_sort(pozitie_stanga, pozitie_dreapta, lista4)
print("Dupa sortare prin interclasare, lista devine:", lista4)



def quick_sort(pozitie_stanga, pozitie_dreapta, lista):
    '''
    Functie ce sorteaza rapid o lista data.
    Observati ca quick_sort este o functie recursiva care la fiecare pas imparte lista in doua subliste
    pe care le ordoneaza.
    Ideea principala a quick_sort este ca initial ne vom alege un element (pentru noi e lista[i]) care, dupa ce trecem
    prin interschimbarile din while, se va afla pe pozitia corecta in lista noastra. Acest element se numeste pivot.
    Tinem minte, dupa while DOAR pivotul e pe pozitia corecta in lista, NU si elementele din stanga si din dreapta lui!
    Apoi, folosindu-ne de pozitia acestui pivot, vom imparti lista in cele doua subliste si le vom ordona la fel.
    Aici este apelul recursiv.

    Daca len(lista)=N:
    De obicei, lista se va imparti de fiecare data in doua subliste aproximativ egale.
    Impartirea listei va fi asemanatoare cu impartirea listei la merge_sort.
    In total se vor realiza aproximativ N*log2(N) pasi.

    In cel mai rau caz (care este, in mod, paradoxal, atunci cand lista este ordonata crescator (corect) de la inceput),
    pivotul va fi primul element din lista. Cum lista se imparte in doua subliste in jurul pivotului, in acest caz
    lista noastra se va imparti intr-o lista de lungime N-1 si o lista goala. Deci la fiecare pas, lungimea listei
    pe care lucram NU se va injumatati, ci doar va scadea cu 1.
    Asta inseamna, ca pentru o lista de lungime N vom efectua N + N-1 + N-2 + ... + 1 = N(N+1)/2 pasi.

    :param pozitie_stanga:
    :param pozitie_dreapta:
    :param lista:
    :return:
    '''
    i = pozitie_stanga
    j = pozitie_dreapta
    pivot = lista[i] #pivotul, care va fi pe pozitia corecta in lista la finalul executarii while-ului
    while i != j:
        while i < j and lista[j] >= pivot:
            j = j - 1
        lista[i] = lista[j]
        while i < j and lista[i] <= pivot:
            i = i + 1
        lista[j] = lista[i]
    lista[i] = pivot
    if pozitie_stanga < i-1:
        quick_sort(pozitie_stanga, i-1, lista)
    if i+1 < pozitie_dreapta:
        quick_sort(i+1, pozitie_dreapta, lista)

lista5 = [10,23,2,15,2,556,5,1]
print("\nLista initiala este:", lista5)
pozitie_stanga = 0
pozitie_dreapta = len(lista5)-1
quick_sort(pozitie_stanga, pozitie_dreapta, lista5)
print("Dupa sortare rapida, lista devine:", lista5)

