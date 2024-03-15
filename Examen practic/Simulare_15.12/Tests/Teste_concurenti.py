from Domain.concurenti import Concurent
from Repo.concurent_repo import ConcurentFileRepo
from Service.concurent_service import ConcurentService


class TesteConcurent:
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
        concurent=Concurent("1","Marius","delaco")
        assert concurent.get_id_concurent() == "1"
        assert concurent.get_nume_concurent() == "Marius"
        assert concurent.get_sponsor_concurent() == "delaco"

    def test_repo(self):
        """
        test pentru modalitatii repo
        :return:
        """
        repo=ConcurentFileRepo("Tests/test_concurenti.txt")
        lista1=repo.get_all()
        assert len(lista1)==3
        lista2=repo.get_by_sponsor("delaco")
        assert lista2.get_id_concurent() == "1"

    def test_service(self):
        """
        test pentru modalitati service
        :return:
        """
        repo=ConcurentFileRepo("Tests/test_concurenti.txt")
        service=ConcurentService(repo)
        lista1=service.cautare_dupa_sponsor("delaco")
        assert len(lista1)==2
