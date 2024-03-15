class Animal:
    def __init__(self,id,nume,pret,specie):
        self.__id=id
        self.__nume=nume
        self.__pret=pret
        self.__specie=specie
    def get_id(self):
        """
        Functie de get_id unui animal
        :return:id
        """
        return self.__id
    def get_nume(self):
        """
        Functie de get_nume unui animal
        :return:nume
        """
        return self.__nume
    def get_pret(self):
        """
        Functie de get_pret unui animal
        :return:pret
        """
        return self.__pret
    def get_specie(self):
        """
        Functie de get_specie unui animal
        :return: specie
        """
        return self.__specie
    def set_nume(self,nume):
        """
        Functie de setare nume pentru un animal
        :param nume: str
        :return: numele nou
        """
        self.__nume=nume
    def set_pret(self,pret):
        """
        Functie de setare a pretului unui animal
        :param pret: int
        :return: pret nou
        """
        self.__pret=pret
    def set_specie(self,specie):
        """
        Functie de setare a speciei unui animal
        :param specie: str
        :return: specia noua
        """
        self.__specie=specie
    def __str__(self):
        return str(self.__id)+','+self.__nume+','+str(self.__pret)+','+self.__specie
