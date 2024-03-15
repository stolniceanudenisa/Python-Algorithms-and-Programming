from Domain.cafea_validator import CafeaValidator
from Repository.cafea_repository import CafeaFileRepo
from Service.cafea_service import CafeaService
from Tests.teste import Teste
from UI.console import Console


def main():
    cafea_repo = CafeaFileRepo('coffees.txt')
    cafea_validator = CafeaValidator()

    cafea_service = CafeaService(cafea_repo, cafea_validator)
    console = Console(cafea_service)

    console.run_ui()


if __name__ == '__main__':
    Teste()
    main()
