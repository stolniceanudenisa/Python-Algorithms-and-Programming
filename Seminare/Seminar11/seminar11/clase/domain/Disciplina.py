from seminar11.clase.domain.Entitate import Entitate


class Disciplina(Entitate):

    def __init__(self, id, nume, profesor):
        super().__init__(id)
        self.__nume = nume
        self.__profesor = profesor

    def get_nume(self):
        return self.__nume

    def get_profesor(self):
        return self.__profesor

    def set_nume(self, nume_nou):
        self.__nume = nume_nou

    def set_profesor(self, profesor_nou):
        self.__profesor = profesor_nou

    def __str__(self):
        return "Disciplina " + str(self.get_id()) + ":\nNume: " + self.get_nume() + "\nProfesor: " + self.get_profesor() + "\n"