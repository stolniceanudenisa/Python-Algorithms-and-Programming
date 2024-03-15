from Domain.student import Student
from Domain.student_validator import StudentValidator
from Repository.student_file_repository import StudentFileRepo


class StudentService:
    def __init__(self, student_repo: StudentFileRepo, student_validator: StudentValidator):
        self.__student_repo = student_repo
        self.__student_validator = student_validator

    def get_all_studenti(self):
        return self.__student_repo.get_all()

    def add_student(self, ids, numest, nrprez, nota):
        student = Student(ids, numest, nrprez, nota)
        self.__student_validator.validate(student)
        self.__student_repo.add(student)

    #
    # def acordare_bonus(self, p, b):
    #     studenti.txt = self.get_all_studenti()
    #     lista = []
    #     for student in studenti.txt:
    #         if student.numar_prezente >= p:
    #             if (student.nota - b <= 10):
    #                 student.nota = student.nota + b
    #                 lista.append(student)
    #     return lista

    def export(self, filename, p, b):
        self.__student_repo.read_file()
        studenti = self.get_all_studenti()
        lista = []
        for student in studenti:
            if student.numar_prezente >= p:
                if (student.nota - b <= 10) and student.nota != 10:
                    student.nota = student.nota + b
                    if student.nota <= 10:
                        lista.append(student)
        self.__student_repo.write_file()
        with open(filename, "w") as f:
            for student in lista:
                string = str(student.id_student) + ',' + str(student.nota) + '\n'
                f.write(string)

    def update_student(self, ids, numes, nrprez, nota):
        student = Student(ids, numes, nrprez, nota)
        self.__student_validator.validate(student)
        self.__student_repo.update(student)

    def delete_student(self, id_student):
        self.__student_repo.delete(id_student)
