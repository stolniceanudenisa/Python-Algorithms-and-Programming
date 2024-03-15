from repository.repository import Repository
from service.angajatService import AngajatService
from service.trainingService import TrainingService
from teste.testAll import testAll
from ui.consola import Consola


def main():
    testAll()

    angajatRepository = Repository()
    trainingRepository = Repository()

    angajatService = AngajatService(angajatRepository, trainingRepository)
    trainingService = TrainingService(trainingRepository, angajatRepository)

    consola = Consola(angajatService, trainingService)

    consola.meniu()

main()