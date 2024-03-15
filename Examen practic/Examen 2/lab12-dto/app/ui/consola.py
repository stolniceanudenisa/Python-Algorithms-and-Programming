"""

  author alex
  date 12/11/2022
  
"""
from app.service.assignmentService import AssignmentService
from app.service.problemService import ProblemService
from app.service.studentService import StudentService


class Consola:
    def __init__(self, studentService: StudentService, problemService: ProblemService, assignmentService: AssignmentService):
        self.__studentService = studentService
        self.__problemService = problemService
        self.__assignmentService = assignmentService

    def printMenu(self):
        print("1. Adauga studenti")
        print("2. Modifica datele despre un student cu id-ul dat")
        print("3. Sterge un student dupa id")
        print("4. Cautare student dupa id")
        print("5. Adauga problema")
        print("6. Modifica o problema prin id")
        print("7. Sterge o problema prin id")
        print("8. Cautare problema de laborator prin id")
        print("9. Asigneaza unui student un laborator")
        print("10. Modifica o asignare")
        print("11. Sterge o asignare")
        print("12. Cautare o asignare dupa id")
        print("13. Scrieti '1' pentru sortarea studentilor dupa nume sau '2' pentru sortarea studentilor dupa nota ")
        print("14. Afiseaza lista cu studentii care au media sub 5")
        print("a. Afiseaza toti sudenti")
        print("b. Afiseaza toate problemele de laborator")
        print("c. Afiseaza toate asignarile")
        print("x. Iesire din program")

    def menu(self):
        while True:
            self.printMenu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.addStudent()
            elif optiune == "2":
                self.updateStudent()
            elif optiune == "3":
                self.deleteStudent()
            elif optiune == "4":
                self.findStudent()
            elif optiune == "5":
                self.addProblem()
            elif optiune == "6":
                self.updateProblem()
            elif optiune == "7":
                self.deleteProblem()
            elif optiune == "8":
                self.findProblem()
            elif optiune == "9":
                self.addAssignment()
            elif optiune == "10":
                self.updateAssignment()
            elif optiune == "11":
                self.deleteAssignment()
            elif optiune == "12":
                self.findAssignment()
            elif optiune == "13":
                self.sorting()
            elif optiune == "14":
                self.printBelowFive(self.__assignmentService.getBelowFive())
            elif optiune == "a":
                self.printStudents(self.__studentService.getAllStudents())
            elif optiune == "b":
                self.printProblems(self.__problemService.getAllProblems())
            elif optiune == "c":
                self.printAssignments(self.__assignmentService.getAllAssignments())
            elif optiune == "x":
                break
            else:
                print("Ati dat o optiune gresita, incercati din nou!")

    def addStudent(self):
        idStudent = int(input("Dati id-ul studentului: "))
        name = input("Dati un nume studentului: ")
        grup = int(input("Dati un grup studentului: "))
        self.__studentService.addStudent(idStudent, name, grup)

    def updateStudent(self):
        idStudent = int(input("Dati id-ul studentului caruia sa i se modifice datele: "))
        newName = input("Dati noul nume al studentului: ")
        newGrup = int(input("Dati noul grup al studentului: "))
        self.__studentService.updateStudent(idStudent, newName, newGrup)

    def deleteStudent(self):
        idStudent = int(input("Dati id-ul studentului: "))
        self.__studentService.deleteStudent(idStudent)

    def findStudent(self):
        idStudent = int(input("Dati id-ul studentului cautat: "))
        print(self.__studentService.findStudent(idStudent))

    def addProblem(self):
        idProblem = int(input("Dati id-ul problemei: "))
        description = input("Dati descrierea problemei: ")
        deadline = int(input("Dati deadline-ul problemei: "))
        self.__problemService.addProblem(idProblem, description, deadline)

    def updateProblem(self):
        newProblemId = int(input("Dati id-ul problemei: "))
        newDescription = input("Dati o noua descrierea problemei: ")
        newDeadline = int(input("Dati noul deadline: "))
        self.__problemService.updateProblem(newProblemId, newDescription, newDeadline)

    def deleteProblem(self):
        idProblem = int(input("Dati numarul(id-ul) problemei: "))
        self.__problemService.deleteProblem(idProblem)

    def findProblem(self):
        idProblem = int(input("Dati id-ul problemei: "))
        self.__problemService.findProblem(idProblem)

    def addAssignment(self):
        idAssignment = int(input("Dati id-ul asignari: "))
        idStudent = int(input("Dati id-ul studentului: "))
        idProblem = int(input("Dati id-ul problemei: "))
        grade = int(input("Dati nota primita de student pentru aceasta problema: "))
        self.__assignmentService.addAssignment(idAssignment, idStudent, idProblem, grade)

    def updateAssignment(self):
        idAssignment = int(input("Dati id-ul asignari: "))
        idStudent = int(input("Dati id-ul studentului: "))
        idProblem = int(input("Dati id-ul problemei: "))
        grade = int(input("Dati noua nota: "))
        self.__assignmentService.updateAssignment(idAssignment, idStudent, idProblem, grade)

    def deleteAssignment(self):
        idAssignment = int(input("Dati id-ul asignari care sa se stearga: "))
        self.__assignmentService.deleteAssignment(idAssignment)

    def findAssignment(self):
        idAssignment = int(input("Dati id-ul asignari cautate: "))
        self.__assignmentService.findAssignment(idAssignment)

    def sorting(self):
        idProblem = int(input("Dati id-ul problemei pe baza careia se va creea statistica: "))
        param = input("Dati criteriul dupa care sa se sorteze lista afisata ('1' dupa nume sau '2' dupa nota): ")
        print(self.__assignmentService.sort(idProblem, param))

    def printStudents(self, param):
        for student in param:
            print(student)
    def printProblems(self, param):
        for problem in param:
            print(problem)

    def printAssignments(self, param):
        for ass in param:
            print(ass)

    def printBelowFive(selfs, param):
        for x in param:
            print(x)