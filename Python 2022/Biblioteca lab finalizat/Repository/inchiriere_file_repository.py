from Domain.inchiriere import Inchiriere
from Repository.inchiriere_repository import InchiriereRepository


class InchiriereFileRepository(InchiriereRepository):
    def __init__(self, filename, client_repository, inchiriere_repository):
        super().__init__(client_repository, inchiriere_repository)
        self.__filename = filename
        self.citeste_din_fisier()

    def adauga(self, inchiriere):
        super().adauga(inchiriere)
        self.scrie_in_fisier()

    # def modifica(self, id_inchiriere):
    # def sterge(self, id_inchirirere):
    def clearFile(self):
        """
        Remove all the notes from the repository
        """
        self.__listainchirieri = []
        self.scrie_in_fisier()

    def citeste_din_fisier(self):
        try:
            f = open(self.__filename, "r")  # deschidem fisierul in modul CITIRE: "read" (de acolo vine "r")
            linie = f.readline().strip("\n")  # citim o prima linie din fisier si scoatem din ea caracterul "\n" (enter)
            while linie != "":  # daca linia nu e goala (adica: daca nu am ajuns la finalul fisierului)
                lista_atribute = linie.split(",")  # despartim linia citita folosind separatorul ,
                # lista_atribute va fi o lista ce contine, ca elemente, valorile regasite pe linia curenta
                id_inchiriere = lista_atribute[0]  # primul element din lista_atribute e id-ul
                id_client = lista_atribute[1]  # al doilea element din lista_atribute e numele disciplinei
                id_carte = lista_atribute[2]  # al treilea element din lista_atribute e numele profesorului
                inchiriere = Inchiriere(id_inchiriere, id_client,
                                        id_carte)  # cream disciplina folosind valorile citite din fisier
                super().adauga(
                    inchiriere)  # apelam metoda adauga din clasa parinte (adica din clasa DisciplinaRepository)
                linie = f.readline().strip(
                    "\n")  # citim linia urmatoare pe care o vom verifica si prelucra cand intram din nou in while
            f.close()  # la final, inchidem fisierul deschis
        except IOError:
            print(
                "Eroare la deschiderea fisierului " + self.__filename)  # mesaj de eroare daca nu s-a putut deschide fisierul

    def scrie_in_fisier(self):
        try:
            f = open(self.__filename, "w")  # deschidem fisierul in modul SCRIERE: "write" (de acolo vine "w")
            lista_inchirieri = super().get_all()  # din lista noastra de inscrieri, aducem toate inscrierile
            for inchiriere in lista_inchirieri:  # parcurgem fiecare inscriere din lista de inscrieri
                id_inchiriere = inchiriere.id_inchiriere
                client_id = inchiriere.client_id
                carte_id = inchiriere.carte_id
                linie = str(id_inchiriere) + "," + str(client_id) + "," + str(
                    carte_id) + "," + "\n"  # cream o linie de tipul liniilor pe care le-am citit din fisier (atributele separate prin virgula si \n la final de rand)
                f.write(linie)  # scriem acea linie in fisier
            f.close()  # la final, inchidem fisierul
        except IOError:
            print(
                "Eroare la deschiderea fisierului " + self.__filename)  # mesaj de eroare daca nu s-a putut deschide fisierul

    # def __read_file(self):
    #     try:
    #         with open(self.filename, 'r') as f:
    #             return jsonpickle.loads(f.read())
    #     except Exception:
    #         return {}
    #
    # def __write_file(self, objects: Dict[str, Inchiriere]):
    #     with open(self.filename, 'w') as f:
    #         f.write(jsonpickle.dumps(objects))

    # def get_all(self):
    #     inchirieri = self.__read_file()
    #     return inchirieri
    #
    # def adauga(self, inchiriere: Inchiriere):
    #     inchirieri = self.__read_file()
    #     id = inchiriere.id_inchiriere()
    #     # if self.gaseste_inchiriere_dupa_id(id) != -1:
    #     #     # nu adaugam inscrierea daca exista deja o inscriere cu acest id
    #     #     raise KeyError("Inchirierea cu acest id exista deja!")
    #     # else:
    #     #     client_id = inchiriere.get_client_id()
    #     #     carte_id = inchiriere.get_carte_id()
    #     # aici vom folosi faptul ca am initializat si referinte spre clientRepository si DisciplinaRepository
    #     # verificam ca client_id sa fie id-ul unui client existent in clientRepository
    #     # de aceea avem nevoie de referinta spre clientRepository, ca sa putem avea acces la lista de clienti, sa facem verificarea
    #     # procedam la fel si pentru carte_id
    #     # daca oricare dintre client_id si disciplina_id nu sunt id-urile unui client / Discipline din repository-urile corespunzatoare, nu facem adaugarea
    #     # if self.__client_repository.get_by_id(client_id) is None or self.__carte_repository.get_by_id(
    #     #         carte_id) is None:
    #     #     raise KeyError("Clientul sau cartea care trebuie inchiriata nu exista!")
    #
    #     # if self.gaseste_inchiriere_dupa_client_id_si_carte_id(client_id, carte_id) != -1:
    #     #     # daca exista deja in lista de inscrieri o inscriere cu acelasi client_id si disciplina_id, nu facem adaugarea
    #     #     raise KeyError(f"Clientul a inchiriat deja cartea cu id-ul {carte_id}!")
    #     # else:
    #     #     # daca totul e in regula, adaugam inscrierea in lista
    #     inchirieri[inchiriere] = inchiriere
    #     self.__write_file(inchirieri)

    # def gaseste_inchiriere_dupa_id(self, id):
    #     '''
    #     Metoda care gaseste o inchiriere in lista de inchirieri, dupa id inchiriere
    #     :param id: id-ul inchirierii cautate
    #     :return: pozitia unui obiectului de tip inchiriere cu id-ul dat in self.__lista_inchirieri;
    #             -1 daca nu exista
    #     '''
    #     inchirieri = self.citeste_din_fisier()
    #     for i in range(0, len(inchirieri)):
    #         inchiriere_curenta = inchirieri[i]
    #         if inchiriere_curenta.id_inchiriere == id:
    #             return i
    #     return -1

    # def cauta_inchiriere_dupa_id(self, id):
    #     '''
    #     Metoda care gaseste o inscriere in lista de inscrieri, dupa id inscriere
    #     :param id: id-ul inchirierii cautate
    #     :return: pozitia unui obiectului de tip inscriere cu id-ul dat in self.__lista_inscrieri;
    #             -1 daca nu exista
    #     '''
    #     inchirieri = self.citeste_din_fisier()
    #     for i in range(0, len(inchirieri)):
    #         inchiriere_curenta = inchirieri[i]
    #         if inchiriere_curenta.id_inchiriere == id:
    #             return inchiriere_curenta
    #     return None
    #
    # def gaseste_inchiriere_dupa_client_id_si_carte_id(self, client_id, carte_id):
    #     '''
    #     Metoda care gaseste o inscriere in lista de inscrieri, dupa id client si id disciplina
    #     :param client_id:
    #     :param: carte_id:
    #     :return: pozitia unui obiectului de tip inscriere cu id client si id disciplina date in self.__lista_inscrieri;
    #             -1 daca nu exista
    #     '''
    #     inchirieri = self.citeste_din_fisier()
    #     for i in range(0, len(inchirieri)):
    #         inchiriere_curenta = inchirieri[i]
    #         if inchiriere_curenta.client_id == client_id and inchiriere_curenta.carte_id == carte_id:
    #             return i
    #     return -1
    #
    # def exista_inchiriere_carte(self, carte_id):
    #     '''
    #     Metoda care verifica daca exista inchirieri la o carte cu id-ul dat
    #     :param carte_id: id-ul cartii cautate
    #     :return: True, daca exista o inchiriere la o carte cu id-ul dat; False altfel
    #     '''
    #     inchirieri = self.citeste_din_fisier()
    #     for i in range(0, len(inchirieri)):
    #         inchiriere_curenta = inchirieri[i]
    #         if inchiriere_curenta.carte_id == carte_id:
    #             return True
    #     return False
