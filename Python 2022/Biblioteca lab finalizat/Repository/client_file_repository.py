from Domain.client import Client
from Repository.client_repository import ClientRepository


class ClientFileRepository(ClientRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.citeste_din_fisier()

    def citeste_din_fisier(self):
        try:
            f = open(self.__filename, "r")  # deschidem fisierul in modul CITIRE: "read" (de acolo vine "r")
            linie = f.readline().strip("\n")  # citim o prima linie din fisier si scoatem din ea caracterul "\n" (enter)
            while linie != "":  # daca linia nu e goala (adica: daca nu am ajuns la finalul fisierului)
                lista_atribute = linie.split(",")  # despartim linia citita folosind separatorul ,
                # lista_atribute va fi o lista ce contine, ca elemente, valorile regasite pe linia curenta
                id_client = lista_atribute[0]  # primul element din lista_atribute e id-ul
                nume_client = lista_atribute[1]  # al doilea element din lista_atribute e numele disciplinei
                cnp_client = lista_atribute[2]  # al treilea element din lista_atribute e numele profesorului
                client = Client(id_client, nume_client,
                                cnp_client)  # cream disciplina folosind valorile citite din fisier
                super().add(client)  # apelam metoda adauga din clasa parinte (adica din clasa DisciplinaRepository)
                linie = f.readline().strip(
                    "\n")  # citim linia urmatoare pe care o vom verifica si prelucra cand intram din nou in while
            f.close()  # la final, inchidem fisierul deschis
        except IOError:
            print(
                "Eroare la deschiderea fisierului " + self.__filename)  # mesaj de eroare daca nu s-a putut deschide fisierul

    def scrie_in_fisier(self):
        try:
            f = open(self.__filename, "w")  # deschidem fisierul in modul SCRIERE: "write" (de acolo vine "w")
            lista_clienti = super().get_all()  # din lista noastra de discipline, aducem toate disciplinele
            for client in lista_clienti:  # parcurgem fiecare disciplina din lista de discipline
                id_client = client.id_client
                nume_client = client.nume_client
                cnp_client = client.cnp_client

                linie = str(
                    id_client) + "," + nume_client + "," + cnp_client + "\n"  # cream o linie de tipul liniilor pe care le-am citit din fisier (atributele separate prin virgula si \n la final de rand)
                f.write(linie)  # scriem acea linie in fisier
            f.close()  # la final, inchidem fisierul
        except IOError:
            print(
                "Eroare la deschiderea fisierului " + self.__filename)  # mesaj de eroare daca nu s-a putut deschide fisierul

    def add(self, client):
        super().add(client)
        self.scrie_in_fisier()

    def update(self, id_client):
        super().update(id_client)
        self.scrie_in_fisier()

    def delete(self, id_client):
        super().delete(id_client)
        self.scrie_in_fisier()
    #
    # def clearFile(self):
    #     """
    #     Remove all the notes from the repository
    #     """
    #     self.__listaclienti = []
    #     self.scrie_in_fisier()

    # def __read_file(self):
    #     try:
    #         with open(self.filename, 'r') as f:
    #             return jsonpickle.loads(f.read())
    #     except Exception:
    #         return {}
    #
    # def __write_file(self, objects: Dict[str, Client]):
    #     with open(self.filename, 'w') as f:
    #         f.write(jsonpickle.dumps(objects))

    # def add(self, client: Client):
    #     """
    #     Adauga un client.
    #     :param client: obiect de tipul client
    #     :return:
    #     """
    #     clienti = self.__read_file()
    #     # if self.get_by_id(client.get_id_client()) is not None:
    #     #     raise KeyError(f'Exista deja un client cu id-ul {client.get_id_client()}')
    #     clienti[client.get_id_client()] = client
    #     self.__write_file(clienti)
    #
    # def get_by_id(self, id_client):
    #     """
    #     Cauta un client dupa id.
    #     :param id_client: id-ul clientului
    #     :return: un client daca exista unul cu id-ul dat, None in caz contrar
    #     """
    #     clienti = self.__read_file()
    #     if id_client in clienti:
    #         return clienti[id_client]
    #     return None
    #
    # def get_by_name(self, nume_client):
    #     """
    #     Cauta un client dupa nume.
    #     :param nume_client: numele clientului.
    #     :return: un client daca exista unul cu numele dat, None in caz contrar.
    #     """
    #     clienti = self.__read_file()
    #     for client in clienti.values():
    #         if client.get_nume_client() == nume_client:
    #             return clienti[client.get_id_client()]
    #     return None
    #
    # def get_by_cnp(self, cnp_client):
    #     """
    #     Cauta un client dupa cnp.
    #     :param cnp_client: cnp-ul clientului.
    #     :return: un client daca exista unul cu cnp-ul dat, None in caz contrar.
    #     """
    #     clienti = self.__read_file()
    #     for client in clienti.values():
    #         if client.get_cnp_client() == cnp_client:
    #             return clienti[client.get_id_client()]
    #     return None
    #
    # def read(self, id_client=None):
    #     """
    #     Citeste un client.
    #     :param id_client: id-ul clientului
    #     :return:
    #         - clietul cu id = id_client sau None daca id_client nu e None
    #         - lista cu toate clientii daca id_client e None
    #     """
    #     clienti = self.__read_file()
    #     if id_client:
    #         if id_client in clienti:
    #             return clienti[id_client]
    #         else:
    #             return None
    #     return list(clienti.values())
    #
    # def update(self, client_nou: Client):
    #     """
    #     Modifica un client dupa id.
    #     :param client_nou: obiect de tipul Client
    #     :return:
    #     """
    #     clienti = self.__read_file()
    #     if self.get_by_id(client_nou.get_id_client()) is None:
    #         raise KeyError(f'Nu exista client cu id-ul {client_nou.get_id_client()} care sa se modifice.')
    #     clienti[client_nou.get_id_client()] = client_nou
    #     self.__write_file(clienti)
    #
    # def delete(self, id_client):
    #     """
    #     Sterge un client dupa id.
    #     :param id_client: id-ul clientului
    #     :return:
    #     """
    #     clienti = self.__read_file()
    #     if self.get_by_id(id_client) is None:
    #         raise KeyError(f'Nu exista client cu id-ul {id_client} care sa se stearga.')
    #
    #     del clienti[id_client]
    #     self.__write_file(clienti)
    #
    # def get_all(self):
    #     """
    #     Da lista de clienti.
    #     :return: o lista de obiecte de tipul Client.
    #     """
    #     clienti = self.__read_file()
    #     return list(clienti.values())
