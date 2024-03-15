from domain.studenti import Studenti
from repository.studenti_repo import *

class StudentiService:
    def __init__(self, student_repository):
        self.student_repository = student_repository

    def add_student(self, id:int, nume:str, prezenta:int, nota):
        """
        Adaugarea studentului in lista.
        Primeste  ca parametrii atributele studentului, formeaza un nou student si il adauga in lista de studenti
        :param id: id-ul studentului, un numar intreg
        :param nume: numele studentlui
        :param prezenta: prezentele studentului, u numar intre
        :param nota: nota studentului
        :return:
        """
        for i in range(1, len(nume) - 1):
            if nume[i] == " " and nume[i - 1] != " " and nume[i + 1] != " ":
                if int(nota) > 0 and int(nota) < 11:#verificam daca toate datele din cerinta sunt respectate
                    if int(prezenta) > -1:
                        student = Studenti(id, nume, prezenta, nota)
                        self.student_repository.add(student)#adauam in lista noul student format
                    else:
                        raise ValueError("Numarul de prezente este prea mic")
                else:
                    raise ValueError("Nota trebuie sa fie intre 1 si 10")
            # else:
            #     raise ValueError("Nume invalid")

    def print_studenti(self):
        """
        Functie ce afiseaza toti studenti din aplicatie
        :return:
        """
        for i in self.student_repository.find_all():
            i.__str__()

    def getBonus(self, p:int, b:int):
        self.student_repository.getBonus(p, b)


