
class Ui:
    def __init__(self, service_animal):
        self.__params = None
        self.__service_animal = service_animal

        self.__comenzi = {
            "1": self.__ui_afisare_animal_dupa_specie,
            "2": self.__ui_pret_total_sejur
        }

    @staticmethod
    def meniu():
        """
        se afiseaza meniul cu optiuni
        """

        print("---------- MENIU ----------")
        print("1.Afisare animale dupa specie")
        print("2.Afisare pret sejur")

    def __ui_afisare_animal_dupa_specie(self):
        """
        se afiseaza animalele care sunt de specia data de la tastatura
        """

        if len(self.__params) != 0:
            print("numar parametrii invalid")
            return
        specie = input("Alegeti specia: ")
        if specie == "":
            print("specie invalida")
            return

        animale_cautate = self.__service_animal.cautare_animal_dupa_specie(specie)
        if len(animale_cautate) == 0:
            print(f"nu exista animale de specia {specie}")
            return

        for animal in animale_cautate:
            print(animal)

    def __ui_pret_total_sejur(self):
        """
        se calculeaza pretul pentru un sejur de numar zile nr_zile dat de la tastatura
        """

        if len(self.__params) != 0:
            print("numar parametrii invalid")
            return
        nume = input("Alegeti numele: ")
        nr_zile = int(input("Alegeti numarul de zile: "))
        if nr_zile < 1:
            print("nr de zile invalid")
            return
        pret_sejur = self.__service_animal.calculeaza_pret_animal_sejur(nume, nr_zile)
        if pret_sejur:
            print(pret_sejur)
        else:
            print(f"nu exista animalul cu numele {nume}")

    def run(self):
        """
        se executa comenzile date
        """

        while True:
            comanda = input(">>> ")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split()
            nume_comanda = parti[0]
            self.__params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("ui error: tip numeric invalid")
            else:
                print("comanda invalida")
