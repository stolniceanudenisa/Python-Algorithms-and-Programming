from service.angajatService import AngajatService
from service.trainingService import TrainingService


class Consola:
    def __init__(self, angajatService: AngajatService, trainingService: TrainingService):
        self.__angajatService = angajatService
        self.__trainingService = trainingService

    def adaugaAngajat(self):
        try:
            idAngajat = input("Dati id-ul angajatului: ")
            nume = input("Dati numele angajatului: ")
            idTraining = input("Dati id-ul training-ului "
                               "(sau nimic daca angajatul nu este asignat la un training): ")
            self.__angajatService.adauga(idAngajat, nume, idTraining)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modificaAngajat(self):
        try:
            idAngajat = input("Dati id-ul angajatului de modificat: ")
            numeNou = input("Dati numele nou al angajatului: ")
            idTrainingNou = input("Dati id-ul training-ului nou: "
                                  "(sau nimic daca angajatul nu este asignat la un training): ")
            self.__angajatService.modifica(idAngajat, numeNou, idTrainingNou)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def stergeAngajat(self):
        try:
            idAngajat = input("Dati id-ul angajatului de sters: ")
            self.__angajatService.sterge(idAngajat)
        except KeyError as e:
            print(e)

    def adaugaTraining(self):
        try:
            idTraining= input("Dati id-ul trainingului: ")
            nume = input("Dati numele trainingului: ")
            descriere = input("Dati descriere trainingului: ")
            durata = int(input("Dati durata (in minute) a trainingului: "))
            self.__trainingService.adaugaTraining(idTraining, nume, descriere, durata)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modificaTraining(self):
        try:
            idTraining = input("Dati id-ul trainingului de modificat: ")
            numeNou = input("Dati noul nume al trainingului: ")
            descriereNoua = input("Dati noua descriere a trainingului: ")
            durataNoua = int(input("Dati noua durata a trainingului: "))
            self.__trainingService.modificaTraining(idTraining, numeNou, descriereNoua, durataNoua)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def stergeTraining(self):
        try:
            idTraining = input("Dati id-ul trainingului de sters: ")
            self.__trainingService.stergeTraining(idTraining)
        except KeyError as e:
            print(e)

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def printMeniu(self):
        print("1. Adauga angajat")
        print("2. Modifica angajat")
        print("3. Sterge angajat")
        print("4. Adauga training")
        print("5. Modifica training")
        print("6. Sterge training")
        print("a. Afiseaza toti angajatii")
        print("t. Afiseaza toate trainingurile")
        print("x. Iesire")

    def meniu(self):
        while True:
            self.printMeniu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.adaugaAngajat()
            elif optiune == "2":
                self.modificaAngajat()
            elif optiune == "3":
                self.stergeAngajat()
            elif optiune == "4":
                self.adaugaTraining()
            elif optiune == "5":
                self.modificaTraining()
            elif optiune == "6":
                self.stergeTraining()
            elif optiune == "a":
                self.afiseaza(self.__angajatService.getAllAngajati())
            elif optiune == "t":
                self.afiseaza(self.__trainingService.getAllTrainings())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita, reincercati!")
