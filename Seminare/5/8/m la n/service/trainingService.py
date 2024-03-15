from domeniu.training import Training
from repository.repository import Repository


class TrainingService:
    def __init__(self, trainingRepository: Repository, angajatTrainingRepository: Repository):
        self.__trainingRepository = trainingRepository
        self.__angajatTrainingRepository = angajatTrainingRepository

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
        inscrieri = self.__angajatTrainingRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdTraining() == idTraining:
                self.__angajatTrainingRepository.sterge(inscriere.getIdEntitate())
        self.__trainingRepository.sterge(idTraining)

    def ordoneazaTraininguriDupaNrParticipanti(self):
        traininguriNrParticipanti = {}
        inscrieri = self.__angajatTrainingRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdTraining() in  traininguriNrParticipanti:
                traininguriNrParticipanti[inscriere.getIdTraining()] += 1
            else:
                traininguriNrParticipanti[inscriere.getIdTraining()] = 1

        idTraininguriOrdonate = sorted(traininguriNrParticipanti,
                                     key=lambda idTraining: traininguriNrParticipanti[idTraining])
        traininguriOrdonate = []
        for idTraining in idTraininguriOrdonate:
            traininguriOrdonate.append((idTraining, traininguriNrParticipanti[idTraining]))
        return traininguriOrdonate