from Repo.hotel_file_repo import HotelRepoFile


class HotelService:
    def __init__(self,hotel_repo:HotelRepoFile):
        self.__hotel_repo=hotel_repo



    def cautare_dupa_specie(self,specie_dorita):
        """
        returneaza o lista  cu animalele ce apartin unei specii asignate
        :param specie_dorita:string
        :return:
        """
        specie_cautata=[]
        animale=self.__hotel_repo.get_all()

        for animal in animale:
            if specie_dorita in animal.get_specie_animal():
                specie_cautata.append(animal)

        return specie_cautata







    def pret_total(self,nume_animal,nr_zile):
        """
        returneaza pretul total al sejurului unui animal
        :param nume_animal:string
        :param nr_zile:int
        :return:
        """
        animale=self.__hotel_repo.get_all()
        pret_animal=0
        for animal in animale:
            if animal.get_nume_animal()==nume_animal:
                pret_animal=animal.get_pret_animal()
                break

        pret_total=int(nr_zile)*int(pret_animal)

        return pret_total

    def print_all(self,lista):
        """
        printeaza toate obiectele dintr-o lista
        :param lista:list
        :return:
        """
        for animal in lista:
            print(animal)
