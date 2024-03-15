
class Animal:
    def __init__(self, id_animal, nume, pret, specie):
        self.__id_animal = id_animal
        self.__nume = nume
        self.__pret = pret
        self.__specie = specie

    def get_id(self):
        """
        returneaza id-ul unic identificabil al animalului
        :return: rez: id-ul unic identificabil al animalului
        """
        return self.__id_animal

    def get_nume(self):
        """
        returneaza numele animalului
        :return: rez: numele animalului
        """
        return self.__nume

    def get_pret(self):
        """
        returneaza pretul animalului
        :return: rez: pretul animalului
        """
        return self.__pret

    def get_specie(self):
        """
        returneaza specia animalului
        :return: rez: specia animalului
        """
        return self.__specie

    def __str__(self):
        """
        genereaza pretty printingul pentru animal
        :return: pretty printingul pentru animal [id_animal] nume pret specie
        """
        return f"[{self.__id_animal}] {self.__nume} {self.__pret} {self.__specie}"

    def __repr__(self):
        """
        ajuta la generarea pretty printingul-ui unui animal
        :return: -
        """
        return str(self)
