# Seminarele 7, 8 și 10 - Săptămânile 7, 8 și 11

**Atenție:** seminarul 9 este separat. 

Scrieți folosind OOP un program pentru gestionarea unei firme de taxi. Vor fi suportate operațiile:
1. CRUD mașină. O mașină are: indicativ, nivel confort (standard, ridicat, premium), plata cu cardul (da / nu), model.
2. CRUD locație. O locație are: nume stradă, număr, bloc, scară, alte indicații.
3. CRUD comenzi. O comandă are: id mașină, id locație, timp final, cost / km, distanță parcursă, status (în desfășurare, finalizată).
4. Ordonarea străzilor descrescător după lungimea indicațiilor
5. Ordonarea mașinilor crescător după costul mediu / km.
6. Determinarea străzilor cu cele mai lungi comenzi (ca distanță).
7. Filtrarea masinilor care au un confort citit de la tastatura.
8. Afisarea vitezei medii pentru comenziile inregistrate in aplicatie
9. Afisarea perechilor formate din indicativul masinii si daca plata s-a efectuat cu cardul sau nu.
10. Undo+Redo în mod eficient.

Propunere de organizare pe iterații:
- Iterația 1: 1-3, repository-uri distincte, validatori.
- Iterația 2: 4-7, repository generic, excepții proprii.
- Iterația 3: 7-8, filter, map, lambda, list comprehensions, recursivitate etc.

Folosiți arhitectură stratificată conform discuțiilor de la curs.

![arhitectura stratificata](https://user-images.githubusercontent.com/2019410/139555775-d89f65b2-2e20-4bf1-b39f-e34b5c42a1c2.png)

https://www.python.org/dev/peps/pep-0008/

More on sorting in Python: https://realpython.com/sorting-algorithms-python/#implementing-timsort-in-python
