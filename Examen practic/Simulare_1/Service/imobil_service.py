from Repo.imobil_file_repo import ImobilFileRepo


class ImobilService:
    def __init__(self, imobil_repo: ImobilFileRepo):
        self.__imobil_repo = imobil_repo

    def get_all_imobil(self):
        """

        :return:
        """
        return self.__imobil_repo.get_all_file()

    def Media_pret(self, tip_imobil):
        """

        :param tip_imobil:
        :return:
        """
        lista_imobil = self.get_all_imobil()

        numar_tip = 0
        suma_pret = 0
        for imobil in lista_imobil:
            if imobil.get_tip_imobil() == tip_imobil:
                suma_pret += int(imobil.get_pret_imobil())
                print(suma_pret)

                numar_tip += 1
        suma = suma_pret / numar_tip
        return suma

    def tranzactie(self, id_imobil, pret_negociat):
        """

        :param id_imobil:
        :param pret_negociat:
        :return:
        """
        if self.__imobil_repo.get_by_id_file(id_imobil).get_tip_imobil() == "vanzare":
            comision = pret_negociat * 2 / 100
        elif self.__imobil_repo.get_by_id_file(id_imobil).get_tip_imobil() == "inchiriere":
            comision = pret_negociat * 50 / 100

        return (self.__imobil_repo.get_by_id_file(id_imobil).get_adresa_imobil(), comision)
