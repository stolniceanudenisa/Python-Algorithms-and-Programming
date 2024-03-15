# descriere - functie care citeste numarul
def CitireNumar():
    n=int(input("Dati numar: "))
    return n

''' 
    descriere - functie care calculeaza cmmdc-ul a doua numere
    input - perechea de numere x si y
    output - cmmdc-ul stocat in x
'''
def cmmdc_euclid(x,y):
    while(y!=0):
        r=x%y
        x=y
        y=r
    return x

if __name__ == "__main__":
    n=CitireNumar()
    m=CitireNumar()
    rezultat=cmmdc_euclid(n,m)
    print(rezultat)