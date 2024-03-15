from functions import *
from validation import *

def test_valid():
    try:
        valid(['add','add',100,'wtf'])
        valid(['list','balance',234])
        assert False
    except ValueError:
        assert True

def test_day():
    assert (valid_day(0) == False)
    assert (valid_day(32) == False)
    assert (valid_day(-3) == False)
    assert (valid_day(3) == True)

def test_append_transaction():
    tr1 = create_transaction(10,'in',234,'random1')
    tr2 = create_transaction(11,'out',3454,'random2')
    tr3 = create_transaction(2,'in',422,'random0')
    trList = [tr3]
    append_transaction(10,'in',234,'random1',trList)
    assert (trList == [tr3,tr1])
    append_transaction(11,'out',3454,'random2',trList)
    assert (trList == [tr3,tr1,tr2])
    append_transaction(2,'in',422,'random0',trList)
    assert (trList == [tr3,tr1,tr2,tr3])

def test_undo():
    tr1 = create_transaction(10, 'in', 234, 'random1')
    tr2 = create_transaction(11, 'out', 3454, 'random2')
    tr3 = create_transaction(2, 'in', 422, 'random0')
    maList = [tr1, tr2, tr3]
    trStack = [[],maList.copy()]
    append_transaction(30, 'out', 909, 'random4',maList)
    undo(trStack,maList)
    assert (maList == [tr1,tr2,tr3])
    undo(trStack,maList)
    assert (maList == [])

def run_all_tests():
    test_day()
    test_valid()
    test_append_transaction()
    test_undo()