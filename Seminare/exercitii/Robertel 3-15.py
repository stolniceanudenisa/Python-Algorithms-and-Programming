import collections

def show_menu():
    print("1. Citire numere din lista ")
    print("2. Gasire secventa de lungime maximă ce contine cel mult trei valori distincte.")
    print("3. Gasire secventa de lungime maximă ce este de tip munte.")
    print("4. Iesire")


def read_list1():
    l = []
    linie = input("Dati numerele din lista, separate printr-un spatiu: ")
    numere = linie.split(",")
    for nr in numere:
        l.append(int(nr))
    return l


def read_list2():
    l = []
    n = int(input("Dati numarul de elemente al listei: "))
    for i in range(n):
        l = l + [int(input("Dati elementele din lista: "))]
    return l


def cea_mai_lunga_subsecventa_val_distincte1(l):
    '''
    Determina cea mai lunga subsecventa de numere ce contine cel mult trei valori distincte.
    :param l - lista de numere:
    :return lista cu cea mai lunga subsecventa de numere ce contine cel mult trei valori distincte:
    '''
    lmax = []
    c = 1
    nr = 0
    for i in range(len(l)):
        c = 1
        for j in range(i + 1, len(l)):

            if l[j - 1] == l[j]:
                c += 1
            elif l[j - 1] != l[j]:
                nr += 1
                c += 1
                if nr == 3:
                    # daca adaug un j=-1 si il adaug in l[i:j+1] imi ia 3,4,5
                    break
        if len(l[i:j]) > len(lmax):
            lmax = l[i:j]
        nr = 0
    return lmax




def longest(a, n, k):
    freq = collections.defaultdict(int)

    start = 0
    end = 0
    now = 0
    l = 0
    for i in range(n):
        freq[a[i]] += 1
        if (freq[a[i]] == 1):
            now += 1
        while (now > k):
            freq[a[l]] -= 1
            if (freq[a[l]] == 0):
                now -= 1
            l += 1
        if (i - l + 1 >= end - start + 1):
            end = i
            start = l
    for i in range(start, end + 1):
        print(a[i], end=" ")



def test_cea_mai_lunga_subsecventa_val_distincte():
    assert cea_mai_lunga_subsecventa_val_distincte([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3]
    assert cea_mai_lunga_subsecventa_val_distincte([1, 2, 3, 2, 1, 3, 4, 7, 8]) == [1, 2, 3, 2, 1, 3]
    assert cea_mai_lunga_subsecventa_val_distincte([2, 2, 2, 2, 2, 1, 4, 5, 6]) == [2, 2, 2, 2, 2, 1, 4]
    assert cea_mai_lunga_subsecventa_val_distincte([1, 2, 3, 3, 2, 1, 2, 1, 3]) == [1, 2, 3, 3, 2, 1, 2, 1, 3]
    assert cea_mai_lunga_subsecventa_val_distincte([1, 2, 3, 3, 2, 1, 2, 1, 3, 7, 8, 5]) == [1, 2, 3, 3]
    assert cea_mai_lunga_subsecventa_val_distincte([4, 4, 4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4, 4, 4]
    assert cea_mai_lunga_subsecventa_val_distincte([1, 1, 1, 1, 2, 2, 2, 2]) == [1, 1, 1, 1, 2, 2, 2, 2]
    assert cea_mai_lunga_subsecventa_val_distincte([1, 1, 1, 1, 2, 2, 2, 2, 7, 8, 9]) == [1, 1, 1, 1, 2, 2, 2, 2, 7]
    assert cea_mai_lunga_subsecventa_val_distincte([1,2,1,1,3,3,3,1,3,3,4]) == [1,2,1,1,3,3,3,1,3,3]


def sir_crescator(lst):
    '''
        Verifica daca un sir este crescator.
        :param: lst - Lista de numere
        :return: True daca sirul este crescator, fals in caz contrar.
    '''
    for i in range(len(lst)-1):
        if lst[i+1] <= lst[i]:
            return False
    return True


def sir_descrescator(lst):
    '''
    Verifica daca un sir este descrescator.
    :param: lst - Lista de numere
    :return: True daca sirul este descrescator, fals in caz contrar.
    '''
    for i in range(len(lst)-1):
        if lst[i] <= lst[i+1]:
            return False
    return True


def munte(lst):
    '''
    Determina daca un sir este de tip munte (valorile cresc pana la un moment dat si apoi descresc).
    :param lst - lista de numere:
    :return True daca sirul este de tip munte, False in caz contrar:
    '''
    p=0
    for j in range(len(lst)-1,0,-1):
        if sir_crescator(lst[:j])==True:
            p=j-1
            break
    if sir_descrescator(lst[p:len(lst)])==True and p!=0:
        return True
    return False


def cea_mai_lunga_subsecventa_munte(lst):
    """
    Determina cea mai lunga subsecventa de numere de tip munte
    :param lst - lista de numere:
    :return lista cu cea mai lunga subsecventa de tip munte:
    """
    subsecventaMax2 = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if munte(lst[i:j+1]) and len(lst[i:j+1])> len(subsecventaMax2):
                subsecventaMax2 = lst[i:j+1]
    return subsecventaMax2


def test_cea_mai_lunga_subsecventa_munte():
    assert cea_mai_lunga_subsecventa_munte([1, 2, 3, 2, 1, 7, 8, 8, 9]) == [1, 2, 3, 2, 1]
    assert cea_mai_lunga_subsecventa_munte([1, 2, 3, 4, 5]) == []
    assert cea_mai_lunga_subsecventa_munte([5, 4, 3, 2, 1]) == []
    assert cea_mai_lunga_subsecventa_munte([2, 2, 2, 2, 2]) == []
    assert cea_mai_lunga_subsecventa_munte([2, 1, 3, 4, 2, 7, 3, 2, 1, 4, 5, 7, 6, 3, 2, 1, 0, 9, 8]) == [1, 4, 5, 7, 6, 3, 2, 1, 0]
    assert cea_mai_lunga_subsecventa_munte([12, 9, 8, 7, 6, 0, 4, 8, 11, 14, 16, 10, 8, 2, 1, 1, 1]) == [0, 4, 8, 11, 14, 16, 10, 8, 2, 1]



def main():
    l = []
    while True:
        show_menu()
        optiune = input("Dati optiunea: ")
        if optiune == '1':
            l = read_list2()
        elif optiune == '2':
            l2 = longest(l,len(l),3)
            print('Afisare cea mai lunga subsecventa ce contine cel mult trei valori distincte: ',l2[:])
        elif optiune == '3':
            l2 = cea_mai_lunga_subsecventa_munte(l)
            print('Afisare cea mai lunga subsecventa de tip munte: ',l2[:])
        elif optiune == '4':
            break
        else:
            print("Optiune invalida.Reincercati.")



if __name__ == '__main__':
    test_cea_mai_lunga_subsecventa_val_distincte()
    test_cea_mai_lunga_subsecventa_munte()
    main()
