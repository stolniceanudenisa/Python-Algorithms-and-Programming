class Apartament:
    def __init__(self,nr_apartament,tip_apartament,pret_total_apartament,pret_inchiriere_apartament):
        self.__nr_apartament=nr_apartament
        self.__tip_apartament=tip_apartament
        self.__pret_total_apartament=pret_total_apartament
        self.__pret_inchiriere_apartament=pret_inchiriere_apartament


    def get_nr_apartament(self):
        """
        returneaza numarul apartamentului
        :return:
        """
        return self.__nr_apartament

    def get_tip_apartament(self):
        """
        returneaza tipul apartamentului
        :return:
        """
        return self.__tip_apartament

    def get_pret_total_apartament(self):
        """
        returenaza pretul total al apartamentului
        :return:
        """
        return self.__pret_total_apartament

    def get_pret_inchiriere_apartament(self):
        '''
        returneaza pretul inchirierii apartamentului
        :return:
        '''
        return self.__pret_inchiriere_apartament

    def __str__(self):
        """
        returneaza schematizarea printului asignat obiectului
        :return:
        """
        return f"Apartamentul cu nr : {self.__nr_apartament} de tipul : {self.__tip_apartament} are un pret total: {self.__pret_total_apartament} si de inchiriere : {self.__pret_inchiriere_apartament} "