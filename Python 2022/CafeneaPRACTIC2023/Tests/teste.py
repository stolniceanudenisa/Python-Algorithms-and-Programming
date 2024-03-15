from Domain.cafea import Cafea
from Domain.cafea_validator import CafeaValidator
from Repository.cafea_repository import CafeaFileRepo
from Service.cafea_service import CafeaService


class Teste:
    def __init__(self):
        self.run_all_tests()

    def run_all_tests(self):
        self.test_domain_cafea()
        self.test_repo_cafea()
        self.test_service_cafea()

    def test_domain_cafea(self):
        cafea = Cafea(111, 'mocca', 'usa', 23.5)
        assert cafea.id_cafea == 111
        assert cafea.nume_cafea == 'mocca'
        assert cafea.tara_de_origine == 'usa'
        assert cafea.pret_cafea == 23.5

    def test_repo_cafea(self):
        cafea_repo = CafeaFileRepo("Tests/test_cafea.txt")
        lista = cafea_repo.get_all()
        assert len(lista) == 4

        cafea = Cafea(112, 'ciocoalba', 'uk', 10)
        cafea_repo.add(cafea)
        assert len(cafea_repo.get_all()) == 4

        var = cafea_repo.get_by_id(112)

    def test_service_cafea(self):
        repo = CafeaFileRepo("Tests/test_cafea.txt")
        validator = CafeaValidator()
        service = CafeaService(repo, validator)
        lista = service.get_all_cafele()
        service.add_cafea(113, 'ciocoverde', 'usa', 13)


