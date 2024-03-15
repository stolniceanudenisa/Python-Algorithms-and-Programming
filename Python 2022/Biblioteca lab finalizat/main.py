from Domain.carte_validator import CarteValidator

from Repository.carte_file_repository import CarteFileRepository
from Repository.client_file_repository import ClientFileRepository
from Repository.inchiriere_file_repository import InchiriereFileRepository
from Service.carte_service import CarteService
from Service.client_service import ClientService
from Service.inchiriere_service import InchiriereService
from UserInterface.console import Console


def main():
    # carte_repository = CarteRepository()
    # carte_validator = CarteValidator()
    # carte_service = CarteService(carte_repository, carte_validator)
    #
    # client_repository = ClientRepository()
    # client_service = ClientService(client_repository)
    #
    # inchiriere_repository = InchiriereRepository(client_repository, carte_repository)
    # inchiriere_service = InchiriereService(inchiriere_repository, client_repository, carte_repository)

    #######################
    carte_repository = CarteFileRepository('carte.txt')
    carte_validator = CarteValidator()
    carte_service = CarteService(carte_repository, carte_validator)

    client_repository = ClientFileRepository('client.txt')
    client_service = ClientService(client_repository)

    inchiriere_repository = InchiriereFileRepository('inchiriere.json', client_repository, carte_repository)
    inchiriere_service = InchiriereService(inchiriere_repository, client_repository, carte_repository)

    #######################

    # carte_service.add_carte('1', 'Fratii Karamazov', 'Roman', 'Fiodor Dostoievski')
    # carte_service.add_carte('2', 'Metamorfoza', 'Nuvela', 'Frank Kafka')
    # carte_service.add_carte('3', 'Livada de visini', 'Piesa de teatru', 'Anton Cehov')
    # carte_service.add_carte('4', 'Suflete moarte', 'Roman', 'Nikolai Gogol')
    # carte_service.add_carte('5', 'Strainul', 'Roman', 'Albert Camus')
    # carte_service.add_carte('6', 'Maestrul si Margareta', 'Roman', 'Mihail Bulgakov')
    # carte_service.add_carte('7', 'Batranul si marea', 'Roman', 'Ernest Hemingway')
    # carte_service.add_carte('8', 'Dincolo de bine si rau', 'Carte filosofica', 'Friedrich Nietzsche')
    # carte_service.add_carte('9', 'Suflete moarte', 'aaa', 'bb')
    # carte_service.add_carte('10', 'Ion', 'Roman', 'Liviu Rebreanu')
    # carte_service.add_carte('11', 'Ion', 'aaa', 'bb')

    # client_service.add_client('1', 'Ion Popa', '5220309019075')
    # client_service.add_client('2', 'Mihai Catalin', '5220311017040')
    # client_service.add_client('3', 'Munteanu Adrian', '5220324015964')
    # client_service.add_client('4', 'Neamt Victor', '5220526015748')
    # client_service.add_client('5', 'Stanescu Silvia', '6221110019741')
    # client_service.add_client('6', 'Vintila Maria', '6221110015314')

    # inchiriere_service.adauga('1', '1', '1')
    # inchiriere_service.adauga('2', '2', '4')
    # inchiriere_service.adauga('3', '3', '5')
    # inchiriere_service.adauga('4', '4', '9')
    # inchiriere_service.adauga('5', '5', '2')
    # inchiriere_service.adauga('6', '6', '2')
    # inchiriere_service.adauga('7', '4', '2')
    # inchiriere_service.adauga('8', '3', '10')
    # inchiriere_service.adauga('9', '6', '11')
    # inchiriere_service.adauga('10', '2', '9')
    # inchiriere_service.adauga('11', '5', '7')
    # inchiriere_service.adauga('12', '3', '2')
    # inchiriere_service.adauga('13', '6', '7')
    # inchiriere_service.adauga('14', '4', '6')
    # inchiriere_service.adauga('15', '4', '5')
    # inchiriere_service.adauga('16', '4', '7')13

    # inchiriere_service.adauga('17', '4', '4')
    # inchiriere_service.adauga('18', '4', '3')
    # inchiriere_service.adauga('19', '4', '1')

    console = Console(carte_service, client_service, inchiriere_service)
    console.run_console2()


if __name__ == '__main__':
    # test_all()
    # test_carte_file_repository()
    main()
