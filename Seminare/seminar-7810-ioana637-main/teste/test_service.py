from domain.CarValidator import CarValidator
from repository.car_repository import CarRepository
from repository.comanda_repository import OrderRepository
from service.car_service import CarService


def test_car_service():
    car_validator = CarValidator()
    car_repository = CarRepository()
    order_repository = OrderRepository()
    car_service = CarService(car_repository, car_validator, order_repository)
    car_service.add_car(12, 23, 'standard', 'Nu', 'model')
    assert len(car_service.get_all()) == 1
    # TODO delete_masina, update_masina etc...

def test_order_service():
    # TODO
    pass

def test_location_service():
    # TODO
    pass


def test_all_services():
    test_car_service()
    test_location_service()
    test_order_service()
