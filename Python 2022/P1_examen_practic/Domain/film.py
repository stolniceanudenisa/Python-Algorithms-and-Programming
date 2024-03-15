class Film:
    def __init__(self, id_film, titlu_film, descriere_film, numar_stele_film):
        """
        Creaaza un film.
        :param id_film: id-ul filmului trebuie sa fie unic.
        :param titlu_film: titlul filmului
        :param descriere_film: descrierea filmului
        :param numar_stele_film: numarul de stele al filmului
        """
        self.__id_film = id_film
        self.__titlu_film = titlu_film
        self.__descriere_film = descriere_film
        self.__numar_stele_film = numar_stele_film

    def get_id_film(self):
        return self.__id_film

    def get_titlu_film(self):
        return self.__titlu_film

    def get_descriere_film(self):
        return self.__descriere_film

    def get_numar_stele_film(self):
        return self.__numar_stele_film

    def set_id_film(self, id_film):
        self.__id_film = id_film

    def set_titlu_film(self, titlu_film):
        self.__titlu_film = titlu_film

    def set_descriere_film(self, descriere_film):
        self.__descriere_film = descriere_film

    def set_numar_stele_film(self, numar_stele_film):
        self.__numar_stele_film = numar_stele_film

    def __str__(self):
        return f" Id-ul filmului: {self.__id_film}, titlul filmului: {self.__titlu_film}," \
               f" descrierea filmului: {self.__descriere_film}, numarul de stele primite: {self.__numar_stele_film}"
