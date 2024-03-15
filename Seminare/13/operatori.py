class NumarComplex:
    def __init__(self, re, im):
        self.__re = re
        self.__im = im

    def __str__(self):
        return f'{self.__re} + {self.__im}i'

    def __eq__(self, other):
        if self.__re == other.__re and self.__im == other.__im:
            return True
        return False
        # return self.__re == other.re and self.im == other.im

    def __neg__(self):
        return NumarComplex(-self.__re, -self.__im)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return NumarComplex(self.__re + other.__re, self.__im + other.__im)

    def __iadd__(self, other):
        self.__re = self.__re + other.__re
        self.__im += other.__im
        return self

n1 = NumarComplex(1, 2)
n2 = NumarComplex(1, 2)

print(n1 == n2)
# echivalent cu
print(n1.__eq__(n2))

# print(n1 == 1) da eroare, pt. ca nu exista 1.__re

print(-n1)

print(n1 != n2)

print(n1+n2)
n3 = n1 + n2
print(n3)
n4 = n1 + n2 + n3
print(n4)

print(id(n1))
n1+=n2
print(id(n1))
print(n1)

print("----------")
def f1(l):
    l = l * 2
    print(id(l))

def f2(l):
    l *= 2
    print(id(l))

l = [1,2,3]
print(id(l))
f1(l)
print(l)
f2(l)
print(l)