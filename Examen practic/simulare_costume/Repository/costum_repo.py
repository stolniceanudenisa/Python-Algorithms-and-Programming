from Domain.costum import Costum


class CostumFileRepo:

    def __init__(self,filename):
        self._storage={}
        self.__filename=filename

    def read_by_file(self):
        """

        :return:
        """
        with open(self.__filename,"r") as f:
            lines=f.readlines()
            self._storage.clear()
            for line in lines:
                line=line.strip() #am copiat linia fara spatii goale
                if line !="":
                    parts=line.split(",") #parts= lista prin impartirea la virgula
                    id_costum=parts[0]
                    denumire_costum=parts[1]
                    tematica_costum=parts[2]
                    pret_costum=parts[3]
                    disponibilitate_costum=parts[4]
                    costum=Costum(id_costum,denumire_costum,tematica_costum,pret_costum,disponibilitate_costum)
                    self._storage[id_costum]=costum






    def get_all_file(self):
        """

        :return:
        """
        self.read_by_file()
        return self._storage.values()

    def get_by_id(self,id_costum):
        """

        :param id_costum:
        :return:
        """
        self.read_by_file()
        if id_costum in self._storage:
            return self._storage[id_costum]
        return None

    def get_by_tematica(self,tematica_costum):
        """

        :param tematica_costum:
        :return:
        """
        self.read_by_file()
        costume=self.get_all_file()
        for costum in costume:
            if costum.get_tematica_costum()==tematica_costum:
                # return self._storage[costum.get_id_costum()]
                return costum