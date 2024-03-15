def toateElementeleDivCu10(l):
    '''
    determina daca toate nr. dintr-o lista sunt divizibile cu 10
    :param l: lista de nr. intregi
    :return: True, dcaa l contine doar nr. divizbile cu 10 sau False, in caz contrar
    '''
    for element in l:
        if element % 10 != 0:
            return False
    return True

def testToateElementeleDivCu10():
    assert(toateElementeleDivCu10([11,12,13]) == False)
    assert (toateElementeleDivCu10([11, 20, 13]) == False)
    assert (toateElementeleDivCu10([20, 30, 40]) == True)

def ceaMaiLungaSecventaDeNrDivCu10(l):
    '''
    determina cea mai lunga secvente de nr. divizibile cu 10 dintr-o lista
    :param l: lista de nr. intregi
    :return: lista de nr. intregi
    '''
    subsecvMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toateElementeleDivCu10(l[i:j+1]) and len(l[i:j+1]) > len(subsecvMax):
                subsecvMax = l[i:j+1]
    return subsecvMax

def testCeaMaiLungaSecventaDeNrDivCu10():
    assert(ceaMaiLungaSecventaDeNrDivCu10([1,2,3]) == [])
    assert(ceaMaiLungaSecventaDeNrDivCu10([1,20,30]) == [20, 30])
    assert(ceaMaiLungaSecventaDeNrDivCu10([20, 30, 4, 50, 60, 70]) == [50, 60, 70])

def palindrom(x):
    '''
    determina daca un nr. este palindrom
    :param x: nr. intreg
    :return: True, daca x e palindrom, altfel False
    '''
    x2 = x
    y = 0
    while x2:
        y = y * 10 + x2 % 10
        x2 = x2 // 10
    return x == y

def testPalindrom():
    assert(palindrom(100) == False)
    assert(palindrom(4) == True)
    assert(palindrom(101) == True)

def numerePalindrom(l):
    '''
    determina nr. aplindrom dintr-o lista
    :param l: lista de nr. intregi
    :return: lista d enr. intregi
    '''
    l2 = []
    for i in range(len(l)):
        if (palindrom(l[i])):
            l2.append(l[i])
    return l2

def testNumerePalindrom():
    assert(numerePalindrom([1,2,3]) == [1,2,3])
    assert(numerePalindrom([21, 32, 43]) == [])
    assert(numerePalindrom([22, 43, 303]) ==[22, 303])

def citireLista():
    l = []
    n = int(input('Dati nr. de elemente al listei: '))
    for i in range(n):
        l.append(int(input()))
    return l

def citireLista2():
    l = []
    linie = input("Dati lista de nr. separate prin spatiu")
    numere = linie.split(" ")
    for i in range(len(numere)):
        l.append(int(numere[i]))
    return l

def printMenu():
    print("1. Citire lista")
    print("2. Afisare lista")
    print("3. Afisare nr. palindrom")
    print("4. Afisare cea mai lunga secventa de nr. divizbile cu 10")
    print("x. Iesire")

def main():
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(l)
        elif optiune == "3":
            print(numerePalindrom(l))
        elif optiune == "4":
            print(ceaMaiLungaSecventaDeNrDivCu10(l))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

testPalindrom()
testNumerePalindrom()
testToateElementeleDivCu10()
testCeaMaiLungaSecventaDeNrDivCu10()
main()