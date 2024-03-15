from domeniu.entitate import Entitate


class Asignare(Entitate):
    def __init__(self, idEntitate, idStudent, nrLab_nrProblema, nota):
        super().__init__(idEntitate)
        self.__idStudent = idStudent
        self.__nrLab_nrProblema = nrLab_nrProblema
        self.__nota = nota

    def getIdStudent(self):
        return self.__idStudent

    def getIdProblema(self):
        return self.__nrLab_nrProblema

    def getNota(self):
        return self.__nota

    def setIdStudent(self, idStudent):
        self.__idStudent = idStudent

    def setIdProblema(self, nrLab_nrProblema):
        self.__nrLab_nrProblema = nrLab_nrProblema

    def setNota(self, nota):
        self.__nota = nota

    def __str__(self):
        return f"Id Asignare: {self.getIdEntitate()}, Id Student: {self.__idStudent}, Numar laborator_Numar Problema: {self.__nrLab_nrProblema}, nota: {self.__nota}"
