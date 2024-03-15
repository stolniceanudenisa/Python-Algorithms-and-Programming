'''
Introducere dictionar
'''

#un dictionar este o structura de date care stocheaza perechi cheie:valoare
#initializam un dictionar gol folosind {}
dictionar = {}

#putem initializa si un dictionar nevid, care sa contina de la inceput niste perechi de chei cu valori
dictionar = {"cheie_1": 100, "cheie_2": "ABC", 10: "AP-22", "data_mea":[24,10,2022]}
print("Dicionarul nostru este:", dictionar)
print("Dimensiunea dictionarului este:", len(dictionar))

#putem accesa valorile din dictionar folosind cheile care le corespund
valoare_1 = dictionar["cheie_1"]
print("Valoarea pentru cheie_1 este:", valoare_1)

valoare_2 = dictionar["data_mea"][1]
print("Valoarea celui de-al doilea element pentru lista corespunzatoare cheii data_mea este:", valoare_2)
print("\n")


#NU putem accesa valorile unui dictionar la fel cum accesam valorile unei lista (folosindu-ne de pozitiile elementelor)
#daca decomentati linia urmatoare si rulati programul veti vedea ca primiti eroare
#pereche_1 = dictionar[0] #daca accesam dictionar[0] NU se va returna prima pereche cheie:valoare din dictionar

#in schimb, putem parcurge un dictionar folosind un for care parcurge in ordine fiecare cheie
#apoi, folosind cheia curenta, accesam valoarea corespunzatoare
print("Parcurgem cheile dictionarului:")
for cheie in dictionar:
    print("Cheia este:", cheie)
    print("Valoarea este:", dictionar[cheie])
    print("\n")
print("\n")

#asa adaugam o noua pereche cheie:valoare in dictionarul nostru
dictionar["cheie_noua"] = "valoare_noua"
print("Dictionarul cu noua pereche cheie:valoare adaugata este:", dictionar)
print("\n")

#asa modificam(updatam) valoarea corespunzatoare unei chei existente
dictionar["cheie_1"] = "VALOARE MODIFICATA"
dictionar["cheie_2"] = 540
print("Dictionarul dupa modificari este:", dictionar)
print("\n")

#asa stergem o pereche cheie:valoare din dictionar
dictionar.pop("cheie_2")
print("Dictionarul dupa stergerea perechii cheie:valoare este:", dictionar)
print("\n")

##################################################################################################################
#o lista poate contine dictionare
lista = []
dictionar_avion_1 = { "cod": 1, "tip": "Airbus", "culoare": "alb", "an_fabricatie": 2010 }
dictionar_avion_2 = { "cod": 2, "tip": "Eurofighter Typhoon", "culoare": "negru", "an_fabricatie": 2014 }
lista.append(dictionar_avion_1)
lista.append(dictionar_avion_2)
print("Lista de dictionare este:", lista)
print("\n")

#primul element al listei este dictionar_avion_1
primul_element = lista[0]
print("Primul element din lista este un dictionar:", primul_element)
an_fabricatie = primul_element["an_fabricatie"]
print("Anul fabricatiei pentru acesta este:", an_fabricatie)
print("\n")

#parcurgem o lista de dictionare parcurgand elementele unei lista cu un for i in range(0, len(lista)):
#fiecare element din lista este un dictionar pe care il parcurgem cu un for cheie in dictionar_curent
print("Parcurgem lista de dictionare:\n")
for i in range(0, len(lista)):
    dictionar_curent = lista[i]
    print("Dictionar", i+1)
    for cheie in dictionar_curent:
        valoare = dictionar_curent[cheie]
        print(cheie, "=", valoare)
    print("\n")
