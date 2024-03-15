n=int(input("dati primul numar "))

def aparitii(n):
    ap1=[0,0,0,0,0,0,0,0,0,0]
    while n>0:
        c=n%10
        ap1[c]+=1
        n=n//10
    nr=0
    for i in range(9,0,-1):
        while ap1[i]!=0:
            nr=nr*10+i
            ap1[i]-=1
    return nr


print(aparitii(n))