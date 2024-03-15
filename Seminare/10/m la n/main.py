from domeniu.trainingValidator import TrainingValidator
from repository.fileAngajatRepository import FileAngajatRepository
from repository.repository import Repository
from service.angajatService import AngajatService
from service.angajatTrainingService import AngajatTrainingService
from service.trainingService import TrainingService
from teste.testAll import testAll
from ui.consola import Consola


def main():
    testAll()

    angajatFileRepository = FileAngajatRepository("angajati.txt")
    trainingRepository = Repository()
    angajatTrainingRepository = Repository()
    trainingValidator = TrainingValidator()

    angajatService = AngajatService(angajatFileRepository, angajatTrainingRepository)
    trainingService = TrainingService(trainingRepository, angajatTrainingRepository, trainingValidator)
    angajatTrainingService = AngajatTrainingService(angajatTrainingRepository, angajatFileRepository, trainingRepository)

    consola = Consola(angajatService, trainingService, angajatTrainingService)

    consola.meniu()

main()