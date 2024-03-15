
class ServiceAnimal:
    def __init__(self, repo_animal):
        self.__repo_animal = repo_animal

    def get_all_service(self):
        """
        returneaza lista de animale
        :return: rez: lista de animale
        """
        return self.__repo_animal.get_all_repo()

    def cautare_animal_dupa_specie(self, specie):
        """
        returneaza lista de animale de specie specie
        :param specie: string
        :return: rez: lista de animale cu specia specie
        """
        animale = self.__repo_animal.get_all_repo()
        animale_cautate = []
        for animal in animale:
            if animal.get_specie() == specie:
                animale_cautate.append(animal)
        return animale_cautate

    def calculeaza_pret_animal_sejur(self, nume, nr_zile):
        """
        returneaza pretul unui sejur de nr_zile zile
        :param nume: string
        :param nr_zile: int
        :return: rez: pretul unui sejur de nr_zile zile
        """
        animale = self.__repo_animal.get_all_repo()
        for animal in animale:
            if animal.get_nume() == nume:
                pret = animal.get_pret() * nr_zile
                return pret
        return False
