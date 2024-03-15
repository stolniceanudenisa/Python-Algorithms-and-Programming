from Service.car_order_service import CarOrderService
from Service.car_service import CarService
from Service.location_service import LocationService


class Console:
    def __init__(self,
                 car_service: CarService,
                 location_service: LocationService,
                 car_order_service: CarOrderService):
        self.car_service = car_service
        self.location_service = location_service
        self.car_order_service = car_order_service

    def show_menu(self):
        print('a[car|loc|cmd]. Adauga masina sau locatie sau comanda.')
        print('u[car|loc|cmd]. Update masina sau locatie sau comanda.')
        print('d[car|loc|cmd]. Delete masina sau locatie sau comanda.')
        print('s[car|loc|cmd]. Show all masina sau locatie sau comanda.')
        print('x. Iesire')

    def run_console(self):
        while True:
            self.show_menu()
            opt = input('Alegeti optiunea: ')
            if opt == 'acar':
                self.handle_add_car()
            elif opt == 'aloc':
                self.handle_add_location()
            elif opt == 'acmd':
                self.handl_add_car_order()
            elif opt == 'scar':
                self.handle_show_all(self.car_service.get_all())
            elif opt == 'sloc':
                self.handle_show_all(self.location_service.get_all())
            elif opt == 'scmd':
                self.handle_show_all(self.car_order_service.get_all())
            elif opt == 'x':
                break
            else:
                print('Optiune invalida, reincercati.')

    def handle_add_car(self):
        try:
            id_car = input('Dati id-ul masinii: ')
            fleet_num = input('Dati indicativul: ')
            comfort_level = input('Dati nivelul de comfort (standard, ridicat, premium): ')
            card_payment = input('Plata cu card? da / nu: ')
            if card_payment == 'da':
                card_payment = True
            else:
                card_payment = False
            model = input('Dati modelul masinii: ')

            self.car_service.add(id_car, fleet_num, comfort_level, card_payment, model)
        except ValueError as ve:
            print('Eroare de validare:', ve)
        except KeyError as ke:
            print('Eroare de cheie', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_show_all(self, objects):
        for obj in objects:
            print(obj)

    def handle_add_location(self):
        try:
            id_location = input('Dati id-ul locatiei: ')
            street_name = input('Dati numele strazii: ')
            street_num = int(input('Dati numarul strazii: '))
            block = input('Dati blocul: ')
            entry = input('Dati scara: ')
            other_info = input('Dati alte informatii: ')

            self.location_service.add(id_location, street_name, street_num,
                                      block, entry, other_info)
        except ValueError as ve:
            print('Eroare de validare:', ve)
        except KeyError as ke:
            print('Eroare de cheie', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handl_add_car_order(self):
        try:
            id_car_order = input('Dati id-ul comenzii: ')
            id_car = input('Dati id-ul masinii: ')
            id_location = input('Dati id-ul locatiei: ')
            final_time = float(input('Dati timpul final: '))
            cost_per_km = float(input('Dati costul per km: '))
            distance_traveled = float(input('Dati distanta parcursa: '))
            status = input('Dati statusul comenzii: ')

            self.car_order_service.add(id_car_order, id_car, id_location, final_time,
                                       cost_per_km, distance_traveled, status)
        except ValueError as ve:
            print('Eroare de validare:', ve)
        except KeyError as ke:
            print('Eroare de cheie', ke)
        except Exception as ex:
            print('Eroare:', ex)
