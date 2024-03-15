from domeniu.angajat import Angajat
from repository.angajatRepository import AngajatRepository
from repository.trainingRepository import TrainingRepository


class AngajatService:
    def __init__(self, angajatRepository: AngajatRepository, trainingRepository: TrainingRepository):
        self.__angajatRepository = angajatRepository
        self.__trainingRepository = trainingRepository

    def getAllAngajati(self):
        '''
        returneaza lista de angajati
        :return: o lista de obiecte de tipul Angajat
        '''
        return self.__angajatRepository.getAll()

    def adauga(self, idAngajat, nume, idTraining):
        '''
        adauga un angajat
        :param idAngajat: string
        :param nume: string
        :param idTraining: string
        :return:
        '''
        if idTraining.strip() != ""  and self.__trainingRepository.getById(idTraining) is None:
            raise ValueError("Nu exista niciun training cu id-ul dat!")
        angajat = Angajat(idAngajat, nume, idTraining)
        self.__angajatRepository.adauga(angajat)

    def modifica(self, idAngajat, numeNou, idTrainingNou):
        '''
        modifica un angajat dupa id
        :param idAngajat: string
        :param numeNou: string
        :param idTrainingNou: string
        :return:
        '''
        if idTrainingNou.strip() != "" and self.__trainingRepository.getById(idTrainingNou) is None:
            raise ValueError("Nu exista niciun training cu id-ul dat!")
        angajatNou = Angajat(idAngajat, numeNou, idTrainingNou)
        self.__angajatRepository.modifica(angajatNou)

    def sterge(self, idAngajat):
        '''
        sterge un angajat dupa id
        :param idAngajat: string
        :return:
        '''
        self.__angajatRepository.sterge(idAngajat)