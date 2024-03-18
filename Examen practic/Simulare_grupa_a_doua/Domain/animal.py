class Animal:
    def __init__(self,nume_animal,pret_animal,specie_animal):
        self.__nume_animal=nume_animal
        self.__pret_animal=pret_animal
        self.__specie_animal=specie_animal


    def get_nume_animal(self):
        """
        returneaza numele la animal
        :return:
        """
        return self.__nume_animal


    def get_pret_animal(self):
        """
        returneaza pretul per animal
        :return:
        """
        return self.__pret_animal


    def get_specie_animal(self):
        """
        returneaza specia animalului
        :return:
        """
        return self.__specie_animal

    def __str__(self):
        """
        returneaza structura printului obiectului
        :return:
        """
        return f"Animalul cu numele {self.__nume_animal} are pretul : {self.__pret_animal} si este specia: {self.__specie_animal} "