"""

  author alex
  date 12/10/2022
  
"""
from app.domeniu.assignment import Assignment
from app.repository.repositoryStudent import StudentRepository
from app.repository.repositoryProblem import ProblemRepository
from app.repository.repositoryAss import AssRepository


class AssignmentService:
    def __init__(self, assignmentRepository: AssRepository, studentRepository: StudentRepository, problemRepository: ProblemRepository):
        self.__assignmentRepository = assignmentRepository
        self.__studentRepository = studentRepository
        self.__problemRepository = problemRepository

    def getAllAssignments(self):
        return self.__assignmentRepository.getAll()

    def addAssignment(self, idAssignment, idStudent, idProblem, grade):
        ass = Assignment(idAssignment, idStudent, idProblem, grade)
        self.__assignmentRepository.save(ass)

    def updateAssignment(self, idAssignment, newIdStudent, newIdProblem, newGrade):
        ass = Assignment(idAssignment, newIdStudent, newIdProblem, newGrade)
        self.__assignmentRepository.update(idAssignment, ass)

    def deleteAssignment(self, idAssignment):
        self.__assignmentRepository.delete(idAssignment)

    def findAssignment(self, idAssignment):
        self.__assignmentRepository.getById(idAssignment)

    def getBelowFive(self):
        gradeList = []
        assignmentList = self.getAllAssignments()
        studentList = self.__studentRepository.getAll()
        for stud in studentList:
            gradeNumber = 0
            gradeSum = 0
            for ass in assignmentList:
                if stud.getIdEntitate() == ass.studentId:
                    gradeSum = gradeSum + int(ass.grade)
                    gradeNumber = gradeNumber + 1
            if gradeNumber != 0:
                gradeList.append(gradeSum/gradeNumber)
        belowFive = []
        i = 0
        for stud in studentList:
            j = 0
            for grade in gradeList:
                if i == j:
                    if grade < 5:
                        belowFive.append((stud.name, grade))
                    break
                j += 1
            i += 1
        return belowFive

    def sort(self, idProblem, param):
        assignments = self.__assignmentRepository.getAll()
        students = self.__studentRepository.getAll()
        list = []
        for ass in assignments:
            if ass.idProblem == idProblem:
                for stud in students:
                    if stud.id == ass.idStudent:
                        list.append([stud.name, ass.grade])

        if param == "1":
            list.sort()
        elif param == "2":
            list.sort(key= lambda x: x[1])

        return list


