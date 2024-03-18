from Repo.hotel_file_repo import HotelRepoFile
from Services.hotel_service import HotelService


class TestService:
    def __init__(self):
        self.__run_all_tests()

    def __run_all_tests(self):
        self.test_service()

    def test_service(self):
        """
        test pentru functionalitatiile din service:cautare_dupa_specie(),pret_total()
        :return:
        """
        repo=HotelRepoFile("Tests/hotel_test.txt")
        service=HotelService(repo)
        animale=repo.get_all()
        animal_specie=service.cautare_dupa_specie("Caine")
        animal_pret=service.pret_total("Rex","10")
        assert len(animal_specie) == 2
        assert animal_pret == 4000