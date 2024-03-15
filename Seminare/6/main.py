from repository.angajatRepository import AngajatRepository
from service.AngajatService import AngajatService
from teste.testAll import testAll
from ui.consola import Consola


def main():
    testAll()

    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)
    consola = Consola(angajatService)

    consola.meniu()

main()