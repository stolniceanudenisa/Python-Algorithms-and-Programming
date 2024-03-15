class Angajat:
    def __init__(self, idAngajat, nume):
        self.__idAngajat = idAngajat
        self.__nume = nume

    def getIdAngajat(self):
        return self.__idAngajat

    def getNume(self):
        return self.__nume

    def setIdAngajat(self, idAngajat):
        self.__idAngajat = idAngajat

    def setNume(self, nume):
        self.__nume = nume

    def __str__(self):
        return f"id: {self.__idAngajat}, nume: {self.__nume}"
