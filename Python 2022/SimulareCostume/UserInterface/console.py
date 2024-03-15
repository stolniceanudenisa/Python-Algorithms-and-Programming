from Service.costum_service import CostumService


class Console:
    def __init__(self, costum_service: CostumService):
        self.__costum_service = costum_service

    def show_menu2(self):
        print("""
        0. Adauga costum
        1. Afisare toate costume disponibile pentru o tematica data, ordonate crescator dupa pret.
        2. Inchiriere costum.
        3. Inchiriere costum.
        4. Exit.
        """)

    def run_console(self):
        while True:
            self.show_menu2()
            option = input('Alegeti optiunea: ')
            if option == '0':
                self.handle_add_costum()
            elif option == '1':
                self.handle_afisare_costume_disponibile_sortate()
            elif option == '2':
                self.handle_inchiriere_costum()
            elif option == '3':
                self.handle_show_all(self.__costum_service.get_all_costume())
            elif option == '4':
                break
            else:
                print('Comanda invalida. Reincercati.')

    def handle_afisare_costume_disponibile_sortate(self):
        pass

    def handle_inchiriere_costum(self):
        pass

    def handle_show_all(self, objects):
        for obj in objects:
            print(obj)

    def handle_add_costum(self):
        try:
            id_costum = input('Dati id-ul costumului: ')
            denumire_costum = input('Dati denumirea costumului: ')
            tematica_costum = input('Dati tematica costumului: ')
            pret_costum = input('Dati pretul costumului: ')
            disponibilitate_costum = input('Dati disponibilitatea costumului: ')

            self.__costum_service.add_costum(id_costum, denumire_costum, tematica_costum, pret_costum, disponibilitate_costum)

        except ValueError as ve:
            print('Eroare de validare: ', ve)
        except KeyError as ke:
            print('Eroare de ID:', ke)
        except Exception as ex:
            print('Eroare: ', ex)

