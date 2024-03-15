from Domain.film import Film


def test_film_getteri():
    film = Film('1', 'Avengers', 'SF', '3')
    assert film.get_id_film() == '1'
    assert film.get_titlu_film() == 'Avengers'
    assert film.get_descriere_film() == 'SF'
    assert film.get_numar_stele_film() == '3'


def test_film_setteri():
    film = Film('1', 'Avengers', 'SF', '3')
    film.set_id_film('7')
    assert film.get_id_film() == '7'

    film.set_titlu_film('Ion')
    assert film.get_titlu_film() == 'Ion'

    film.set_descriere_film('Romanesc')
    assert film.get_descriere_film() == 'Romanesc'

    film.set_numar_stele_film('2')
    assert film.get_numar_stele_film() == '2'
