class Costum:
    def __init__(self,id_costum,denumire_costum,tematica_costum,pret_costum,disponibilitate_costum:False):
        self.__id_costum=id_costum
        self.__denumire_costum=denumire_costum
        self.__tematica_costum=tematica_costum
        self.__pret_costum=int(pret_costum)
        self.__disponibilitate_costum=disponibilitate_costum


    def get_id_costum(self):
        return self.__id_costum

    def get_denumire_costum(self):
        return self.__denumire_costum

    def get_tematica_costum(self):
        return  self.__tematica_costum

    def get_pret_costum(self):
        return  self.__pret_costum

    def get_disponibilitate_costum(self):
        return  self.__disponibilitate_costum


    def set_id_costum(self,id_costum_nou):
        self.__id_costum=id_costum_nou

    def set_denumire_costum(self,denumire_costum_nou):
        self.__denumire_costum=denumire_costum_nou

    def set_tematica_costum(self,tematica_costum_nou):
        self.__tematica_costum=tematica_costum_nou

    def set_pret_costum(self,pret_costum_nou):
        self.__pret_costum=pret_costum_nou

    def set_disponibilitate_costum(self,disponibilitate_costum_nou):
        self.__disponibilitate_costum=disponibilitate_costum_nou

    def __str__(self):
        return f"Costumul cu id-ul {self.__id_costum} are denumirea: {self.__denumire_costum}, tematica :{self.__tematica_costum} ,pretul :{self.__pret_costum} si disponibilitatea : {self.__disponibilitate_costum}"