from Domain.animal import Animal


class TestDomain:
    def __init__(self):
        self.__run_all_tests()

    def __run_all_tests(self):
        self.test_getteri()

    def test_getteri(self):
        """
        test pentru getteri
        :return:
        """
        animal=Animal("Jerry","2000","Soarece")
        assert animal.get_nume_animal() == "Jerry"
        assert animal.get_specie_animal() == "Soarece"
        assert animal.get_pret_animal() == "2000"