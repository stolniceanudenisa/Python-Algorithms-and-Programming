from Repository.costum_repo import CostumFileRepo


class CostumService:
    def __init__(self,costum_repo:CostumFileRepo):
        self.__costum_repo=costum_repo

    def ordonare_dupa_pret(self,costume):
        """

        :param costume:
        :return:
        """
        return sorted(costume, key=lambda costum:costum.get_pret_costum() )   # sau luam valorile tot intr un dictionar si faceam sorted(costume.items() adica tuple din key si valori , key= d:d[3] fiind a treia valoare pretul nostru


    def afisare_costume_disponibile(self,tematica_costum:None):
        """

        :param tematica_costum:
        :return:
        """
        costume=self.__costum_repo.get_all_file()
        costume_disponibile=[]
        for costum in costume:
            if costum.get_tematica_costum() == tematica_costum and costum.get_disponibilitate_costum()== "True":
                costume_disponibile.append(costum)
            elif tematica_costum is None and costum.get_disponibilitate_costum()== "True" :
                costume_disponibile.append(costum)


        return self.ordonare_dupa_pret(costume_disponibile)

    def print_costume_disponibile(self,tematica_costum:None):
        """

        :param tematica_costum:
        :return:
        """
        for costum in self.afisare_costume_disponibile(tematica_costum):
            print(costum)




    def inchiriere_costum(self,id_costum):
        """

        :param id_costum:
        :return:
        """
        costume=self.__costum_repo.get_all_file()
        if self.__costum_repo.get_by_id(id_costum) is None:
            return (f"Costumul cu id-ul {id_costum} nu exista")
        elif self.__costum_repo.get_by_id(id_costum).get_disponibilitate_costum()=="False":
             return (f"Ne pare rau. Costumul este inchiriat de alta persoana. Dar va sugeram costumul :{self.afisare_costume_disponibile(None)[0].get_denumire_costum()}")
        elif self.__costum_repo.get_by_id(id_costum).get_disponibilitate_costum()=="True":
            return (self.__costum_repo.get_by_id(id_costum))
