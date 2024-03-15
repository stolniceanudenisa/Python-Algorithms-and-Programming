from Domain.car_validator import CarValidator
from Repository.car_order_repository import CarOrderRepository
from Repository.car_repository import CarRepository
from Repository.location_repository import LocationRepository
from Service.car_order_service import CarOrderService
from Service.car_service import CarService
from Service.location_service import LocationService
from Tests.test_car_repository import test_car_repository
from UserInterface.Console import Console


def main():
    car_repository = CarRepository('cars.json')
    car_validator = CarValidator()
    car_service = CarService(car_repository, car_validator)

    location_repository = LocationRepository('locations.json')
    location_service = LocationService(location_repository)

    car_order_repository = CarOrderRepository('car orders.json')
    car_order_service = CarOrderService(car_order_repository,
                                        car_repository,
                                        location_repository)


    console = Console(car_service, location_service, car_order_service)
    console.run_console()


if __name__ == '__main__':
    test_car_repository()

    main()
