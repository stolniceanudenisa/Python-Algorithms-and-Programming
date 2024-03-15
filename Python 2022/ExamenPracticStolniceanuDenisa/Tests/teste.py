from Domain.cafea import Cafea
from Domain.cafea_validator import CafeaValidator
from Repository.cafea_repository import CafeaFileRepo
from Service.cafea_service import CafeaService


class Teste:
    def __init__(self):
        self.run_all_tests()
        print('Testele au trecut!')

    def run_all_tests(self):
        self.test_domain()
        self.test_repo()
        self.test_service()

    def test_domain(self):
        pass

    def test_repo(self):
        cafea = Cafea(1, 'Lapte', 'ro', 12.5)
        assert cafea.id_cafea == 1
        assert cafea.nume_cafea == 'Lapte'
        assert cafea.tara_de_origine == 'ro'
        assert cafea.pret_cafea == 12.5

        cafea_repo = CafeaFileRepo("Tests/test_cafea.txt")
        cafele = cafea_repo.get_all()

        cafea = Cafea(2, 'Mocca', 'uk', 20)
        cafea_repo.add(cafea)

        try:
            cafea_repo.add(cafea)
            assert True  # exista deja cafeaua cu id '1'
        except KeyError:
            ...

        assert cafea_repo.get_by_id(61) is None
        assert cafea_repo.get_by_id(1) is None
        assert len(cafele) == 4

    def test_valid(self):
        cafea_validator = CafeaValidator()
        cafea = Cafea(2, 'Mocca', 'uk', 20)
        cafea_validator.validate(cafea)
        assert len('Mocca') > 3
        assert float(20) > 0
        assert ('Mocca').isupper()

    def test_service(self):
        cafea_repo = CafeaFileRepo("Tests/test_cafea.txt")
        cafea_validator = CafeaValidator()
        cafea_service = CafeaService(cafea_repo, cafea_validator)

        cafele = cafea_service.get_all_cafele()
        assert len(cafele) == 4
        cafea_service.add_cafea(3, 'Neagra', 'ro', 10)

        try:
            cafea_service.add_cafea(1, 'Lapte', 'ro', 12.5)
            assert True
        except KeyError:
            ...

        rez = cafea_service.afis_cafele_tara('ro')
        assert len(rez) == 2
