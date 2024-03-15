from Domain.concurenti import Concurent


class ConcurentFileRepo:
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
                    parts=line.split(",")
                    id_concurent=parts[0]
                    nume_concurent=parts[1]
                    sponsor_concurent=parts[2]
                    concurent=Concurent(id_concurent,nume_concurent,sponsor_concurent)
                    self.__storage[id_concurent]=concurent



    def get_all(self):
        """
        returneaza o lista cu toate obiectele stocate
        :return:
        """
        self.read_all_files()
        return self.__storage.values()


    def get_by_sponsor(self,sponsor_dorit):
        """
        returneaza obiectul:concurent ce contine sponsorul dorit
        :return:
        """
        self.read_all_files()
        concurenti=self.get_all()
        for concurent in concurenti:
            if concurent.get_sponsor_concurent() == sponsor_dorit:
                return concurent


