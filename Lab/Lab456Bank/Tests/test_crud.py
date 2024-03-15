from Domain.tranzactie import creeaza_tranzactie, get_ziua
from Logic.crud import create, read, update, delete_from_a_day, delete_between_a_period, delete_tranzactions_by_type
from Tests.test_elim_tranz_mai_mici_decat_suma import test_elim_tranz_mai_mici_decat_suma
from Tests.test_elimina_tranz_anumit_tip import test_elimina_tranz_anumit_tip
from Tests.test_sold_cont_la_o_data import test_sold_cont_la_o_data
from Tests.test_suma_totala_tranzactii_anumit_tip import test_suma_totala_tranzactii_anumit_tip
from Tests.test_tipareste_tranz_tip_ordonat_dupa_suma import test_tipareste_tranz_tip_ordonat_dupa_suma
from Tests.test_tipareste_tranzactii_de_un_anumit_tip import test_tipareste_tranzactii_de_un_anumit_tip
from Tests.test_tranzactii_inainte_de_o_zi_mai_mari_decat_s import test_tranzactii_inainte_de_o_zi_mai_mari_decat_s
from Tests.test_tranzactii_mai_mari_decat_o_suma_data import test_tranzactii_mai_mari_decat_o_suma_data
from Tests.test_undo_redo import test_undo_redo


def get_data():
    return [
        creeaza_tranzactie(12, 200, 'intrare'),
        creeaza_tranzactie(2, 1200, 'iesire'),
        creeaza_tranzactie(31, 50, 'iesire'),
        creeaza_tranzactie(4, 10000, 'intrare'),
        creeaza_tranzactie(15, 100.50, 'intrare'),
        creeaza_tranzactie(26, 144, 'iesire'),
        creeaza_tranzactie(7, 341121, 'iesire'),
    ]


def test_create():
    tranzactii = get_data()
    params = (18, 800, 'intrare', [], [])
    t_new = creeaza_tranzactie(*params[:-2])
    new_tranzactii = create(tranzactii, *params)

    assert len(new_tranzactii) == len(tranzactii) + 1
    assert t_new in new_tranzactii


def test_read():
    tranzactii = get_data()
    some_t = tranzactii[2]
    assert read(tranzactii, get_ziua(some_t)) == some_t
    assert read(tranzactii, None) == tranzactii


def test_update():
    tranzactii = get_data()
    t_updated = creeaza_tranzactie(15, 1550, 'iesire')
    updated = update(tranzactii, t_updated, [], [])
    assert t_updated in updated
    assert t_updated not in tranzactii
    assert len(updated) == len(tranzactii)


def test_delete_from_a_day():
    tranzactii = get_data()
    to_delete = 4
    deleted = delete_from_a_day(tranzactii, to_delete, [], [])
    assert len(deleted) != len(tranzactii)
    assert len(deleted) == 6


def test_delete_between_a_period():
    tranzactii = get_data()
    ziua_inceput_to_delete = 6
    ziua_sfarsit_to_delete = 22
    deleted = delete_between_a_period(tranzactii, ziua_inceput_to_delete, ziua_sfarsit_to_delete, [], [])
    assert len(deleted) == 4
    assert len(tranzactii) != len(deleted)


def test_delete_tranzactions_by_type():
    tranzactii = get_data()
    tip_to_delete = 'intrare'
    deleted = delete_tranzactions_by_type(tranzactii, tip_to_delete, [], [])
    assert len(deleted) == 4
    assert len(deleted) != len(tranzactii)


def test_all():
    test_create()
    test_read()
    test_update()
    test_delete_from_a_day()
    test_delete_between_a_period()
    test_delete_tranzactions_by_type()
    test_tranzactii_mai_mari_decat_o_suma_data()
    test_tranzactii_inainte_de_o_zi_mai_mari_decat_s()
    test_tipareste_tranzactii_de_un_anumit_tip()

    test_suma_totala_tranzactii_anumit_tip()
    test_sold_cont_la_o_data()
    test_tipareste_tranz_tip_ordonat_dupa_suma()

    test_elimina_tranz_anumit_tip()
    test_elim_tranz_mai_mici_decat_suma()

    test_undo_redo()
