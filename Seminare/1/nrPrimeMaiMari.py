def isPrime(n):
    '''
    Determina daca un numar este prim.
    :param num: int, numarul dat
    :return: True daca num e prim si False in cazcontrar
    '''
    if n < 2:
        return False
    for d in range(2, n // 2 + 1):
        if n % d == 0:
            return False
    return True

def main():
    n = int(input("n="))
    k = int(input("k="))

    while k != 0:
        #if isPrime(n) == True
        #if isPrime(n) is True
        if isPrime(n):
            print(n)
            k -= 1
        n += 1

main()