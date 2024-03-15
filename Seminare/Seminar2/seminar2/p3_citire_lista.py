'''
Problema 2. Cititi o lista de la tastatura.
'''


def citire_lista():
    '''
    Functie care citeste o lista.
    Date intrare: -
    Date iesire: lista citita
    '''
    lista = [] #initializam lista cu o lista vida. Pe masura ce citim valori de la tastatura, le vom introduce in lista
    lungime_lista = int(input("Introduceti lungimea listei citite:"))
    for i in range(0, lungime_lista):
        element = int(input("Introduceti un element in lista:"))
        lista.append(element)
    return lista

lista_mea = citire_lista()
print("Lista citita este:", lista_mea)