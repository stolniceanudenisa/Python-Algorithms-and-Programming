from Domain.cafea import Cafea
from Domain.cafea_validator import CafeaValidator
from Repository.cafea_repository import CafeaFileRepo


class CafeaService:
    def __init__(self, cafea_repo: CafeaFileRepo, cafea_validator: CafeaValidator):
        self.__cafea_repo = cafea_repo
        self.__cafea_validator = cafea_validator

    def get_all_cafele(self):
        """
        Returneaza toate cafelele din storage
        :return: cafelele
        """
        return self.__cafea_repo.get_all()

    def add_cafea(self, idc, nume, tara, pret):
        """
        Adauga o cafea
        :param idc: id-ul
        :param nume: numele
        :param tara: tara
        :param pret: pretul
        :return:
        """
        self.__cafea_repo.read_file()
        cafea = Cafea(idc, nume, tara, pret)
        self.__cafea_validator.validate(cafea)
        self.__cafea_repo.add(cafea)
        self.__cafea_repo.write_file()

    def afis_cafele_tara(self, nume_tara):
        """
        Afiseaza cafelele care fac parte dintr-o tara respectiva
        :param nume_tara:
        :return:
        """
        cafele = self.get_all_cafele()
        lista = []
        for cafea in cafele:
            if cafea.tara_de_origine == nume_tara:
                lista.append(cafea)
        return lista
