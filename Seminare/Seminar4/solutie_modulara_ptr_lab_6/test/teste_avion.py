from seminar4.solutie_modulara_ptr_lab_6.entities.avion import *
from seminar4.solutie_modulara_ptr_lab_6.operations.operatii_avion import *

#####
#####-----------------------------------------------TESTE
#####

def test_model():
    #testam functiile din MODEL
    avion = initializeaza_avion(123, "Boeing", "alb", 2010)
    assert avion == { "cod": 123, "tip": "Boeing", "culoare": "alb", "an_fabricatie": 2010}
    assert get_culoare(avion) == "alb"
    set_tip(avion, "Hercules")
    assert get_tip(avion) == "Hercules"

    print("Testele au trecut!")

def test_operations():
    #testam functiile din operations:

    # testam functiile din REPOSITORY
    lista_avioane = []
    avion1 = initializeaza_avion(123, "Boeing", "alb", 2010)
    adauga_avion(lista_avioane, avion1)
    assert len(lista_avioane) == 1
    modifica_avion(lista_avioane, 123, "Cessna", "alb", "1999")
    assert len(lista_avioane) == 1
    assert get_tip(lista_avioane[0]) == "Cessna"
    sterge_avion(lista_avioane, 123)
    assert len(lista_avioane) == 0

    # testam functiile din CONTROLLER
    lista_avioane = []
    avion2 = initializeaza_avion(123, "Cessna", "alb", 2010)
    lista_avioane.append(avion2)
    assert returneaza_numarul_avioanelor_dupa_tip(lista_avioane) == {"Cessna": 1}

    print("Testele au trecut!")


def teste():
    test_model()
    test_operations()
