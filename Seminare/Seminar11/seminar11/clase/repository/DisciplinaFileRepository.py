from seminar11.clase.domain.Disciplina import Disciplina
from seminar11.clase.repository.DisciplinaRepository import DisciplinaRepository


class DisciplinaFileRepository(DisciplinaRepository):

    def __init__(self, nume_fisier):
        super().__init__()
        self.__nume_fisier = nume_fisier
        self.citeste_din_fisier()

    def adauga(self, disciplina):
        super().adauga(disciplina) #cerem metodei adauga din clasa parinte sa adauge disciplina in lista de discipline
        self.scrie_in_fisier() #aceasta lista modificata noi o salvam in fisier

    def modifica(self, disciplina):
        super().modifica(disciplina) #cerem metodei adauga din clasa parinte sa modifice disciplina in lista de discipline
        self.scrie_in_fisier() #aceasta lista modificata noi o salvam in fisier

    def sterge(self, id):
        super().sterge(id) #cerem metodei adauga din clasa parinte sa adauge disciplina cu acel id din lista de discipline
        self.scrie_in_fisier() #aceasta lista modificata noi o salvam in fisier

    def citeste_din_fisier(self):
        try:
            f = open(self.__nume_fisier, "r") #deschidem fisierul in modul CITIRE: "read" (de acolo vine "r")
            linie = f.readline().strip("\n") #citim o prima linie din fisier si scoatem din ea caracterul "\n" (enter)
            while linie != "": #daca linia nu e goala (adica: daca nu am ajuns la finalul fisierului)
                lista_atribute = linie.split(",") #despartim linia citita folosind separatorul ,
                #lista_atribute va fi o lista ce contine, ca elemente, valorile regasite pe linia curenta
                id = int(lista_atribute[0]) #primul element din lista_atribute e id-ul
                nume = lista_atribute[1] #al doilea element din lista_atribute e numele disciplinei
                profesor = lista_atribute[2] #al treilea element din lista_atribute e numele profesorului
                disciplina = Disciplina(id, nume, profesor) #cream disciplina folosind valorile citite din fisier
                super().adauga(disciplina) #apelam metoda adauga din clasa parinte (adica din clasa DisciplinaRepository)
                linie = f.readline().strip("\n") #citim linia urmatoare pe care o vom verifica si prelucra cand intram din nou in while
            f.close() #la final, inchidem fisierul deschis
        except IOError:
            raise IOError("Eroare la deschiderea fisierului " + self.__nume_fisier) #mesaj de eroare daca nu s-a putut deschide fisierul

    def scrie_in_fisier(self):
        try:
            f = open(self.__nume_fisier, "w") #deschidem fisierul in modul SCRIERE: "write" (de acolo vine "w")
            lista_discipline = super().get_all() #din lista noastra de discipline, aducem toate disciplinele
            for disciplina in lista_discipline: #parcurgem fiecare disciplina din lista de discipline
                id = disciplina.get_id()
                nume = disciplina.get_nume()
                profesor = disciplina.get_profesor()
                linie = str(id) + "," + nume + "," + profesor + "\n" #cream o linie de tipul liniilor pe care le-am citit din fisier (atributele separate prin virgula si \n la final de rand)
                f.write(linie) #scriem acea linie in fisier
            f.close() #la final, inchidem fisierul
        except IOError:
            raise IOError("Eroare la deschiderea fisierului " + self.__nume_fisier)  #mesaj de eroare daca nu s-a putut deschide fisierul