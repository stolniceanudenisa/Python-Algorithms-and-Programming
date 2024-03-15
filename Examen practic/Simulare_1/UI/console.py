from Repo.imobil_file_repo import ImobilFileRepo
from Service.imobil_service import ImobilService


class Console:
    def __init__(self, imobil_repo: ImobilFileRepo, imobil_service: ImobilService):
        self.__imobil_repo = imobil_repo
        self.__imobil_service = imobil_service

    def Menu(self):
        print("""
        1. Media pe pret dorit.
        2. Afisare tranzactie.
        """)

    def run_console(self):
        while True:
            self.Menu()
            optiune = input("Dati optiunea : ")
            if optiune == "1":
                print(self.handle_media_pe_pret())


            elif optiune == '2':
                print(self.handle_tranzactie())
            else:
                print("optiune invalida.")

    def handle_media_pe_pret(self):
        tip_oferta = input("tipul imobilului: ")
        return self.__imobil_service.Media_pret(tip_oferta)

    def handle_tranzactie(self):
        id_imobil = input("id-ul imobilului: ")
        pret_negociere = int(input("pret negociere: "))
        return self.__imobil_service.tranzactie(id_imobil, pret_negociere)
