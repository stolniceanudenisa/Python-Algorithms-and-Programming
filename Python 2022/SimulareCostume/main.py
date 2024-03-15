from Repository.costum_file_repository import CostumFileRepository
from Service.costum_service import CostumService
from UserInterface.console import Console


def main():
    costumRepository = CostumFileRepository('costum.txt')
    costumService = CostumService(costumRepository)

    console = Console(costumService)
    console.run_console()

if __name__ == '__main__':
    # test_all()
    main()


# def main():
#     # carte_repository = CarteRepository()
#     # carte_validator = CarteValidator()
#     # carte_service = CarteService(carte_repository, carte_validator)
#     #
#     # client_repository = ClientRepository()
#     # client_service = ClientService(client_repository)
#     #
#     # inchiriere_repository = InchiriereRepository(client_repository, carte_repository)
#     # inchiriere_service = InchiriereService(inchiriere_repository, client_repository, carte_repository)
#
#     #######################
#     carte_repository = CarteFileRepository('carte.txt')
#     carte_validator = CarteValidator()
#     carte_service = CarteService(carte_repository, carte_validator)
#
#     client_repository = ClientFileRepository('client.txt')
#     client_service = ClientService(client_repository)
#
#     inchiriere_repository = InchiriereFileRepository('inchiriere.json', client_repository, carte_repository)
#     inchiriere_service = InchiriereService(inchiriere_repository, client_repository, carte_repository)
#
#
