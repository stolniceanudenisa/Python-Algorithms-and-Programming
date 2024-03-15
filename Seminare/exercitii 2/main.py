from Repository.angajatRepository import AngajatRepository
from Service.angajatService import AngajatService
from Tests.testAll import testAll
from UI.consola import Consola


def main():
    # testAll()

    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)
    consola = Consola(angajatService)

    consola.meniu()


main()
