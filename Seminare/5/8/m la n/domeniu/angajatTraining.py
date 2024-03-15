from domeniu.entitate import Entitate


class AngajatTraining(Entitate):
    def __init__(self, idAngajatTraining, idAngajat, idTraining):
        super().__init__(idAngajatTraining)
        self.__idAngajat = idAngajat
        self.__idTraining = idTraining

    def getIdAngajat(self):
        return self.__idAngajat

    def getIdTraining(self):
        return self.__idTraining

    def setIdAngajat(self, idAngajat):
        self.__idAngajat = idAngajat

    def setIdTraining(self, idTraining):
        self.__idTraining = idTraining

    def __str__(self):
        return f'id: {self.getIdEntitate()}, id angajat: {self.__idAngajat},' \
               f' id training: {self.__idTraining}'