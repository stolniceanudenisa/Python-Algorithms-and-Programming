import jsonpickle as jsonpickle

from Domain.costum import Costum
from Repository.costum_repository import CostumRepository

class CostumFileRepository(CostumRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.citeste_din_fisier()

    def citeste_din_fisier(self):
        try:
            f = open(self.__filename, "r")  # deschidem fisierul in modul CITIRE: "read" (de acolo vine "r")
            linie = f.readline().strip("\n")  # citim o prima linie din fisier si scoatem din ea caracterul "\n" (enter)
            while linie != "":  # daca linia nu e goala (adica: daca nu am ajuns la finalul fisierului)
                lista_atribute = linie.split(",")  # despartim linia citita folosind separatorul ,
                id_costum = lista_atribute[0]  # primul element din lista_atribute e id-ul
                denumire_costum = lista_atribute[1]  # al doilea element din lista_atribute e numele disciplinei
                tematica_costum = lista_atribute[2]  # al doilea element din lista_atribute e numele disciplinei
                pret_costum = lista_atribute[3]  # al treilea element din lista_atribute e numele profesorului
                disponibilitate_costum = lista_atribute[4]
                costum = Costum(id_costum, denumire_costum, tematica_costum, pret_costum, disponibilitate_costum)
                super().add(costum)  # apelam metoda adauga din clasa parinte (adica din clasa DisciplinaRepository)
                linie = f.readline().strip(
                    "\n")  # citim linia urmatoare pe care o vom verifica si prelucra cand intram din nou in while
            f.close()  # la final, inchidem fisierul deschis
        except IOError:
            print(
                "Eroare la deschiderea fisierului " + self.__filename)  # mesaj de eroare daca nu s-a putut deschide fisierul

    def scrie_in_fisier(self):
        try:
            f = open(self.__filename, "w")  # deschidem fisierul in modul SCRIERE: "write" (de acolo vine "w")
            lista_costume = super().get_all()  # din lista noastra de discipline, aducem toate disciplinele
            for costum in lista_costume:  # parcurgem fiecare disciplina din lista de discipline
                id_costum = costum.get_id_costum()
                denumire_costum = costum.get_denumire_costum()
                tematica_costum = costum.get_tematica_costum()
                pret_costum = costum.get_pret__costum()
                disponibilitate_costum = costum.get_disponibilitate_costum()
                linie = str(
                    id_costum) + "," +denumire_costum + "," + tematica_costum + "," + pret_costum + " " + disponibilitate_costum + "\n"  # cream o linie de tipul liniilor pe care le-am citit din fisier (atributele separate prin virgula si \n la final de rand)
                f.write(linie)  # scriem acea linie in fisier
            f.close()  # la final, inchidem fisierul
        except IOError:
            print(
                "Eroare la deschiderea fisierului " + self.__filename)  # mesaj de eroare daca nu s-a putut deschide fisierul

    def add(self, costum: Costum):
        super().add(costum)
        self.scrie_in_fisier()
