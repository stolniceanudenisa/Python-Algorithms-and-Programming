from seminar9.clase.domain.ValidatorException import ValidatorException


class DisciplinaValidator:

    def __init__(self):
        self.__erori = []

    def valideaza(self, disciplina):
        self.__erori = []
        self.valideaza_nume(disciplina.get_nume())
        self.valideaza_nume(disciplina.get_profesor())
        if len(self.__erori) > 0:
            raise ValidatorException(self.__erori)
        else:
            return True

    def valideaza_nume(self, nume):
        self.__erori = []
        if len(nume) < 2:
            self.__erori.append("Eroare la validarea disciplinei: Nume invalid! (are mai putin de 2 caractere)")
        if len(self.__erori) > 0:
            raise ValidatorException(self.__erori)
        else:
            return True