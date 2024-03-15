from Service.angajatService import AngajatService


class Consola:
    def __init__(self, angajatService: AngajatService):
        self.__angajatService = angajatService

    def handle_adaugaAngajat(self):
        try:
            idAngajat = input('Dati id-ul angajatului: ')
            nume = input('Dati numele angajatului: ')
            self.__angajatService.adaugaAngajat(idAngajat, nume)
        except KeyError as e:
            print(e)

    def handle_modificaAngajat(self):
        try:
            idAngajat = input('Dati id-ul angajatului existent: ')
            numeNou = input('Dati noul nume al angajatului: ')
            self.__angajatService.modificaAngajat(idAngajat, numeNou)
        except KeyError as e:
            print(e)

    def handle_stergeAngajat(self):
        try:
            idAngajat = input('Dati id-ul angajatului care va fi sters: ')
            self.__angajatService.stergeAngajat(idAngajat)
        except KeyError as e:
            print(e)

    def handle_afiseazatotiAngajatii(self, entitati):
        for entitate in entitati:
            print(entitate)

    def printMeniu(self):
        print("1. Adauga angajat. ")
        print("2. Modifica angajat. ")
        print("3. Stergre angajat. ")
        print("a. Afiseaza toti angajatii. ")
        print("x. Exit.")

    def meniu(self):
        while True:
            self.printMeniu()
            optiune = input("Introduceti optiunea: ")
            if optiune == "1":
                self.handle_adaugaAngajat()
            elif optiune == "2":
                self.handle_modificaAngajat()
            elif optiune == "3":
                self.handle_stergeAngajat()
            elif optiune == "a":
                self.handle_afiseazatotiAngajatii(self.__angajatService.getAllAngajati())
            elif optiune == "x":
                break
            else:
                print("Optiune invalida. Reincercati. ")
