#  indicativ, nivel confort (standard, ridicat, premium), plata cu cardul (da / nu), model.
from domain.Car import Car


class CarDTO(Car):

    def __init__(self, id, indicativ, confort, plata_card, model, suma_cost, nr_cost):
        super().__init__(id, indicativ, confort, plata_card, model)
        self.__suma_cost = suma_cost
        self.__nr_cost = nr_cost

    # def get_indicativ(self):
    #     return self.__indicativ
    #
    # def set_indicativ(self, indicativ):
    #     self.__indicativ = indicativ

    @property
    def suma_cost(self):
        return self.__suma_cost

    @suma_cost.setter
    def suma_cost(self, value):
        self.__suma_cost = value

    @property
    def nr_cost(self):
        return self.__nr_cost

    @nr_cost.setter
    def nr_cost(self, value):
        self.__nr_cost = value


    def __str__(self):
        return super().__str__() + ' cost mediu: '+ str(self.__suma_cost / self.__nr_cost)


