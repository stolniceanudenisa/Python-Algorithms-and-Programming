#test getteri si setteri
from Domain.costum import Costum
from Repository.costum_repo import CostumFileRepo


class Test_repo:
    def __init__(self):
        self.__run_all_test_repo()


    def __run_all_test_repo(self):
        self.test_repo()

    def test_repo(self):
        repo=CostumFileRepo("Teste/costume_teste.txt")
        assert len(repo.get_all_file())==4

        assert repo.get_by_id("1").get_denumire_costum()=="bluza"


