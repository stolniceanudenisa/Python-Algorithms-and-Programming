from Domain.imobil import Imobil
from Repo.imobil_repo import ImobilRepo


class ImobilFileRepo(ImobilRepo):

    def __init__(self, filename):
        ImobilRepo.__init__(self)
        self.__filename = filename

    def __read_from_file(self):
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            self._storage.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_imobil = parts[0]
                    adresa_imobil = parts[1]
                    pret_imobil = parts[2]
                    tip_imobil = parts[3]
                    imobil = Imobil(id_imobil, adresa_imobil, pret_imobil, tip_imobil)
                    self._storage[imobil.get_id_imobil()] = imobil

    def get_all_file(self):
        """
        returneaza toate imobilele
        :return:
        """
        self.__read_from_file()
        return self._storage.values()

    def get_by_id_file(self, id_imobil):
        """

        :param id_imobil:
        :return:
        """
        self.__read_from_file()
        if id_imobil in self._storage:
            return self._storage[id_imobil]
        return None
