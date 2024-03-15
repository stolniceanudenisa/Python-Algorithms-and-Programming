from typing import List

from Domain.car import Car
from Domain.car_validator import CarValidator
from Repository.car_repository import CarRepository


class CarService:
    def __init__(self,
                 car_repository: CarRepository,
                 car_validator: CarValidator):
        self.car_repository = car_repository
        self.car_validator = car_validator

    def add(self,
            id_car: str,
            fleet_number: str,
            comfort_level: str,
            card_payment: bool,
            model: str):
        car = Car(id_car, fleet_number, comfort_level, card_payment, model)
        self.car_validator.validate(car)
        self.car_repository.create(car)

    def update(self,
               id_car: str,
               fleet_number: str,
               comfort_level: str,
               card_payment: bool,
               model: str):
        car = Car(id_car, fleet_number, comfort_level, card_payment, model)
        self.car_validator.validate(car)
        self.car_repository.update(car)

    def delete(self, id_car: str):
        self.car_repository.delete(id_car)

    def get_all(self) -> List[Car]:
        return self.car_repository.read()
