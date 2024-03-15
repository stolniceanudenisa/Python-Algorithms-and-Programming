from Repository.costum_repo import CostumFileRepo
from Service.costum_service import CostumService


class Console:
    def __init__(self,costum_repo:CostumFileRepo,costum_service:CostumService):
        self.__costum_repo=costum_repo
        self.__costum_service=costum_service


    def Menu(self):
        print("""
        1. Afisare costume disponibile
        2. Inchiriere Costum
        3. Afisare toate
        """)


    def run_ui(self):
        while True:
            self.Menu()
            optiune=input("Dati o optiune: ")

            if optiune == "1":
                self.handle_costume_disponibile()
            elif optiune=="2":
                print(self.handle_inchiriere())
            elif optiune=='3':
                self.handle_print(self.get_all_service())
            else:
                print("alegeti o optiune valida .")

    def handle_costume_disponibile(self):
        tematica_dorita=input("Alegeti tematica: ")
        if tematica_dorita == "":
            tematica_dorita=None
        self.__costum_service.print_costume_disponibile(tematica_dorita)

    def handle_inchiriere(self):
        id_costum=input("Alegeti id-ul costumului: ")
        return self.__costum_service.inchiriere_costum(id_costum)

    def handle_print(self,costume):
        for costum in costume:
            print(costum)

    def get_all_service(self):
        return self.__costum_repo.get_all_file()
