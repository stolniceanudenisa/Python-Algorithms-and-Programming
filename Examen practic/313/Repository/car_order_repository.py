from typing import Dict, Union, Optional, List

import jsonpickle

from Domain.car_order import CarOrder


class CarOrderRepository:

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __read_file(self):
        try:
            with open(self.filename, 'r') as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __write_file(self, objects: Dict[str, CarOrder]):
        with open(self.filename, 'w') as f:
            f.write(jsonpickle.dumps(objects))

    def create(self, car_order: CarOrder) -> None:
        """
        TODO
        :param car_order:
        :return:
        """
        car_orders = self.__read_file()
        if self.read(car_order.id_car_order) is not None:
            raise KeyError(f'Exista deja o comanda id-ul {car_order.id_car}.')

        car_orders[car_order.id_car_order] = car_order
        self.__write_file(car_orders)

    def read(self, id_car_order=None) -> Union[Optional[CarOrder], List[CarOrder]]:
        """
        TODO

        """

        car_orders = self.__read_file()
        if id_car_order:
            if id_car_order in car_orders:
                return car_orders[id_car_order]
            else:
                return None

        return list(car_orders.values())

    def update(self, car_order: CarOrder) -> None:
        """
        TODO
        :param car_order:
        :return:
        """

        car_orders = self.__read_file()
        if self.read(car_order.id_car_order) is None:
            msg = f'Nu exista o comanda cu id-ul {car_order.id_car} de actualizat.'
            raise KeyError(msg)

        car_orders[car_order.id_car_order] = car_order
        self.__write_file(car_orders)

    def delete(self, id_car_order: str) -> None:
        """
        TODO
        :param id_car_order:
        :return:
        """
        car_orders = self.__read_file()
        if self.read(id_car_order) is None:
            raise KeyError(
                f'Nu exista o comanda cu id-ul {id_car_order} pe care sa o stergem.')

        del car_orders[id_car_order]
        self.__write_file(car_orders)