def show_menu():
    print("1. Citire numere din lista ")
    print("2. Afisare secventa in care in oricare trei elemente consecutive exista o valoare care se repeta.")
    print("3. Afisare secventa in care diferentele (x[j+1] - x[j]) si (x[j+2] - x[j+1]) au semne contrare.")
    print("x. Iesire")


def read_list1():
    l = []
    linie = input("Dati numerele din lista, separate printr-un spatiu: ")
    numere = linie.split(" ")
    for nr in numere:
        l.append(int(nr))
    return l


def read_list2():
    l = []
    n = int(input("Dati numarul de elemente al listei: "))
    for i in range(n):
        l = l + [int(input("Dati elementele din lista: "))]
    return l


def sir_crescator(lst):
    '''
    Verifica daca un sir este crescator.
    :param: lst - Lista de numere
    :return: True daca sirul este crescator, fals in caz contrar.
    '''
    for i in range(len(lst)-1):
        if lst[i+1] < lst[i]:
            return False
    return True


def sir_descrescator(lst):
    '''
    Verifica daca un sir este descrescator.
    :param: lst - Lista de numere
    :return: True daca sirul este descrescator, fals in caz contrar.
    '''
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            return False
    return True


def semnElement(x):
    '''
    Determina semnul unui element.
    :param x:
    :return: true semnul +, false semnul -
    '''
    if x < 0:
        return True
    else:
        return False


def egale(x, y):
    """
    Determina daca doua elemente sunt egale.
    :param Cele doua elemente:
    :return True daca elementele sunt egale, False in caz contrar:
    """
    if x == y:
        return True
    return False


def verifegale(lst):
    """
    Determina daca numerele din lista au valori egale 3 cate 3
    :param lst:
    :return True sau False:
    """
    if len(lst) > 1:
        for i in range(0, len(lst) - 2):
            if egale(lst[i],lst[i+1]) == egale(lst[i+1],lst[i+2]) == egale(lst[i],lst[i+2]):
                return False
    return True


def totegal(lst):
    if len(lst) > 1:
        for i in range(0, len(lst)):
            if lst[0] != lst[i]:
                return False
    return True


def cea_mai_lunga_nr_consec(lst):
    """
    Determina cea mai lunga subsecventa de numere in care in oricare trei elemente consecutive exista o valoare care se repeta.
    :param lst - lista de numere:
    :return lista cu cea mai lunga subsecventa cu proprietatea ceruta:
    """
    subsecventaMax2 = []
    if sir_crescator(lst) == True or  sir_descrescator(lst) == True:
        return subsecventaMax2
    for i in range(len(lst)):
        for j in range(len(lst)):
            if verifegale(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax2):
                subsecventaMax2 = lst[i:j + 1]
    return subsecventaMax2


def test_toate_semnele_egale():
    assert cea_mai_lunga_nr_consec([1, 2, 3, 4, 5, 6]) == []
    assert cea_mai_lunga_nr_consec([1, 2, 2, 3, 5, 6, 7, 8, 2, 2, 3]) == [1, 2, 2, 3]
    assert cea_mai_lunga_nr_consec([20, 19, 13, 5, 4, 2, 0]) == []
    assert cea_mai_lunga_nr_consec([3, 4, 3, 3, 5, 3, 6, 7]) == [3, 4, 3, 3, 5, 3]
    assert cea_mai_lunga_nr_consec([2, 4, 5, 3, 3, 4, 3, 3, 2, 3, 3, 3, 3, 8, 9]) == [5, 3, 3, 4, 3, 3, 2, 3, 3]


def toateSemneleAlternante(lst):
    """
    Determina daca numerele din lista au semnul alternant sau nu
    :param lst:
    :return True sau False:
    """
    if len(lst) > 1:
        for i in range(0, len(lst) - 2):
            if semnElement(lst[i+1]-lst[i]) == semnElement(lst[i + 2]-lst[i+1]):
                return False
    return True


def get_longest_alternating_signs(lst):
    """
    Determina cea mai lunga subsecventa de numere a caror diferenta are semne alternante
    :param lst - lista de numere:
    :return lista cu cea mai lunga subsecventa de numere a caror diferenta are semne alternante:
    """
    subsecventaMax2 = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if toateSemneleAlternante(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax2):
                subsecventaMax2 = lst[i:j + 1]
    return subsecventaMax2


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([1, 3, 2, 7, 5]) == [1, 3, 2, 7, 5]
    assert get_longest_alternating_signs([8, 3, 10, 11, 12]) == [8, 3, 10]
    assert get_longest_alternating_signs([1, 4, 2, 8, 4, 5]) == [1, 4, 2, 8, 4, 5]
    assert get_longest_alternating_signs([4, 7, 5, 9, 2, 13, 4, 5, 6, 7]) == [4, 7, 5, 9, 2, 13, 4, 5]
    assert get_longest_alternating_signs([100, 45, 10, 11, 4, 22, 10, 16, 6, 12]) == [45, 10, 11, 4, 22, 10, 16, 6, 12]


def main():
    l = []
    while True:
        show_menu()
        optiune = input("Dati optiunea: ")
        if optiune == '1':
            l = read_list1()
        elif optiune == '2':
            if sir_crescator(l) == False:
                l2 = cea_mai_lunga_nr_consec(l)
                print('Afisare secventa in care exista o valoare care se repeta', l2[:])
            elif totegal(l) == True:
                print('Toate elementele din secventa sunt egale:', l[:])
            else:
                print('Elementele sunt ordonate crescator. Nu exista subsecventa ceruta. ')
        elif optiune == '3':
            if sir_crescator(l) == False:
                l2 = get_longest_alternating_signs(l)
                print('Afisare secventa in care diferentele au semne contrare', l2[:])
            elif totegal(l) == True:
                print('Toate elementele din secventa sunt egale:', l[0])
            else:
                print('Elementele sunt ordonate crescator. Nu exista subsecventa ceruta.')
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida.Reincercati.")


if __name__ == '__main__':
    test_toate_semnele_egale()
    test_get_longest_alternating_signs()
    main()
