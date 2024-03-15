from copy import deepcopy

print("\n")
lista1 = [1,2,[100,20]]
print("lista1 =",lista1)
lista2 = lista1
print(id(lista1))
print(id(lista2))
lista3 = lista1.copy()
print(id(lista3))
lista4 = lista1[:]
lista5 = deepcopy(lista1)
print("lista2 =",lista2)
print("lista3 =",lista3)
print("lista4 =",lista4)
print("lista5 =",lista5)

lista1[0] = 4

print("\nlista1[0] = 4\n")
print("lista1 =",lista1)
print("lista2 =",lista2)
print("lista3 =",lista3)
print("lista4 =",lista4)
print("lista5 =",lista5)

lista1[2][0] = 88

print("\nlista1[2][0] = 88\n")
print("lista1 =",lista1)
print("lista2 =",lista2)
print("lista3 =",lista3)
print("lista4 =",lista4)