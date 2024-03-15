from Domain.inchiriere import Inchiriere
from Repository.carte_file_repository import CarteFileRepository
from Repository.client_file_repository import ClientFileRepository


# from Repository.carte_repository import CarteRepository
# from Repository.client_repository import ClientRepository


class InchiriereRepository:

    def __init__(self, client_repository: ClientFileRepository, carte_repository: CarteFileRepository):
        self.__lista_inchirieri = []
        self.__client_repository = client_repository
        self.__carte_repository = carte_repository

    def __len__(self):
        return len(self.__lista_inchirieri)

    def get_all(self):
        return self.__lista_inchirieri

    def adauga(self, inchiriere: Inchiriere):
        # id = inchiriere.get_id_inchiriere()
        id = inchiriere.id_inchiriere
        if self.gaseste_inchiriere_dupa_id(id) != -1:
            # nu adaugam inscrierea daca exista deja o inscriere cu acest id
            raise KeyError("Inchirierea cu acest id exista deja!")
        else:
            client_id = inchiriere.client_id
            carte_id = inchiriere.carte_id
            # aici vom folosi faptul ca am initializat si referinte spre clientRepository si DisciplinaRepository
            # verificam ca client_id sa fie id-ul unui client existent in clientRepository
            # de aceea avem nevoie de referinta spre clientRepository, ca sa putem avea acces la lista de clienti, sa facem verificarea
            # procedam la fel si pentru carte_id
            # daca oricare dintre client_id si disciplina_id nu sunt id-urile unui client / Discipline din repository-urile corespunzatoare, nu facem adaugarea
            # if self.__client_repository.get_by_id(client_id) is None or self.__carte_repository.get_by_id(
            #         carte_id) is None:
            #     raise KeyError("Clientul sau cartea care trebuie inchiriata nu exista!")

            if self.gaseste_inchiriere_dupa_client_id_si_carte_id(client_id, carte_id) != -1:
                # daca exista deja in lista de inscrieri o inscriere cu acelasi client_id si disciplina_id, nu facem adaugarea
                raise KeyError(f"Clientul a inchiriat deja cartea cu id-ul {carte_id}!")
            else:
                # daca totul e in regula, adaugam inscrierea in lista
                self.__lista_inchirieri.append(inchiriere)

    def gaseste_inchiriere_dupa_id(self, id):
        '''
        Metoda care gaseste o inchiriere in lista de inchirieri, dupa id inchiriere
        :param id: id-ul inchirierii cautate
        :return: pozitia unui obiectului de tip inchiriere cu id-ul dat in self.__lista_inchirieri;
                -1 daca nu exista
        '''
        for i in range(0, len(self.__lista_inchirieri)):
            inchiriere_curenta = self.__lista_inchirieri[i]
            if inchiriere_curenta.id_inchiriere == id:
                return i
        return -1

    def cauta_inchiriere_dupa_id(self, id):
        '''
        Metoda care gaseste o inscriere in lista de inscrieri, dupa id inscriere
        :param id: id-ul inchirierii cautate
        :return: pozitia unui obiectului de tip inscriere cu id-ul dat in self.__lista_inscrieri;
                -1 daca nu exista
        '''
        for i in range(0, len(self.__lista_inchirieri)):
            inchiriere_curenta = self.__lista_inchirieri[i]
            if inchiriere_curenta.id_inchiriere == id:
                return inchiriere_curenta
        return None

    def gaseste_inchiriere_dupa_client_id_si_carte_id(self, client_id, carte_id):
        '''
        Metoda care gaseste o inscriere in lista de inscrieri, dupa id client si id disciplina
        :param client_id:
        :param: carte_id:
        :return: pozitia unui obiectului de tip inscriere cu id client si id disciplina date in self.__lista_inscrieri;
                -1 daca nu exista
        '''
        for i in range(0, len(self.__lista_inchirieri)):
            inchiriere_curenta = self.__lista_inchirieri[i]
            if inchiriere_curenta.client_id == client_id and inchiriere_curenta.carte_id == carte_id:
                return i
        return -1

    def exista_inchiriere_carte(self, carte_id):
        '''
        Metoda care verifica daca exista inchirieri la o carte cu id-ul dat
        :param carte_id: id-ul cartii cautate
        :return: True, daca exista o inchiriere la o carte cu id-ul dat; False altfel
        '''
        for i in range(0, len(self.__lista_inchirieri)):
            inchiriere_curenta = self.__lista_inchirieri[i]
            if inchiriere_curenta.carte_id == carte_id:
                return True
        return False
