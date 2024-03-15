from service.studentService import StudentService
from service.problemaService import ProblemaLaboratorService
from service.asignareService import AsignareService
from domeniu.exceptii.duplicateError import DuplicateError

from utils import clear_file


class Consola:
    def __init__(self, studentService: StudentService, problemaLaboratorService: ProblemaLaboratorService, asignareService: AsignareService):
        self.__studentService = studentService
        self.__problemaLaboratorService = problemaLaboratorService
        self.__asignareService = asignareService

    def adaugaStudent(self):
        try:
            idStudent = input("Dati id-ul studentului: ")
            nume = input("Dati numele studentului: ")
            grup = input("Dati grupul studentului: ")
            self.__studentService.adaugaStudent(idStudent, nume, grup)
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)

    def adaugaProblemaLaborator(self):
        try:
            idProblemaLaborator = input("Dati numarul laboratorului si numarul problemei de laborator: ")
            descriere = input("Dati descrierea problemei de laborator: ")
            deadline = input("Dati deadline-ul problemei de laborator: ")
            self.__problemaLaboratorService.adaugaProblemaLaborator(idProblemaLaborator, descriere, deadline)
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)

    def adaugaAsignare(self):
        try:
            idAsignare = input("Dati id-ul asignari: ")
            idStudent = input("Dati id-ul studentului: ")
            idProblemaLaborator = input("Dati numarul laboratorului si numarul problemei de laborator: ")
            nota = input("Dati nota primita de student pe acest laborator si problema: ")
            while float(nota) > 10 or float(nota) < 1:
                print("Nota trebuie sa fie in intervalul 1 - 10")
                nota = input("Dati nota primita de student pe acest laborator si problema: ")
            self.__asignareService.adaugaAsignare(idAsignare, idStudent, idProblemaLaborator, nota)
        except KeyError as e1:
            print(e1)
        except DuplicateError as e2:
            print(e2)

    def stergeStudent(self):
        try:
            idStudent = input("Dati id-ul studentului: ")
            self.__studentService.stergeStudent(idStudent)
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)

    def stergeProblemaLaborator(self):
        try:
            idProblemaLaborator = input("Dati numarul laboratorului si numarul problemei: ")
            self.__problemaLaboratorService.stergeProblemaLaborator(idProblemaLaborator)
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)

    def stergeAsignare(self):
        try:
            idAsignare = input("Dati id-ul asignari care sa se stearga: ")
            self.__asignareService.stergeAsignare(idAsignare)
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)

    def modificaStudent(self):
        try:
            idStudent = input("Dati id-ul studentului caruia sa i se modifice datele: ")
            numeNou = input("Dati noul nume al studentului: ")
            grupNou = input("Dati noul grup al studentului: ")
            self.__studentService.modificaStudent(idStudent, numeNou, grupNou)
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)

    def modificaProblemaLaborator(self):
        try:
            idProblemaLaborator = input("Dati numarul laboratorului si numarul problemei de laborator careia sa i se modifice datele: ")
            descriereNoua = input("Dati noua descriere a problemei de laborator: ")
            deadlineNou = input("Dati noul deadline al problemei de laborator: ")
            self.__problemaLaboratorService.modificaProblemaLaborator(idProblemaLaborator, descriereNoua, deadlineNou)
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)

    def modificaAsignare(self):
        try:
            idAsignare = input("Dati id-ul asignari: ")
            idStudent = input("Dati id-ul studentului: ")
            idProblemaLaborator = input("Dati numarul laboratorului si numarul problemei de laborator: ")
            nota = input("Dati nota primita de student pe acest laborator si problema: ")
            while float(nota) > 10 or float(nota) < 1:
                print("Nota trebuie sa fie in intervalul 1 - 10")
                nota = input("Dati nota primita de student pe acest laborator si problema: ")
            self.__asignareService.modificaAsignare(idAsignare, idStudent, idProblemaLaborator, nota)
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)

    def cautareStudent(self):
        try:
            idStudent = input("Dati id-ul studentului cautat: ")
            print(self.__studentService.cautaStudent(idStudent))
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)

    def cautareProblemaLaborator(self):
        try:
            idProblemaLaborator = input("Dati numarul laboratorului si numarul problemei de laborator cautate: ")
            print(self.__problemaLaboratorService.cautareProblemaLaborator(idProblemaLaborator))
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)

    def cautareAsignare(self):
        try:
            idAsignare = input("Dati id-ul asignari cautate: ")
            print(self.__asignareService.cautareAsignare(idAsignare))
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)

    def sortare(self):
        try:
            idProblemaLaborator = input("Dati id-ul problemei pe baza careia se va creea statistica: ")
            param = input("Dati criteriul dupa care sa se sorteze lista afisata ('1' dupa nume sau '2' dupa nota): ")
            print(self.__asignareService.ordonare(idProblemaLaborator, param))
        except KeyError as e1:
            print(e1)
        except ValueError as e2:
            print(e2)


    def afiseazaStudent(self, entitati):
        for entitate in entitati:
            print(entitate)

    def afiseazaProblemaLaborator(self, entitati):
        for entitate in entitati:
            print(entitate)

    def afiseazaAsignare(self, entitati):
        for entitate in entitati:
            print(entitate)

    def afiseazaStudentiCuMedieSubCinci(self, rez):
        for x in rez:
            print(x)

    def printMeniu(self):
        print("1. Adauga studenti")
        print("2. Modifica datele despre un student cu id-ul dat")
        print("3. Sterge un student dupa id")
        print("4. Cautare student dupa id")
        print("5. Adauga problema de laborator")
        print("6. Modifica datele despre o problema de laborator cu numarul laboratorului si numarul problemei dat")
        print("7. Sterge o problema de laborator dupa numarul laboratorului si numarul problemei")
        print("8. Cautare problema de laborator dupa id")
        print("9. Asigneaza unui student un laborator")
        print("10. Modifica o asignare")
        print("11. Sterge o asignare")
        print("12. Cautare o asignare dupa id")
        print("13. Scrieti '1' pentru sortarea studentilor dupa nume sau '2' pentru sortarea studentilor dupa nota ")
        print("14. Afiseaza lista cu studentii care au media sub 5")
        print("15. Sterge toti studentii din fisier")
        print("16. Sterge toate problemele din fisier")
        print("17. Sterge toate asignarile din fisier")
        print("a. Afiseaza toti sudenti")
        print("b. Afiseaza toate problemele de laborator")
        print("c. Afiseaza toate asignarile")
        print("x. Iesire din program")

    def meniu(self):
        while True:
            self.printMeniu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.adaugaStudent()
            elif optiune == "2":
                self.modificaStudent()
            elif optiune == "3":
                self.stergeStudent()
            elif optiune == "4":
                self.cautareStudent()
            elif optiune == "5":
                self.adaugaProblemaLaborator()
            elif optiune == "6":
                self.modificaProblemaLaborator()
            elif optiune == "7":
                self.stergeProblemaLaborator()
            elif optiune == "8":
                self.cautareProblemaLaborator()
            elif optiune == "9":
                self.adaugaAsignare()
            elif optiune == "10":
                self.modificaAsignare()
            elif optiune == "11":
                self.stergeAsignare()
            elif optiune == "12":
                self.cautareAsignare()
            elif optiune == "13":
                self.sortare()
            elif optiune == "14":
                self.afiseazaStudentiCuMedieSubCinci(self.__asignareService.getStudentiCuMedieSubCinci())
            elif optiune == "15":
                clear_file("studenti.json")
            elif optiune == "16":
                clear_file("problema_laborator.json")
            elif optiune == "17":
                clear_file("asignare.json")
            elif optiune == "a":
                self.afiseazaStudent(self.__studentService.getAllStudenti())
            elif optiune == "b":
                self.afiseazaProblemaLaborator(self.__problemaLaboratorService.getAllProblemeLaborator())
            elif optiune == "c":
                self.afiseazaAsignare(self.__asignareService.getAllAsignari())
            elif optiune == "x":
                exit(0)
            else:
                print("Ati dat o optiune gresita, incercati din nou!")
