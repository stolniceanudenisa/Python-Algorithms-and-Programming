from Domain.tranzactie import creeaza_tranzactie
from Logic.crud import create, delete_from_a_day, delete_between_a_period, delete_tranzactions_by_type, update
from UserInterface.console import handle_undo, handle_redo


def test_undo_redo():
    tranzactii = []
    tranzactii = create(tranzactii, 12, 234, 'intrare', [], [])
    tranzactii = create(tranzactii, 3, 999, 'iesire', [], [])
    tranzactii = create(tranzactii, 7, 12333, 'intrare', [], [])
    tranzactii = create(tranzactii, 13, 4342, 'iesire', [], [])
    tranzactii = create(tranzactii, 1, 10, 'intrare', [], [])
    tranzactii = create(tranzactii, 27, 10000, 'iesire', [], [])
    undo_list = []
    redo_list = []
    params = (17, 300, 'iesire', undo_list, redo_list)
    new_tranzactii = create(tranzactii, *params)

    assert len(tranzactii) + 1 == len(new_tranzactii)

    new_tranzactii = handle_undo(new_tranzactii, undo_list, redo_list)
    assert len(tranzactii) == len(new_tranzactii)

    new_tranzactii = handle_redo(new_tranzactii, undo_list, redo_list)
    assert len(tranzactii) + 1 == len(new_tranzactii)

    ###############################################################################

    tranzactii = []
    tranzactii = create(tranzactii, 12, 234, 'intrare', [], [])
    tranzactii = create(tranzactii, 3, 999, 'iesire', [], [])
    tranzactii = create(tranzactii, 7, 12333, 'intrare', [], [])
    tranzactii = create(tranzactii, 13, 4342, 'iesire', [], [])
    tranzactii = create(tranzactii, 1, 10, 'intrare', [], [])
    tranzactii = create(tranzactii, 27, 10000, 'iesire', [], [])
    undo_list = []
    redo_list = []

    ziua_tranzactie = 13
    new_tranzactii = delete_from_a_day(tranzactii, ziua_tranzactie, undo_list, redo_list)
    assert len(tranzactii) != len(new_tranzactii)

    assert len(new_tranzactii) == 5

    new_tranzactii = handle_undo(new_tranzactii, undo_list, redo_list)
    assert len(new_tranzactii) == 6

    new_tranzactii = handle_redo(new_tranzactii, undo_list, redo_list)
    assert len(tranzactii) != len(new_tranzactii)
    assert len(new_tranzactii) == 5

    new_tranzactii = handle_undo(new_tranzactii, undo_list, redo_list)
    assert len(new_tranzactii) == 6

    ###############################################################################
    tranzactii = []
    tranzactii = create(tranzactii, 1, 200.234, 'intrare', undo_list, redo_list)
    tranzactii = create(tranzactii, 2, 1200.777, 'iesire', undo_list, redo_list)
    tranzactii = create(tranzactii, 11, 50.23, 'iesire', undo_list, redo_list)
    tranzactii = create(tranzactii, 14, 10000, 'intrare', undo_list, redo_list)
    tranzactii = create(tranzactii, 22, 100.50, 'intrare', undo_list, redo_list)

    undo_list = []
    redo_list = []
    new_tranzactii = delete_between_a_period(tranzactii, 9, 16, undo_list, redo_list)

    assert len(new_tranzactii) == 3
    assert len(tranzactii) != len(new_tranzactii)

    new_tranzactii = handle_undo(new_tranzactii, undo_list, redo_list)
    assert len(new_tranzactii) == 5

    new_tranzactii = handle_redo(new_tranzactii, undo_list, redo_list)
    assert len(new_tranzactii) == 3
    assert len(tranzactii) != len(new_tranzactii)

    new_tranzactii = handle_undo(new_tranzactii, undo_list, redo_list)
    assert len(new_tranzactii) == 5

    ###############################################################################

    tranzactii = []
    tranzactii = create(tranzactii, 12, 234, 'intrare', [], [])
    tranzactii = create(tranzactii, 3, 999, 'iesire', [], [])
    tranzactii = create(tranzactii, 7, 12333, 'intrare', [], [])
    tranzactii = create(tranzactii, 13, 4342, 'iesire', [], [])
    tranzactii = create(tranzactii, 1, 10, 'intrare', [], [])
    tranzactii = create(tranzactii, 27, 10000, 'iesire', [], [])
    undo_list = []
    redo_list = []
    tip_tranzactie = 'iesire'
    new_tranzactii = delete_tranzactions_by_type(tranzactii, tip_tranzactie, undo_list, redo_list)
    assert len(tranzactii) != len(new_tranzactii)
    assert len(new_tranzactii) == 3

    new_tranzactii = handle_undo(new_tranzactii, undo_list, redo_list)
    assert len(new_tranzactii) == 6

    new_tranzactii = handle_redo(new_tranzactii, undo_list, redo_list)
    assert len(tranzactii) != len(new_tranzactii)
    assert len(new_tranzactii) == 3

    ###############################################################################

    tranzactii = []
    tranzactii = create(tranzactii, 12, 234, 'intrare', [], [])
    tranzactii = create(tranzactii, 3, 999, 'iesire', [], [])
    tranzactii = create(tranzactii, 7, 12333, 'intrare', [], [])
    tranzactii = create(tranzactii, 13, 4342, 'iesire', [], [])
    tranzactii = create(tranzactii, 1, 10, 'intrare', [], [])
    tranzactii = create(tranzactii, 27, 10000, 'iesire', [], [])
    undo_list = []
    redo_list = []

    new_tranz = creeaza_tranzactie(7, 1111, 'iesire')

    new_tranzactii = update(tranzactii, new_tranz, undo_list, redo_list)
    assert len(tranzactii) == len(new_tranzactii)

    new_tranzactii = handle_undo(new_tranzactii, undo_list, redo_list)

    assert tranzactii == new_tranzactii

    new_tranzactii = handle_redo(new_tranzactii, undo_list, redo_list)
    assert tranzactii != new_tranzactii
