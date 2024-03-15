from seminar11.clase.domain.Entitate import Entitate


class Inscriere(Entitate):

    def __init__(self, id, student_id, disciplina_id, nota):
        super().__init__(id)
        self.__student_id = student_id
        self.__disciplina_id = disciplina_id
        self.__nota = nota

    def get_student_id(self):
        return self.__student_id

    def get_disciplina_id(self):
        return self.__disciplina_id

    def get_nota(self):
        return self.__nota

    def set_student_id(self, student_id_nou):
        self.__student_id = student_id_nou

    def set_disciplina_id(self, disciplina_id_nou):
        self.__disciplina_id = disciplina_id_nou

    def set_nota(self, nota_noua):
        self.__nota = nota_noua

    def __str__(self):
        #Observati ca dupa ultimul + de la final de rand apare \ -> avem +\
        #inseamna ca vom concatena sirul de caractere in continuare, doar ca acea continuare va fi scrisa pe randul urmator
        return "Inscriere: " + str(self.get_id()) + "\n" +\
            "ID Student: " + str(self.get_student_id()) + "\n" +\
            "ID Disciplina: " + str(self.get_disciplina_id()) + "\n" +\
            "Nota: " + str(self.get_nota()) + "\n"