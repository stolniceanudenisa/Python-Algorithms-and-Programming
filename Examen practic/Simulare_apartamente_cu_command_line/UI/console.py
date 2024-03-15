from Repo.apartament_repo import ApartamentFileRepo
from Service.apartament_service import ApartamentService


class Console:
    def __init__(self,apartament_repo:ApartamentFileRepo,apartament_service:ApartamentService):
        self.__apartament_repo=apartament_repo
        self.__apartament_service=apartament_service
        self.__comenzi={
            "cauta_apartament":self.handle_cauta,
            "det_pret":self.handle_inchiriere

        }


    def Menu(self):
        print("""
        1. cauta apartament de un anumit tip.
        2. determina pretul inchiriere apartament
        """)


    def run_ui(self):
        while True:
            command=input(">>> ")
            command=command.strip()
            params=command.split()
            nume_comanda=params[0]
            params=params[1:]
            if nume_comanda in self.__comenzi:
                self.__comenzi[nume_comanda](params)


    def handle_cauta(self,params):
        tip_cautat=params[0]
        return self.handle_print(self.__apartament_service.cautare_dupa_tip(tip_cautat))

    def handle_inchiriere(self,params):
        nume_apartament=params[0]
        nr_de_luni=params[1]
        print( self.__apartament_service.pret_inchiriere_ap(nume_apartament,nr_de_luni))

    def handle_print(self,lista):
        self.__apartament_service.printall(lista)
