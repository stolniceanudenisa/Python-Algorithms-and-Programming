from domeniu.exceptii.duplicateError import DuplicateError
from service.angajatService import AngajatService
from service.angajatTrainingService import AngajatTrainingService
from service.trainingService import TrainingService


class Consola:
    def __init__(self, angajatService: AngajatService,
                 trainingService: TrainingService,
                 angajatTrainingService: AngajatTrainingService):
        self.__angajatService = angajatService
        self.__trainingService = trainingService
        self.__angajatTrainingService = angajatTrainingService

    def adaugaAngajat(self):
        try:
            idAngajat = input("Dati id-ul angajatului: ")
            nume = input("Dati numele angajatului: ")
            self.__angajatService.adauga(idAngajat, nume)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modificaAngajat(self):
        try:
            idAngajat = input("Dati id-ul angajatului de modificat: ")
            numeNou = input("Dati numele nou al angajatului: ")
            self.__angajatService.modifica(idAngajat, numeNou)
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
        except DuplicateError as e:
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

    def inscrieAngajatLaTraining(self):
        try:
            idAngajatTraining = input("Dati id-ul inscrierii: ")
            idAngajat = input("Dati id-ul angajatului")
            idTraining = input("Dati id-ul trainingului: ")
            self.__angajatTrainingService.adaugaInscriere(idAngajatTraining, idAngajat, idTraining)
        except DuplicateError as e:
            print(e)
        except KeyError as e:
            print(e)

    def stergeInscriere(self):
        idAngajat = input("Dati id-ul angajatului: ")
        idTraining = input("Dati id-ul trainingului:")
        self.__angajatTrainingService.stergeInscriere(idAngajat, idTraining)

    def ordoneazaTraininguriDupaParticipanti(self):
        rezultat = self.__trainingService.ordoneazaTraininguriDupaNrParticipanti()
        self.afiseaza(rezultat)

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
        print("7. Inscrie angajat la training")
        print("8. Sterge inscriere")
        print("9. Ordoneaza traininguri dupa participanti")
        print("a. Afiseaza toti angajatii")
        print("t. Afiseaza toate trainingurile")
        print("i. Afiseaza toate inscrierile")
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
            elif optiune == "7":
                self.inscrieAngajatLaTraining()
            elif optiune == "8":
                self.stergeInscriere()
            elif optiune == "9":
                self.ordoneazaTraininguriDupaParticipanti()
            elif optiune == "a":
                self.afiseaza(self.__angajatService.getAllAngajati())
            elif optiune == "t":
                self.afiseaza(self.__trainingService.getAllTrainings())
            elif optiune == "i":
                self.afiseaza(self.__angajatTrainingService.getAllInscrieri())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita, reincercati!")
