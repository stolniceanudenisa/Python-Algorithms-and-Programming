from Domain.client import Client


class ClientRepository:

    def __init__(self):
        self.__storage = {}

    def __len__(self):
        return len(self.__storage)

    def get_clienti(self):
        """
        Return the dictionary with people from repo
        :return: self.__people
        :rtype: dictionary {ID_person : Person}
        """
        return self.__storage

    def set_clienti(self, clienti):
        """
        Replaces the current list of people with the given list
        :param clienti: the dictionary of people that will overwrite self.__people
        :type clienti: dictionary {ID_person : Person}
        """
        self.__storage = clienti

    def add(self, client: Client):
        """
        Adauga un client.
        :param client: obiect de tipul client
        :return:
        """
        # if self.get_by_id(client.get_id_client()) is not None:
        #     raise KeyError(f'Exista deja un client cu id-ul {client.get_id_client()}')

        self.__storage[client.id_client] = client

    def get_by_id(self, id_client):
        """
        Cauta un client dupa id.
        :param id_client: id-ul clientului
        :return: un client daca exista unul cu id-ul dat, None in caz contrar
        """
        if id_client in self.__storage:
            return self.__storage[id_client]
        return None

    def get_by_name(self, nume_client):
        """
        Cauta un client dupa nume.
        :param nume_client: numele clientului.
        :return: un client daca exista unul cu numele dat, None in caz contrar.
        """
        for client in self.__storage.values():
            if client.nume_client == nume_client:
                return self.__storage[client.id_client]
        return None

    def get_by_cnp(self, cnp_client):
        """
        Cauta un client dupa cnp.
        :param cnp_client: cnp-ul clientului.
        :return: un client daca exista unul cu cnp-ul dat, None in caz contrar.
        """
        for client in self.__storage.values():
            if client.cnp_client == cnp_client:
                return self.__storage[client.id_client]
        return None

    def read(self, id_client=None):
        """
        Citeste un client.
        :param id_client: id-ul clientului
        :return:
            - clietul cu id = id_client sau None daca id_client nu e None
            - lista cu toate clientii daca id_client e None
        """
        if id_client:
            if id_client in self.__storage:
                return self.__storage[id_client]
            else:
                return None
        return list(self.__storage.values())

    def update(self, client_nou: Client):
        """
        Modifica un client dupa id.
        :param client_nou: obiect de tipul Client
        :return:
        """
        # id_client_nou = client_nou.get_id_client()
        if self.get_by_id(client_nou.id_client) is None:
            raise KeyError(f'Nu exista client cu id-ul {client_nou.id_client} care sa se modifice.')

        self.__storage[client_nou.id_client] = client_nou

    def delete(self, id_client):
        """
        Sterge un client dupa id.
        :param id_client: id-ul clientului
        :return:
        """
        if self.get_by_id(id_client) is None:
            raise KeyError(f'Nu exista client cu id-ul {id_client} care sa se stearga.')

        del self.__storage[id_client]
        # self.__storage.pop(id_carte)     sau asa cu pop

    def get_all(self):
        """
        Da lista de clienti.
        :return: o lista de obiecte de tipul Client.
        """
        return list(self.__storage.values())

    def clear_clienti(self):
        """
        Sterge toti clientii.
        :return:
        """
        self.__storage.clear()
