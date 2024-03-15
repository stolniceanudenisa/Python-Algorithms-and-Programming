class AngajatRepository:
    def __init__(self):
        # self.__angajati = []
        self.__angajati = {}

    def getAll_lista(self):
        '''
        Da dictionarul de angajati (dictionarul = self.__angajati).
        :return: o lista de obiecte de tipul angajat.
        '''
        return self.__angajati

    def getAll(self):
        '''
        Da lista de angajati.
        :return: o lista de obiecte de tipul angajat.
        '''
        return list(self.__angajati.values())

    def getById(self, idAngajat):
        '''
        Cauta un angajat dupa id.
        :param idAngajat: string.
        :return: un angajat daca exista unul cu id-ul dat, None in caz contrar.
        '''

        # return self.__angajati.get(idAngajat, None)

        if idAngajat in self.__angajati:
            return self.__angajati[idAngajat]
        return None

    def add(self, angajat):
        '''
        Adauga un angajat.
        :param angajat: obiect de tipul Angajat
        :return:
        '''
        if self.getById(angajat.getIdAngajat()) is not None:
            raise KeyError('Exista deja un angajat cu id-ul dat.')
        self.__angajati[angajat.getIdAngajat] = angajat

    def modifica(self, angajatNou):
        '''
        Modifica un angajat dupa id.
        :param angajatNou: obiect de tipul Angajat
        :return:
        '''
        if self.getById(angajatNou.getIdAngajat()) is None:
            raise KeyError('Nu exista niciun angajat cu id-ul dat.')
        self.__angajati[angajatNou.getIdAngajat()] = angajatNou

    def sterge(self, idAngajat):
        '''
        Sterge un angajat dupa id.
        :param idAngajat: string
        :return:
        '''
        if self.getById(idAngajat) is None:
            raise KeyError('Nu exista niciun angajat cu id-ul dat.')
        self.__angajati.pop(idAngajat)
