from seminar6.clase.domain.Student import Student

class StudentController:

    def __init__(self, repository):
        self.__repository = repository

    def get_all(self):
        '''
        Metoda ce returneaza lista de obiecte din repository
        :return: lista de obiecte din repository
        '''
        return self.__repository.get_all()

    def adauga(self, id_student, nume_student):
        '''
        Metoda ce adauga un student in lista (din repository)
        :param id_student:
        :param nume_student:
        '''
        student = Student(id_student, nume_student)
        self.__repository.adauga(student)