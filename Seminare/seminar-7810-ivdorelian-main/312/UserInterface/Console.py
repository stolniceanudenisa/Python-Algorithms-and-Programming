from Domain.car_validator import CarValidationError
from Repository.exceptions import DuplicateIdError
from Service.car_order_service import CarOrderService
from Service.car_service import CarService
from Service.location_service import LocationService
from Service.undo_redo_service import UndoRedoService


class Console:
    def __init__(self,
                 car_service: CarService,
                 location_service: LocationService,
                 car_order_service: CarOrderService,
                 undo_redo_service: UndoRedoService):
        self.car_service = car_service
        self.location_service = location_service
        self.car_order_service = car_order_service
        self.undo_redo_service = undo_redo_service

    def show_menu(self):
        print('a[car|loc|ord] - adaugare masina sau locatie sau comanda.')
        print('u[car|loc|ord] - update masina sau locatie sau comanda.')
        print('d[car|loc|ord] - delete masina sau locatie sau comanda.')
        print('s[car|loc|ord] - show all masina sau locatie sau comanda.')
        print('locord - show locations ordered by the street name length descendingly.')
        print('carmeancost - show cars ordered by the mean cost per km.')
        print('commonmodels - show streets together with the most common car model going there.')
        print('Undo.')
        print('Redo.')
        print('x. Iesire')

    def run_console(self):
        while True:
            self.show_menu()
            opt = input('Alegeti optiunea: ')

            if opt == 'acar':
                self.handle_add_car()
            elif opt == 'aloc':
                self.handle_add_location()
            elif opt == 'aord':
                self.handle_add_car_order()
            elif opt == 'scar':
                self.handle_show_all(self.car_service.get_all())
            elif opt == 'sloc':
                self.handle_show_all(self.location_service.get_all())
            elif opt == 'sord':
                self.handle_show_all(self.car_order_service.get_all())
            elif opt == 'locord':
                self.handle_show_all(self.location_service.get_ordered_by_street_len_desc())
            elif opt == 'carmeancost':
                self.handle_show_all(self.car_order_service.get_cars_ordered_by_mean_cost_per_km())
            elif opt == 'commonmodels':
                self.handle_show_all(self.car_order_service.get_most_frequent_car_model_for_each_street())
            elif opt == 'undo':
                self.undo_redo_service.do_undo()
            elif opt == 'redo':
                self.undo_redo_service.do_redo()
            elif opt == 'x':
                break
            else:
                print('Comanda invalida, reincearca.')

    def handle_add_car(self):
        try:
            id_car = input('Dati id-ul masinii: ')
            fleet_number = input('Dati indicativul: ')
            comfort_level = input('Dati nivelul de comfort: ')
            model = input('Dati modelul masinii: ')

            self.car_service.add_car(id_car, fleet_number, comfort_level, model)
        except CarValidationError as cve:
            print('Eroare de validare:', cve)
        except DuplicateIdError as de:
            print('ID Duplicat:', de)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_show_all(self, objects):
        for obj in objects:
            print(obj)

    def handle_add_location(self):
        try:
            id_location = input('Dati id-ul locatiei: ')
            street_name = input('Dati numele strazii: ')
            street_number = int(input('Dati nr strazii: '))

            self.location_service.add_location(id_location, street_name, street_number)
        except ValueError as ve:
            print('Eroare de validare:', ve)
        except KeyError as ke:
            print('Eroare de ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_add_car_order(self):
        try:
            id_car_order = input('Dati id-ul comenzii: ')
            id_car = input('Dati id-ul masinii: ')
            id_location = input('Dati id-ul locatiei: ')
            cost_per_km = float(input('Dati costul per km: '))

            self.car_order_service.add_car_order(id_car_order, id_car, id_location, cost_per_km)
        except ValueError as ve:
            print('Eroare de validare:', ve)
        except KeyError as ke:
            print('Eroare de ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)