from Domain.animal import Animal


class Teste:
    def __init__(self, service_animal, repo_animal):
        self.__service_animal = service_animal
        self.__repo_animal = repo_animal

    def run_all(self):
        """
        se executa toate testele
        :return: -
        """
        self.teste_domain()
        self.teste_repo()
        self.teste_service()
        print("teste trecute")
        print()

    @staticmethod
    def teste_domain():
        """
        se executa testele ce tin de domeniul entitatii animal
        :return: -
        """
        animal1 = Animal(1, "Tom", 300, "pisica")
        assert animal1.get_id() == 1
        assert animal1.get_nume() == "Tom"
        assert animal1.get_pret() == 300
        assert animal1.get_specie() == "pisica"

    def teste_repo(self):
        """
        se testeaza metodele din repository-ul pentru animale
        :return: -
        """
        animale = self.__repo_animal.get_all_repo()
        assert len(animale) == 11

    def teste_service(self):
        """
        se testeaza metodele din service-ul pentru animale
        :return: -
        """
        specie1 = "caine"
        specie2 = "pisica"
        nume = "Oleaca"
        nume_inexistent = "Raul"
        nr_zile = 7

        animale = self.__service_animal.get_all_service()
        assert len(animale) == 11

        animale_cautate1 = self.__service_animal.cautare_animal_dupa_specie(specie1)
        assert len(animale_cautate1) == 4
        animale_cautate2 = self.__service_animal.cautare_animal_dupa_specie(specie2)
        assert len(animale_cautate2) == 4

        pret_sejur = self.__service_animal.calculeaza_pret_animal_sejur(nume, nr_zile)
        assert pret_sejur == 3584
        pret_sejur = self.__service_animal.calculeaza_pret_animal_sejur(nume_inexistent, nr_zile)
        assert pret_sejur is False
