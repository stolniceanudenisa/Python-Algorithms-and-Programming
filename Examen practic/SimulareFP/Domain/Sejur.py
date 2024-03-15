class Sejur:
    def __init__(self,nume,nr_zile):
        self.__nume=nume
        self.__nr_zile=nr_zile
    def get_nume(self):
        """
        Functie de get_nume
        :return: nume
        """
        return self.__nume
    def get_nr_zile(self):
        """
        Functie de get_nr_zile
        :return:nr_zile
        """
        return self.__nr_zile
    def set_nume(self,nume):
        """
        Functie de setare nume
        :param nume: str
        :return: numele setat
        """
        self.__nume=nume
    def set_nr_zile(self,nr_zile):
        """
        Functie de setare nr_zile
        :param nr_zile: int
        :return: numar de zile setat
        """
        self.__nr_zile=nr_zile
    def __str__(self):
        return self.__nume+','+str(self.__nr_zile)