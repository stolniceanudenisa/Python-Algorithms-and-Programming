from typing import List

from Domain.add_operation import AddOperation
from Domain.car import Car
from Domain.car_validator import CarValidator
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService


class CarService:
    def __init__(self,
                 car_repository: Repository,
                 car_validator: CarValidator,
                 undo_redo_service: UndoRedoService):
        self.car_repository = car_repository
        self.car_validator = car_validator
        self.undo_redo_service = undo_redo_service

    def add_car(self,
                id_car: str,
                fleet_number: str,
                comfort_level: str,
                model: str):
        """
        TODO
        """
        car = Car(id_car, fleet_number, comfort_level, model)
        self.car_validator.validate(car)
        self.car_repository.create(car)

        self.undo_redo_service.clear_redo()
        add_operation = AddOperation(self.car_repository, car)
        self.undo_redo_service.add_to_undo(add_operation)

    def update_car(self,
                   id_car: str,
                   fleet_number: str,
                   comfort_level: str):
        """
        TODO
        """
        car = Car(id_car, fleet_number, comfort_level)
        self.car_validator.validate(car)
        self.car_repository.update(car)

    def delete_car(self, id_car: str):
        self.car_repository.delete(id_car)

    def get_all(self) -> List[Car]:
        return self.car_repository.read()
