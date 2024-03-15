from Domain.car_validator import CarValidator
from Repository.json_repository import JsonRepository

from Service.car_order_service import CarOrderService
from Service.car_service import CarService
from Service.location_service import LocationService
from Service.undo_redo_service import UndoRedoService
from Tests.test_car_repository import test_car_repository
from UserInterface.Console import Console


def main():

    undo_redo_service = UndoRedoService()

    car_repository = JsonRepository('cars.json')
    car_validator = CarValidator()
    car_service = CarService(car_repository, car_validator, undo_redo_service)

    location_repository = JsonRepository('locations.json')
    location_service = LocationService(location_repository, undo_redo_service)

    car_order_repository = JsonRepository('orders.json')
    car_order_service = CarOrderService(car_order_repository,
                                        car_repository,
                                        location_repository,
                                        undo_redo_service)

    # car_service.add_car('20', '4242', 'standard', 'logan')
    # car_service.add_car('21', '5634', 'premium', 'toyota')
    # location_service.add_location('10', 'clujului', 23)

    console = Console(car_service,
                      location_service,
                      car_order_service,
                      undo_redo_service)
    console.run_console()


if __name__ == '__main__':
    test_car_repository()
    main()