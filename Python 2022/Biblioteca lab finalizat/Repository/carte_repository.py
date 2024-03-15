from Domain.carte import Carte


class CarteRepository:

    def __init__(self):
        self.__storage = {}

    def __len__(self):
        return len(self.__storage)

    def get_carti(self):
        """
        Return the dictionary with people from repo
        :return: self.__people
        :rtype: dictionary {ID_person : Person}
        """
        return self.__storage

    def set_carti(self, carti):
        """
        Replaces the current list of people with the given list
        :param carti: the dictionary of people that will overwrite self.__people
        :type carti: dictionary {ID_person : Person}
        """
        self.__storage = carti

    def add(self, carte: Carte):
        """
        Adauga o carte.
        :param carte: obiect de tipul carte
        :return:
        """
        # if self.get_by_id(carte.id_carte) is not None:
        #     raise KeyError(f'Exista deja o carte cu id-ul {carte.id_carte}')

        self.__storage[carte.id_carte] = carte

    def get_by_id(self, id_carte):
        """
        Cauta o carte dupa id.
        :param id_carte: string.
        :return: o carte daca exista una cu id-ul dat, None in caz contrar.
        """
        if id_carte in self.__storage:
            return self.__storage[id_carte]
        return None

    def get_by_title(self, titlu_carte):
        """
        Cauta o carte dupa titlu.
        :param titlu_carte: titlul cartii.
        :return: o carte daca exista una cu titlul dat, None in caz contrar.
        """
        for carte in self.__storage.values():
            if carte.titlu_carte == titlu_carte:
                return self.__storage[carte.id_carte]
        return None

    def get_by_descriere(self, descriere_carte):
        """
        Cauta o carte dupa desciere.
        :param descriere_carte: descrierea cartii.
        :return: o carte daca exista una cu descrierea data, None in caz contrar.
        """
        for carte in self.__storage.values():
            if carte.descriere_carte == descriere_carte:
                return self.__storage[carte.id_carte]
        return None

    def get_by_autor(self, autor_carte):
        """
        Cauta o carte dupa autor.
        :param autor_carte: autorul cartii.
        :return: o carte daca exista una cu autorul dat, None in caz contrar.
        """
        for carte in self.__storage.values():
            if carte.autor_carte == autor_carte:
                return self.__storage[carte.id_carte]
        return None

    def update(self, carte_noua: Carte):
        """
        Modifica o carte dupa id.
        :param carte_noua: obiect de tipul Carte
        :return:
        """
        if self.get_by_id(carte_noua.id_carte) is None:
            raise KeyError(f'Nu exista carte cu id-ul {carte_noua.id_carte} care sa se modifice.')

        self.__storage[carte_noua.id_carte] = carte_noua

    def delete(self, id_carte):
        """
        Sterge o carte dupa id.
        :param id_carte: id-ul cartii
        :return:
        """

        if self.get_by_id(id_carte) is None:
            raise KeyError(f'Nu exista carte cu id-ul {id_carte} care sa se stearga.')

        del self.__storage[id_carte]
        # self.__storage.pop(id_carte)  sau asa cu pop

    def get_all(self):
        """
        Da lista de carti.
        :return: o lista de obiecte de tipul Carte.
        """
        return list(self.__storage.values())
