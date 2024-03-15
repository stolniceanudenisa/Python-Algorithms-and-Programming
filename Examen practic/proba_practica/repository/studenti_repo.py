from domain.studenti import *

class StudentiRepository:
    def __init__(self, fileName):
        self.studenti = []
        self.fileName = fileName


    def read(self):
        with open(self.fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                linie = line.split(",")
                id = linie[0]
                nume = linie[1]
                prezente = linie[2]
                nota = linie[3]
                student = Studenti(id, nume, prezente, nota)
                self.studenti.insert(int(id) - 1, student)

    def write(self, student):
        with open(self.fileName, "w") as f:
            f.write(str(student.__str__()))

    def getBonus(self, p:int, b:int):
        for i in range(0, len(self.studenti)):
            if self.studenti[i].get_prezenta() >= p:#daca stundetul are mai multe prezente decat p
                if(self.studenti[i].get_nota() + b <= 10):
                    self.studenti[i].set_nota(int(self.studenti[i].get_nota() + b))
                    with open("bonus.txt", "w") as g:
                        g.write(str(self.studenti[i].get_id() + " , " + self.studenti[i].get_nota))

    def add(self, student):
        """
        Adauga un student nou in aplicatie si in fisier
        :param student: un student
        :return:
        """
        try:
            if(self.find_id(student.get_id()) is None):#daca cumva exista deja un asemenea student, ridicam o eroare
                self.studenti.append(student)#adaugam in aplicatie
                self.write(student)#adaugam in fisier
            else:
                raise ValueError("Exista un student cu acest id")
        except ValueError as v:
            print(v)

    def find_id(self, id):
        """
        Gaseste id-ul studentului in lista de studenti
        Functie folosita pentru a idetifica daca exista sau nu un student in lista cu id in momentul in care adaugam un nou student
        :param id:
        :return:
        """
        for student in self.studenti:
            if student.get_id() == id:
                return id
        return None

    def find_all(self):
        """
        Returneaza o lista de studenti
        :return:
        """
        return list(self.studenti)