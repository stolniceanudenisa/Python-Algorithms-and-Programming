def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)


def gcd2(a, b):
    r=1
    while (b!=0):
        r=a%b
        a=b
        b=r
        
    return a

#MAIN
print gcd2(12, 30)
