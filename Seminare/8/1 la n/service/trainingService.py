from domeniu.training import Training
from repository.repository import Repository


class TrainingService:
    def __init__(self, trainingRepository: Repository, angajatRepository: Repository):
        self.__trainingRepository = trainingRepository
        self.__angajatRepository = angajatRepository

    def getAllTrainings(self):
        '''

        :return:
        '''
        return self.__trainingRepository.getAll()

    def adaugaTraining(self, idTraining, nume, descriere, durata):
        '''

        :param idTraining:
        :param nume:
        :param descriere:
        :param durata:
        :return:
        '''
        training = Training(idTraining, nume, descriere, durata)
        self.__trainingRepository.adauga(training)

    def modificaTraining(self, idTraining, numeNou, descriereNoua, durataNoua):
        '''

        :param idTraining:
        :param numeNou:
        :param descriereNoua:
        :param durataNoua:
        :return:
        '''
        training = Training(idTraining, numeNou, descriereNoua, durataNoua)
        self.__trainingRepository.modifica(training)

    def stergeTraining(self, idTraining):
        '''

        :param idTraining:
        :return:
        '''
        angajati = self.__angajatRepository.getAll()
        for angajat in angajati:
            if angajat.getIdTraining() == idTraining:
                angajat.setIdTraining('')
                self.__angajatRepository.modifica(angajat)
        self.__trainingRepository.sterge(idTraining)
