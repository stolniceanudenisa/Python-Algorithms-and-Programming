from Problema2 import CitireNumar, verif_prim

''' 
    descriere - functie care gaseste cel mai mare numar prim, mai mare decat un numar dat
    input - numarul n
    output - numarul n care se modifica, pana cand ajunge un numar prim mai mare decat el insusi
'''
def gasire_primul_numar_mai_mare(n):
    n+=1
    while(verif_prim==False):
        n+=1
    return n

if __name__ == "__main__":
    n=CitireNumar()
    rezultat=gasire_primul_numar_mai_mare(n)
    print(rezultat)

