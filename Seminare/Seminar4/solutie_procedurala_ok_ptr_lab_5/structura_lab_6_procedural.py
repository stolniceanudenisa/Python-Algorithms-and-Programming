'''
Cerinta: Creati o aplicatie tip consola care sa managerieze o flota de avioane.
Un avion este descris printr-un cod numeric unic, un tip, o culoare si un an al fabricatiei.
'''

#####
#####-----------------------------------------------DOMENIU/MODEL
#####

#aici initializam entitatile noastre din problema -> avionul

def initializeaza_avion(cod, tip, culoare, an_fabricatie):
    '''
    Functie care initializeaza un avion cu niste valori pentru proprietatile cod, tip, culoare si an_fabricatie
    :param cod: codul numeric unic al avionului creat
    :param tip: tipul avionului creat
    :param culoare: culoarea avionului creat
    :param an_fabricatie: anul fabricatiei avionului creat
    :return: dictionar care va descrie un anumit avion
    '''
    dictionar_avion = { "cod": cod, "tip": tip, "culoare": culoare, "an_fabricatie": an_fabricatie }
    return dictionar_avion

#------------------getteri:
#returneaza o proprietate a dictionarului avion (pe care il transmitem ca parametru)

def get_cod(avion):
    return avion["cod"]

def get_tip(avion):
    return avion["tip"]

def get_culoare(avion):
    return avion["culoare"]

def get_an_fabricatie(avion):
    return avion["an_fabricatie"]

#------------------setteri
#setam o proprietate a dictionarului avion transmis ca parametru astfel incat ea sa aiba o anumita valoare data
def set_cod(avion, cod_nou):
    avion["cod"] = cod_nou

def set_tip(avion, tip_nou):
    avion["tip"] = tip_nou

def set_culoare(avion, culoare_noua):
    avion["culoare"] = culoare_noua

def set_an_fabricatie(avion, an_nou):
    avion["an_fabricatie"] = an_nou

#------------------to_string
#in functia to_string(avion) vom formata frumos proprietatile avionului
def to_string(avion):
    string = ""
    string = string + "Avion cod = " + str(get_cod(avion)) + "\n"
    string = string + "tip = " + get_tip(avion) + "\n"
    string = string + "culoare = " + get_culoare(avion) + "\n"
    string = string + "an_fabricatie = " + str(get_an_fabricatie(avion)) + "\n"
    return string

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

#####
#####-----------------------------------------------INTERFATA UTILIZATOR/USER INTERFACE(UI)
#####

#pana acum am doar am returnat valori, liste, dictionare. Nu am citit si nu am facut printuri in consola
#aici vom citi valori si vom tipari in consola valorile returnate de functiile pe care le-am scris mai sus

def ui_adauga_avion(lista_avioane, lista_undo):
    try:
        cod = int(input("Introduceti cod:"))
        if exista_cod(lista_avioane, cod) == False:
            tip = input("Introduceti tip:")
            culoare = input("Introduceti culoare:")
            an_fabricatie = int(input("Introduceti anul fabricatiei:"))
            avion = initializeaza_avion(cod, tip, culoare, an_fabricatie)
            adauga_avion(lista_avioane, avion)
            #----------------------------Pentru undo------------------------------
            #acum am efectuat o adaugare de avion
            #cand vom vrea sa facem undo la aceasta operatie, va trebui sa stergem avionul adaugat
            #noi putem sterge un avion din lista, dupa codul lui unic
            #de aceea, in lista pe care o vom folosi pentru undo, adaugam numele operatiei opuse adaugarii pe care am facut-o
            #(in cazul nostru, operatia opusa lui "adauga" este "sterge")
            #si mai adaugam si parametrii pe care functia de stergere ii va folosi cand va fi apelata (codul avionului adaugat acum)
            #functia de stergere propriu zisa va fi apelata cand facem undo, in functia def undo(lista_avioane, lista_undo): definita putin mai sus
            lista_parametri = [cod] #lista_parametri este o lista formata din codul avionului adaugat
            adauga_in_undo(lista_undo, "sterge", lista_parametri)
            #---------------------------------------------------------------------
        else:
            print("Cod deja folosit! Reincercati")
    except:
        print("Date incorecte! Reincercati!")

def ui_tipareste_avioane(lista_avioane):
    if len(lista_avioane) == 0:
        print("Lista de avioane este goala!")
    for i in range(0, len(lista_avioane)):
        avion_curent = lista_avioane[i]
        print(to_string(avion_curent))

def ui_sterge_avion(lista_avioane, lista_undo):
    try:
        cod = int(input("Introduceti codul avionului pe care vreti sa il stergeti:"))
        if exista_cod(lista_avioane, cod) == True:
            avion_sters = sterge_avion(lista_avioane, cod)
            # ----------------------------Pentru undo------------------------------
            #acum am efectuat stergerea unui avion
            #cand vom vrea sa facem undo la aceasta operatie, va trebui sa adaugam inapoi avionul pe care l-am sters
            #functia sterge_avion() pe care am apelat-o mai sus ne returneaza avionul sters
            #in lista pe care o vom folosi pentru undo, adaugam numele operatiei opuse stergerii pe care am facut-o
            #(in cazul nostru, operatia opusa lui "sterge" este "adauga")
            #si mai adaugam si parametrii pe care functia de adaugare ii va folosi cand va fi apelata
            #(adica o lista continand doar avionul pe care acum l-am sters si pe care cand facem undo vom vrea sa il adaugam inapoi)
            #functia de adaugare propriu zisa va fi apelata cand vom face undo, in functia def undo(lista_avioane, lista_undo): definita putin mai sus
            lista_parametri = [avion_sters] #lista_parametri este o lista formata din avionul sters
            adauga_in_undo(lista_undo, "adauga", lista_parametri)
            #----------------------------------------------------------------------
        else:
            print("Cod inexistent! Reincercati!")
    except:
        print("Date incorecte! Reincercati!")

def ui_modifica_avion(lista_avioane, lista_undo):
    try:
        cod = int(input("Introduceti codul avionului pe care vreti sa il modificati:"))
        if exista_cod(lista_avioane, cod) == True:
            tip = input("Introduceti tip:")
            culoare = input("Introduceti culoare:")
            an_fabricatie = int(input("Introduceti anul fabricatiei:"))
            avion = get_avion_by_cod(lista_avioane, cod)
            #----------------------------Pentru undo------------------------------
            #acum am efectuat modificarea unui avion
            #cand vom vrea sa facem undo la aceasta operatie, va trebui sa modificam inapoi avionul cu datele initiale
            #functia get_avion_by_cod() pe care am apelat-o mai sus ne returneaza avionul pe care URMEAZA sa il modificam
            #in lista pe care o vom folosi pentru undo, adaugam numele operatiei opuse modificarii pe care am facut-o
            #(in cazul nostru, operatia opusa lui "modifica" este tot "modifica") DOAR CA:
            #aici sunt importanti parametrii pe care functia de modificare ii va folosi cand va fi apelata
            #(adica datele avionului INAINTE de modificare, pe care le vom restabili cand vom face undo la aceasta modificare)
            #functia care modifica avionul inapoi va fi apelata cand vom face undo, in functia def undo(lista_avioane, lista_undo): definita putin mai sus
            lista_parametri = [get_cod(avion), get_tip(avion), get_culoare(avion), get_an_fabricatie(avion)] #lista parametrilor de care functia modifica_avion pe care o vom apela cand facem undo va avea nevoie:
            #este important ca in aceasta lista sa adaugam datele avionului INAINTE de modificare, pentru ca atunci cand facem undo ele sa ne descrie avionul initial
            adauga_in_undo(lista_undo, "modifica", lista_parametri)
            #----------------------------------------------------------------------
            modifica_avion(lista_avioane, cod, tip, culoare, an_fabricatie) #modificam avionul DOAR DUPA CE am salvat datele initiale in lista de undo
        else:
            print("Cod inexistent! Reincercati!")
    except:
        print("Date incorecte! Reincercati!")

def ui_tipareste_avioane_dupa_culoare(lista_avioane):
    culoare = input("Introduceti culoarea:")
    avioane = returneaza_avioane_dupa_culoare(lista_avioane, culoare)
    ui_tipareste_avioane(avioane)

def ui_tipareste_numarul_avioanelor_dupa_tip(lista_avioane):
    dictionar = returneaza_numarul_avioanelor_dupa_tip(lista_avioane)
    print(dictionar)

def ui_tipareste_lista_sortata(lista_avioane):
    lista_sortata = sorteaza_avioane_dupa_an_fabricatie(lista_avioane)
    ui_tipareste_avioane(lista_sortata)

def ui_sterge_avioane_interval(lista_avioane, lista_undo):
    try:
        pozitie_inceput = int(input("Introduceti pozitia de inceput a intervalului:"))
        pozitie_final = int(input("Introduceti pozitia de sfarsit a intervalului:"))
        if exista_interval(lista_avioane, pozitie_inceput, pozitie_final):
            avioane_sterse = sterge_avioane_interval(lista_avioane, pozitie_inceput, pozitie_final)
            #----------------------------Pentru undo------------------------------
            #acum am efectuat stergerea mai multor avioane
            #cand vom vrea sa facem undo la aceasta operatie, va trebui sa adaugam inapoi avioanele pe care l-am sters
            #functia sterge_avioane_interval() pe care am apelat-o mai sus ne returneaza avioanele sterse
            #in lista pe care o vom folosi pentru undo, adaugam numele operatiei opuse stergerii pe care am facut-o
            #(in cazul nostru, operatia opusa lui "sterge" este "adauga")
            #si mai adaugam si parametrii pe care functia de adaugare ii va folosi cand va fi apelata
            #(adica lista avioanelor pe care acum le-am sters si pe care cand facem undo vom vrea sa le adaugam inapoi: avioane_sterse)
            #functia de adaugare propriu zisa va fi apelata cand vom face undo, in functia def undo(lista_avioane, lista_undo): definita putin mai sus
            adauga_in_undo(lista_undo, "adauga", avioane_sterse)
            #----------------------------------------------------------------------
        else:
            print("Interval gresit! Reincercati!")
    except:
        print("Interval invalid! Reincercati!")

def ui_undo(lista_avioane, lista_undo):
    if len(lista_undo) == 0:
        print("Lista e in starea initiala.")
    else:
        undo(lista_avioane, lista_undo)

def meniu():
    meniu = "MENIU\n"
    meniu = meniu + "1. Tipareste toate avioanele\n"
    meniu = meniu + "2. Adauga avion\n"
    meniu = meniu + "3. Sterge avion\n"
    meniu = meniu + "4. Modificare avion\n"
    meniu = meniu + "5. Tipareste toate avioanele de o anumita culoare\n"
    meniu = meniu + "6. Tipareste numarul avioanelor, dupa tip\n"
    meniu = meniu + "7. Tipareste toate avioanele, sortate descrescator dupa anul fabricatiei\n"
    meniu = meniu + "8. Sterge avioane dintr-un interval de pozitii\n"
    meniu = meniu + "9. Undo\n"
    meniu = meniu + "0. Iesire\n"
    return meniu

def lista_avioane_precompletata():
    lista_avioane = []
    avion1 = initializeaza_avion(123, "Boeing", "alb", 2010)
    avion2 = initializeaza_avion(124, "MIG", "negru", 2006)
    avion3 = initializeaza_avion(125, "Eurofighter Typhoon", "gri", 2008)
    avion4 = initializeaza_avion(126, "Hercules", "alb", 2010)
    avion5 = initializeaza_avion(127, "MIG", "camuflaj", 2003)
    lista_avioane.append(avion1)
    lista_avioane.append(avion2)
    lista_avioane.append(avion3)
    lista_avioane.append(avion4)
    lista_avioane.append(avion5)
    return lista_avioane


def program():
    lista_avioane = lista_avioane_precompletata()
    lista_undo = [] #initializam o lista de undo, care la inceput va fi goala
    #o dam ca parametru doar functiilor care fac operatii ce modifica lista de avioane: adauga, modifica, sterge, sterge interval
    ruleaza = True
    while ruleaza == True:
        meniul_meu = meniu()
        print(meniul_meu)
        comanda = input("Introduceti comanda:")
        if comanda == "1":
            ui_tipareste_avioane(lista_avioane)
        elif comanda == "2":
            ui_adauga_avion(lista_avioane, lista_undo)
        elif comanda == "3":
            ui_sterge_avion(lista_avioane, lista_undo)
        elif comanda == "4":
            ui_modifica_avion(lista_avioane, lista_undo)
        elif comanda == "5":
            ui_tipareste_avioane_dupa_culoare(lista_avioane)
        elif comanda == "6":
            ui_tipareste_numarul_avioanelor_dupa_tip(lista_avioane)
        elif comanda == "7":
            ui_tipareste_lista_sortata(lista_avioane)
        elif comanda == "8":
            ui_sterge_avioane_interval(lista_avioane, lista_undo)
        elif comanda == "9":
            ui_undo(lista_avioane, lista_undo)
        elif comanda == "0":
            ruleaza = False
        else:
            print("Comanda invalida! Reincercati!")


#####
#####-----------------------------------------------TESTE
#####

def test():
    #testam functiile din MODEL
    avion = initializeaza_avion(123, "Boeing", "alb", 2010)
    assert avion == { "cod": 123, "tip": "Boeing", "culoare": "alb", "an_fabricatie": 2010}
    assert get_culoare(avion) == "alb"
    set_tip(avion, "Hercules")
    assert get_tip(avion) == "Hercules"

    #testam functiile din REPOSITORY
    lista_avioane = []
    avion1 = initializeaza_avion(123, "Boeing", "alb", 2010)
    adauga_avion(lista_avioane, avion1)
    assert len(lista_avioane) == 1
    modifica_avion(lista_avioane, 123, "Cessna", "alb", "1999")
    assert len(lista_avioane) == 1
    assert get_tip(lista_avioane[0]) == "Cessna"
    sterge_avion(lista_avioane, 123)
    assert len(lista_avioane) == 0

    #testam functiile din CONTROLLER
    lista_avioane = []
    avion2 = initializeaza_avion(123, "Cessna", "alb", 2010)
    lista_avioane.append(avion2)
    assert returneaza_numarul_avioanelor_dupa_tip(lista_avioane) == {"Cessna":1}

    print("Testele au trecut!")



test()
program()