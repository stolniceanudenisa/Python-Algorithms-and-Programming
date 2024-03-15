class Console:

    def __init__(self, studentService):
        self.studentService = studentService

    def print_all(self):
        self.studentService.print_studenti()

    def add(self):
        """
        Functie de preluare a datelor de la utilizator si adaugarea unui student in lista
        :return:
        """
        print("Id-ul studentului: ")
        id = input()
        print("Numele studentului: ")
        nume = input()
        print("Prezentele studentului:")
        prezente = input()
        print("Nota studentului:")
        nota = input()
        self.studentService.add_student(id, nume, prezente, nota)

    def getBonuses(self):
        print("Valorea bonusului pe care vrei sa il adaugi:")
        b = input()
        print("Numarul minim de prezente pentru a primi bonusul")
        p = input()
        self.studentService.getBonus(p, b)

    def printMenu(self):
        menu = ""
        menu += "1. Afiseaza toti studenti din fisier\n"
        menu += "2. Adauga un nou student"
        menu += "3. Adauga bonusuri"
        print(menu)

    def Menu(self):
        while True:
            self.printMenu()
            optiune = input("Dati optiune: ")
            if optiune == "1":
                self.print_all()
            elif optiune == "2":
                self.add()
            elif optiune == "3":
                self.getBonuses()
            elif optiune == "x":
                break