from domain.Comanda import Comanda


class OrderWithCarAndLocation():
    def __init__(self, order, car, location):
        self.__order = order
        self.__car = car
        self.__location = location

    def __str__(self):
        return 'Order: {} - car {}, location {}'.format(self.__order, self.__car, self.__location)
