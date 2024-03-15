from Logic.crud import create
from Tests.test_crud import test_crud
from UserInterface.console import run_ui


def main():
    prajituri = []
    prajituri = create(prajituri, 1, 'ecler', 'gustos', 10, 345, 2022)
    prajituri = create(prajituri, 2, 'amandina', 'rau', 50, 500, 2002)
    prajituri = create(prajituri, 3, 'inghetata ciocolata', 'bun', 30, 668, 1990)
    prajituri = create(prajituri, 4, 'tort', 'ok', 22, 240, 1994)
    prajituri = create(prajituri, 5, 'briosa', 'dulce', 77, 780, 2015)
    prajituri = create(prajituri, 6, 'tiramisu', 'savuroasa', 13, 500, 2022)
    prajituri = create(prajituri, 7, 'tarta', 'foarte buna', 21, 660, 2015)
    prajituri = run_ui(prajituri)


if __name__ == '__main__':
    test_crud()
    main()