# d mașină, id locație, timp final, cost / km, distanță parcursă, status (în desfășurare, finalizată).
from domain.entity import Entity


class Comanda(Entity):
    def __init__(self,id, car_id, locatie_id, time, cost_km, distance, status):
        super().__init__(id)
        self.__car_id = car_id
        self.__locatie_id = locatie_id
        self.__time =time
        self.__cost_km = cost_km
        self.__distance = distance
        self.__status = status

    @property
    def car_id(self):
        return self.__car_id

    @property
    def locatie_id(self):
        return self.__locatie_id

    @property
    def status(self):
        return self.__status

    @property
    def time(self):
        return self.__time

    @property
    def cost_km(self):
        return self.__cost_km

    @property
    def distance(self):
        return self.__distance

    def __str__(self):
        return 'Comanda {}, car_id {}, location_id {}, status: {}, time: {}, cost_km {}, distance: {}'\
            .format(self.id, self.car_id, self.locatie_id, self.status, self.time, self.cost_km, self.distance)


