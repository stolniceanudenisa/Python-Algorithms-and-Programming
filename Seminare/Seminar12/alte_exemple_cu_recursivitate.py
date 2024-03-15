'''
Alte exemple cu functii recursive.

Observati ca daca tiparim INAINTE de apelarea recursiva a functiei functie_recursiva1,
tiparirile noastre vor aparea in ordine in consola.

In schimb, daca tiparim DUPA ce apelam recursiv functia functie_recursiva2,
se va intra in functie_recursiva2(n+1), care la randul ei va intra, inainte sa tipareasca, in
functie_recursiva2((n+1)+1), ..., pana cand ajungem la final si se termina apelurile recursive la functia
functie_recursiva2.
In acel moment, suntem in functie_recursiva2(4), am trecut de linia care apeleaza recursiv functie_recursiva(5)
(care nu a facut/returnat nimic) si mergem mai departe sa facem print-ul "n este: 4".
Apoi, dupa ce terminam asta, ne intoarcem in functia care apelase functie_recursiva2(4), adica functie_recursiva2(3)
si facem print-ul "n este: 3". Si mergem inapoi tot asa, pana ajungem la valoarea initiala pe care i-am dat-o lui n.

Observati ca spre deosebire de primul caz (functie_recursiva1) cand valorile lui n erau tiparite in ordinea apelarii,
pentru functie_recursiva2, ele sunt tiparite in ordine inversa apelarii (intai ultima valoare, ..., apoi prima)
Desi noi nu am schimbat in continutul functiei decat locul unde se face tiparirea.

ASADAR:
Daca tiparim inainte de apelul recursiv, tiparirile se desfasoara normal.
Daca tiparim dupa apelul recursiv, tiparirile sunt facute in ordine inversa.
'''

def functie_recursiva1(n):
    if n < 5:
        print("n este:", n)
        functie_recursiva1(n+1)

print("IN FUNCTIE RECURSIVA 1:")
functie_recursiva1(1)

def functie_recursiva2(n):
    if n < 5:
        functie_recursiva2(n+1)
        print("n este:", n)

print("IN FUNCTIE RECURSIVA 2:")
functie_recursiva2(1)
