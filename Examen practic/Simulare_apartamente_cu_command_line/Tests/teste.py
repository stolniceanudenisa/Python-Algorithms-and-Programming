from Domain.apartament import Apartament
from Repo.apartament_repo import ApartamentFileRepo
from Service.apartament_service import ApartamentService


class Teste:
    def __init__(self):
        self.__run_all_tests()

    def __run_all_tests(self):
        self.test_getteri()
        self.test_repo()
        self.test_service()

    def test_repo(self):
        """
        teste pentru modalitatiile din repository
        :return:
        """
        repo=ApartamentFileRepo("Tests/teste_apartament.txt")
        apartamente=repo.get_all()
        assert len(apartamente) == 4
        apartamente2=repo.get_by_tip("3")
        assert apartamente2.get_nr_apartament() == "3"

    def test_service(self):
        """
        teste pentru modalitatiile din service
        :return:
        """
        repo=ApartamentFileRepo("Tests/teste_apartament.txt")
        service=ApartamentService(repo)
        apartament1=service.cautare_dupa_tip("3")
        assert apartament1[0].get_nr_apartament() == "3"
        apartament2=service.pret_inchiriere_ap("1","3")
        assert apartament2 == 300




    def test_getteri(self):
        """
        teste pentru modalitatiile din domain
        :return:
        """
        apartament=Apartament("1","3","5000","500")
        assert apartament.get_nr_apartament() == "1"
        assert apartament.get_tip_apartament() == "3"
        assert apartament.get_pret_inchiriere_apartament() == "500"
        assert apartament.get_pret_total_apartament() == "5000"