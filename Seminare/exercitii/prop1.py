# [i] < x[i+1] < ... < x[i+p]
# crescator

def citire():
    l = []
    n = int(input())
    for i in range(n):
        l = l + [int(input())]
    return l


def lungscv():
    l = citire()
    ok = 1
    c = 1
    cmax = 0
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
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

    return l[p:pmax + 1]


def main():
    print(lungscv())

if __name__ == '__main__':
    main()