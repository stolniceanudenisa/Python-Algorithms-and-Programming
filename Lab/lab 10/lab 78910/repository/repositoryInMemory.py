from domeniu.exceptii.duplicateError import DuplicateError
from repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entitati = {}

    def getAll(self):
        '''
        returneaza lista de entitati
        :return:  o lista de obiecte de tipul Entitate
        '''
        return list(self.entitati.values())

    def getById(self, idEntitate):
        '''
        returneaza entitatea cu id-ul dat
        :param idEntitate:  string
        :return:  un obiect de tipul Entitate daca exista unul cu id-ul dat, altfel None
        '''
        if idEntitate in self.entitati:
            return self.entitati[idEntitate]

    def adauga(self, entitate):
        '''
        adauga o entitate in dictionar
        :param entitate:  obiect de tipul Entitate
        :return:
        '''
        #if self.getById(entitate.getIdEntitate()) is not None:
            #raise DuplicateError("Exista deja o entitate cu id-ul dat")
        self.entitati[entitate.getIdEntitate()] = entitate

    def sterge(self, idEntitate):
        '''
        sterge o entitate din dictionar
        :param idEntitate: string
        :return:
        '''
        if self.getById(idEntitate) is None:
            raise KeyError("Nu exista nici o entitate cu id-ul dat")
        self.entitati.pop(idEntitate)

    def modifica(self, idEntitate, entitateNoua):
        '''
        functia modifica toate datele despre o entitate cu id-ul dat
        :param idEntitate: string
        :param entitateNoua: noua entitate de tipul Entitate
        :return:
        '''
        if self.getById(idEntitate) is None:
            raise KeyError("Nu exista nici o entitate cu id-ul dat")
        self.entitati[idEntitate] = entitateNoua

    def cauta(self, idEntitate):
        '''
        functia cauta si afiseaza entitatea cu id-ul dat
        :param idEntitate: string
        :return:
        '''
        if self.getById(idEntitate) is None:
            raise KeyError("Nu exista nici o entitate cu id-ul dat")
        return self.entitati[idEntitate]