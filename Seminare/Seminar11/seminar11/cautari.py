def cautare_secventiala(L, element):
    '''
    Functie care cauta un element in lista. Returneaza pozitia lui.
    :param L: lista
    :param element: element cautat
    :return: pozitia elementului, daca el exista in lista; None, altfel
    '''
    for i in range(len(L)):
        element_curent = L[i]
        if element_curent == element:
            return i
    return None


def cautare_binara(pozitie_stanga, pozitie_dreapta, element, L):
    '''
    Functie de cautare al elementului dat intr-o lista ORDONATA CRESCATOR.
    Functia cautare_binara este recursiva si cauta elementul in urmatorul mod:
    Calculeaza pozitia din mijloc a listei si verifica daca elementul e =, < sau > decat elementul din mijlocul listei:
        -> daca elementul cautat e = cu elementul din mijlocul listei, am incheiat cautarea si il returnam

        -> daca elementul cautat e < decat elementul din mijlocul listei, pentru ca lista este ordonata crescator,
            stim cu siguranta ca elementul (daca exista in lista) se va afla pe o pozitie din intervalul [pozitie_stanga, mijloc]
            deci il cautam acolo, apeland recursiv functia cautare_binara, cu mijloc in loc de pozitie_dreapta

        -> daca elementul cautat e > decat elementul din mijlocul listei, pentru ca lista este ordonata crescator,
            stim cu siguranta ca elementul (daca exista in lista) se va afla pe o pozitie din intervalul [mijloc, pozitie_dreapta]
            deci il cautam acolo, apeland recursiv functia cautare_binara, cu mijloc in loc de pozitie_stanga
    Cautarea se termina cand elementul e gasit in lista (element == L[mijloc])
        sau cand pozitie_stanga > pozitie_dreapta (inseamna ca am parcurs lista si nu am gasit elementul)

    Model matematic recursiv:
    L = [el_1, ..., el_n]

                                                    |mijloc, daca element == L[mijloc]
    cautare_binara(stanga, dreapta, element, L) =   |cautare_binara(stanga, mijloc, element, L), daca element < L[mijloc]
                                                    |cautare_binara(mijloc, dreapta, element, L), daca element > L[mijloc]

    unde mijloc = (stanga+dreapta)//2

    :param pozitie_stanga: pozitia capatului stang al (sub)listei in care se face cautarea
    :param pozitie_dreapta: pozitia capatului drept al (sub)listei in care se face cautarea
    :param element: elementul cautat
    :param L: lista data
    :return: pozitia elementului, daca el exista in lista; None, altfel
    '''
    if pozitie_stanga >= pozitie_dreapta: #am epuizat cautarea si elementul nu a fost gasit
        return None
    mijloc = (pozitie_stanga + pozitie_dreapta) // 2 #pozitia din mijlocul (sub)listei in care facem cautarea
    if element == L[mijloc]:
        return mijloc #daca elementul se afla pe pozitia din mijloc, returnam pozitia lui
    #tinem minte ca lista este ordonata crescator (incepe cu cele mai mici elemente si se termina cu cele mai mari)
    if element < L[mijloc]: #daca element < elementul de pe pozitia din mijloc, va trebui sa il cautam in sublista [pozitie_stanga, ..., mijloc]
        return cautare_binara(pozitie_stanga, mijloc, element, L)
    if element > L[mijloc]: #daca element > elementul de pe pozitia din mijloc, va trebui sa il cautam in sublista [mijloc, ..., pozitie_dreapta]
        return cautare_binara(mijloc, pozitie_dreapta, element, L)


element = 10
L1 = [1,2,3,4,5,6,7,8,9,10]
pozitie = cautare_secventiala(L1, element)
print("Pozitia elementului", element, "in lista", L1, "este:", pozitie)

element2 = 4
L2 = [1,2,3,4,5,6,7,8,9,10]
pozitie2 = cautare_binara(0, len(L2)-1, element2, L2)
print("Pozitia elementului", element2, "in lista", L2, "este:", pozitie2)
