from seminar4.solutie_modulara_ptr_lab_6.entities.avion import *
from seminar4.solutie_modulara_ptr_lab_6.operations.operatii_avion import *

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

