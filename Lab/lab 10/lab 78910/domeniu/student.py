from domeniu.entitate import Entitate

class Student(Entitate):
    def __init__(self, idEntitate, nume, grup):
        super().__init__(idEntitate)
        self.__nume = nume
        self.__grup = grup

    def getNume(self):
        return self.__nume

    def getGrup(self):
        return self.__grup

    def setNume(self, nume):
        self.__nume = nume

    def setGrup(self, grup):
        self.__grup = grup


    def __str__(self):
        return f"id: {self.getIdEntitate()}, nume: {self.__nume}, grup: {self.__grup}"

