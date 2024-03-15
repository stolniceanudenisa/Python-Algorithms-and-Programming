from Domain.clasament import Clasament


class ClasamentFileRepo:
    def __init__(self,filename):
        self.__filename=filename
        self.__storage={}


    def read_all_files(self):
        """
        deschide fisierul anexat si insereaza in self.__storage elementele fisierului
        :return:
        """
        with open(self.__filename,"r") as f:
            lines=f.readlines()
            self.__storage.clear()
            for line in lines:
                line=line.strip()
                if line !="":
                    parts = line.split(",")
                    denumire_proba=parts[0]
                    id_concurent=parts[1]
                    punctaj_concurent=parts[2]
                    clasament=Clasament(denumire_proba,id_concurent,punctaj_concurent)
                    self.__storage[id_concurent]=clasament



    def get_all(self):
        """
        returneaza o lista cu toate obiectele stocate
        :return:
        """
        self.read_all_files()
        return self.__storage.values()


    def get_by_id(self,id_concurent):
        """
        returneaza obiectul:concurent ce contine sponsorul dorit
        :return:
        """
        self.read_all_files()
        return self.__storage[id_concurent]
