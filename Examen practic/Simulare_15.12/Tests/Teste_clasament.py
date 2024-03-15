from Domain.clasament import Clasament
from Domain.concurenti import Concurent
from Repo.clasament_repo import ClasamentFileRepo
from Repo.concurent_repo import ConcurentFileRepo
from Service.clasament_service import ClasamentService
from Service.concurent_service import ConcurentService


class TesteClasament:
    def __init__(self):
        self.__run_all_tests()

    def __run_all_tests(self):
        self.test_getteri()
        self.test_repo()
        self.test_service()

    def test_getteri(self):
        """
        test pentru modalitatii getteri
        :return:
        """
        clasament=Clasament("alergat","1","5")
        assert clasament.get_id_concurent() == "1"
        assert clasament.get_denumire_proba() == "alergat"
        assert clasament.get_punctaj_concurent() == "5"

    def test_repo(self):
        """
        test pentru modalitatii repo
        :return:
        """
        repo=ClasamentFileRepo("Tests/test_clasament.txt")
        lista1=repo.get_all()
        assert len(lista1)==2
        lista2=repo.get_by_id("1")
        assert lista2.get_id_concurent() == "1"

    def test_service(self):
        """
        test pentru modalitati service
        :return:
        """
        repo=ClasamentFileRepo("Tests/test_clasament.txt")
        service=ClasamentService(repo)
        lista1=service.clasament()
        assert len(lista1)
