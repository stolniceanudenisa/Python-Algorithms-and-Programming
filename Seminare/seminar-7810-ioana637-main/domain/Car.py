#  indicativ, nivel confort (standard, ridicat, premium), plata cu cardul (da / nu), model.
from domain.entity import Entity


class Car(Entity):

    def __init__(self, id, indicativ, confort, plata_card, model):
        super().__init__(id)
        self.__indicativ = indicativ
        self.__confort = confort
        self.__plata_card = plata_card
        self.__model = model

    # def get_indicativ(self):
    #     return self.__indicativ
    #
    # def set_indicativ(self, indicativ):
    #     self.__indicativ = indicativ

    @property
    def indicativ(self):
        return self.__indicativ

    @indicativ.setter
    def indicativ(self, value):
        self.__indicativ = value

    @property
    def confort(self):
        return self.__confort

    @confort.setter
    def confort(self, value):
        self.__confort = value

    @property
    def plata_card(self):
        return self.__plata_card

    @plata_card.setter
    def plata_card(self, value):
        self.__plata_card = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value


    def search_text(self, search) -> True or False:
        return (search in self.__model or search in self.__confort)


    def __str__(self):
        return 'Car {}. {} - {}, confort: {}, plata card: {}'.format(self.id,
                                        self.indicativ, self.model, self.confort, self.plata_card)



