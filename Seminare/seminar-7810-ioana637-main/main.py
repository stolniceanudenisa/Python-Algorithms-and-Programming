
from UI.user_interface import UserInterface
from domain.CarValidator import CarValidator
from domain.LocationValidator import LocationValidator
from domain.OrderValidator import OrderValidator
from repository.car_file_repository import CarFileRepository
from repository.car_repository import CarRepository
from repository.comanda_repository import OrderRepository
from repository.locatie_repository import LocatieRepository
from service.car_service import CarService
from service.location_service import LocationService
from service.order_service import OrderService
from teste.test_all import test_all

test_all()
# car_repository = CarRepository()
car_repository = CarFileRepository('cars.pkl')
location_repository = LocatieRepository()
order_repository = OrderRepository()

car_validator = CarValidator()
order_validator = OrderValidator()
location_validator = LocationValidator()

car_service = CarService(car_repository, car_validator, order_repository)
location_service = LocationService(location_repository, location_validator, order_repository)
order_service = OrderService(order_repository, order_validator, car_repository, location_repository)

# testing data
#if run with car file repo, for the second run please comment this line, the car will be stored in the file
car_service.add_car(1, '1', 'high', 'da', '1234')
location_service.add_location(1, 'kogalniceanu', 1, 1, 1, 'nimic')
location_service.add_location(2, 'rebreanu', 2, 2, 2, 'nimic 2')
order_service.add_order(1, 1, 1, 20, 3, 10, 'done')
order_service.add_order(2, 1, 1, 20, 3, 7, 'done')
order_service.add_order(3, 1, 1, 20, 3, 12, 'done')
order_service.add_order(4, 1, 2, 20, 3, 20, 'done')
order_service.add_order(50, 1, 2, 20, 3, 14, 'done')

console = UserInterface(car_service, location_service, order_service)
console.runUI()
