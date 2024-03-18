from Repo.hotel_file_repo import HotelRepoFile
from Services.hotel_service import HotelService


class Console:
    def __init__(self,hotel_repo:HotelRepoFile,hotel_service:HotelService):
        self.__hotel_repo=hotel_repo
        self.__hotel_service=hotel_service


    def Menu(self):
        print("""
        1. Cautare animal pe baza de specie.
        2. Pret Total
        3. Toate Animalele
        """)



    def run_ui(self):
        while True:
            self.Menu()
            optiune=input("Dati o optiune : ")
            if optiune == '1':
                self.handle_print(self.handle_cautare())

            elif optiune == '2':
                print(self.handle_pret_total())

            elif optiune == '3':
                self.handle_print(self.handle_get_all())

    def handle_cautare(self):
        specie_cautata=input("Dati o specie:")
        return self.__hotel_service.cautare_dupa_specie(specie_cautata)

    def handle_print(self,lista):
        self.__hotel_service.print_all(lista)


    def handle_pret_total(self):
        nume_animal=input("Dati un nume de animal:")
        numar_zile=int(input("Dati un numar de zile:"))
        return self.__hotel_service.pret_total(nume_animal,numar_zile)

    def handle_get_all(self):
        return self.__hotel_repo.get_all()
