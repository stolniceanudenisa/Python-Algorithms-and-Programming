#prime number
def prim(n):
    if n==0 or n==1:
        return False 
    if n==2 or n==3:
        return True
    d=3
    while d*d<=n and n%d!=0:
        d+=2

    if n%d==0:
        return False
    else:
        return True



n=int(input("number n is: "))
ok=False

for i in range(1, n/2):
    if i*i==n:
        ok=True

if ok:
    print("n is square root.")
else:
    print("n is NOT square root.")


if prim(n)!=True:
    print("not prime")
else:
    print("is prime")




