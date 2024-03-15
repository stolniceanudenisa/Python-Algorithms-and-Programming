def show_menu():
    print('1. Citire lista de numere intregi')
    print('5. Determina cea mai lunga subsecventa care are toate elementele egale.')
    print('x. Iesire')


def read_list():
    lst = []
    lst_str = input('Dati numerele separate prin spatiu: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst


def cea_mai_lunga_secv_care_are_toate_el_egale(lst):
    '''
    Determina cea mai lunga subsecventa care are toate elementele egale.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''
    n = len(lst)
    lc = 1
    rezultat=1
    for i in range(1,n):
        if lst[i]==lst[i-1]:
            lc=lc+1
        else:
            rezultat=max(rezultat,lc)
            lc=1
    rezultat = max(rezultat,lc)
    return rezultat


def main():
    lst = []
    while True:
        show_menu()
        optiune = input('Optiunea: ')
        if optiune == '1':
            lst = read_list()
        elif optiune == '5':
            print('Cea mai lunga subsecventa care are toate elementele egale este: ', print(cea_mai_lunga_secv_care_are_toate_el_egale(lst)))
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida. ')


if __name__ == '__main__':
    main()