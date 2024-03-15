'''
Recapitulam listele. Pentru introducere, deschideti fisierul seminar2/p2_introducere_liste.py
'''

#listele pot contine nu doar numere, ci si siruri de caractere
lista =  ["sir_caractere1", "sir_caractere2", "ABC"]

#in acest caz tiparirea listei, accesarea unui element, a lungimii sau adaugarea de noi elemente in lista se fac LA FEL
print("Lista mea este:", lista)
print("Primul element din lista este:", lista[0])
print("Ultimul element din lista este:", lista[len(lista)-1])
print("Lungimea listei este:", len(lista))
lista.append("sir_nou")
print("Dupa adaugarea unui nou element, lista devine:", lista)
print("\n")

####################################################################################################################
#in acelasi fel, o lista poate contine ca elemente si alte liste, de exemplu
lista = [] #initializam o lista vida
lista.append([1,7])
lista2 = [3,5]
lista.append(lista2)
print("Lista mea este acum o lista de liste:", lista)
print("Lungimea listei este:", len(lista))
primul_element = lista[0]
print("Primul element din lista este:", primul_element)
print("Primul element din lista este tot o lista, cu lungimea:", len(primul_element))
ultimul_element_sublista = primul_element[len(primul_element)-1]
print("Ultimul element al primei liste din lista este:", ultimul_element_sublista)
print("Primul element al celei de-a doua liste din lista este:", lista[1][0])
print("\n")

###################################################################################################################
#Dar nu este obligatoriu ca o lista sa contina DOAR numere, DOAR siruri de caractere sau DOAR alte liste
#LISTELE POT FI ETEROGENE, adica aceeasi lista poate contine si numere, si siruri de caractere, si alte liste
lista = []
lista.append(8)
lista.append([3,30])
lista.append("caractere")
print("Lista mea este:", lista)
print("Lungimea listei este:", len(lista))
print("Al doilea element din lista este:", lista[1])
print("\n")

###################################################################################################################
#adaugare la finalul listei
print("Lista este acum:", lista)
lista.append(10)
print("Lista dupa ce am adaugat un element la final este:", lista)

#adaugare pe o anumita pozitie in lista
lista.insert(2,"ABC")
print("Lista dupa ce am adaugat un element pe pozitia 2 este:", lista)

#stergerea elementului de pe o anumita pozitie din lista
lista.pop(3) #3 este POZITIA IN LISTA A ELEMENTULUI pe care vrem sa il stergem
print("Lista dupa ce am sters elementul de pe pozitia 3 este:", lista)

#stergerea unui anumit element din lista
lista.remove(8) #8 este ELEMENTUL pe care vrem sa il stergem
print("Lista dupa ce am sters elementul 8 din lista este:", lista)

#modificam un element existent in lista
lista[2] = "AP-22"
print("Lista dupa modificarea elementului de pe pozitia 2 este:", lista)
print("\n")

###################################################################################################################
print("Parcurgem elementele listei folosind pozitia lor in lista")
#parcurgere a listei
for i in range(0, len(lista)):
    print(lista[i])

print("\n")
print("Parcurgem elementele listei unul cate unul, fara sa mai fie nevoie de pozitii")
for element in lista:
    print(element)
