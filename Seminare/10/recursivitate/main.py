def lungimeLista(l, nr = 0):
    if len(l) == 0:
        return nr
    return lungimeLista(l[1:], nr + 1)

assert lungimeLista([]) == 0
assert lungimeLista([1]) == 1
assert lungimeLista([1,2,3]) == 3

def sumaElementelor(l):
    if l == []:
        return 0
    return l[0] + sumaElementelor(l[1:])

assert sumaElementelor([]) == 0
assert sumaElementelor([4]) == 4
assert sumaElementelor([2,5,6]) == 13

# n - pozitiv
def produsCifre(n):
    if n < 10:
        return n
    return n % 10 * produsCifre(n // 10)

assert produsCifre(0) == 0
assert produsCifre(4) == 4
assert produsCifre(245) == 40

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

assert factorial(1) == 1
assert factorial(5) == 120

def cmmdc1(x, y):
    if x == y:
        return x
    if x > y:
        return cmmdc1(x - y, y)
    return cmmdc1(x, y - x)

assert cmmdc1(4, 4) == 4
assert cmmdc1(4, 9) == 1
assert cmmdc1(8, 12) == 4

def cmmdc2(x, y):
    if y == 0:
        return x
    return cmmdc2(y, x % y)

assert cmmdc2(4, 4) == 4
assert cmmdc2(4, 9) == 1
assert cmmdc2(8, 12) == 4

def cmmdcLista(l, cmmdc = None):
    if l == []:
        return cmmdc
    if cmmdc == None:
        cmmdc = l[0]
    return cmmdcLista(l[1:], cmmdc1(l[0], cmmdc))

assert cmmdcLista([]) == None
assert cmmdcLista([4,9,6]) == 1
assert cmmdcLista([12, 14, 16]) == 2

def minim(l, min = None):
    if l == []:
        return min
    if min == None:
        min = l[0]
    if l[0] < min:
        return minim(l[1:], l[0])
    return minim(l[1:], min)

assert minim([]) == None
assert minim([2]) == 2
assert minim([98, 23, 54, 11, 78]) == 11

# cu slicing
def cautareSecventiala1(l, x, i = 0):
    if l == []:
        return None
    if l[0] == x:
        return i
    return cautareSecventiala1(l[1:], x, i + 1)

assert cautareSecventiala1([45, 2, 34], 5) == None
assert cautareSecventiala1([45, 2, 34], 34) == 2

# fara slicing
def cautareSecventiala2(l, x, i = 0):
    if i >= len(l):
        return None
    if l[i] == x:
        return i
    return cautareSecventiala2(l, x, i + 1)

assert cautareSecventiala2([45, 2, 34], 5) == None
assert cautareSecventiala2([45, 2, 34], 34) == 2

def cautareBinara(l, x, st = 0, dr = None):
    if dr == None:
        dr = len(l) - 1
    if st > dr:
        return None
    mij = (st + dr) // 2
    if l[mij] == x:
        return mij
    if x < l[mij]:
        return cautareBinara(l, x, st, mij - 1)
    return cautareBinara(l, x, mij + 1, dr)

assert cautareBinara([1,2,3,4], 5) == None
assert cautareBinara([1,2,3,4], 1) == 0
assert cautareBinara([1,2,3,4], 2) == 1
assert cautareBinara([1,2,3,4], 3) == 2
assert cautareBinara([1,2,3,4], 4) == 3

def filtrare1(l, func, result = []):
    if l == []:
        return result
    if func(l[0]):
        result.append(l[0])
    return filtrare1(l[1:], func, result)

def impar(x):
    return x % 2

assert filtrare1([1,2,3], lambda x : x % 2 == 1, []) == [1,3]
assert filtrare1([1,2,3], impar, []) == [1,3]

def filtrare2(l, func):
    if l == []:
        return []
    if func(l[0]):
        return [l[0]] + filtrare2(l[1:], func)
    return filtrare2(l[1:], func)

assert filtrare2([1,2,3], lambda x : x % 2 == 1) == [1,3]
assert filtrare2([1,2,3], impar) == [1,3]

def fibonacci1(n, x = 1, y = 1):
    if n <= 2:
        return y
    return fibonacci1(n - 1, y, x + y)

assert fibonacci1(1) == 1
assert fibonacci1(2) == 1
assert fibonacci1(3) == 2
assert fibonacci1(4) == 3
assert fibonacci1(5) == 5
assert fibonacci1(6) == 8

def fibonacci2(n):
    if n <= 2:
        return 1
    return fibonacci2(n - 1) + fibonacci2(n - 2)

assert fibonacci2(1) == 1
assert fibonacci2(2) == 1
assert fibonacci2(3) == 2
assert fibonacci2(4) == 3
assert fibonacci2(5) == 5
assert fibonacci2(6) == 8

def sortare(l, i = 0, j = 1):
    if i > len(l) - 2:
        return
    if l[i] > l[j]:
        aux = l[i]
        l[i] = l[j]
        l[j] = aux
    if j < len(l) - 1:
        sortare(l, i, j + 1)
    sortare(l, i + 1, i + 2)

l = [45,23, 67, 11, 100, 99]
sortare(l)
assert l == [11, 23, 45, 67, 99, 100]


# for i in range(0, len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if l[i] , l[j]:
#             swap l[i], l[j]
