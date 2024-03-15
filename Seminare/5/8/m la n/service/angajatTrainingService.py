from domeniu.angajatTraining import AngajatTraining
from domeniu.exceptii.duplicateError import DuplicateError
from repository.repository import Repository


class AngajatTrainingService:
    def __init__(self, angajatTrainingRepository: Repository,
                 angajatRepository: Repository,
                 trainingRepository: Repository):
        self.__angajatTrainingRepository = angajatTrainingRepository
        self.__angajatRepository = angajatRepository
        self.__trainingRepository = trainingRepository

    def adaugaInscriere(self, idAngajatTraining, idAngajat, idTraining):
        if self.__angajatRepository.getById(idAngajat) is None:
            raise KeyError("Nu exista un angajat cu id-ul dat")
        if self.__trainingRepository.getById(idTraining) is None:
            raise KeyError("Nu exista un training cu id-ul dat")

        inscrieri = self.__angajatTrainingRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdAngajat() == idAngajat and inscriere.getIdTraining() == idTraining:
                raise DuplicateError("Angajatul este deja inscris la trainingul dat")

        inscriere = AngajatTraining(idAngajatTraining, idAngajat, idTraining)
        self.__angajatTrainingRepository.adauga(inscriere)

    def getAllInscrieri(self):
        return self.__angajatTrainingRepository.getAll()

    def stergeInscriere(self, idAngajat, idTraining):
        inscrieri = self.__angajatTrainingRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdAngajat() == idAngajat and inscriere.getIdTraining() == idTraining:
                self.__angajatTrainingRepository.sterge(inscriere.getIdEntitate())
