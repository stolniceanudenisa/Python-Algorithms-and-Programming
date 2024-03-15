from typing import Dict, Union, Optional, List

import jsonpickle

from Domain.car import Car

class CarRepository:

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __read_file(self):
        try:
            with open(self.filename, 'r') as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __write_file(self, objects: Dict[str, Car]):
        with open(self.filename, 'w') as f:
            f.write(jsonpickle.dumps(objects))

    def create(self, car: Car) -> None:
        """
        TODO
        :param car:
        :return:
        """
        cars = self.__read_file()
        if self.read(car.id_car) is not None:
            raise KeyError(f'Exista deja o masina id-ul {car.id_car}.')

        cars[car.id_car] = car
        self.__write_file(cars)

    def read(self, id_car=None) -> Union[Optional[Car], List[Car]]:
        """
        TODO

        """

        cars = self.__read_file()
        if id_car:
            if id_car in cars:
                return cars[id_car]
            else:
                return None

        return list(cars.values())

    def update(self, car: Car) -> None:
        """
        TODO
        :param car:
        :return:
        """

        cars = self.__read_file()
        if self.read(car.id_car) is None:
            msg = f'Nu exista o masina cu id-ul {car.id_car} de actualizat.'
            raise KeyError(msg)

        cars[car.id_car] = car
        self.__write_file(cars)

    def delete(self, id_car: str) -> None:
        """
        TODO
        :param id_car:
        :return:
        """
        cars = self.__read_file()
        if self.read(id_car) is None:
            raise KeyError(
                f'Nu exista o masina cu id-ul {id_car} pe care sa o stergem.')

        del cars[id_car]
        self.__write_file(cars)