from typing import List

from Domain.car import Car
from Domain.car_order import CarOrder
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService
from ViewModels.car_mean_cost_per_km import CarMeanCostPerKm
from ViewModels.street_most_common_car_model import StreetMostCommonCarModel


class CarOrderService:
    def __init__(self,
                 car_order_repository: Repository,
                 car_repository: Repository,
                 location_repository: Repository,
                 undo_redo_service: UndoRedoService):
        self.car_order_repository = car_order_repository
        self.car_repository = car_repository
        self.location_repository = location_repository
        self.undo_redo_service = undo_redo_service

    def add_car_order(self,
                      id_car_order: str,
                      id_car: str,
                      id_location: str,
                      cost_per_km: float):
        """
        TODO
        """
        car_order = CarOrder(id_car_order, id_car, id_location, cost_per_km)

        # ar merge si intr-un validator
        if self.car_repository.read(id_car) is None:
            raise KeyError(f'Nu exista masina cu id-ul {id_car}')
        if self.location_repository.read(id_location) is None:
            raise KeyError(f'Nu exista locatie cu id-ul {id_location}')

        self.car_order_repository.create(car_order)

    def update_car_order(self,
                         id_car_order: str,
                         id_car: str,
                         id_location: str,
                         cost_per_km: float):
        """
        TODO
        """
        car_order = CarOrder(id_car_order, id_car, id_location, cost_per_km)

        # ar merge si intr-un validator
        if self.car_repository.read(id_car) is None:
            raise KeyError(f'Nu exista masina cu id-ul {id_car}')
        if self.location_repository.read(id_location) is None:
            raise KeyError(f'Nu exista locatie cu id-ul {id_location}')

        self.car_order_repository.update(car_order)

    def delete_car_order(self, id_car_order: str):
        self.car_order_repository.delete(id_car_order)

    def get_all(self) -> List[CarOrder]:
        return self.car_order_repository.read()

    def get_cars_ordered_by_mean_cost_per_km(self) -> List[CarMeanCostPerKm]:

        result = []
        d = {} # d[id_car] = lista cu costuri pentru masina cu id-ul id_car
        for order in self.get_all():
            id_car = order.id_car
            if id_car not in d:
                d[id_car] = [order.cost_per_km]
            else:
                d[id_car].append(order.cost_per_km)

        for id_car in d:
            car = self.car_repository.read(id_car)
            mean_cost_per_km = sum(d[id_car]) / len(d[id_car])
            result.append(CarMeanCostPerKm(car.fleet_number, car.comfort_level, mean_cost_per_km))

        # for car in self.car_repository.read():
        #     #orders_for_car = list(filter(lambda order: order.id_car == car.id_entity, self.get_all()))
        #     orders_for_car = [order for order in self.get_all() if order.id_car == car.id_entity]
        #     sum_of_costs = sum([order.cost_per_km for order in orders_for_car])
        #     result.append(CarMeanCostPerKm(car.fleet_number, car.comfort_level, sum_of_costs / len(orders_for_car)))
        #

        return sorted(result, key=lambda x: x.mean_cost_per_km)

    def get_most_common_model(self, cars: List[Car]) -> str:
        d = {}
        for car in cars:
            if car.model in d:
                d[car.model] += 1
            else:
                d[car.model] = 1

        max_key = list(d.keys())[0]
        for key in d:
            if d[key] > d[max_key]:
                max_key = key

        return max_key

    def get_most_frequent_car_model_for_each_street(self) -> List[StreetMostCommonCarModel]:
        """
        Determina modelul masinii care vine cel mai des la comanda pentru fiecare strada.
        :return:
        """
        result = []
        for loc in self.location_repository.read():
            orders_to_loc = [order for order in self.get_all() if order.id_location == loc.id_entity]
            cars_in_orders = [self.car_repository.read(ord.id_car) for ord in orders_to_loc]
            most_common_model = self.get_most_common_model(cars_in_orders)
            result.append(StreetMostCommonCarModel(loc.street_name, most_common_model))

        return result


