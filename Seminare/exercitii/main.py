from typing import List


def show_menu():
    print('1. Citire lista de numere intregi')
    print('2. x[i] < x[i+1] < ... < x[i+p]')
    print('3. Oricare doua elemente consecutive sunt relativ prime intre ele (a, b relativ prime daca si numai daca cmmdc(a,b) = 1).')
    print('4. Determina cea mai lunga subsecvența ce contine doar numere prime.')
    print('5. Determina cea mai lunga subsecventa care are toate elementele egale.')
    print('6. Determina cea mai lunga subsecvența in care sunt toate elementele distincte intre ele')
    print('x. Iesire')


def read_list():
    lst = []
    lst_str = input('Dati numerele separate prin spatiu: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst


def prima_prop():
    lst = read_list()
    c = 1
    cmax = 0
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            c += 1
        else:
            if (cmax < c):
                cmax = c
                pmax = i
            p = pmax - c + 1
            c = 1
    if (c != 1):
           if (cmax < c):
            cmax = c
    return lst[p:pmax + 1]



def cea_mai_lunga_secv_contine_doar_nrprime(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecvența ce contine doar din numere prime.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''
    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_is_prime = True
            for num in lst[st:dr + 1]:
                if is_prime(num) != True:
                    all_is_prime = False
                    break
            if all_is_prime:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result


def cea_mai_lunga_secv_care_are_toate_el_egale(lst):
    '''
    Determina cea mai lunga subsecventa care are toate elementele egale.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''
    n = len(lst)
    lc=1
    pmax=0
    lmax=1
    pc=0
    for i in range(n):
        if lst[i]==lst[i+1]:
            lc+=1
    return lc


def cea_mai_lunga_subsecventa_semne_contrare(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa in care diferentele (x[j+1] - x[j]) si (x[j+2] - x[j+1]) au semne contrare.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''
    n = len(lst)
    result = []
    lmax = 0
    lc = 0
    pc = 0
    pmax = 0
    for i in range(n):
        if lst[i+1] - lst[i] < 0 and lst[i+2] - lst[i+1] > 0 or lst[i+1] - lst[i] > 0 and lst[i+2] - lst[i+1] < 0:
            lc+=2 # ?????? din cat in cat
            dif1 = lst[i+1] - lst[i]
            dif2 = lst[i+2] - lst[i+1]
        elif (lst[i+1] - lst[i] < 0 and lst[i+2] - lst[i+1] < 0) or lst[i+1] - lst[i] > 0 and lst[i+2] - lst[i+1] > 0:
            if lc > lmax:
                lmax = lc
                pmax = pc
            lc = 1
            pc = i
    for j in range(pmax, pmax+lmax+1):
        print(lst[j])
    #return result


def semne_contrare(lst):
    '''
    Determina semnul diferentei a doua numere consecutive dintr-o lista.
    :param:----------------
    :return: ----------------
    '''


def is_prime(n: int) -> bool:
    '''
    Determina daca un numar dat este prim.
    :param n: numarul dat
    :return: True daca numarul e prim si False altfel
    '''
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1): # +1 ca sa ia si radicalul in sine
        if n % d == 0:                    # pt ca range(a,b) merge pana la mai mic strict decat b
            return False
    return True


def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(15) == False
    assert is_prime(29) == True


def get_primes(lst):
    '''
    Determina numerele prime dintr-o lista.
    :param lst: lista de numere.
    :return: o lista cu numerele prime din lst.
    '''
    result = []
    for num in lst:
        if is_prime(num):
            result.append(num)
    return result


def get_longest_subarray_all_divisible_by_10(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa in care toate elementele sunt divizibile cu 10.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''
    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_div_10 = True
            for num in lst[st:dr+1]:
                if num % 10 != 0:
                    all_div_10 = False
                    break
            if all_div_10:
                if dr - st + 1 > len(result):
                    result = lst[st:dr+1]
    return result


def main():
    lst = []
    while True:
        show_menu()
        optiune = input('Optiunea: ')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print('x[i] < x[i+1] < ... < x[i+p] este:', prima_prop())
        elif optiune == '4':
            print('Cea mai lunga subsecvența cu numere prime este:', cea_mai_lunga_secv_contine_doar_nrprime(lst))
        elif optiune == '5':
            print('Cea mai lunga subsecventa care are toate elementele egale este: ', cea_mai_lunga_secv_care_are_toate_el_egale(lst))
        elif optiune == '6':
            print('Cea mai lunga subsecvența in care sunt toate elementele distincte intre ele este: ', cea_mai_lunga_subsecventa_semne_contrare(lst))
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida. ')


if __name__ == '__main__':
    test_is_prime()
    main()

