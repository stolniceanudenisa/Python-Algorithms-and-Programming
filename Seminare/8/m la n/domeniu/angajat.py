from domeniu.entitate import Entitate


class Angajat(Entitate):
    def __init__(self, idAngajat, nume):
        super().__init__(idAngajat)
        self.__nume = nume

    def getNume(self):
        return self.__nume

    def setNume(self, nume):
        self.__nume = nume

    def __str__(self):
        return f"id: {self.getIdEntitate()}, nume: {self.__nume}"