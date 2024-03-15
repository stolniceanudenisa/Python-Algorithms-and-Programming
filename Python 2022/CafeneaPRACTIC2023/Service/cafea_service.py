import random

from Domain.cafea import Cafea
from Domain.cafea_validator import CafeaValidator
from Repository.cafea_repository import CafeaFileRepo


class CafeaService:
    def __init__(self, cafea_repo: CafeaFileRepo, cafea_validator: CafeaValidator):
        self.__cafea_repo = cafea_repo
        self.__cafea_validator = cafea_validator

    def get_all_cafele(self):
        return self.__cafea_repo.get_all()

    def add_cafea(self, idc, nume, tara, pret):
        cafea = Cafea(idc, nume, tara, pret)
        self.__cafea_validator.validate(cafea)
        self.__cafea_repo.add(cafea)

    def update_cafea(self, idc, nume, tara, pret):
        cafea = Cafea(idc, nume, tara, pret)
        self.__cafea_validator.validate(cafea)
        self.__cafea_repo.update(cafea)

    def delete_cafea(self, id_cafea):
        self.__cafea_repo.delete(id_cafea)

    def afisare_cafele_sortate(self):
        cafele = self.get_all_cafele()
        rez = sorted(cafele, key=lambda x: (x.tara_de_origine, x.pret_cafea))
        return rez

    def filtrare_cafele(self, tara, pret):
        cafele = self.get_all_cafele()
        lista = []
        if tara == ' ':
            for cafea in cafele:
                if cafea.pret_cafea <= float(pret):
                    lista.append(cafea)
            if len(lista) == 0:
                print('Nu exista astfel de cafele.')
            for cafea in lista:
                print(cafea)

        elif pret == ' ':
            for cafea in cafele:
                if cafea.tara_de_origine == tara:
                    lista.append(cafea)
            if len(lista) == 0:
                print('Nu exista astfel de cafele.')
            for cafea in lista:
                print(cafea)

        else:
            for cafea in cafele:
                if cafea.tara_de_origine == tara:
                    if float(cafea.pret_cafea) <= float(pret):
                        lista.append(cafea)
            if len(lista) == 0:
                print('Nu exista astfel de cafele.')
            for cafea in lista:
                print(cafea)

    def afis_masini_token(self, token):
        masini = self.get_all_masini()
        lista = []
        for masina in masini:
            if masina.token == token:
                lista.append(masina)
            return lista

    def sortare_masini_token(self):
        masini = self.get_all_masini()
        rez = sorted(masini, key=lambda x: x.token, reverse=True)
        return rez

    def sortare_masini_model(self):
        masini = self.get_all_masini()
        rez = sorted(masini, key=lambda x: (x.marca, x.model), reverse=True)
        return rez

    def sortare_marca_model_toke(self):
        pass

    def sortare_profit(self):
        pass

    def afis_cafele_ord_desc_pret(self):
        cafele = self.get_all_cafele()
        rez = sorted(cafele, key=lambda x: x.pret_cafea, reverse=True)
        return rez

    def afis_cafele_tara_desc_nume(self, tara):
        cafele = self.get_all_cafele()
        lista = []
        for caf in cafele:
            if caf.tara_de_origine == tara:
                lista.append(caf)
        rez = sorted(lista, key=lambda x: x.nume_cafea, reverse=True)
        return rez

    def delete_cafele_aceeasi_tara(self, tara):
        cafele = self.get_all_cafele()
        lista = []
        for caf in cafele:
            if caf.tara_de_origine != tara:
                lista.append(caf)
        return lista

    def delete_cafele_aceeasi_tara_de_tot(self, taracafea):
        self.__cafea_repo.delete_dupa_tara(taracafea)

    def pret_maxim(self):
        cafele = self.get_all_cafele()
        pret_maxim = -1
        for cafea in cafele:
            if float(cafea.pret_cafea) > float(pret_maxim):
                pret_maxim = cafea.pret_cafea
        for cafea in cafele:
            if float(cafea.pret_cafea) != pret_maxim:
                print(cafea)

    def delete_cafele_pret_maxim(self):
        self.__cafea_repo.delete_cafea_prm()

    def delete_cafele_cu_cifra_continuta(self, cifra):
        self.__cafea_repo.delete_caf_cifra_continuta(cifra)

    def add_random(self, n, lista_tari, lista_preturi):
        """
        Creeaza n cafele random.
        :param n: numarul de cafele de generat
        :param lista_tari:  lista de tari din care se alege
        :param lista_preturi:  lista de preturi din care se alege
        :return:
        """
        listanume = ['mocca', 'ciocon', 'cappuccino', 'starbucks', 'ted', 'tucano']
        i = 1
        lista = self.__cafea_repo.read_file()
        ok = 1
        while i <= n:
            idcafea = random.randrange(50, 70)
            nume = random.choice(listanume)
            tari = random.choice(lista_tari)
            preturi = random.choice(lista_preturi)
            cafea = Cafea(idcafea, nume, tari, preturi)
            for el in lista:
                if el.tara_de_origine == tari and el.pret_cafea == preturi:
                    ok = 0
            if ok == 1:
                self.__cafea_validator.validate(cafea)
                lista.append(cafea)
                i += 1
        self.__cafea_repo.save_to_file(lista)

    def export(self, filename):
        lista = self.__cafea_repo.read_file()
        rez = sorted(lista, key=lambda x: (x.tara_de_origine, x.pret_cafea))
        with open(filename, "w") as f:
            for el in rez:
                string = str(el.id_cafea) + ',' + el.nume_cafea + ',' + el.tara_de_origine + ',' + str(
                    el.pret_cafea) + '\n'
                f.write(string)

    def generare_import(self):
        """
        Genereaza jucatori cu nume si prenume dintr-un fisier existent.
        """
        return self.__cafea_repo.generare_i()

    def cautare_cafea_dupa_id(self, id_cafea):
        """
        Cauta si afiseaza o cafea cu un id respectiv.
        :param id_cafea: id-ul clientului cautat.
        :return: cafeaua cu id-ul respectiv.
        """
        try:
            if self.__cafea_repo.get_by_id(id_cafea) not in self.get_all_cafele():
                raise ValueError(f'Cafeaua cu id-ul {id_cafea} nu exista.')
        except ValueError as ve:
            print(ve)
        # return list(filter(lambda cafea: cafea.id_cafea == id_cafea, self.get_all_cafele()))
        return [cafea for cafea in self.get_all_cafele() if cafea.id_cafea == id_cafea]

    def cautare_cafea_dupa_nume(self, nume_cafea):
        # return [cafea for cafea in self.get_all_cafele() if cafea.nume_cafea == nume_cafea]
        return list(filter(lambda cafea: cafea.nume_cafea == nume_cafea, self.get_all_cafele()))

    def update_undo(self, crt_undo, cifra):
        """
        Adauga la lista de undo o lista care contine toate elementele ce urmeaza a fi sterse din multimea de produse.
        :param crt_undo: lista care retine toate stergerile
        :type crt_undo: list
        :param cif: cifra dupa care se fac stergerile (daca aceasta apare in pret)
        :type cifra: int
        :return: lista de undo cu update-ul facut (adaugarea elementelor ce urmeaza a fi sterse)
        :type return: list
        """
        lista = self.__cafea_repo.read_file()
        lista = [el for el in lista if str(cifra) in str(el.id_cafea)]

        copy_list = []
        for el in lista:
            copy_list.append(Cafea(el.id_cafea, el.nume_cafea, el.tara_de_origine, el.pret_cafea))

        crt_undo.append(copy_list)
        return crt_undo

    def undo(self, crt_undo):
        """
        Adauga la multimea de produse toate elementele sterse la ultima stergere.
        :param crt_undo: lista care retine toate stergerile
        :type crt_undo: list
        :return: lista de undo cu update-ul facut (stergerea ultimei pozitii pt ca stergerea produselor a fost refacuta)
        :type return: list
        """
        errors = []
        if len(crt_undo) < 1:
            errors.append('Nu se mai poate face undo!')
        else:
            for el in crt_undo[-1]:
                self.add_cafea(el.id_cafea, el.nume_cafea, el.tara_de_origine, el.pret_cafea)

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

        crt_undo.pop(-1)
        return crt_undo

    def update_undo2(self, crt_undo, idcafea):
        """
        Adauga la lista de undo o lista care contine toate elementele ce urmeaza a fi sterse din multimea de produse.
        :param crt_undo: lista care retine toate stergerile
        :type crt_undo: list
        :param cif: cifra dupa care se fac stergerile (daca aceasta apare in pret)
        :type cifra: int
        :return: lista de undo cu update-ul facut (adaugarea elementelor ce urmeaza a fi sterse)
        :type return: list
        """
        lista = self.__cafea_repo.read_file()
        lista = [el for el in lista if str(idcafea) in str(el.id_cafea)]

        copy_list = []
        for el in lista:
            copy_list.append(Cafea(el.id_cafea, el.nume_cafea, el.tara_de_origine, el.pret_cafea))

        crt_undo.append(copy_list)
        return crt_undo

    def undo2(self, crt_undo):
        errors = []
        if len(crt_undo) < 1:
            errors.append('Nu se mai poate face undo!')
        else:
            for el in crt_undo[-1]:
                self.add_cafea(el.id_cafea, el.nume_cafea, el.tara_de_origine, el.pret_cafea)

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

        crt_undo.pop(-1)
        return crt_undo

    def update_undo3(self, crt_undo, idcafea):
        lista = self.__cafea_repo.read_file()
        lista = [el for el in lista if str(idcafea) in str(el.id_cafea)]

        copy_list = []
        for el in lista:
            copy_list.append(Cafea(el.id_cafea, el.nume_cafea, el.tara_de_origine, el.pret_cafea))

        crt_undo.append(copy_list)
        return crt_undo

    def undo3(self, crt_undo):
        errors = []
        if len(crt_undo) < 1:
            errors.append('Nu se mai poate face undo!')
        else:
            for el in crt_undo[-1]:
                self.update_cafea(el.id_cafea, el.nume_cafea, el.tara_de_origine, el.pret_cafea)

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

        crt_undo.pop(-1)
        return crt_undo

    def update_undo4(self, crt_undo, numec, tara, pret):
        lista = self.__cafea_repo.read_file()
        lista = [el for el in lista if (str(numec) in str(el.nume_cafea), str(tara) in str(el.tara_de_origine),
                                        str(pret) in str(el.pret_cafea))]

        copy_list = []
        for el in lista:
            copy_list.append(Cafea(el.id_cafea, el.nume_cafea, el.tara_de_origine, el.pret_cafea))

        crt_undo.append(copy_list)
        return crt_undo

    def undo4(self, crt_undo):
        errors = []
        if len(crt_undo) < 1:
            errors.append('Nu se mai poate face undo!')
        else:
            for el in crt_undo[-1]:
                self.add_cafea(el.id_cafea, el.nume_cafea, el.tara_de_origine, el.pret_cafea)

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

        crt_undo.pop(-1)
        return crt_undo

# 12,irish,irlanda,20.0
# 22,a,ggg,22.5
# 23,b,fff,22.5
# 24,c,eee,20.0
# 66,irish,irlanda,13.0
# 13,esspresso,irlanda,14,5
# 3,latte,nu stiu,15.0
# 15,cappuccino,nu stiu,5.0
# 1,cioco,aaaaaa,15.5
# 2,lapte,bbbb,3.1
# 18,mocca,usa,3.0
