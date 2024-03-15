from seminar11.clase.repository.RepositoryException import DuplicateIDException, InexistentIDException


class Repository:

    def __init__(self):
        self._lista = []

    def get_all(self):
        '''
        Metoda care returneaza lista de entitati
        :return:
        '''
        return self._lista

    def adauga(self, entitate):
        '''
        Metoda care adauga o entitate in lista
        :param entitate:
        :return:
        '''
        if self.gaseste_dupa_id(entitate.get_id()) is not None:
            raise DuplicateIDException("Exista deja o entitate cu acest id!")
        else:
            self._lista.append(entitate)

    def modifica(self, entitate_noua):
        '''
        Metoda care modifica o entitate existenta
        :param entitate_noua:
        :return:
        '''
        id_entitate_noua = entitate_noua.get_id()
        if self.gaseste_dupa_id(id_entitate_noua) is None:
            raise InexistentIDException("Entitatea cu acest id nu exista!")
        else:
            index = self.gaseste_dupa_id(id_entitate_noua)
            self._lista[index] = entitate_noua

    def sterge(self, id):
        '''
        Metoda care sterge din lista o entitate dupa id
        :param id:
        :return:
        '''
        if self.gaseste_dupa_id(id) is None:
            raise InexistentIDException("Entitatea cu acest id nu exista!")
        else:
            index = self.gaseste_dupa_id(id)
            self._lista.pop(index)

    def gaseste_dupa_id(self, id):
        '''
        Metoda care returneaza pozitia in lista a unei entitati, dupa id
        :param id:
        :return: pozitia entitatii in lista, daca ea exista; -1, altfel
        '''
        for i in range(0, len(self._lista)):
            entitate_curenta = self._lista[i]
            if entitate_curenta.get_id() == id:
                return i
        return None

    def get_by_id(self, id):
        '''
        Metoda ce returneaza entitatea dupa id-ul dat
        :param id:
        :return: entitatea cu id-ul dat, daca ea exista; -1 altfel
        '''
        for i in range(0, len(self._lista)):
            entitate_curenta = self._lista[i]
            if entitate_curenta.get_id() == id:
                return entitate_curenta
        return None