from repository.repository import Repository
from service.angajatService import AngajatService
from service.angajatTrainingService import AngajatTrainingService
from service.trainingService import TrainingService
from teste.testAll import testAll
from ui.consola import Consola


def main():
    testAll()

    angajatRepository = Repository()
    trainingRepository = Repository()
    angajatTrainingRepository = Repository()

    angajatService = AngajatService(angajatRepository, angajatTrainingRepository)
    trainingService = TrainingService(trainingRepository, angajatTrainingRepository)
    angajatTrainingService = AngajatTrainingService(angajatTrainingRepository, angajatRepository, trainingRepository)

    consola = Consola(angajatService, trainingService, angajatTrainingService)

    consola.meniu()

main()