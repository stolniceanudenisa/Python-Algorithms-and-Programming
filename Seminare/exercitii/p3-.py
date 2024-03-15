'''
    descriere - Determina o data calendaristica (sub forma an, luna, zi) pornind de
    la doua numere întregi care reprezintă anul si numărul de ordine al zilei in anul respectiv.
    input - anul si numarul de ordine al zilei.
    output - o data calendaristica (sub forma an, luna, zi)
'''

def an_bisect(anul):
    if anul % 4 == 0:
        return True
    return False

An = int(input("Dati anul de nastere: "))
nr_ordine_zi = int(input("Dati numarul de ordine al zilei din an: "))

#ex:  70 70//30==2 70%30==10

if nr_ordine_zi > 365 or nr_ordine_zi <= 0:
    print("Numărul zilei nu este în anul curent! Introduceti alt numar de ordine al zilei.")
else:
    print(str(An),".",nr_ordine_zi // 30,".",nr_ordine_zi % 30)