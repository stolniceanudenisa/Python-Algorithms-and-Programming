a = int(input("a="))
c = 0
s1 = 0
def sum(b):
    s2 = 0
    c1 = 0
    while b != 0:
        c1 = b % 10
        s2 = s2 + c1
        b = b / 10
print(sum(a))
