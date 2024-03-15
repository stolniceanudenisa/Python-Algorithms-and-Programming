'''
Metodele 'magice' in Python sunt metode care se executa automat, fara sa trebuiasca sa le apelam noi explicit.
Noi am mai folosit astfel de metode: __init__() si __str__()
'''
class Student:

    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    '''
    def __str__(self):
        return "Student " + self.nume + ", " + str(self.varsta) + " ani"
    '''

#Metoda magica __init__() se apeleaza automat cand instantiem o clasa (adica cream un obiect) desi noi nu vedem apelul.
student1 = Student("Ana", 20)

#Vrem sa il tiparim in consola pe student1.
#Cand apelam print(student1), interpretorul Python merge in clasa Student si cauta metoda magica __str__().
#Observati ca acum noi am comentat metoda __str__() din clasa Student.
#Daca aceasta metoda este comentata, interpretorul nu stie sa formateze frumos obiectul pe care vrem sa il tiparim.
#Daca rulati programul asa, in consola se va tipari ceva de genul: <__main__.Student object at 0x000001AA74E70CA0>
print(student1)
#Decomentati metoda magica __str__() din clasa Student. Veti vedea ca acum se va tipari frumos: Student Ana, 19 ani


'''
Alte metode 'magice' in Python si supraincarcarea operatorilor

__init__() si __str__() nu sunt singurele metode magice din Python. 
De fapt, exista multe alte astfel de metode care fac diferite lucruri.
De exemplu:
__add__(), pentru adunare (+)
__sub__(), pentru scadere (-)
__mul__(), pentru inmultire (*)
__eq__(), pentru verificarea egalitatii (==)
__le__(), pentru mai mic sau egal (<=)
__gt__(), pentru mai mare (>)
... 
Gasiti o lista completa + alte explicatii si exemple aici: https://python-course.eu/oop/magic-methods.php

Ce inseamna asta pentru noi?
Inseamna ca atunci cand avem:
a = 1
b = 2
c = a + b
Pentru c = a + b realizarea adunarii specificata de operatorul +, se face prin apelarea automata a metodei __add__()
Ne amintim ca o metoda magica se apeleaza fara sa facem noi apelul explicit.
La fel cum interpretorul Python stia sa apeleze automat metoda __init__() cand instantiam o clasa (s = Student("A", 1))
sau metoda __str__() cand voiam sa tiparim un obiect (print(s)), 
interpretorul va apela automat metoda __add__() atunci cand folosim operatorul +
La final, variabila c va avea valoarea 3.

Similar, pentru:
sir1 = "abc"
sir2 = "...de"
sir3 = sir1 + sir2 #avem operatorul +, deci se apeleaza in mod automat metoda magica __add__()
Apelarea automata a metodei __add__() pentru doua siruri de caractere va returna concatenarea lor: sir3 va fi "abc...de"

Iar pentru:
lista1 = [1,2,4]
lista2 = [0,10,20]
lista3 = lista1 + lista2 #avem operatorul +, deci se apeleaza in mod automat metoda magica __add__() 
Apelarea automata a metodei __add__() va returna cele doua liste concatenate: lista3 va fi [1,2,4,0,10,20]

Asadar, pentru tipul int, + realizeaza adunarea a 2 numere, iar pentru tipul string (sir de caractere) sau pentru liste, 
+ realizeaza concatenarea lor.
Altfel spus, acelasi operator, +, produce comportamente diferite pentru obiecte de tipuri diferite 
(in Python numerele (1,2,3000,...), sirurile de caractere ("abc", "d"), listele ([1, "abc", [100]]) sunt toate obiecte)
Daca numerele, sirurile de caractere si listele sunt obiecte, inseamna ca ele sunt instante ale unei clase.
(Conform definitiei, un obiect este o instanta a unei clase)
Inseamna ca in clasele corespunzatoare pentru numere, siruri de caractere, liste, exista metoda magica __add__() si
este implementata in moduri diferite, in asa fel incat atunci cand folosim operatorul + pentru numere cei doi termeni
vor fi adunati, iar pentru siruri de caractere si liste se va realiza concatenarea lor.

De ce este asta important pentru noi? 
Pentru ca si noi putem face acelasi lucru pentru clasele pe care le definim in programul nostru (ex. Student, Carte,...)
Putem defini metode magice ( __add__(), __eq__(), ...) pe care sa le implementam in asa fel incat atunci cand operatori
precum +, == sunt folositi ca sa faca operatii pe obiectele claselor noastre, sa obtinem comportamentul pe care il dorim
Asta inseamna supraincarcarea operatorilor. 
'''

print("\nExemple de supraincarcare a operatorilor pentru clasa Bani:\n")

class Bani:

    def __init__(self, suma, moneda):
        self.__suma = suma
        self.__moneda = moneda

    def get_suma(self):
        return self.__suma

    def get_moneda(self):
        return self.__moneda

    def __str__(self):
        return str(self.get_suma()) + " " + self.get_moneda()

    def __add__(self, other):
        '''
        Supraincarcarea operatorului +
        Aduna sumele pentru doua obiecte de tip Bani
        Exemple:
        Bani(1, "RON") + Bani(2, "RON") (rezultatul va fi Bani(3, "RON"))
        Bani(4, "RON") + 7              (rezultatul va fi Bani(11, "RON")))
        Metoda considera drept element curent (self) primul termen al adunarii, iar parametrul other devine
        al doilea termen.
        :param other (inseamna celalalt): obiectul din cealalta parte a operatorului +
                                          (cel pe care il adaugam la obiectul curent)
                                          poate fi un obiect de tip Bani sau un numar
        :return: obiect de tip Bani unde suma este cea obtinuta prin adunare
        '''
        if type(other) == Bani:
            return Bani(self.get_suma()+other.get_suma(), self.get_moneda())
        elif type(other) == int or type(other) == float:
            suma_noua = self.get_suma() + other
            return Bani(suma_noua, self.get_moneda())

    def __radd__(self, other):
        '''
        Supraincarcarea operatorului +
        Aduna suma pentru doua obiecte de tip Bani tratand cazul special in care primul termen al adunarii este un numar
        iar obiectul de tip Bani este abia al doilea termen.
        Numele __radd__() cu r in fata vine de la reverse (inseamna invers).
        Metoda interpreteaza inversat ordinea termenilor adunarii astfel incat, chiar daca este al doilea termen
        in adunare, elementul curent (self) devine obiectul de tip Bani, iar parametrul other devine numarul.
        Exemplu:
        7 + Bani(4, "RON")              (rezultatul va fi Bani(11, "RON")))
        Metoda __radd__() interpreteaza adunarea drept Bani(4, "RON") + 7 astfel ca elementul curent (self)
        devine obiectul de tip bani, iar parametrul other devine 7.
        Deoarece metoda __add__() stie deja sa lucreze cu termenii in aceasta ordine, pur si simplu o vom apela pe ea.
        :param other (inseamna celalalt): obiectul din cealalta parte a operatorului +
                                          (cel pe care il adaugam la obiectul curent)
                                          in general, acesta va fi un numar
        :return: obiect de tip Bani unde suma este cea obtinuta prin adunare
        '''
        return Bani.__add__(self, other)

    def __iadd__(self, other):
        '''
        Supraincarcarea operatorului += atunci cand avem expresii de tipul:
        ban = Bani(10, "RON")
        ban += Bani(1, "RON") #inseamna ban = ban + Bani(1, "RON"), doar ca este scris intr-o forma mai scurta
        (acum ban a devenit Bani(11, "RON"))
        Operatia += se numeste adunare "in-place", de acolo vine i-ul din numele metodei __iadd__()
        Metoda __iadd__() interpreteaza adunarea de mai sus drept Bani(10, "RON") + Bani(1, "RON") astfel ca
        elementul curent (self) devine obiectul Bani(10, "RON"), iar parametrul other devine obiectul Bani(1, "RON").
        Deoarece metoda __add__() stie deja sa lucreze cu termenii in aceasta ordine, pur si simplu o vom apela pe ea.
        :param other (inseamna celalalt): obiectul din cealalta parte a operatorului +=
                                          (cel pe care il adaugam la obiectul curent)
                                          poate fi un obiect de tip Bani sau un numar
        :return: obiect de tip Bani unde suma este cea obtinuta prin adunare
        '''
        return Bani.__add__(self, other)

    def __eq__(self, other):
        '''
        Supraincarcarea operatorului ==
        Verifica daca doua obiecte de tip Bani sunt egale.
        Bani(10, "RON") == Bani(10, "RON") #True
        Bani(10, "RON") == 10 #True
        Bani(10, "RON") == 1  #False
        :param other (inseamna celalalt): obiectul din cealalta parte a operatorului ==
                                         (cel cu care comparam obiectul curent)
                                         poate fi un obiect de tip Bani sau un numar
        :return: True, daca obiectele sunt egale; False altfel
        '''
        if type(other) == Bani:
            if self.get_suma() == other.get_suma() and self.get_moneda() == other.get_moneda():
                return True
        elif type(other) == int or type(other) == float:
            if self.get_suma() == other:
                return True
        return False

    def __sub__(self, other):
        '''
        Supraincarcarea operatorului -
        Scade sumele a doua obiecte de tip Bani sau un numar dintr-un obiect de tip Bani.
        Bani(10, "RON") - Bani(4, "RON")
        Bani(10, "RON") - 5
        Exista si formele __isub__() si __rsub__()
        :param other: obiectul de tip Bani sau numarul din cealalta parte a operatorului -
        :return: obiect de tip Bani unde suma este cea obtinuta prin efectuarea scaderii
        '''
        if type(other) == Bani:
            suma_noua = self.get_suma() - other.get_suma()
            return Bani(suma_noua, self.get_moneda())
        if type(other) == int or type(other) == float:
            suma_noua = self.get_suma() - other
            return Bani(suma_noua, self.get_moneda())

    def __mul__(self, other):
        '''
        Supraincarcarea operatorului *
        Inmulteste o suma de bani cu un numar.
        Bani(10, "RON") * 2
        Exista si formele __imul__(), __rmul__()
        :param other: numar
        :return: obiect de tip Bani unde suma este cea obtinuta prin efectuarea inmultirii
        '''
        if type(other) == int or type(other) == float:
            suma_noua = self.get_suma() * other
            return Bani(suma_noua, self.get_moneda())

    def __truediv__(self, other):
        '''
        Supraincarcarea operatorului /
        Imparte o suma de bani la un numar.
        Bani(10, "RON") / 4
        Exista si formele __itruediv__(), __rtruediv__()
        :param other: numar
        :return: obiect de tip Bani unde suma este cea obtinuta prin efectuarea impartirii.
        '''
        if type(other) == int or type(other) == float:
            suma_noua = self.get_suma() / other
            return Bani(suma_noua, self.get_moneda())

    def __le__(self, other):
        '''
        Supraincarcarea operatorului <= (denumirea le vine de la "less than equal"; l de la less, e de la equal)
        Verifica daca un obiect de tip Bani este <= decat alt obiect de tip Bani sau un numar.
        Bani(10, "RON") <= Bani(20, "RON")
        Bani(10, "RON") <= 10
        :param other: obiect de tip Bani sau numar
        :return: True, daca inegalitatea este satisfacuta; False, altfel
        '''
        if type(other) == Bani:
            if self.get_suma() <= other.get_suma():
                return True
        elif type(other) == int or type(other) == float:
            if self.get_suma() <= other:
                return True
        return False

    def __lt__(self, other):
        '''
        Supraincarcarea operatorului < (denumirea vine de la "less than", l de la less, t de la than)
        Verifica daca un obiect de tip Bani este < decat alt obiect de tip Bani sau un numar.
        Bani(10, "RON") < Bani(20, "RON")
        Bani(10, "RON") < 11
        :param other: obiect de tip Bani sau numar
        :return: True, daca inegalitatea este satisfacuta; False, altfel
        '''
        pass

    def __gt__(self, other):
        '''
        Supraincarcarea operatorului > (denumirea vine de la "greather than", g de la greater, t de la than)
        Verifica daca un obiect de tip Bani este > decat alt obiect de tip Bani sau un numar.
        Bani(10, "RON") > Bani(2, "RON")
        Bani(10, "RON") > 9
        :param other: obiect de tip Bani sau numar
        :return: True, daca inegalitatea este satisfacuta; False, altfel
        '''
        if type(other) == Bani:
            if self.get_suma() > other.get_suma():
                return True
        elif type(other) == int or type(other) == float:
            if self.get_suma() > other:
                return True
        return False

    def __ge__(self, other):
        '''
        Supraincarcarea operatorului >= (denumirea vine de la "greater or equal", g de la greater, e de la equal)
        Verifica daca un obiect de tip Bani este >= decat alt obiect de tip Bani sau un numar.
        Bani(10, "RON") >= Bani(1, "RON")
        Bani(10, "RON") >= 10
        :param other: obiect de tip Bani sau numar
        :return: True, daca inegalitatea este satisfacuta; False, altfel
        '''
        pass


ban1 = Bani(2,"RON")
ban2 = Bani(10,"RON")

print("Operatorul + \n")

ban3 = ban1 + ban2
print(ban1, "+", ban2, "=", ban3)
ban4 = ban2 + 1
print(ban2, "+ 1 =", ban4)
ban5 = 1 + ban1
print("1 +", ban1, "=", ban5)
print(ban5, "devine:")
ban5 += ban2
print(ban5)
print(ban5, "+ 100 devine:")
ban5 += 100
print(ban5)
ban6 = 50 + ban1 + 5 + ban2 + ban3
print("50 +", ban1, "+ 5 +", ban2, "+", ban3, "=", ban6)

print("\n\nOperatorul == \n")

valoare_de_adevar1 = ban1 == ban2
print(ban1, "==", ban2, "este", valoare_de_adevar1)
ban7 = Bani(2, "RON")
valoare_de_adevar2 = ban1 == ban7
print(ban1, "==", ban7, "este", valoare_de_adevar2)
valoare_de_adevar3 = ban1 == 2
print(ban1, "== 2 este", valoare_de_adevar3)

print("\n\nOperatorii - * / <= >\n")

ban8 = ban6 - ban1
print(ban6, "-", ban1, "=", ban8)
ban9 = ban1 * 5
print(ban1, "* 5 =", ban9)
ban10 = ban9 / 4
print(ban9, "/ 4 =", ban10)
valoare_de_adevar4 = ban1 <= ban2
print(ban1, "<=", ban2, "este", valoare_de_adevar4)
valoare_de_adevar5 = ban3 > 6
print(ban3, "> 6 este", valoare_de_adevar5)
