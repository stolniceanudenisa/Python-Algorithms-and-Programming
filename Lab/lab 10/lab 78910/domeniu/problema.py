from domeniu.entitate import Entitate

class Problema(Entitate):
    def __init__(self, idEntitate, descriere, deadline):
        super().__init__(idEntitate)
        self.__descriere = descriere
        self.__deadline = deadline

    def getDescriere(self):
        return self.__descriere

    def getDeadline(self):
        return self.__deadline

    def setDescriere(self, descriere):
        self.__descriere = descriere

    def setDeadline(self, deadline):
        self.__deadline = deadline

    def __str__(self):
        return f"Numar laborator_Numar Problema: {self.getIdEntitate()}, descriere: {self.__descriere}, deadline: {self.__deadline}"
