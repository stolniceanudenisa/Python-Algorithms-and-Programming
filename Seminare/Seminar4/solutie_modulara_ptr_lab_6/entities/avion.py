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
