from Domain.apartament import Apartament


class ApartamentFileRepo:
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
                    nr_apartament=parts[0]
                    tip_apartament=parts[1]
                    pret_total=parts[2]
                    pret_inchiriere=parts[3]
                    apartament=Apartament(nr_apartament,tip_apartament,pret_total,pret_inchiriere)
                    self.__storage[nr_apartament]=apartament


    def get_all(self):
        """
        returneaza o lista cu toate obiectele din self.__storage
        :return:
        """
        self.read_all_files()
        return self.__storage.values()

    def get_by_tip(self,tip_apartament):
        """
        returneaza apartamentul ce ii are asignat tipul apartamentului dorit
        :param tip_apartament:string
        :return:
        """
        self.read_all_files()
        apartamente=self.get_all()
        for apartament in apartamente:
            if apartament.get_tip_apartament() == tip_apartament:
                return apartament
        return None
