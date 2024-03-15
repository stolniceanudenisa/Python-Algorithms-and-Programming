from domeniu.entitate import Entitate


class Training(Entitate):
    def __init__(self, idTraining, nume, descriere, durata):
        super().__init__(idTraining)
        self.__nume = nume
        self.__descriere = descriere
        self.__durata = durata

    def getNume(self):
        return self.__nume

    def getDescriere(self):
        return self.__descriere

    def getDurata(self):
        return self.__durata

    def setNume(self, nume):
        self.__nume = nume

    def setDescriere(self, descriere):
        self.__descriere = descriere

    def setDurata(self, durata):
        self.__durata = durata

    def __str__(self):
        return f'id: {self.getIdEntitate()}, nume: {self.__nume},' \
               f'descriere: {self.__descriere}, durata: {self.__durata}'

