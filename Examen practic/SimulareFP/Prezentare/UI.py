from Business.Service import Service
from Domain.Animal import Animal


class Consola:
    def __init__(self, service: Service):
        self.service = service
        self.comenzi = {
            "adauga_animal":self.add,
            "sterge_animal":self.delete,
            "modifica_animal":self.update,
            "cauta_id":self.find_by_id,
            "cauta_specie":self.find_by_specie,
            "pret_total":self.pret_total,
            "printeaza_animalele":self.print_all

        }
    def add(self,params):
        """
        Functie de adaugare in fisier

        """
        if len(params)!=4:
            print("Numar parametrii invalid!")
            return
        id=int(params[0])
        nume=params[1]
        pret=int(params[2])
        specie=params[3]
        animal=Animal(id,nume,pret,specie)
        self.service.add(animal)
        print("Adaugare efectuata cu succes!")

    def delete(self,params):
        """
        Functie de stergere din fisier(dupa id-ul animalului)
        """
        if len(params)!=1:
            print("Numar parametrii invalid!")
            return
        id=int(params[0])
        self.service.delete(id)
        print("Stergere efctuata cu succes!")
    def update(self,params):
        """
        Functie de modificare a unui animal

        :return: animal modificat
        """
        if len(params)!=4:
            print("Numar parametrii invalid!")
            return
        id=int(params[0])
        nume = params[1]
        pret = int(params[2])
        specie = params[3]
        animal = Animal(id, nume, pret, specie)
        self.service.update(animal)
        print("Modificare efectuata cu succes!")

    def find_by_id(self,params):
        """
        Functie de cautare a unui animal dupa id-ul sau.
        :param params:
        :return: Animalul cu id-ul respectiv
        """
        if len(params)!=1:
            print("Numar parametrii invalid!")
            return
        id=int(params[0])
        print(self.service.find_by_id(id))
    def find_by_specie(self,params):
        """
        Functie de cautare a animalelor de o specie anume.
        :param params: -
        :return: Animalele de specie data
        """
        if len(params)!=1:
            print("Numar parametrii invalid!")
            return
        specie=params[0]
        self.service.find_by_specie(specie)
    def pret_total(self,params):
        """
        Functie care afiseaza pretul total platit de un animal pentru sejur(pt un nr. de zile)
        :param params:
        :return: Pret total
        """
        if len(params)!=2:
            print("Numar parametrii invalid!")
            return
        nume=params[0]
        nr_zile=int(params[1])
        rez=self.service.pret_total(nume,nr_zile)
        if rez==-1:
            print("Nu exista niciun animal cu acest nume in acest hotel!")
        else:
            print(rez)


    def print_all(self,params):
        """
        Functie care afiseaza toate animalele.
        :param params:
        :return: Toate animalele
        """
        if len(params)!=0:
            print("Numar parametrii invalid!")
            return
        self.service.print_all()

    def ui_printeaza_HI(self):
        print("adauga_animal")
        print("sterge_animal")
        print("modifica_animal")
        print("cauta_id")
        print("cauta_specie")
        print("pret_total")
        print("printeaza_animalele")

    def runUI(self):
        print("Pentru a accesa o lista cu comenzi si cu parametrii asteptati ca input, introdu comanda help, iar pentru"
              "a iesi introdu comanda exit")
        while True:
            command = input(">>>")
            command = command.strip()
            parti = command.split()
            nume_comanda = parti[0]
            params = parti[1:]
            if nume_comanda == "exit":
                print("BYE!")
                return
            if nume_comanda in self.comenzi:
                try:
                    self.comenzi[nume_comanda](params)
                except ValueError:
                    print("Eroare invalida! tip numeric invalid!")
