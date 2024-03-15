class DisciplinaRepository:

    def __init__(self):
        self.__lista_discipline = []

    def get_all(self):
        return self.__lista_discipline

    def adauga(self, disciplina):
        '''
        Metoda care adauga o noua disciplina in lista
        :param disciplina:
        :return:
        Arunca o eroare daca id-ul disciplinei pe care vrem sa o introducem exista deja in lista. Eroarea e tratata in UI.
        '''
        if self.gaseste_disciplina_dupa_id(disciplina.get_id()) != -1:
            raise KeyError("Exista deja o disciplina cu acest id!")
        else:
            self.__lista_discipline.append(disciplina)

    def sterge(self, id):
        '''
        Metoda care sterge o disciplina din lista
        :param id:
        :return:
        Arunca o eroare daca id-ul disciplinei pe care vrem sa o stergem nu exista in lista. Eroarea e tratata in UI.
        '''
        if self.gaseste_disciplina_dupa_id(id) == -1:
            raise KeyError("Disciplina cu acest id nu exista!")
        else:
            index = self.gaseste_disciplina_dupa_id(id)
            self.__lista_discipline.pop(index)

    def modifica(self, id, nume_nou, profesor_nou):
        '''
        Metoda care modifica o disciplina din lista
        :param id:
        :param nume_nou:
        :param profesor_nou:
        :return:
        Arunca o eroare daca id-ul disciplinei pe care vrem sa o modificam nu exista in lista. Eroarea e tratata in UI.
        '''
        if self.gaseste_disciplina_dupa_id(id) == -1:
            raise KeyError("Disciplina cu acest id nu exista!")
        else:
            index = self.gaseste_disciplina_dupa_id(id)
            disciplina = self.__lista_discipline[index]
            disciplina.set_nume(nume_nou)
            disciplina.set_profesor(profesor_nou)

    def gaseste_disciplina_dupa_id(self, id):
        '''
        Metoda care returneaza pozitia in lista de discipline a unei discipline, dupa id
        :param id:
        :return: pozitia disciplinei in lista, daca ea exista in lista de discipline; -1, altfel
        '''
        for i in range(0, len(self.__lista_discipline)):
            disciplina_curenta = self.__lista_discipline[i]
            if disciplina_curenta.get_id() == id:
                return i
        return -1