from Repo.hotel_file_repo import HotelRepoFile


class TestRepo:
    def __init__(self):
        self.__run_all_tests()

    def __run_all_tests(self):
        self.test_repo()

    def test_repo(self):
        """
        test pentru functionalitatiile din repo:get_by_specie(),get_all()
        :return:
        """
        repo=HotelRepoFile("Tests/hotel_test.txt")
        animale=repo.get_all()
        animal_specie=repo.get_by_specie("Caine")
        assert len(animale) == 4
        assert animal_specie.get_nume_animal() == "Rex"