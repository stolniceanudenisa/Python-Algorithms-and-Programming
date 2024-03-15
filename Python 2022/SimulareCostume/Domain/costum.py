class Costum:
    def __init__(self, id_costum, denumire_costum, tematica_costum, pret__costum, disponibilitate_costum):
        """
        Creaaza un film.
        :param id_costum: id-ul costumului trebuie sa fie unic
        :param denumire_costum: denumirea costumului
        :param tematica_costum: tematica costumului
        :param pret__costum: pretul costumului
        :param disponibilitate_costum: disponibilitatea costumului: True sau False
        """
        self.__id_costum = id_costum
        self.__denumire_costum = denumire_costum
        self.__tematica_costum = tematica_costum
        self.__pret__costum = pret__costum
        self.__disponibilitate_costum = disponibilitate_costum

    def get_id_costum(self):
        return self.__id_costum

    def get_denumire_costum(self):
        return self.__denumire_costum

    def get_tematica_costum(self):
        return self.__tematica_costum

    def get_pret__costum(self):
        return self.__pret__costum

    def get_disponibilitate_costum(self):
        return self.__disponibilitate_costum

    def set_id_costum(self, id_costum):
        self.__id_costum = id_costum

    def set_denumire_costum(self, denumire_costum):
        self.__denumire_costum = denumire_costum

    def set_tematica_costum(self, tematica_costum):
        self.__tematica_costum = tematica_costum

    def set_pret__costum(self, pret__costum):
        self.__pret__costum = pret__costum

    def set_disponibilitate_costum(self, disponibilitate_costum):
        self.__disponibilitate_costum = disponibilitate_costum

    def __str__(self):
        return f" Id-ul costumului: {self.__id_costum}, denumirea costumului: {self.__denumire_costum}," \
               f" tematica costumului: {self.__tematica_costum}, pretul costumului: {self.__pret__costum}," \
               f" disponobilitatea costumului: {self.__disponibilitate_costum} "
