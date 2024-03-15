from Domain.carte import Carte


def test_carte_getteri():
    carte = Carte('1', 'ion', 'roman', 'lvr')

    assert carte.get_id_carte() == '1'
    assert carte.get_titlu_carte() == 'ion'
    assert carte.get_descriere_carte() == 'roman'
    assert carte.get_autor_carte() == 'lvr'


def test_carte_setteri():
    carte = Carte('1', 'ion', 'roman', 'lvr')

    carte.set_id_carte('7')
    assert carte.get_id_carte() == '7'

    carte.set_titlu_carte('moara cu noroc')
    assert carte.get_titlu_carte() == 'moara cu noroc'

    carte.set_descriere_carte('nuvela')
    assert carte.get_descriere_carte() == 'nuvela'

    carte.set_autor_carte('ioan slavici')
    assert carte.get_autor_carte() == 'ioan slavici'
