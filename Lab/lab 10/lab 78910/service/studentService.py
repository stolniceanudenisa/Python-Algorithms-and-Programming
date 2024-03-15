from domeniu.student import Student
from repository.repository import Repository


class StudentService:
    def __init__(self, studentRepository: Repository, asignareRepository: Repository):
        self.__sudentRepository = studentRepository
        self.__asignareRepository = asignareRepository

    def getAllStudenti(self):
        '''
        returneaza lista de studenti
        :return: o lista de obiecte de tipul Student
        '''
        return self.__sudentRepository.getAll()

    def adaugaStudent(self, idStudent, nume, grup):
        '''
        adauga un student
        :param idStudent:   string
        :param nume:    string
        :param grup:    string
        :return:
        '''
        student = Student(idStudent, nume, grup)
        self.__sudentRepository.adauga(student)

    def stergeStudent(self, idStudent):
        '''
        sterge un student care are id-ul idStudent
        :param idStudent: string
        :return:
        '''
        asignari = self.__asignareRepository.getAll()
        for asignare in asignari:
            if asignare.getIdStudent() == idStudent:
                self.__asignareRepository.sterge(asignare.getIdEntitate())
        self.__sudentRepository.sterge(idStudent)

    def modificaStudent(self, idStudent, numeNou, grupNou):
        '''
        functia modifica toate datele despre un student cu id-ul dat
        :param idStudent: string
        :param numeNou: string
        :param grupNou: string
        :return:
        '''
        studentNou = Student(idStudent, numeNou, grupNou)
        self.__sudentRepository.modifica(studentNou)

    def cautaStudent(self, idStudent):
        '''
        functia cauta si afiseaza studentul cu id-ul dat
        :param idStudent: string
        :return:
        '''
        return self.__sudentRepository.cauta(idStudent)