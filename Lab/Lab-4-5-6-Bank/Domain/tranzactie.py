def creeaza_tranzactie(ziua_tranzactie, suma_tranzactie: float, tip_tranzactie):
    '''
    Creeaza un dictionar ce contine ziua tranzaciei efectuate, suma introdusa si tipul tranzactiei.
    :param ziua_tranzactie:
    :param suma_tranzactie:
    :param tip_tranzactie:
    :return:
    '''
    return {
        'ziua':ziua_tranzactie,
        'suma':suma_tranzactie,
        'tip':tip_tranzactie,
    }


def get_ziua(tranzactie):
    '''
    Getter pentru ziua efectuarii tranzactiei.
    :param tranzactie: tranzactia efectuata.
    :return: ziua in care a fost efectuata tranzactia.
    '''
    return tranzactie['ziua']


def get_suma(tranzactie):
    '''
    Getter pentru suma efectuarii tranzactiei.
    :param tranzactie: tranzactia efectuata.
    :return: suma care a fost introdusa in banca.
    '''
    return tranzactie['suma']


def get_tip(tranzactie):
    '''
    Getter pentru tipul de tranzactie.
    :param tranzactie:t ranzactia efectuata.
    :return: tipul de tranzactie efectuat.
    '''
    return tranzactie['tip']


def get_str(tranzactie):
    return f'Tranzactia facuta in ziua {get_ziua(tranzactie)}, in care a fost introdusa suma: {get_suma(tranzactie)}, de tipul: {get_tip(tranzactie)}'