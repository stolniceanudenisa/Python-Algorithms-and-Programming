from Domain.client import Client
from Repository.client_file_repository import ClientFileRepository


# from Repository.client_repository import ClientRepository


class ClientService:
    def __init__(self, client_repository: ClientFileRepository):
        self.__client_repository = client_repository

    def add_client(self, id_client, nume_client, cnp_client):
        """
        Adauga un client.
        :param id_client: id-ul clientului
        :param nume_client: numele clientului
        :param cnp_client: cnp-ul clientului
        :return:
        """
        client = Client(id_client, nume_client, cnp_client)
        self.__client_repository.add(client)

    def update_client(self, id_client, nume_nou, cnp_nou):
        """
        Modifica un client dupa id.
        :param id_client: id-ul clientului
        :param nume_nou: numele nou al clientului
        :param cnp_nou: cnp-ul clientului
        :return:
        """
        client = Client(id_client, nume_nou, cnp_nou)
        self.__client_repository.update(client)

    def delete_client(self, id_client):
        """
        Sterge un client dupa id.
        :param id_client: id-ul clientului
        :return:
        """
        self.__client_repository.delete(id_client)

    def get_all_clienti(self):
        """
        Da toata lista de clienti.
        :return: o lista de obiecte de tip Client
        """
        return self.__client_repository.get_all()

    def cautare_client_dupa_id(self, id_client):
        """
        Cauta si afiseaza un client cu un id respectiv.
        :param id_client: id-ul clientului cautat.
        :return: clientul cu id-ul respectiv.
        """
        try:
            if self.__client_repository.get_by_id(id_client) not in self.get_all_clienti():
                raise ValueError(f'Clientul cu id-ul {id_client} nu exista.')
        except ValueError as ve:
            print(ve)
        return list(filter(lambda client: client.id_client == id_client, self.get_all_clienti()))

    def cautare_client_dupa_nume(self, nume_client):
        """
        Cauta si afiseaza un client cu un nume respectiv.
        :param nume_client: numele-ul clientului cautat.
        :return: clientul sau clientii cu numele respectiv.
        """
        try:
            if self.__client_repository.get_by_name(nume_client) not in self.get_all_clienti():
                raise ValueError(f'Clientul cu numele {nume_client} nu exista.')
        except ValueError as ve:
            print(ve)
        return list(filter(lambda client: client.nume_client == nume_client, self.get_all_clienti()))

    def cautare_client_dupa_cnp(self, cnp_client):
        """
        Cauta si afiseaza un client cu un cnp respectiv.
        :param cnp_client: cnp-ul clientului cautat.
        :return: clientul cu cnp-ul respectiv
        """
        try:
            if self.__client_repository.get_by_cnp(cnp_client) not in self.get_all_clienti():
                raise ValueError(f'Clientul cu cnp-ul {cnp_client} nu exista.')
        except ValueError as ve:
            print(ve)
        return list(filter(lambda client: client.cnp_client == cnp_client, self.get_all_clienti()))

    # def get_all_prof(self):
    #     return self.client_repository.read()
