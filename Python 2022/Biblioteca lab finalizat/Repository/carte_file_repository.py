from Domain.carte import Carte
from Repository.carte_repository import CarteRepository


class CarteFileRepository(CarteRepository):
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
                id_carte = lista_atribute[0]  # primul element din lista_atribute e id-ul
                titlu_carte = lista_atribute[1]  # al doilea element din lista_atribute e numele disciplinei
                descriere_carte = lista_atribute[2]  # al treilea element din lista_atribute e numele profesorului
                autor_carte = lista_atribute[3]
                carte = Carte(id_carte, titlu_carte, descriere_carte,
                              autor_carte)  # cream disciplina folosind valorile citite din fisier
                super().add(carte)  # apelam metoda adauga din clasa parinte (adica din clasa DisciplinaRepository)
                linie = f.readline().strip(
                    "\n")  # citim linia urmatoare pe care o vom verifica si prelucra cand intram din nou in while
            f.close()  # la final, inchidem fisierul deschis
        except IOError:
            print(
                "Eroare la deschiderea fisierului " + self.__filename)  # mesaj de eroare daca nu s-a putut deschide fisierul

    def scrie_in_fisier(self):
        try:
            f = open(self.__filename, "w")  # deschidem fisierul in modul SCRIERE: "write" (de acolo vine "w")
            lista_carti = super().get_all()  # din lista noastra de discipline, aducem toate disciplinele
            for carte in lista_carti:  # parcurgem fiecare disciplina din lista de discipline
                id_carte = carte.id_carte
                titlu_carte = carte.titlu_carte
                decsriere_carte = carte.descriere_carte
                autor_carte = carte.autor_carte
                linie = str(
                    id_carte) + "," + titlu_carte + "," + decsriere_carte + "," + autor_carte + "\n"  # cream o linie de tipul liniilor pe care le-am citit din fisier (atributele separate prin virgula si \n la final de rand)
                f.write(linie)  # scriem acea linie in fisier
            f.close()  # la final, inchidem fisierul
        except IOError:
            print(
                "Eroare la deschiderea fisierului " + self.__filename)  # mesaj de eroare daca nu s-a putut deschide fisierul

    def add(self, carte: Carte):
        super().add(carte)
        self.scrie_in_fisier()

    def update(self, id_carte):
        super().update(id_carte)
        self.scrie_in_fisier()

    def delete(self, id_carte):
        super().delete(id_carte)
        self.scrie_in_fisier()

    # def clearFile(self):
    #     """
    #     Remove all the notes from the repository
    #     """
    #     self.__listacarti = []
    #     self.scrie_in_fisier()
    #
    # def size(self):
    #     """
    #     Get the size of file
    #     :return: integer
    #     """
    #     return len(self.__listacarti)

    # def __read_file_metoda2(self):
    #     try:
    #         with open(self.filename, 'r') as f:
    #             return jsonpickle.loads(f.read())
    #     except Exception:
    #         return {}
    #
    # def __write_file_metoda2(self, objects: Dict[str, Carte]):
    #     with open(self.filename, 'w') as f:
    #         f.write(jsonpickle.dumps(objects))

    # def add(self, carte: Carte):
    #     """
    #     Adauga o carte.
    #     :param carte: obiect de tipul carte
    #     :return:
    #     """
    #     carti = self.__read_file()
    #     # if self.get_by_id(carte.get_id_carte()) is not None:
    #     #     raise KeyError(f'Exista deja o carte cu id-ul {carte.get_id_carte()}')
    #
    #     carti[carte.get_id_carte()] = carte
    #     self.__write_file(carti)

    # def update(self, carte_noua: Carte):
    #     """
    #     Modifica o carte dupa id.
    #     :param carte_noua: obiect de tipul Carte
    #     :return:
    #     """
    #     carti = self.__read_file()
    #     if self.get_by_id(carte_noua.get_id_carte()) is None:
    #         raise KeyError(f'Nu exista carte cu id-ul {carte_noua.get_id_carte()} care sa se modifice.')
    #     carti[carte_noua.get_id_carte()] = carte_noua
    #     self.__write_file(carti)
    #
    # def delete(self, id_carte):
    #     """
    #     Sterge o carte dupa id.
    #     :param id_carte: id-ul cartii
    #     :return:
    #     """
    #     carti = self.__read_file()
    #     if self.get_by_id(id_carte) is None:
    #         raise KeyError(f'Nu exista carte cu id-ul {id_carte} care sa se stearga.')
    #
    #     del carti[id_carte]
    #     self.__write_file(carti)
    #
