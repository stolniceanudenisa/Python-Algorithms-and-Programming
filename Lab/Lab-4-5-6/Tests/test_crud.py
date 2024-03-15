from Domain.prajitura import creeaza_prajitura, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        creeaza_prajitura(1, 'p1', 'desc1', 100, 50, 2018),
        creeaza_prajitura(2, 'p2', 'desc2', 60.7, 80.32, 2015),
        creeaza_prajitura(3, 'p3', 'desc3', 0, 20, 2012),
        creeaza_prajitura(4, 'p4', 'desc4', 153534, 150, 2017),
        creeaza_prajitura(5, 'p5', 'desc5', 40.7775, 40.32, 2016),
    ]


def test_create():
    prajituri = get_data()
    params = (100, 'pnew', 'descnew', 2021, 2021.32, 2021)
    p_new = creeaza_prajitura(*params)
    new_prajituri = create(prajituri, *params)
    #assert new_prajituri[-1] == p_new #il adauga la final
    assert len(new_prajituri) == len(prajituri) + 1

    #found = False
    #for prajitura in new_prajituri:
        #if prajitura == p_new:
            #found = True
    #assert found

    assert p_new in new_prajituri

    #testam daca se lanseaza exceptie pentru id duplicat
    params2= (100, 'fnjsjfd', 'sdjskmvmkdm', 322, 32, 555)
    try:
        _ = create(new_prajituri, *params2)
        assert False
    except ValueError:
        assert True #sau pass


def test_read():
    prajituri = get_data()
    some_p = prajituri[2]
    assert read(prajituri, get_id(some_p)) == some_p
    assert read(prajituri, None) == prajituri


def test_update():
    prajituri = get_data()
    p_updated = creeaza_prajitura(1, 'new name', 'new desc', 111, 2222, 1999)
    updated = update(prajituri, p_updated)
    assert p_updated in updated
    assert p_updated not in prajituri
    assert len(updated) == len(prajituri)


def test_delete():
    prajituri = get_data()
    to_delete = 3
    p_deleted = read(prajituri, to_delete)
    deleted = delete(prajituri, to_delete)
    assert p_deleted not in deleted
    assert p_deleted in prajituri
    assert len(deleted) == len(prajituri)-1



def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()


