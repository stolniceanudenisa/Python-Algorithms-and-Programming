'''
INTRODUCERE LISTE
'''

#initializam o variabila ca lista folosind []
#prin [] definim o lista vida in Python
lista_mea = [] #variabila lista_mea este acum o lista vida

#putem initializa o variabila si cu o lista nevida
lista_mea = [5, 10, 23, 1] #in acest caz, variabila lista_mea va fi o lista formata din 5, 10, 23 si 1

#putem tipari lista folosind functia print()
print("Lista mea este: ", lista_mea)
print("\n")

#putem accesa elementele din lista folosind pozitia pe care se afla (la fel ca la vectorii din C++)
#in programare incepem intotdeauna numaratoarea de la pozitia 0!
#deci: primul element din lista va fi pe pozitia 0, al doilea pe pozitia 1, ..., ultimul pe pozitia lungimea listei - 1
primul_element = lista_mea[0]
al_doilea_element = lista_mea[1]
print("Primul element este:", primul_element)
print("Al doilea element este:", al_doilea_element)
print("\n")

#putem accesa lungimea listei folosind functia predefinita len()
lungime_lista = len(lista_mea)
print("Lungimea listei este:", lungime_lista)
print("\n")

#daca vrem sa parcurgem lista, o putem face cu un for
for i in range(0, len(lista_mea)): #vrem sa parcurgem toate pozitiile din lista, de la pozitia 0 pana la pozitia lungime_lista-1
    print("Elementul de pe pozitia", i, " este:", lista_mea[i])
print("\n")

#daca vrem sa adaugam un element in lista, folosim functia predefinita append() asa:
element_nou = 100
lista_mea.append(element_nou)
print("Am adaugat 100. Acum lista este:", lista_mea)

#vedem ca dupa ce am adaugat un element nou, lungimea listei creste
lungime_lista = len(lista_mea)
print("Noua lungime a listei este:", lungime_lista)
print("\n")

#acum, daca vom parcurge din nou lista, vom vedea ca in ea a aparut si valoarea 100 (adaugata la final)
for i in range(0, len(lista_mea)):
    print("Elementul de pe pozitia", i, " este:", lista_mea[i])
print("\n")

#daca vrem sa parcurgem lista doar de la al doilea pana la al treilea element, modificam range-ul de la for
print("Parcurgem lista doar de la al doilea pana la al treilea element.")
for i in range(1, 3):#variabila i va primi, pe rand, valorile 1 si 2
    print("Elementul de pe pozitia", i, " este:", lista_mea[i])
print("\n")

#daca vrem sa tiparim in consola sublista de la elementul al doilea pana la al treilea, o putem face astfel:
print("Sublista de la elementul al doilea pana la al treilea este:", lista_mea[1:3])
print("\n")

#tiparim sublista de la elementul al doilea pana la finalul ei
print("Sublista de la elementul al doilea pana la finalul listei este:", lista_mea[1:])
print("\n")

#tiparim sublista de la inceput pana la al treilea element
print("Sublista de la inceputul listei pana la al treilea element este:", lista_mea[:3])