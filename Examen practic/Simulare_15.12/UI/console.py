from Repo.clasament_repo import ClasamentFileRepo
from Repo.concurent_repo import ConcurentFileRepo
from Service.clasament_service import ClasamentService
from Service.concurent_service import ConcurentService


class Console:
    def __init__(self,concurent_repo:ConcurentFileRepo,concurent_service:ConcurentService,clasament_repo:ClasamentFileRepo,clasament_service:ClasamentService):
        self.__concurent_repo=concurent_repo
        self.__concurent_service=concurent_service
        self.__clasament_repo=clasament_repo
        self.__clasament_service=clasament_service



    def Menu(self):
        print("""
        1. Cautare dupa sponsor
        2. Clasament
        """)


    def run_ui(self):
        while True:
            self.Menu()
            optiune=input("Dati o optiune: ")
            if optiune =="1":
                self.handle_print(self.handle_cautare())
            elif optiune =="2":
                self.handle_clasament()
    def handle_cautare(self):
        sponsor_dorit=input("Dati un sponsor pentru cautare: ")
        return self.__concurent_service.cautare_dupa_sponsor(sponsor_dorit)


    def handle_print(self,lista):
        for object in lista:
            print(object)

    def handle_clasament(self):
        print(self.__clasament_service.clasament_final())
        self.__clasament_service.clasament()
        self.__clasament_service.print_clasament()