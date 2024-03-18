from Domain.animal import Animal


class HotelRepoFile:
    def __init__(self,filename):
        self.__filename=filename
        self.__storage={}


    def read_all_file(self):
        """
        functia deschide fisierul si incarca parametrii obiectului animal
        cu ce gaseste in fisier si introduce in self.__storage
        :return:
        """
        with open(self.__filename,"r") as f:
            lines=f.readlines()
            self.__storage.clear()
            for line in lines:
                line=line.strip()
                if line !="":
                    parts=line.split(",")
                    nume_animal=parts[0]
                    pret_animal=parts[1]
                    specie_animal=parts[2]
                    animal=Animal(nume_animal,pret_animal,specie_animal)
                    self.__storage[nume_animal]=animal


    def get_by_specie(self,specie_animal):
        """
        cauta in lista animalelor ,animalul cu specia respectica si il returneaza
        :param specie_animal:
        :return:
        """
        self.read_all_file()
        for animal in self.get_all():
            if animal.get_specie_animal() == specie_animal:
                return animal

    def get_all(self):
        """
        returneaza toata lista de animale
        :return:
        """
        self.read_all_file()
        return self.__storage.values()