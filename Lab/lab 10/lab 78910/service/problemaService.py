from domeniu.problema import Problema
from repository.repository import Repository


class ProblemaLaboratorService:
    def __init__(self, problemaLaboratorRepository: Repository, asignareRepository: Repository):
        self.__problemaLaboratorRepository = problemaLaboratorRepository
        self.__asignareRepository = asignareRepository

    def getAllProblemeLaborator(self):
        '''
        returneaza lista de probleme de laborator
        :return: o lista de obiecte de tipul ProblemaLaborator
        '''
        return self.__problemaLaboratorRepository.getAll()

    def adaugaProblemaLaborator(self, idProblemaLaborator, descriere, deadline):
        '''
        adauga o problema de laborator
        :param idProblemaLaborator:   string
        :param descriere:    string
        :param deadline:    string
        :return:
        '''
        problemaLaborator = Problema(idProblemaLaborator, descriere, deadline)
        self.__problemaLaboratorRepository.adauga(problemaLaborator)

    def stergeProblemaLaborator(self, idProblemaLaborator):
        '''
        sterge un student care are id-ul idStudent
        :param idStudent: string
        :return:
        '''
        asignari = self.__asignareRepository.getAll()
        for asignare in asignari:
            if asignare.getIdProblema() == idProblemaLaborator:
                self.__asignareRepository.sterge(asignare.getIdEntitate())
        self.__problemaLaboratorRepository.sterge(idProblemaLaborator)

    def modificaProblemaLaborator(self, idProblemaLaborator, descriereNoua, deadlineNou):
        '''
        functia modifica toate datele despre o problema de laborator cu id-ul dat
        :param idProblemaLaborator: string
        :param descriereNoua: string
        :param deadlineNou: string
        :return:
        '''
        problemaLaboratorNoua = Problema(idProblemaLaborator, descriereNoua, deadlineNou)
        self.__problemaLaboratorRepository.modifica(problemaLaboratorNoua)

    def cautareProblemaLaborator(self, idProblemaLaborator):
        '''
        functia cauta si afiseaza laboratorul si numarul problemei cu id-ul dat
        :param idProblemaLaborator: string
        :return:
        '''
        return self.__problemaLaboratorRepository.cauta(idProblemaLaborator)