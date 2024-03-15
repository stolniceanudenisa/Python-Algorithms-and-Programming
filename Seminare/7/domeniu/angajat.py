class Angajat:
    def __init__(self, idAngajat, nume, idTraining):
        # relatie de 1 la n intre entitati
        self.__idAngajat = idAngajat
        self.__nume = nume
        self.__idTraining = idTraining

    def getIdAngajat(self):
        return self.__idAngajat

    def getNume(self):
        return self.__nume

    def getIdTraining(self):
        return self.__idTraining

    def setIdTraining(self, idTraining):
        self.__idTraining = idTraining

    def setIdAngajat(self, idAngajat):
        self.__idAngajat = idAngajat

    def setNume(self, nume):
        self.__nume = nume

    def __str__(self):
        return f"id: {self.__idAngajat}, nume: {self.__nume}, id training: {self.__idTraining}"