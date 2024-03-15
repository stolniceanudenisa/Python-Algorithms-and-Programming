#  nume stradă, număr, bloc, scară, alte indicații.
from domain.entity import Entity


class Locatie(Entity):
    def __init__(self, id, strada, numar, bloc, scara, indicatii):
        super().__init__(id)
        self.__strada = strada
        self.__numar = numar
        self.__bloc = bloc
        self.__scara =scara
        self.__indicatii = indicatii


    @property
    def strada(self):
        return self.__strada

    @property
    def numar(self):
        return self.__numar

    @property
    def indicatii(self):
        return self.__indicatii

    @property
    def bloc(self):
        return self.__bloc

    @property
    def scara(self):
        return self.__scara

    def __str__(self):
        return 'Locatie {} strada: {} nr. {}, bloc: {}, scara: {}, indicatii: {}'\
            .format(self.id, self.strada, self.numar, self.bloc, self.scara, self.indicatii)

