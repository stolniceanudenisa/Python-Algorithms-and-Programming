import random

from Domain.cafea import Cafea


class CafeaFileRepo:
    def __init__(self, filename):
        self.__filename = filename
        self.__storage = {}

    def read_file(self):
        lista = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            self.__storage.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(',')
                    idcafea = parts[0]
                    nume = parts[1]
                    tara = parts[2]
                    pret = parts[3]
                    cafea = Cafea(idcafea, nume, tara, float(pret))
                    lista.append(cafea)
                    self.__storage[idcafea] = cafea
        return lista

    def write_file(self):
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
        with open(self.__filename, 'w') as f:
            for el in lista:
                string = str(el.id_cafea) + ',' + el.nume_cafea + ',' + el.tara_de_origine + ',' + str(
                    el.pret_cafea) + '\n'
                f.write(string)

    def get_all(self):
        self.read_file()
        return self.__storage.values()

    def add(self, cafea: Cafea):
        self.read_file()
        if self.get_by_id(cafea.id_cafea) is not None:
            raise KeyError(f'Exista deja cafeaua cu id-ul {cafea.id_cafea}')
        self.__storage[cafea.id_cafea] = cafea
        self.write_file()

    def get_by_id(self, id_cafea):
        if id_cafea in self.__storage:
            return self.__storage[id_cafea]
        return None

    def update(self, cafea: Cafea):
        self.read_file()
        if self.get_by_id(cafea.id_cafea) is None:
            raise KeyError(f'Nu exista cafeaua cu id-ul {cafea.id_cafea} care sa se modifice.')
        self.__storage[cafea.id_cafea] = cafea
        self.write_file()

    def delete(self, id_cafea):
        self.read_file()
        if self.get_by_id(id_cafea) is None:
            raise KeyError(f'Nu exista cafeaua cu id-ul {id_cafea} care sa se stearga.')
        del self.__storage[id_cafea]
        self.write_file()

    def delete_dupa_tara(self, tara_cafea):
        self.read_file()
        cafele = self.get_all()
        rez = {}
        for cafea in cafele:
            if cafea.tara_de_origine != tara_cafea:
                rez[cafea.id_cafea] = cafea
        self.__storage = rez
        self.write_file()

    def delete_cafea_prm(self):
        self.read_file()
        cafele = self.get_all()
        rez = {}
        pret_maxim = -1
        for cafea in cafele:
            if float(cafea.pret_cafea) > float(pret_maxim):
                pret_maxim = cafea.pret_cafea

        for cafea in cafele:
            if float(cafea.pret_cafea) != float(pret_maxim):
                rez[cafea.id_cafea] = cafea
        self.__storage = rez
        self.write_file()

    def delete_caf_cifra_continuta(self, cifra):
        self.read_file()
        cafele = self.get_all()
        rez = {}
        for cafea in cafele:
            if str(cifra) not in str(cafea.id_cafea):
                rez[cafea.id_cafea] = cafea
        self.__storage = rez
        self.write_file()

    def generare_i(self):
        """
        Genereaza jucatori cu nume si prenume dintr-un fisier existent.
        """
        lista = self.read_file()
        # lista_posturi = ['fundas', 'pivot', 'extrema']
        cnt = 0
        with open('import.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line != '':
                    line = line.strip()
                    nume, tara = line.split(',')
                    # pana aici am numele si prenumele de adaugat
                    ok = 1
                    for el in lista:
                        if el.nume_cafea == nume and el.tara_de_origine == tara:
                            ok = 0
                    if ok == 1:
                        # generez id si pret apoi adaug la lista mea
                        id = random.randint(170, 210)
                        pret = random.uniform(15.5, 80.5)
                        cafea = Cafea(id, nume, tara, pret)
                        lista.append(cafea)
                        cnt = cnt + 1
        self.save_to_file(lista)
        return cnt
