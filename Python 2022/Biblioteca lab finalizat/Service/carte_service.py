from Domain.carte import Carte
from Domain.carte_validator import CarteValidator
from Repository.carte_file_repository import CarteFileRepository


# from Repository.carte_repository import CarteRepository


class CarteService:
    def __init__(self, carte_repository: CarteFileRepository,
                 carte_validator: CarteValidator):
        self.__carte_repository = carte_repository
        self.__carte_validator = carte_validator

    def add_carte(self, id_carte, titlu_carte, descriere_carte, autor_carte):
        """
        Adauga o carte
        :param id_carte: id-ul cartii
        :param titlu_carte: titlul cartii
        :param descriere_carte: descrierea cartii
        :param autor_carte: autorul cartii
        :return:
        """

        carte = Carte(id_carte, titlu_carte, descriere_carte, autor_carte)
        self.__carte_validator.validate(carte)
        self.__carte_repository.add(carte)

    def update_carte(self, id_carte, titlu_nou, descriere_noua, autor_nou):
        """
        Modifica o carte dupa id.
        :param id_carte: id-ul cartii
        :param titlu_nou: titlul nou al cartii
        :param descriere_noua: descrierea noua a cartii
        :param autor_nou: autorul nou al cartii
        :return:
        """
        carte = Carte(id_carte, titlu_nou, descriere_noua, autor_nou)
        self.__carte_validator.validate(carte)
        self.__carte_repository.update(carte)

    def delete_carte(self, id_carte):
        """
        Sterge o carte dupa id.
        :param id_carte: id-ul cartii
        :return:
        """
        self.__carte_repository.delete(id_carte)

    def get_all_carti(self):
        """
        Da toata lista de carti.
        :return: o lista de obiecte de tip Carte
        """
        return self.__carte_repository.get_all()

    def cautare_carte_dupa_id(self, id_carte):
        """
        Cauta si afiseaza o carte cu un id respectiv.
        :param id_carte: id-ul cartii cautate.
        :return: cartea cu id-ul respectiv.
        """
        # return list(filter(lambda carte: carte.id_carte == id_carte, self.get_all_carti()))
        try:
            if self.__carte_repository.get_by_id(id_carte) not in self.get_all_carti():
                raise ValueError(f'Cartea cu id-ul {id_carte} nu exista.')
        except ValueError as ve:
            print(ve)
        return [carte for carte in self.get_all_carti() if carte.id_carte == id_carte]

    def cautare_carte_dupa_titlu(self, titlu_carte):
        """
        Cauta si afiseaza o carte cu un titlu respectiv.
        :param titlu_carte: titlul cartii cautate.
        :return: cartea sau cartile cu titlul respectiv.
        """
        try:
            if self.__carte_repository.get_by_title(titlu_carte) not in self.get_all_carti():
                raise ValueError(f'Cartea cu titlul {titlu_carte} nu exista.')
            return list(filter(lambda carte: carte.titlu_carte == titlu_carte, self.get_all_carti()))
        except ValueError as ve:
            print(ve)
        return list(filter(lambda carte: carte.titlu_carte == titlu_carte, self.get_all_carti()))

    def cautare_carte_dupa_descriere(self, descriere_carte):
        """
        Cauta si afiseaza o carte cu o descriere respectiva.
        :param descriere_carte: descrierea cartii cautate.
        :return: cartea sau cartile cu descrierea respectiva.
        """
        try:
            if self.__carte_repository.get_by_descriere(descriere_carte) not in self.get_all_carti():
                print(f'Cartea cu descrierea-ul {descriere_carte} nu exista.')
        except ValueError as ve:
            print(ve)
        return list(filter(lambda carte: carte.descriere_carte == descriere_carte, self.get_all_carti()))

    def cautare_carte_dupa_autor(self, autor_carte):
        """
        Cauta si afiseaza o carte cu autorul respectiv.
        :param autor_carte: autorul cartii cautate.
        :return: cartea sau cartile cu autorul respectiv.
        """
        try:
            if self.__carte_repository.get_by_autor(autor_carte) not in self.get_all_carti():
                raise ValueError(f'Cartea cu autorul {autor_carte} nu exista.')
        except ValueError as ve:
            print(ve)
        return list(filter(lambda carte: carte.autor_carte == autor_carte, self.get_all_carti()))

    def sort_carti_autor(self):
        carti = self.get_all_carti()
        return sorted(carti, key=lambda x: len(x.autor_carte), reverse=True)

    # def get_all_prof(self):
    #     return self.carte_repository.read()
