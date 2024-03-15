from domeniu.exceptii.duplicateError import DuplicateError


class Repository:
    def __init__(self):
        self._entitati = {}

    def getAll(self):
        '''
        returneaza lista de entitati
        :return: o lista de obiecte de tipul Entitate
        '''
        return list(self._entitati.values())

    def getById(self, idEntitate):
        '''
        returneaza entitatea cu id-ul dat
        :param idEntitate: string
        :return: un obiect de tipul Entitate, daca exista unul cu id-ul dat, altfel None
        '''

        if idEntitate in self._entitati:
            return self._entitati[idEntitate]
        return None

    def adauga(self, entitate):
        '''
        adaua un entiate in dictionar
        :param entitate: obiect de tipul Entitate
        :return:
        '''
        if self.getById(entitate.getIdEntitate()) is not None:
            raise DuplicateError("Exista deja o entitate cu id-ul dat!")
        self._entitati[entitate.getIdEntitate()] = entitate

    def modifica(self, entiateNoua):
        '''
        modifica o entitate dupa id
        :param entiateNoua: obiect de tipul Entitate
        :return:
        '''
        if self.getById(entiateNoua.getIdEntitate()) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self._entitati[entiateNoua.getIdEntitate()] = entiateNoua

    def sterge(self, idEntitate):
        '''
        sterge o entitate dupa id
        :param idEntitate: string
        :return:
        '''
        if self.getById(idEntitate) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self._entitati.pop(idEntitate)

