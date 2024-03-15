from domeniu.angajat import Angajat
from repository.repository import Repository


class AngajatService:
    def __init__(self, angajatRepository: Repository, angajatTrainingRepository: Repository):
        self.__angajatRepository = angajatRepository
        self.__angajatTrainingRepository = angajatTrainingRepository

    def getAllAngajati(self):
        '''
        returneaza lista de angajati
        :return: o lista de obiecte de tipul Angajat
        '''
        return self.__angajatRepository.getAll()

    def adauga(self, idAngajat, nume):
        '''
        adauga un angajat
        :param idAngajat: string
        :param nume: string
        :return:
        '''
        angajat = Angajat(idAngajat, nume)
        self.__angajatRepository.adauga(angajat)

    def modifica(self, idAngajat, numeNou):
        '''
        modifica un angajat dupa id
        :param idAngajat: string
        :param numeNou: string
        :return:
        '''
        angajatNou = Angajat(idAngajat, numeNou)
        self.__angajatRepository.modifica(angajatNou)

    def sterge(self, idAngajat):
        '''
        sterge un angajat dupa id
        :param idAngajat: string
        :return:
        '''
        inscrieri = self.__angajatTrainingRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdAngajat() == idAngajat:
                self.__angajatTrainingRepository.sterge(inscriere.getIdEntitate())
        self.__angajatRepository.sterge(idAngajat)