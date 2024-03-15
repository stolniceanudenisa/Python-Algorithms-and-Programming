from seminar10.clase.domain.Inscriere import Inscriere
from seminar10.clase.repository.InscriereRepository import InscriereRepository


class InscriereFileRepository(InscriereRepository):
    def __init__(self, nume_fisier, student_repository, inscriere_repository):
        super().__init__(student_repository, inscriere_repository)
        self.__nume_fisier = nume_fisier
        self.citeste_din_fisier()

    def adauga(self, inscriere):
        super().adauga(inscriere) #cerem metodei adauga din clasa parinte sa adauge inscrierea in lista de inscrieri
        self.scrie_in_fisier() #aceasta lista modificata noi o salvam in fisier

    def modifica(self, inscriere):
        super().modifica(inscriere) #cerem metodei adauga din clasa parinte sa modifice inscrierea in lista de inscrieri
        self.scrie_in_fisier() #aceasta lista modificata noi o salvam in fisier

    def sterge(self, id):
        super().sterge(id) #cerem metodei adauga din clasa parinte sa adauge inscrierea cu acel id din lista de inscrieri
        self.scrie_in_fisier() #aceasta lista modificata noi o salvam in fisier

    def citeste_din_fisier(self):
        try:
            f = open(self.__nume_fisier, "r") #deschidem fisierul in modul CITIRE: "read" (de acolo vine "r")
            linie = f.readline().strip("\n") #citim o prima linie din fisier si scoatem din ea caracterul "\n" (enter)
            while linie != "": #daca linia nu e goala (adica: daca nu am ajuns la finalul fisierului)
                lista_atribute = linie.split(",") #despartim linia citita folosind separatorul ,
                #lista_atribute va fi o lista ce contine, ca elemente, valorile regasite pe linia curenta
                id = int(lista_atribute[0]) #primul element din lista_atribute e id-ul inscrierii
                student_id = int(lista_atribute[1]) #al doilea element din lista_atribute e id-ul studentului
                disciplina_id = int(lista_atribute[2]) #al treilea element din lista_atribute e id-ul disciplinei
                nota = int(lista_atribute[3])  #al patrulea element din lista_atribute e nota
                inscriere = Inscriere(id, student_id, disciplina_id, nota) #cream inscrierea folosind valorile citite din fisier
                super().adauga(inscriere) #apelam metoda adauga din clasa parinte (adica din clasa InscriereRepository)
                linie = f.readline().strip("\n") #citim linia urmatoare pe care o vom verifica si prelucra cand intram din nou in while
            f.close() #la final, inchidem fisierul deschis
        except IOError:
            print("Eroare la deschiderea fisierului " + self.__nume_fisier) #mesaj de eroare daca nu s-a putut deschide fisierul

    def scrie_in_fisier(self):
        try:
            f = open(self.__nume_fisier, "w") #deschidem fisierul in modul SCRIERE: "write" (de acolo vine "w")
            lista_inscrieri = super().get_all() #din lista noastra de inscrieri, aducem toate inscrierile
            for inscriere in lista_inscrieri: #parcurgem fiecare inscriere din lista de inscrieri
                id = inscriere.get_id()
                student_id = inscriere.get_student_id()
                disciplina_id = inscriere.get_disciplina_id()
                nota = inscriere.get_nota()
                linie = str(id) + "," + str(student_id) + "," + str(disciplina_id) + "," + str(nota) + "\n" #cream o linie de tipul liniilor pe care le-am citit din fisier (atributele separate prin virgula si \n la final de rand)
                f.write(linie) #scriem acea linie in fisier
            f.close() #la final, inchidem fisierul
        except IOError:
            print("Eroare la deschiderea fisierului " + self.__nume_fisier)  #mesaj de eroare daca nu s-a putut deschide fisierul