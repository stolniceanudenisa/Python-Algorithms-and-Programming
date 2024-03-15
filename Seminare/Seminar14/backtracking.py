'''
Vom folosi metoda backtracking pentru problemele la care este nevoie sa generam toate solutiile posibile.
Backtracking vine de la back = inapoi si tracking = urmarire. Inseamna faptul de a merge inapoi pe urmele noastre.
Asta este important deoarece noi avem nevoie sa generam toate solutiile posibile.
De exemplu, daca problema ne cere sa generam toate permutarile pentru lista [1,2], metoda backtracking va incerca sa
genereze pe rand toate combinatiile posibile ([1,2],[2,1]) dar pentru a le obtine va trebui sa faca mai multe incercari.
Daca a generat lista formata din [1] si vrea sa mai adauge inca un element in ea, va incerca prima data sa il adauge din
nou pe 1: [1,1], dar noi trebuie sa generam permutari (la permutari, elementele nu se repeta). Deci solutia [1,1] este
invalida (in cod, vom impune constrangeri pentru validarea permutarilor generate).
Pentru asta, algoritmul de backtracking merge "inapoi pe urmele sale", stergand din lista doar elementul care strica
validitatea solutiei (al doilea 1 pe care tocmai l-am adaugat) si incercand sa ii dea o alta valoare (singura valoare
pe care o mai poate da acum este 2). Astfel, se obtine solutia [1,2].
Pentru a cauta urmatoarele solutii, stergem din lista valoarea 2 (lista ramane [1]) si incercam sa adaugam alta valoare.
Dar observam ca nu exista alta valoare disponibila de adaugat, deci mergem si mai inapoi, stergandu-l si pe 1 din lista.
Acum lista noastra este goala. Vom incerca sa adaugam pe prima pozitie valoarea urmatoare lui 1. Ea exista si este 2.
O adaugam (lista devine [2]). Incercam sa completam lista cu valoarea 1 pe pozitia urmatoare. Este in regula, putem sa o
adaugam (lista devine [2,1]). Daca vrem sa cautam alta valoare pentru aceasta pozitie, incercam sa introducem cealalta
valoare posibila, adica 2. Din nou, lista devine [2,2], iar noi vrem permutari. Deci aceasta lista nu este valida.
Stergem ultimul 2 din lista (lista ramane [2]) si incercam sa dam alta valoare pentru pozitia aceea. Doar ca nu mai avem
alte valori disponibile din care sa alegem (le-am epuizat pe toate: 1 si 2). Deci trebuie sa ne intoarcem cu un pas si
mai inapoi si sa stergem 2 din lista. Lista devine goala. Vom incerca sa dam urmatoarea valoare pentru prima pozitie.
Dar pentru ca valorile noastre disponibile sunt doar 1 si 2 (si deja am creat solutii cu ele pe prima pozitie), nu mai
putem da alta valoare pentru prima pozitie. Algoritmul se va opri.
'''

def backtracking_toate_combinatiile_posibile(lungime_maxima, cifra_maxima, pozitie, rezultat_intermediar):
    '''
    Functie care foloseste metoda backtracking pentru a genera toate combinatiile posibile pentru un interval de cifre.
    :param lungime_maxima: lungimea maxima a solutiei pe care o construim
    :param cifra_maxima: cifra maxima pana la care sa generam toate combinatiile de numere posibile
    :param rezultat_intermediat: rezultatul intermediar obtinut
    :return: rezultat final
    '''
    if este_final(rezultat_intermediar, pozitie, lungime_maxima) == True:
        print(rezultat_intermediar)
    else:
        for i in range(1, cifra_maxima+1):
            if verifica_conditie(rezultat_intermediar, i, cifra_maxima) == True:
                rezultat_intermediar[pozitie] = i
                backtracking_toate_combinatiile_posibile(lungime_maxima, cifra_maxima, pozitie+1, rezultat_intermediar)
                rezultat_intermediar[pozitie] = 0

def este_final(rezultat, pozitie, lungime_maxima):
    '''
    Functie care verifica daca rezultatul curent este cel final necesar rezolvarii problemei.
    :param rezultat: rezultatul obtinut pana in acest moment
    :param pozitie: ultima pozitie ocupata din lista rezultat
    :param lungime_maxima: lungimea maxima admisa
    :return: True, daca rezultat este rezultatul final; False, altfel
    '''
    if pozitie == lungime_maxima:
        return True
    else:
        return False

def verifica_conditie(rezultat_intermediar, cifra_noua, cifra_maxima):
    '''
    Functie care impune constrangeri asupra rezultatului intermediar (verifica ca o anumita conditie sa fie indeplinita)
    :param rezultat_intermediar: rezultatul obtinut pana in acest moment
    :param cifra_noua: noua cifra pe care vrem sa o adaugam la rezultat. Asupra ei se impun constrangerile
                        trebuie ca: 1 <= noua_cifra <= cifra_maxima
    :param cifra_maxima: cifra maxima pana la care noua cifra adaugata poate lua valori
    :return: True, daca conditiile impuse sunt indeplinite; False, altfel
    '''
    if 1 <= cifra_noua and cifra_noua <= cifra_maxima:
        return True
    else:
        return False


lungime_maxima = 2
cifra_maxima = 3
lista_initiala = []
for i in range(0, lungime_maxima):
    lista_initiala.append(0)

print("Toate combinatiile de numere de", lungime_maxima, "cifre formate din numere de la 1 la", cifra_maxima, "sunt:")
backtracking_toate_combinatiile_posibile(lungime_maxima, cifra_maxima, 0, lista_initiala)

#Din punct de vedere al complexitatii de timp, generarea tuturor combinatiilor de numere de la 1 la N va executa N la
#puterea N pasi. Daca vrem doar permutarile, se vor executa N! pasi.
#Ambele complexitati sunt foarte mari, iar de aceea acesti algoritmi nu sunt folositi pentru solutii de dimensiuni mari.