from Logic.crud import create
from Tests.test_crud import test_all
from UserInterface.console import run_ui1


def main():
    tranzactii = []
    undo_list = []
    redo_list = []
    # redo functioneaza doar asupra lui undo
    # redo anuleaza un undo
    tranzactii = create(tranzactii, 12, 200.234, 'intrare', undo_list, redo_list)
    tranzactii = create(tranzactii, 2, 1200.777, 'iesire', undo_list, redo_list)
    tranzactii = create(tranzactii, 31, 50.23, 'iesire', undo_list, redo_list)
    tranzactii = create(tranzactii, 4, 10000, 'intrare', undo_list, redo_list)
    tranzactii = create(tranzactii, 15, 100.50, 'intrare', undo_list, redo_list)
    tranzactii = create(tranzactii, 4, 4444, 'intrare', undo_list, redo_list)
    tranzactii = create(tranzactii, 26, 144.189, 'iesire', undo_list, redo_list)
    tranzactii = create(tranzactii, 7, 341121, 'iesire', undo_list, redo_list)
    tranzactii = create(tranzactii, 4, 1999.10, 'iesire', undo_list, redo_list)
    tranzactii = create(tranzactii, 8, 44121, 'iesire', undo_list, redo_list)
    tranzactii = create(tranzactii, 30, 3132, 'iesire', undo_list, redo_list)
    tranzactii = create(tranzactii, 4, 12.986, 'iesire', undo_list, redo_list)
    tranzactii = run_ui1(tranzactii, undo_list, redo_list)


if __name__ == '__main__':
    test_all()
    main()
