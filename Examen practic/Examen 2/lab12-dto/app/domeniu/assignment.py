"""

  author alex
  date 12/10/2022
  
"""
from app.domeniu.entitate import Entitate
from dataclasses import dataclass

'''
class Assignment(Entitate):
    def __init__(self, idAssignment, idStudent, idProblem, grade):
        super().__init__(idAssignment)
        self.__idStudent = idStudent
        self.__idProblem = idProblem
        self.__grade = grade

    def getIdStudent(self):
        return self.__idStudent

    def getIdProblem(self):
        return self.__idProblem

    def getGrade(self):
        return self.__grade

    def setIdStudent(self, idStudent):
        self.__idStudent = idStudent

    def setIdProblem(self, idProblem):
        self.__idProblem = idProblem

    def setGrade(self, grade):
        self.__grade = grade

    def __str__(self):
        return f"id asignare: {self.getIdEntitate()}, id student: {self.getIdStudent()}, id problema: {self.getIdProblem()}, nota: {self.getGrade()}"
'''

@dataclass
class Assignment:
    id: int
    idStudnet: int
    idProblem: int
    grade: int

    def __str__(self):
        return f"id asignare: {self.id}, id student: {self.idStudnet}, id problema: {self.idProblem}, nota: {self.grade}"