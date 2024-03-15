from domeniu.entitate import Entitate


class Angajat(Entitate):
    def __init__(self, idAngajat, nume, idTraining):
        # relatie de 1 la n intre entitati
        super().__init__(idAngajat)
        self.__nume = nume
        self.__idTraining = idTraining

    def getNume(self):
        return self.__nume

    def getIdTraining(self):
        return self.__idTraining

    def setIdTraining(self, idTraining):
        self.__idTraining = idTraining

    def setNume(self, nume):
        self.__nume = nume

    def __str__(self):
        return f"id: {self.getIdEntitate()}, nume: {self.__nume}, id training: {self.__idTraining}"