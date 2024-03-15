from domain.ValidationException import ValidationException
from repository.repository_exception import RepositoryException
from service.service_exception import ServiceException


class UserInterface:
    def __init__(self, car_service, location_service, order_service):
        self.__car_service = car_service
        self.__location_service = location_service
        self.__order_service = order_service

    def __print_menu(self):
        print("""
        1. Masini
        2. Locatii
        3. Comenzi
        4. Rapoarte
        """)

    def __print_menu_reports(self):
        print("""
        RAPOARTE ----
        1. Ordonarea străzilor descrescător după lungimea indicațiilor
        2. Ordonarea mașinilor crescător după costul mediu / km.
        3. Determinarea străzilor cu cele mai lungi comenzi (ca distanță).
        4. Filtrarea masinilor care au un confort citit de la tastatura.
        5. Afisarea vitezei medii pentru comenziile inregistrate in aplicatie
        6. Afisarea perechilor formate din indicativul masinii si daca plata s-a efectuat cu cardul sau nu.
        b. Back
        """)

    def __print_menu_car(self):
        print("""
        1. Adaugare masina
        2. Editare
        3. Stergere 
        a. afisare
        b. Back
        """)

    def __print_menu_order(self):
        print("""
        1. Adaugare comanda
        2. Editare
        3. Stergere 
        a. afisare
        aa. afisare completa
        b. Back
        """)

    def __print_menu_location(self):
        print("""
        1. Adaugare locatie
        2. Editare
        3. Stergere 
        4. Undo
        a. afisare
        b. Back
        """)

    def __show_raports(self):
        while True:
            self.__print_menu_reports()
            op = input('Optiune: ')
            if op == '1':
                self.__sort_streets_based_on_indications()
            elif op == '2':
                self.__sort_cars_cost_km()
            elif op == '3':
                self.__get_streets_ordered_by_orders()
            elif op == '4':
                self.__get_cars_filtered_by_confort()
            elif op == '5':
                self.__get_speed_for_orders()
            elif op == '6':
                self.__get_cars_pairs_with_indicativ_and_plata_card()
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __show_cars(self):
        while True:
            self.__print_menu_car()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_masini_add()
            elif op == '2':
                self.__handle_masini_remove()
            elif op == '4':
                self.__sort_cars_cost_km()
            elif op == 'a':
                self.__show_list(self.__car_service.get_all())
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __handle_masini_remove(self):
        try:
            id_car = int(input('Dati id-ul de sters: '))
            self.__car_service.remove_car(id_car)
        except Exception as ex:
            print(ex)

    def __handle_masini_add(self):
        try:
            id_car = int(input('ID-ul: '))
            indicator = int(input('Indicativul: '))
            comfort_level = input('Nivelul de comfort (standard, high, premium): ')
            card_payment = input('Plata cu cardul (da sau nu): ')
            model = input('Modelul: ')
            self.__car_service.add_car(
                id_car,
                indicator,
                comfort_level,
                card_payment,
                model
            )
            print('Masina a fost adaugata!')
        except RepositoryException as ex:
            print('Eroare in repository:', ex)
        except ServiceException as ex:
            print('Eroare in service:', ex)
        except ValidationException as ex:
            print('Eroare in validator:', ex)

    def __show_list(self, objects):
        for object in objects:
            print(object)

    def runUI(self):
        while (True):
            self.__print_menu()
            op = input('Optiune: ')
            if op == '1':
                self.__show_cars()
            elif op == '2':
                self.__show_locations()
            elif op == '3':
                self.__show_orders()
            elif op == '4':
                self.__show_raports()
            elif op == 'x':
                break
            else:
                print('Comanda invalida!')

    def __show_locations(self):
        while True:
            self.__print_menu_location()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_location_add()
            elif op == '4':
                self.__location_service.undo()
            elif op == 'a':
                self.__show_list(self.__location_service.get_all())
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __show_orders(self):
        while True:
            self.__print_menu_order()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_order_add()
            elif op == 'a':
                self.__show_list(self.__order_service.get_all())
            elif op == 'aa':
                self.__show_list(self.__order_service.get_all_with_cars_and_locations())
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __handle_location_add(self):
        try:
            id_location = input('ID-ul: ')
            street_name= input('Numele strazii: ')
            number = input('Numarul strazii: ')
            block = input('Scara: ')
            building = input('Cladirea: ')
            notes = input('Observatii: ')
            self.__location_service.add_location(
                id_location,
                street_name,
                number,
                block,
                building,
                notes
            )
            print('Locatia a fost adaugata!')
        except Exception as err:
            print('Eroare:', err)

    def __handle_order_add(self):
        try:
            id_order = input('ID-ul comenzii: ')
            id_car = input('ID-ul masinii: ')
            id_location = input('ID-ul locatiei: ')
            final_time = input('Timpul final: ')
            km_cost = input('Costul per km: ')
            distance = input('Distanta parcursa: ')
            status = input('Starea comenzii: ')
            self.__order_service.add_order(
                id_order,
                id_car,
                id_location,
                final_time,
                km_cost,
                distance,
                status
            )
            print('Comanda a fost adaugata!')
        except Exception as err:
            print('Erori:', err)
        finally:
            self.__show_list(self.__order_service.get_all())


    def __sort_streets_based_on_indications(self):
        result = self.__location_service.sort_streets()
        for street in result:
            print(street)

    def __get_streets_ordered_by_orders(self):
        result = self.__order_service.get_streets_ordered()
        for street in result:
            print(street)

    def __sort_cars_cost_km(self):
        result = self.__order_service.sort_cars()
        for car in result:
            print(car)

    def __get_cars_filtered_by_confort(self):
        confort = input('Dati confortul')
        # validare confortul citit de la tastatura (optional)
        self.__show_list(self.__car_service.get_cars_by_confort(confort))

    def __get_speed_for_orders(self):
        print(self.__order_service.get_speed_for_orders())

    def __get_cars_pairs_with_indicativ_and_plata_card(self):
        self.__show_list(self.__car_service.get_pairs_with_indicativ_and_plata_card())




