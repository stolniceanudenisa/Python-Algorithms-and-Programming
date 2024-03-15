from Domain.film import Film


class FilmRepository:
    def __init__(self):
        self.__storage = {}

    def get_by_id(self, id_film):
        """
        Gaseste un film dupa id.
        :param id_film:
        :return:
        """
        if id_film in self.__storage:
            return self.__storage[id_film]
        return None

    def add(self, film: Film):
        if self.get_by_id(film.get_id_film()) is not None:
            raise KeyError(f'Exista deja un film cu id-ul {film.get_id_film()}')
        self.__storage[film.get_id_film()] = film

    def delete(self, id_film):
        """
        Sterge un film dupa id.
        :param id_film:
        :return:
        """
        if self.get_by_id(id_film) is None:
            raise KeyError(f'Nu exista film cu id-ul :{id_film} care sa se stearga.')
        del self.__storage[id_film]
        # self.__storage.pop(id_film)

    def cautare_film_dupa_id(self):
        pass

    def cautare_film_dupa_titlu(self):
        pass

    def cautare_film_dupa_descriere(self):
        pass

    def cautare_film_dupa_numar_stele(self):
        pass

    def get_all(self):
        """
        Da lista de filme.
        :return:
        """
        return list(self.__storage.values())
