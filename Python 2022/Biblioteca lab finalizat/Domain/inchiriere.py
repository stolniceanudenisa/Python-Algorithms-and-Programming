from dataclasses import dataclass


@dataclass
class Inchiriere:
    id_inchiriere: str
    client_id: str
    carte_id: str

    def __str__(self):
        return "Inchiriere: " + str(self.id_inchiriere) + "\nID Client: " + str(
            self.client_id) + "\nID Carte: " + str(self.carte_id) + "\n"

    # def __init__(self, id_inchiriere, client_id, carte_id):
    #     self.__id_inchiriere = id_inchiriere
    #     self.__client_id = client_id
    #     self.__carte_id = carte_id
    #
    # def get_id_inchiriere(self):
    #     return self.__id_inchiriere
    #
    # def get_client_id(self):
    #     return self.__client_id
    #
    # def get_carte_id(self):
    #     return self.__carte_id
    #
    # def set_id_inchiriere(self, id_inchiriere_nou):
    #     self.__id_inchiriere = id_inchiriere_nou
    #
    # def set_client_id(self, client_id_nou):
    #     self.__client_id = client_id_nou
    #
    # def set_carte_id(self, carte_id_nou):
    #     self.__carte_id = carte_id_nou

    # def __str__(self):
    #     return "Inchiriere: " + str(self.get_id_inchiriere()) + "\nID Client: " + str(
    #         self.get_client_id()) + "\nID Carte: " + str(self.get_carte_id()) + "\n"

    # return "Inchiriere: " + str(
    #     self.get_id_inchiriere()) + ":\nID Client: " + self.get_client_id() + "\nID Carte: " + self.get_carte_id() + "\n"

    # return f"Id-ul inchirierii: {self.__id_inchiriere}, Id-ul clientului care inchiriaza cartea: {self.__client_id}," \
    #        f" Id-ul cartii care va fi inchiriate: {self.__carte_id}"
