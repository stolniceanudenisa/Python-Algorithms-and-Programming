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
    :return:
    '''
    for avion in lista_avioane:
        if get_cod(avion) == cod:
            lista_avioane.remove(avion)

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

#####
#####-----------------------------------------------INTERFATA UTILIZATOR/USER INTERFACE(UI)
#####

#pana acum am doar am returnat valori, liste, dictionare. Nu am citit si nu am facut printuri in consola
#aici vom citi valori si vom tipari in consola valorile returnate de functiile pe care le-am scris mai sus

def ui_adauga_avion(lista_avioane):
    cod = int(input("Introduceti cod:"))
    tip = input("Introduceti tip:")
    culoare = input("Introduceti culoare:")
    an_fabricatie = int(input("Introduceti anul fabricatiei:"))
    avion = initializeaza_avion(cod, tip, culoare, an_fabricatie)
    lista_avioane.append(avion)

def ui_tipareste_avioane(lista_avioane):
    if len(lista_avioane) == 0:
        print("Lista de avioane este goala!")
    for i in range(0, len(lista_avioane)):
        avion_curent = lista_avioane[i]
        print(to_string(avion_curent))

def ui_sterge_avion(lista_avioane):
    cod = int(input("Introduceti codul avionului pe care vreti sa il stergeti:"))
    sterge_avion(lista_avioane, cod)

def ui_modifica_avion(lista_avioane):
    cod = int(input("Introduceti codul avionului pe care vreti sa il modificati:"))
    tip = input("Introduceti tip:")
    culoare = input("Introduceti culoare:")
    an_fabricatie = int(input("Introduceti anul fabricatiei:"))
    modifica_avion(lista_avioane, cod, tip, culoare, an_fabricatie)

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

def meniu():
    meniu = "MENIU\n"
    meniu = meniu + "1. Tipareste toate avioanele\n"
    meniu = meniu + "2. Adauga avion\n"
    meniu = meniu + "3. Sterge avion\n"
    meniu = meniu + "4. Modificare avion\n"
    meniu = meniu + "5. Tipareste toate avioanele de o anumita culoare\n"
    meniu = meniu + "6. Tipareste numarul avioanelor, dupa tip\n"
    meniu = meniu + "7. Tipareste toate avioanele, sortate descrescator dupa anul fabricatiei\n"
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
    ruleaza = True
    while ruleaza == True:
        meniul_meu = meniu()
        print(meniul_meu)
        comanda = input("Introduceti comanda:")
        if comanda == "1":
            ui_tipareste_avioane(lista_avioane)
        elif comanda == "2":
            ui_adauga_avion(lista_avioane)
        elif comanda == "3":
            ui_sterge_avion(lista_avioane)
        elif comanda == "4":
            ui_modifica_avion(lista_avioane)
        elif comanda == "5":
            ui_tipareste_avioane_dupa_culoare(lista_avioane)
        elif comanda == "6":
            ui_tipareste_numarul_avioanelor_dupa_tip(lista_avioane)
        elif comanda == "7":
            ui_tipareste_lista_sortata(lista_avioane)
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