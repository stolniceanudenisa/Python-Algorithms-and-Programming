def cmmdc(a, b):
    '''
    determina cel mai mare divizor a doua numere
    :param a: nr. intreg
    :param b: nr. intreg
    :return: cel mai mare divizor al lui a si b, nr. intreg
    '''
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def main():
    a = int(input("a="))
    b = int(input("b="))
    print(cmmdc(a,b))

main()