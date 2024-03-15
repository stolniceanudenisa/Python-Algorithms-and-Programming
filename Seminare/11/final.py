def cautareSecventiala(l, x):
    for i in range(len(l)):
        if x == l[i]:
            return i
    return None

def cautareBinara(l, x):
    st = 0
    dr = len(l) - 1
    while st < dr:
        mij = (st + dr) // 2
        if l[mij] == x:
            return mij
        elif l[mij] < x:
            dr = mij - 1
        else:
            st = mij + 1
    return None

def bubbleSort(l):
    for i in range(len(l) - 1):
        swapped = False
        for j in range(len(l) - i - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        if swapped is False:
            return

l = [45, 23, 21, 19, 50]
bubbleSort(l)
assert l == [19, 21, 23, 45, 50]

def selectionSort(l):
    for i in range(len(l)):
        minIndex = i
        for j in range(i + 1, len(l)):
            if l[j] < l[minIndex]:
                minIndex = j
        l[i], l[minIndex] = l[minIndex],l[i]

l = [45, 23, 21, 19, 50]
selectionSort(l)
assert l == [19, 21, 23, 45, 50]

def insertionSort(l):
    for i in range(1, len(l)):
        j = i
        while j >= 1 and l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1

def insertionSort2(l):
    for i in range(1, n):
        key = l[i]
        j = i-1
        while j >=0 and key < l[j] :
                l[j+1] = l[j]
                j -= 1
        l[j+1] = key

l = [45, 23, 21, 19, 50]
insertionSort(l)
assert l == [19, 21, 23, 45, 50]

# grupa 312
def partition(l, st, dr):
    pivot = l[dr]
    pivotIndex = dr
    for i in range(st, dr):
        if (i < pivotIndex and l[i] > pivot) or (i > pivotIndex and l[i] < pivot):
            l[i], l[pivotIndex] = l[pivotIndex], l[i]
            pivotIndex = i
    return pivotIndex

# grupa 315
def partition(l, st, dr):
    pivot = l[dr]
    k = st - 1
    for i in range(st, dr):
        if l[i] < pivot:
            k += 1
            l[i], l[k] = l[k], l[i]
    l[dr], l[k + 1] = l[k + 1], l[dr]
    return k + 1

def quickSort(l, st = 0, dr = None):
    if dr is None:
        dr = len(l) - 1
    if st < dr:
        partitionIndex = partition(l, st, dr)
        quickSort(l, st, partitionIndex - 1)
        quickSort(l, partitionIndex + 1, dr)

l = [45, 23, 21, 19, 50]
quickSort(l)
print(l)
assert l == [19, 21, 23, 45, 50]

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

def mergeSort(l, st, dr):
    if st < dr:
        mij = (st + dr) // 2
        mergeSort(l, st, mij)
        mergeSort(l, mij + 1, dr)
        merge(l, st, mij, dr)

def mergeSort2(l, st = 0, dr = None):
    if dr is None:
        dr = len(l) - 1
    if st < dr:
        mij = (st + dr) // 2
        mergeSort(l, st, mij)
        mergeSort(l, mij + 1, dr)
        merge(l, st, mij, dr)

l = [45, 23, 21, 19, 50]
mergeSort(l, 0, len(l) - 1)
assert l == [19, 21, 23, 45, 50]
