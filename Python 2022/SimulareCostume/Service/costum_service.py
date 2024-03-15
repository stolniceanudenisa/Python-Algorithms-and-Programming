from Domain.costum import Costum
from Repository.costum_file_repository import CostumFileRepository


class CostumService:
    def __init__(self, costum_repository: CostumFileRepository):
        self.__costum_repository = costum_repository

    def add_costum(self, id_costum, denumire_costum, tematica_costum, pret_costum, disponibilitate_costum):

        costum = Costum(id_costum, denumire_costum, tematica_costum, pret_costum, disponibilitate_costum)
        self.__costum_repository.add(costum)

    def get_all_costume(self):
        """
        Da toata lista de carti.
        :return: o lista de obiecte de tip Carte
        """
        return self.__costum_repository.get_all()

