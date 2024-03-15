from dataclasses import dataclass


@dataclass
class Client:
    """
    Creaaza un client.
    - id_client: id-ul clientului trebuie sa fie unic.
    - nume_client: numele clientului
    - cnp_client: cnp-ul clientului
    """

    id_client: str
    nume_client: str
    cnp_client: str

    def __str__(self):
        return "Id-ul clientului: " + str(
            self.id_client) + ":\nnumele clientului: " + self.nume_client + "\nCNP-ul clientului: " + self.cnp_client + "\n"

    # def __init__(self, id_client, nume_client, cnp_client):
    #     self.__id_client = id_client
    #     self.__nume_client = nume_client
    #     self.__cnp_client = cnp_client
    #
    # def get_id_client(self):
    #     return self.__id_client
    #
    # def get_nume_client(self):
    #     return self.__nume_client
    #
    # def get_cnp_client(self):
    #     return self.__cnp_client
    #
    # def set_id_client(self, id_client):
    #     self.__id_client = id_client
    #
    # def set_nume_client(self, nume_client):
    #     self.__nume_client = nume_client
    #
    # def set_cnp_client(self, cnp_client):
    #     self.__cnp_client = cnp_client

    # @property
    # def id_client(self):
    #     return self.__id_client
    #
    # @property
    # def nume_client(self):
    #     return self.__nume_client
    #
    # @property
    # def cnp_client(self):
    #     return self.__cnp_client

    # def __str__(self):
    #     return f"Id-ul clientului: {self.__id_client}, numele clientului: {self.__nume_client}, CNP-ul clientului: {self.__cnp_client}"
    #
    # def __str__(self):
    #     return "Id-ul clientului: " + str(
    #         self.get_id_client()) + ":\nnumele clientului: " + self.get_nume_client() + "\nCNP-ul clientului: " + self.get_cnp_client() + "\n"



