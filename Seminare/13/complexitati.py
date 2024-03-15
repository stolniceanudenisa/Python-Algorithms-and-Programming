#complexitate timp:
    # omega(1)
    # big theta(1)
    # O(1), O(n)
#complexitate spatiu:
    # omega(1)
    # big theta(1)
    # O(1), O(n)

def f1(a, b):
    c = a + b
    return c

#complexitate timp:
    # omega(1)
    # big theta(1)
    # O(1), O(n)
#complexitate spatiu:
    # omega(n)
    # big theta(n)
    # O(n)
def f2(l):
    return l[0] + l[1]

#complexitate timp:
    # omega(n)
    # big theta(n)
    # O(n)
#complexitate spatiu:
    # omega(1)
    # big theta(1)
    # O(1)
def f3(n):
    s = 0
    for i in range(n):
        x = 0
        s += i
    return s

#complexitate timp:
    # omega(n^2)
    # big theta(n^2)
    # O(n^2)
#complexitate spatiu:
    # omega(1)
    # big theta(1)
    # O(1)
def f4(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

#complexitate timp:
    # omega(n^2)
    # big theta(n^2)
    # O(n^2)
#complexitate spatiu:
    # omega(1)
    # big theta(1)
    # O(1)
def f5(n):
    for j in range(n):
        for i in range(n//2):
            print(i, j)

#complexitate timp:
    # omega(n)
    # big theta(n)
    # O(n)
#complexitate spatiu:
    # omega(1)
    # big theta(1)
    # O(1)
def f6(n):
    for i in range(n):
        for j in range(2, 5):
            print(i, j)

#complexitate timp:
    # omega(n^2)
    # big theta(n^2)
    # O(n^2)
#complexitate spatiu:
    # omega(1)
    # big theta(1)
    # O(1)
def f7(n):
    for i in range(n):
        f8(i)

def f8(n):
    for i in range(n):
        print(i)

#complexitate timp:
    # omega(n)
    # big theta(n)
    # O(n)
#complexitate spatiu:
    # omega(n)
    # big theta(n)
    # O(n)
def f9(n):
    if n == 0:
        return 0
    return n + f9(n-1)

#complexitate timp:
    # omega(1)
    # big theta(n)
    # O(n)
#complexitate spatiu:
    # omega(n)
    # big theta(n)
    # O(n)
def f10(l):
    '''
    verifica daca exista un nr. par in lista
    :param l:
    :return:
    '''
    for i in range(len(l)):
        if l[i] % 2 == 0:
            return True
    return False

f9(5)