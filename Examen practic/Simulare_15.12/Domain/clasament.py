class Clasament:
    def __init__(self,denumire_proba,id_concurent,punctaj_concurent):
        self.__denumire_proba=denumire_proba
        self.__id_concurent=id_concurent
        self.__punctaj_concurent=punctaj_concurent

    def get_denumire_proba(self):
        """
        returneaza denumirea probei
        :return:
        """
        return self.__denumire_proba

    def get_id_concurent(self):
        """
        returneaza id concurent
        :return:
        """
        return self.__id_concurent

    def get_punctaj_concurent(self):
        """
        returneaza punctaj concurent
        :return:
        """
        return self.__punctaj_concurent

    def __str__(self):
        """
        returneaza sablonul clasamentului
        :return:
        """
        return f"la proba : {self.__denumire_proba} concurentul cu id-ul: {self.__id_concurent} a avut un punctaj de : {self.__punctaj_concurent}"