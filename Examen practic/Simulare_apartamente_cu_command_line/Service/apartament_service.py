from Repo.apartament_repo import ApartamentFileRepo


class ApartamentService:
    def __init__(self,apartament_repo:ApartamentFileRepo):
        self.__apartament_repo=apartament_repo


    def cautare_dupa_tip(self,tip_cautat):
        """
        returneaza o lista cu toate apartamentele ce au tipul respectiv asignat
        :param tip_cautat:string
        :return:
        """
        apartamente=self.__apartament_repo.get_all()
        apartamente_cautate=[]
        for apartament in apartamente:
            if apartament.get_tip_apartament() == tip_cautat:
                apartamente_cautate.append(apartament)

        return apartamente_cautate


    def pret_inchiriere_ap(self,nr_apartament,nr_de_luni):
        """
        returneaza produsul dintre nr_apartament si nr_de_luni si va reprezenta pretul total al inchirierii pe (nr_de_luni)
        :param nr_apartament:string
        :param nr_de_luni:string
        :return:
        """
        apartamente=self.__apartament_repo.get_all()
        for apartament in apartamente:
            if apartament.get_nr_apartament() == nr_apartament:
                pret_total=int(apartament.get_pret_inchiriere_apartament())*int(nr_de_luni)
                break
        return pret_total

    def printall(self,lista):
        for object in lista:
            print(object)