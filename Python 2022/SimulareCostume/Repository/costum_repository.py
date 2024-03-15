from Domain.costum import Costum


class CostumRepository:

    def __init__(self):
        self.__storage = {}

    def __len__(self):
        return len(self.__storage)

    def get_costume(self):
        """

        """
        return self.__storage

    def add(self, costum: Costum):
        """
        Adauga o carte.
        :param costum: obiect de tipul carte
        :return:
        """
        # if self.get_by_id(carte.get_id_carte()) is not None:
        #     raise KeyError(f'Exista deja o carte cu id-ul {carte.get_id_carte()}')

        self.__storage[costum.get_id_costum()] = costum

    def get_all(self):
        """
        Da lista de carti.
        :return: o lista de obiecte de tipul Carte.
        """
        return list(self.__storage.values())