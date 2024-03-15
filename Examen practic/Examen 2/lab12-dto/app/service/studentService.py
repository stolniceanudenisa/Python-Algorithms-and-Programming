"""

  author alex
  date 12/10/2022
  
"""
from app.domeniu.student import Student
from app.repository.repositoryStudent import StudentRepository


class StudentService:
    def __init__(self, studentRepository: StudentRepository):
        self.__studentRepository = studentRepository

    def getAllStudents(self):
        return self.__studentRepository.getAll()

    def addStudent(self, idStudent, studentName, studentGrup):
        student = Student(idStudent, studentName, studentGrup)
        self.__studentRepository.save(student)

    def updateStudent(self, idStudent, newName, newGrup):
        student = Student(idStudent, newName, newGrup)
        self.__studentRepository.update(idStudent, student)

    def deleteStudent(self, idStudent):
        self.__studentRepository.delete(idStudent)

    def findStudent(self, idStudent):
        return self.__studentRepository.getById(idStudent)



