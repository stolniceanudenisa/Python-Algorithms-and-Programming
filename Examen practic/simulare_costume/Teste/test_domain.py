#test getteri si setteri
from Domain.costum import Costum


class Test_domain:
    def __init__(self):
        self.__run_all_test_domain()

    def __run_all_test_domain(self):
        self.test_getteri()
        self.test_setteri()

    def test_getteri(self):
        costum=Costum("1","bluza","vara","1000","True")
        assert costum.get_id_costum()=="1"
        assert costum.get_denumire_costum()=="bluza"
        assert costum.get_tematica_costum()=="vara"
        assert costum.get_pret_costum()==1000

    def test_setteri(self):
        costum = Costum("1", "bluza", "vara", "1000", "True")
        costum.set_id_costum("2")
        costum.set_denumire_costum("2")
        costum.set_tematica_costum("2")
        costum.set_pret_costum("2")
        assert costum.get_id_costum() == "2"
        assert costum.get_denumire_costum() == "2"
        assert costum.get_tematica_costum() == "2"
        assert costum.get_pret_costum() == "2"

