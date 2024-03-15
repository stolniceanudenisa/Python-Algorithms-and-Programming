from seminar4.solutie_modulara_ptr_lab_6.entities.avion import *

#####
#####-----------------------------------------------REPOSITORY
#####

#aici facem OPERATII DE BAZA cu lista noastra de avioane

#adaugam elemente
def adauga_avion(lista_avioane, avion_nou):
    '''
    Functie ce adauga un nou avion
    :param lista_avioane:
    :param avion_nou:
    :return:
    '''
    lista_avioane.append(avion_nou)

#stergem elemente
def sterge_avion(lista_avioane, cod):
    '''
    Functie care sterge un aviod dupa codul sau unic
    :param lista_avioane:
    :param cod: codul unic de identificare al avionului
    :return: avion_sters
    '''

    avion_sters = {}
    i = 0
    while i < len(lista_avioane):
        avion_curent = lista_avioane[i]
        if get_cod(avion_curent) == cod:
            avion_sters = lista_avioane.pop(i)
            i = i - 1
        i = i + 1
    return avion_sters

#modificam elemente
def modifica_avion(lista_avioane, cod, tip_nou, culoare_noua, an_nou):
    '''
    Functie care modifica proprietatile unui avion
    :param lista_avioane:
    :param cod:
    :param tip_nou:
    :param culoare_noua:
    :param an_nou:
    :return:
    '''
    for i in range(0, len(lista_avioane)):
        avion_curent = lista_avioane[i]
        if get_cod(avion_curent) == cod:
            set_tip(avion_curent, tip_nou)
            set_culoare(avion_curent, culoare_noua)
            set_an_fabricatie(avion_curent, an_nou)

def get_avion_by_cod(lista_avioane, cod):
    '''
    Functie ce returneaza un avion dupa cod
    :param lista_avioane:
    :param cod:
    :return: avion
    '''

    for avion in lista_avioane:
        if get_cod(avion) == cod:
            return avion
    return {}


#####
#####-----------------------------------------------CONTROLLER
#####

#aici facem OPERATII COMPLEXE cu avioanele noastre

def returneaza_avioane_dupa_culoare(lista_avioane, culoare):
    '''
    Functie care returneaza lista avioanelor avand culoarea data
    :param lista_avioane: lista tuturor avioanelor
    :param culoare: culoarea data
    :return: lista avioanelor a caror culoare e egala cu culoarea data
    '''
    lista_avioane_culoare = []
    for i in range(0, len(lista_avioane)):
        avion_curent = lista_avioane[i]
        if get_culoare(avion_curent) == culoare:
            lista_avioane_culoare.append(avion_curent)
    return lista_avioane_culoare

def returneaza_numarul_avioanelor_dupa_tip(lista_avioane):
    '''
    Functie ce returneaza numarul avioanelor noastre pentru fiecare tip de avion
    :param lista_avioane:
    :return: un dictionar in care cheile sunt tipurile de avion din lista,
            iar valorile reprezinta numarul avioanelor de acel tip
    '''
    dictionar = {}
    for i in range(0, len(lista_avioane)):
        avion_curent = lista_avioane[i]
        tip = get_tip(avion_curent)
        if tip not in dictionar:
            dictionar[tip] = 1
        else:
            dictionar[tip] = dictionar[tip] + 1
    return dictionar

def sorteaza_avioane_dupa_an_fabricatie(lista_avioane):
    '''
    Functie care returneaza lista avioanelor sortata dupa anul fabricatiei
    :param lista_avioane:
    :return:
    '''
    #vrem ca lista sa fie sortata dupa anul fabricatiei
    #deci pentru key= dam numele functiei care returneaza anul fabricatiei (getter-ul definit de noi in MODEL)
    #vrem ca lista sa fie sortata descrescator, deci pentru reverse= dam valoarea True (reverse inseamna invers)
    lista_sortata = sorted(lista_avioane, key=get_an_fabricatie, reverse=True)
    return lista_sortata

def exista_cod(lista_avioane, cod):
    '''
    Functie care verifica daca un cod de identificare exista in lista de avioane
    :param lista_avioane:
    :param cod:
    :return: True, daca codul exista deja in lista; False, altfel
    '''
    if get_avion_by_cod(lista_avioane, cod) != {}:
        return True
    else:
        return False

def exista_interval(lista, inceput, final):
    '''
    Functie care verifica daca un interval dat exista in lista
    :param lista:
    :param inceput:
    :param final:
    :return: True, daca intervalul exista in lista (e unul corect); False, altfel
    '''
    if inceput < 1 or inceput > final or final > len(lista):
        return False
    else:
        return True

def sterge_avioane_interval(lista_avioane, inceput, final):
    '''
    Functie care sterge toate avioanele dintr-un interval dat
    :param lista_avioane:
    :param inceput: pozitia de inceput a intervalului
    :param final: pozitia de sfarsit a intervalului
    :return: avioane_sterse
    '''
    avioane_sterse = []
    pozitie = inceput - 1
    for numar_de_stergeri in range(final-inceput+1):
        avion = lista_avioane[pozitie]
        avion_sters = sterge_avion(lista_avioane, get_cod(avion))
        avioane_sterse.append(avion_sters)
    return avioane_sterse

def adauga_in_undo(lista_undo, nume_comanda, lista_parametri):
    '''
    Functie care adauga o comanda si parametrii aferenti in lista de undo
    :param lista_undo:
    :param nume_comanda:
    :param lista_parametri:
    :return:
    '''
    #initial nume_comanda e un sir de caractere de genul "modifica", "sterge", "adauga"
    #iar lista_parametri contine parametrii de care avem nevoie pentru a executa comanda
    #(daca nume_comanda e "modifica", lista_parametri e o lista cu parametrii initiali ai avionului: [124, "MIG", "negru", 2006])
    lista_parametri.insert(0, nume_comanda) #adaugam pe prima pozitie in lista_parametri numele comenzii
    #astfel, lista_parametri, devine ["modifica", 124, "MIG", "negru", 2006]
    lista_undo.append(lista_parametri) #adaugam aceasta lista in lista_undo (la final)

def undo(lista_avioane, lista_undo):
    '''
    Functie care face undo la ultima operatie
    :param lista_avioane:
    :param lista_undo:
    :return:
    '''
    #Exemplu de executie:
    #daca apelam undo dupa ce intai am facut o adaugare de avion (cu codul, sa zicem, 130) si apoi o modificare a avionului cu codul 124
    #lista_undo va arata in felul urmator: [   ["sterge", 130],     ["modifica", 124, "MIG", "negru", 2006]  ]
    #observati ca lista_undo este o lista de liste.
    #Ficare sublista a listei de undo contine:
    #pe prima pozitie (pozitia 0): numele operatiei pe care trebuie sa o efectuam ca sa facem undo ("sterge", "modifica")
    #apoi pe urmatoarele pozitii: parametrii acestei operatii
    if len(lista_undo) != 0:
        lista_comanda = lista_undo[len(lista_undo)-1] #ia din lista de undo ultima sublista -> cea corespunzatoare ultimei operatii efectuate (in cazul din exemplul nostru: ["modifica", 124, "MIG", "negru", 2006])
        nume_operatie = lista_comanda[0] #nume operatie va fi primul element din lista_comanda -> adica "modifica"
        if nume_operatie == "sterge": #daca pentru a face undo la ultima operatie e nevoie sa facem o stergere
            cod = lista_comanda[1] #stim ca parametrul corespunzator (codul unic al avionului) e in lista_comanda pe pozitia 1
            sterge_avion(lista_avioane, cod) #efectuam stergerea cu parametrul cod pe care l-am extras
        elif nume_operatie == "adauga": #daca pentru a face undo la ultima operatie e nevoie sa facem o adaugare
            for avion in lista_comanda[1:]: #stim ca parametrii corespunzatori (avionul/avioanele) pe care le adaugam sunt in lista_comanda de la pozitia 1 pana la finalul listei (daca avem de adaugat un singur avion, el va fi singurul parametru din lista)
                adauga_avion(lista_avioane, avion) #adaugam pe rand avioanele din lista_comanda (daca adaugam un singur avion, se va intra in for doar o singura data)
        elif nume_operatie == "modifica": #daca pentru a face undo la ultima operatie e nevoie sa facem o modificare --> ceea ce vom face in exemplul nostru
            cod = lista_comanda[1] #luam din lista_comanda pe rand parametrii pentru cod, tip, culoare si an ce descriu avionul initial
            tip = lista_comanda[2]
            culoare = lista_comanda[3]
            an = lista_comanda[4]
            modifica_avion(lista_avioane, cod, tip, culoare, an) #apelam modificarea pentru avion cu acesti parametri
        lista_undo.pop() #dupa ce am efectuat o operatie de undo, o eliminam din lista de undo
        #noi am efectuat "modifica", deci dupa lista_undo.pop() lista noastra va ramane cu o singura sublista: [ ["sterge", 130] ]
