def binarySearch(l, st, dr, x):
    if st < dr:
        mij = (st + dr) // 2
        if x == l[mij]:
            return mij
        elif x < l[mij]:
            return binarySearch(l, st, mij - 1, x)
        else:
            return binarySearch(l, mij + 1, dr, x)
    return None

def exponentialSearch(l, x):
    if l[0] == x:
        return 0
    i = 1
    while i < len(l) and l[i] <= x:
        i = i * 2
    return binarySearch(l, i // 2, min(i, len(l) - 1), x)

assert exponentialSearch([1, 5, 7, 8, 11, 20, 25, 33, 35, 40], 12) == None
assert exponentialSearch([1, 5, 7, 8, 11, 20, 25, 33, 35, 40], 8) == 3
assert exponentialSearch([1, 5, 7, 8, 11, 20, 25, 33, 35, 40], 35) == 8

def insertionSort(l, st, dr):
    for i in range(st + 1, dr + 1):
        j = i
        while j >= st + 1 and l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1

def merge(l, st, mij, dr):
    n1 = mij - st + 1
    n2 = dr - mij
    l1 = []
    l2 = []
    for i in range(st, mij + 1):
        l1.append(l[i])
    for i in range(mij + 1, dr + 1):
        l2.append(l[i])
    i = 0
    j = 0
    k = st
    while i < n1 and j < n2:
        if l1[i] < l2[j]:
            l[k] = l1[i]
            i += 1
        else:
            l[k] = l2[j]
            j += 1
        k += 1
    while i < n1:
        l[k] = l1[i]
        i += 1
        k += 1
    while j < n2:
        l[k] = l2[j]
        j += 1
        k += 1

def timSort(l):
    minRun = 4
    for i in range(0, len(l), minRun):
        insertionSort(l, i, min(i + minRun - 1, len(l) - 1))
    size = minRun
    while size < len(l):
        for i in range(0, len(l), 2 * size):
            st = i
            mij = min(i + size - 1, len(l) - 1)
            dr = min(i + 2 * size - 1, len(l) - 1)
            merge(l, st, mij, dr)
        size = 2 * size

l = [23, 11, 8, 7, 20, 19, 45, 40, 12]
timSort(l)
assert l == [7, 8, 11, 12, 19, 20, 23, 40, 45]

l = [1, 5, 3, 10, 9, 7, 2, 11, 43, 21]
timSort(l)
print(l)

l = [1, 5, 3, 10, 9, 7, 2, 11, 43, 21, 4]
timSort(l)
print(l)

l = [1, 5, 3, 10, 9, 7, 2, 11, 43, 21, 4, 0]
timSort(l)
print(l)

# 14 elemente
l = [1, 5, 3, 10, 9, 7, 2, 11, 43, 21, 4, 0, 8, 6]
timSort(l)
print(l)