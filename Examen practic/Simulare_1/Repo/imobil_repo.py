from Domain.imobil import Imobil


class ImobilRepo:
    def __init__(self):
        self._storage = {}

    def add(self, imobil: Imobil):
        """
        Adauga un imobil
        :param imobil: obiect de tip imobil
        :return:
        """
        if imobil.get_id_imobil() in self._storage:
            raise KeyError("id duplicat")
        self._storage[imobil.get_id_imobil()] = imobil

    def get_by_id(self, id_imobil):
        """

        :param id_imobil:
        :return:
        """
        if id_imobil in self._storage:
            return self._storage[id_imobil]
        return None

    def get_by_tip(self, tip_imobil):
        """

        :param tip_imobil:
        :return:
        """
        for imobil in self._storage.values():
            if imobil.get_tip_imobil() == tip_imobil:
                return self._storage[imobil.get_id_imobil()]
        return None

    def get_all(self):
        """
        returneaza toate imobilele
        :return:
        """
        return self._storage.values()
