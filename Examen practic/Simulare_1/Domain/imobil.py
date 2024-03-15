class Imobil:
    def __init__(self, id_imobil, adresa_imobil, pret_imobil, tip_imobil):
        """
        creeaza un obiect de tip imobil
        :param id_imobil:string
        :param adresa_imobil:string
        :param pret_imobil:string
        :param tip_imobil: string
        """
        self.__id_imobil = id_imobil
        self.__adresa_imobil = adresa_imobil
        self.__pret_imobil = pret_imobil
        self.__tip_imobil = tip_imobil

    def get_id_imobil(self):
        return self.__id_imobil

    def get_adresa_imobil(self):
        return self.__adresa_imobil

    def get_pret_imobil(self):
        return self.__pret_imobil

    def get_tip_imobil(self):
        return self.__tip_imobil

    def set_id_imobil(self, id_imobil_nou):
        self.__id_imobil = id_imobil_nou

    def set_adresa_imobil(self, adresa_imobil_nou):
        self.__adresa_imobil = adresa_imobil_nou

    def set_pret_imobil(self, pret_imobil_nou):
        self.__pret_imobil = pret_imobil_nou

    def set_tip_imobil(self, tip_imobil_nou):
        self.__tip_imobil = tip_imobil_nou

    def __str__(self):
        return f"Id imobil: {self.__id_imobil},adresa imobil : {self.__adresa_imobil}," \
               f"pret imobil: {self.__pret_imobil},tip imobil: {self.__tip_imobil}"
