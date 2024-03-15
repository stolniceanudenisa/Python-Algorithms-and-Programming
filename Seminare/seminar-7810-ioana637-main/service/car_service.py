from domain import CarValidator
from domain.Car import Car
from repository.car_repository import CarRepository
from repository.comanda_repository import OrderRepository


class CarService:
    """

    """

    def __init__(self, car_repo: CarRepository, car_validator: CarValidator, order_repo: OrderRepository):
        """

        :param car_repo:
        :param car_validator:
        :param order_repo:
        """
        self.__repository = car_repo
        self.__validator = car_validator
        self.__order_repository = order_repo

    def add_car(self, id, indicativ, confort, plata_card, model):
        """

        :param id:
        :param indicativ:
        :param confort:
        :param plata_card:
        :param model:
        :return:
        """
        car = Car(id, indicativ, confort, plata_card, model)
        self.__validator.validate(car)
        self.__repository.create(car)

    def delete_car(self, id):
        if len(self.__order_repository.findByCarId(id)) > 0:
            raise ValueError('Masina nu poate fi stearsa')
        self.__repository.delete(id)

    def get_all(self):
        return self.__repository.read()

    def get_cars_by_confort(self, confort):
        # return list(filter(lambda car: car.confort == confort, self.get_all()))
        return [car for car in self.get_all() if car.confort == confort]

    def get_pairs_with_indicativ_and_plata_card(self):
        cars_indicative = list(map(lambda car: car.indicativ, self.get_all()))
        cars_plata_card = list(map(lambda car: car.plata_card, self.get_all()))
        return list(zip(cars_indicative, cars_plata_card))