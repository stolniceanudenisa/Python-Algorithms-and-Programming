from repository.angajatRepository import AngajatRepository
from repository.trainingRepository import TrainingRepository
from service.angajatService import AngajatService
from service.trainingService import TrainingService
from teste.testAll import testAll
from ui.consola import Consola


def main():
    testAll()

    angajatRepository = AngajatRepository()
    trainingRepository = TrainingRepository()

    angajatService = AngajatService(angajatRepository, trainingRepository)
    trainingService = TrainingService(trainingRepository, angajatRepository)

    consola = Consola(angajatService, trainingService)

    consola.meniu()

main()