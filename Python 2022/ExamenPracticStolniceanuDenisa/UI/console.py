from Service.cafea_service import CafeaService


class Console:
    def __init__(self, cafea_service: CafeaService):
        self.__cafea_service = cafea_service

    def menu(self):
        print("""
        1. Afisarea tuturor cafelelor.
        2. Afisare toate cafele din tara respectiva.
        3. Adaugare cafea.
        x. Exit
        """)

    def run_ui(self):
        while True:
            self.menu()
            opt = input('Introduceti optiunea: ')
            if opt == '1':
                self.handle_afisare_cafele()
            elif opt == '2':
                self.handle_afis_cafele_tara()
            elif opt == '3':
                self.handle_add_cafea()
            elif opt == 'x':
                break
            else:
                print('Optiune invalida. Reincercati.')

    def handle_afisare_cafele(self):
        cafele = self.__cafea_service.get_all_cafele()
        for cafea in cafele:
            print(cafea)

    def handle_afis_cafele_tara(self):
        nume_tara = input('Dati numele tarii: ')
        rez = self.__cafea_service.afis_cafele_tara(nume_tara)
        for cafea in rez:
            print(cafea)

    def handle_add_cafea(self):
        idc = input('Dati id-ul cafelei: ')
        nume = input('Dati numele cafelei: ')
        tara = input('Dati tara cafelei: ')
        pret = float(input('Dati pretul cafelei: '))
        try:
            self.__cafea_service.add_cafea(idc, nume, tara, pret)
            self.handle_afisare_cafele()
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
