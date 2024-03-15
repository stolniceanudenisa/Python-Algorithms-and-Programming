from Domain.cafea import Cafea


class CafeaFileRepo:
    def __init__(self, filename):
        self.__filename = filename
        self.__storage = {}

    def read_file(self):
        """
        Citeste din fisier toate cafelele
        :return:
        """
        lista = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            self.__storage.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(',')
                    idc = parts[0]
                    numec = parts[1]
                    tara = parts[2]
                    pret = parts[3]
                    cafea = Cafea(idc, numec, tara, float(pret))
                    self.__storage[idc] = cafea
                    lista.append(cafea)
        return lista

    def write_file(self):
        """
        Scrie in fisier
        :return:
        """
        with open(self.__filename, "w") as f:
            cafele = self.__storage
            for key in cafele:
                idc = cafele[key].id_cafea
                nume = cafele[key].nume_cafea
                tara = cafele[key].tara_de_origine
                pret = cafele[key].pret_cafea
                f.write(str(idc) + ',' + nume + ',' + tara + ',' + str(pret) + '\n')

    def save_to_file(self, lista):
        """
        Salveaza in fisier lista lista, stergand tot ce era acolo initial.
        :param and type lista: lista ce trebuie salvata,list
        """
        with open(self.__filename, "w") as f:
            for el in lista:
                string = str(el.id_cafea) + ',' + el.nume_cafea + ',' + el.tara_de_origine + ',' + str(
                    el.pret_cafea) + '\n'
                f.write(string)

    def get_all(self):
        """
        Returneaza toate cafelele din storage
        :return:
        """
        self.read_file()
        return self.__storage.values()

    def add(self, cafea: Cafea):
        """
        Adauga o cafea
        :param cafea: obiectul de tip cafea
        :return:
        """
        self.read_file()
        if self.get_by_id(cafea.id_cafea) is not None:
            raise KeyError(f'Deja exista cafeaua cu id-ul: {cafea.id_cafea}')
        if self.get_by_name(cafea.id_cafea) is not None:
            raise ValueError(f'Deja exista cafeaua cu numele: {cafea.nume_cafea}')
        self.__storage[cafea.id_cafea] = cafea
        self.write_file()

    def get_by_id(self, id_cafea):
        """
        Returneaza o cafea cu un id respectiv
        :param id_cafea: id-ul
        :return: True, sau None daca nu exista
        """
        self.read_file()
        if id_cafea in self.__storage:
            return self.__storage[id_cafea]
        return None

    def get_by_name(self, id_cafea):
        """
        Cauta o cafea dupa id
        :param id_cafea: id-ul cafelei
        :return:
        """
        self.read_file()
        cafele = self.get_all()
        for cafea in cafele:
            if cafea.nume_cafea in self.__storage:
                return self.__storage[id_cafea]
        return None
