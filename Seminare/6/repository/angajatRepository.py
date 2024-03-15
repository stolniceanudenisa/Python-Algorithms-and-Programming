class AngajatRepository:
    def __init__(self):
        self.__angajati = {}

    def getAll(self):
        '''
        returneaza lista de angajati
        :return: o lista de obiecte de tipul Angajat
        '''

        # daca am scrie return self.__angajati, am return aun dictionar de angajati,
        # iar layerele "de mai sus" au nevoie de o lista (ex.: cand afisam angajatii,
        # este mai citibil daca afisam o lista de angajati vs un dictionar
        return list(self.__angajati.values())

    def getById(self, idAngajat):
        '''
        returneaza angajatul cu id-ul dat
        :param idAngajat: string
        :return: un obiect de tipul Angajat, daca exista unul cu id-ul dat, altfel None
        '''

        # return self.__angajati.get(idAngajat, None)

        if idAngajat in self.__angajati:
            return self.__angajati[idAngajat]
        return None

    def adauga(self, angajat):
        '''
        adaua un angajat in dictionar
        :param angajat: obiect de tipul Angajat
        :return:
        '''
        if self.getById(angajat.getIdAngajat()) is not None:
            raise KeyError("Exista deja un angajat cu id-ul dat!")
        self.__angajati[angajat.getIdAngajat()] = angajat

    def modifica(self, angajatNou):
        '''
        modifica un angajat dupa id
        :param angajatNou: obiect de tipul Angajat
        :return:
        '''
        if self.getById(angajatNou.getIdAngajat()) is None:
            raise KeyError("Nu exista niciun angajat cu id-ul dat!")
        self.__angajati[angajatNou.getIdAngajat()] = angajatNou

    def sterge(self, idAngajat):
        '''
        sterge un angajat dupa id
        :param idAngajat: string
        :return:
        '''
        if self.getById(idAngajat) is None:
            raise KeyError("Nu exista niciun angajat cu id-ul dat!")
        self.__angajati.pop(idAngajat)

