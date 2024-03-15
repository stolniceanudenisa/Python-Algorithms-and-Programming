from dataclasses import dataclass


@dataclass
class Carte:
    """
    Creeaza o carte.
    - id_carte: id-ul cartii trebuie sa fie unic.
    - titlu_carte: titlul cartii
    - descriere_care: descrierea cartii
    - autor_carte: autorul cartii
    """

    id_carte: str
    titlu_carte: str
    descriere_carte: str
    autor_carte: str

    def __str__(self):
        return "Id-ul cartii: " + str(
            self.id_carte) + ":\ntitlul cartii: " + self.titlu_carte + "\ndescrierea cartii: " + self.descriere_carte + "\nautorul cartii: " + self.autor_carte + "\n"

    # def __init__(self, id_carte, titlu_carte, descriere_carte, autor_carte):
    #     self.__id_carte = id_carte
    #     self.__titlu_carte = titlu_carte
    #     self.__descriere_carte = descriere_carte
    #     self.__autor_carte = autor_carte
    #
    # def get_id_carte(self):
    #     return self.__id_carte
    #
    # def get_titlu_carte(self):
    #     return self.__titlu_carte
    #
    # def get_descriere_carte(self):
    #     return self.__descriere_carte
    #
    # def get_autor_carte(self):
    #     return self.__autor_carte
    #
    # def set_id_carte(self, id_carte):
    #     self.__id_carte = id_carte
    #
    # def set_titlu_carte(self, titlu_carte):
    #     self.__titlu_carte = titlu_carte
    #
    # def set_descriere_carte(self, descriere_carte):
    #     self.__descriere_carte = descriere_carte
    #
    # def set_autor_carte(self, autor_carte):
    #     self.__autor_carte = autor_carte

    # @property
    # def id_carte(self):
    #     return self.__id_carte
    #
    # @property
    # def titlu_carte(self):
    #     return self.__titlu_carte
    #
    # @property
    # def descriere_carte(self):
    #     return self.__descriere_carte
    #
    # @property
    # def autor_carte(self):
    #     return self.__autor_carte

    # def __str__(self):
    #     return f"Id-ul cartii: {self.__id_carte}, titlul cartii: {self.__titlu_carte}," \
    #            f" descrierea cartii: {self.__descriere_carte}, autorul cartii: {self.__autor_carte}"

    # def __str__(self):
    #     return "Id-ul cartii: " + str(
    #         self.get_id_carte()) + ":\ntitlul cartii: " + self.get_titlu_carte() + "\ndescrierea cartii: " + self.get_descriere_carte() + "\nautorul cartii: " + self.get_autor_carte() + "\n"
