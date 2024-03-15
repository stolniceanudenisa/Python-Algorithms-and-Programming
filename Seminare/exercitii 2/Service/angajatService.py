from Domain.angajat import Angajat
from Repository.angajatRepository import AngajatRepository


class AngajatService:
    def __init__(self, angajatRepository: AngajatRepository):
        self.__angajatRepository = angajatRepository

    def getAllAngajati(self):
        '''
        Da toata lista de angajati
        :return: o lista de obiecte de tip Angajat
        '''
        return self.__angajatRepository.getAll()

    def adaugaAngajat(self, idAngajat, nume):
        '''
        Adauga un angajat
        :param idAngajat: string
        :param nume: string
        :return:
        '''
        angajat = Angajat(idAngajat, nume)
        self.__angajatRepository.add(angajat)

    def modificaAngajat(self, idAngajat, numeNou):
        '''
        Modifica un angajat dupa id
        :param idAngajat: string
        :param numeNou: string
        :return:
        '''
        angajat = Angajat(idAngajat, numeNou)
        self.__angajatRepository.modifica(angajat)

    def stergeAngajat(self, idAngajat):
        '''
        Sterge un angajat dupa id.
        :param idAngajat: string
        :return:
        '''
        self.__angajatRepository.sterge(idAngajat)
