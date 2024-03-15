class Concurent:
    def __init__(self,id_concurent,nume_concurent,sponsor_concurent):
        self.__id_concurent=id_concurent
        self.__nume_concurent=nume_concurent
        self.__sponsor_concurent=sponsor_concurent

    def get_id_concurent(self):
        """
        returneaza id_ul concurentului
        :return:
        """
        return self.__id_concurent

    def get_nume_concurent(self):
        """
        returneaza numele concurentului
        :return:
        """
        return self.__nume_concurent

    def get_sponsor_concurent(self):
        """
        returneaza sponsorul concurentului
        :return:
        """
        return self.__sponsor_concurent


    def __str__(self):
        """
        returneaza sablonul printului
        :return:
        """
        return f"Concurentul cu id-ul: {self.__id_concurent}, numele : {self.__id_concurent} este sponsorizat de : {self.__sponsor_concurent} "

