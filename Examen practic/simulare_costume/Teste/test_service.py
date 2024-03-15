#test getteri si setteri
from Domain.costum import Costum
from Repository.costum_repo import CostumFileRepo
from Service.costum_service import CostumService


class Test_service:
    def __init__(self):
        self.__run_all_test_service()


    def __run_all_test_service(self):
        self.test_service()

    def test_service(self):
        repo=CostumFileRepo("Teste/costume_teste.txt")
        service=CostumService(repo)
        lista_vara=service.afisare_costume_disponibile("vara")
        assert len(lista_vara)==1
        #costum= repo.get_by_id("2")
        costum=service.inchiriere_costum("2")
        #print(costum)
        #assert service.inchiriere_costum("2") == costum
        assert service.inchiriere_costum("2")







Test_service()