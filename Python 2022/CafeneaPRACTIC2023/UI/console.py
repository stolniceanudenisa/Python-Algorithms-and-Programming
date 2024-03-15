import random

from termcolor import colored

from Service.cafea_service import CafeaService


class Console:
    def __init__(self, cafea_service: CafeaService):
        self.__cafea_service = cafea_service
        self.__crt_undo = []

    def menu(self):
        print("""
        1. Adaugare cafea cu id aleator.
        2. Afisare toate cafele sortate alfabetic dupa tara de origine.
        21. Afisarea tuturor cafelelor ordonate descrecator dupa pret.
        22. Afisarea tuturor cafelelor dintr-o tara, ordonate descrecator dupa nume.
        3. Filtare cafele in functie de tara de origine si pret.
        
        31. Filtrare cărți după titlu si anAparitie. La pornirea aplicației filtru este setat pe 
            sir vid si -1 (se văd toate cărțile din fișier). Utilizatorul poate modifica filtru 
            oricând, folosind o comanda din meniul aplicației (da un alt text si alt număr). 
            Aplicația afișează filtru curent si lista cărților (aplicând filtru curent) după 
            acționarea oricărui element de meniu. La afișare sunt incluse produsele care in 
            titlu conțin textul si au prețul mai mic decât prețul din filtru. Filtrarea nu 
            afectează fișierul cu cărțile (2p)
        
        4. Update cafea.
        5. Stergere cafea.
        51. Stergere toate cafele din aceeasi tara.
        52. Stergere toate cafele avand pretul maxim.
        53. Se dă o cifra se șterg toate cafelele pentru care id-ul produsului conține cifra data, afișează un mesaj cu numărul produselor șterse.
        54. Se da o litera si se sterg toate cafelele in care litera apare in nume.  INCA NU
      
        6. Generare cafea cu totul aleator. Utilizatorul introduce numărul de cafele de 
           generat, o lista de tari de origine si o lista de preturi (un string cu titlurile/artiștii separate cu 
           virgula). Aplicația adaugă melodii generate aleator si tipărește numarul de cafele care s-au 
           adăugat. Cafelele adăugate apar imediat si in fișier.     
        
        7. Export.
        71. Importa cafele dintr-un fisier. Generare aleatorie.
        8. Cautare cafea dupa id.
        9. Cautare cafea dupa nume.
        10. Undo la stergere dupa cifra.   
        11. Undo la stergere normala.   
        12. Undo la update. 
        13. Undo la add.
        a1. Afisare cafele.
        x. Exit
        """)

    def run_ui(self):
        while True:
            self.menu()
            opt = input('Alegeti optiunea: ')
            if opt == '1':
                self.handle_adaugare_cafea()
            elif opt == '2':
                self.handle_afis_cafele_sort()
            elif opt == '21':
                self.handle_afis_cafele_ord_desc_pret()
            elif opt == '22':
                self.handle_afis_cafele_tara_desc_nume()
            elif opt == '3':
                self.handle_filtrare_cafele()
            elif opt == '4':
                self.update_cafea()
            elif opt == '5':
                self.delete_cafea()
            elif opt == '51':
                self.handle_delete_cafele_aceeasi_tara_de_tot()
            elif opt == '52':
                self.handle_delete_cafele_cu_pret_maxim()
            elif opt == '53':
                self.handle_delete_cafele_cu_cifra_continuta()
            elif opt == '6':
                self.handle_generare_cafea()
            elif opt == '7':
                self.handle_export()
            elif opt == '71':
                self.handle_import()
            elif opt == '8':
                self.cautare_cafea_dupa_id()
            elif opt == '9':
                self.cautare_cafea_dupa_nume()
            elif opt == '10':
                self.handle_undo_dupa_stergere_cifra()
            elif opt == '11':
                self.handle_undo_stergere_normala()
            elif opt == '12':
                self.handle_undo_la_update()
            elif opt == '13':
                self.handle_undo_la_add()
            elif opt == 'a1':
                self.handle_afisare_cafele()
            elif opt == 'x':
                break
            else:
                print('Optiune invalida. Reincercati.')

    def handle_adaugare_cafea(self):
        idc = random.randint(1, 100)
        numec = input('Dati numele cafelei: ')
        tara = input('Dati tara de origine a cafelei: ')
        pret = float(input('Dati pretul cafelei:'))
        self.__crt_undo = self.__cafea_service.update_undo4(self.__crt_undo, numec, tara,
                                                            pret)  # adauga la lista de undo produsele ce urmeaza a fi sterse
        try:
            self.__cafea_service.add_cafea(idc, numec, tara, pret)
            print(colored('Cafeaua a fost adaugata cu succes.', 'green'))
            self.handle_afisare_cafele()
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(str(ve))

    def handle_undo_la_add(self):
        try:
            self.__crt_undo = self.__cafea_service.undo4(self.__crt_undo)
            print(colored('S-a refacut cu succes ultima operatie de stergere!', 'green'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))
        self.handle_afisare_cafele()

    def handle_afisare_cafele(self):
        cafele = self.__cafea_service.get_all_cafele()
        for caf in cafele:
            print(caf)

    def handle_afis_cafele_sort(self):
        rez = self.__cafea_service.afisare_cafele_sortate()
        for cafea in rez:
            print(cafea)

    def handle_filtrare_cafele(self):
        tara = input('Dati tara de origine a cafelei: ')
        pret = input('Dati pretul cafelei: ')
        self.__cafea_service.filtrare_cafele(tara, pret)

    def update_cafea(self):
        idc = input('Dati id-ul cafelei care se va modifica: ')
        numec = input('Dati noul nume al cafelei: ')
        tara = input('Dati noua tara de origine a cafelei: ')
        pret = float(input('Dati pretul cafelei:'))

        self.__crt_undo = self.__cafea_service.update_undo3(self.__crt_undo,
                                                            int(idc))  # adauga la lista de undo produsele ce urmeaza a fi updatate

        try:
            self.__cafea_service.update_cafea(idc, numec, tara, pret)
            print(colored('Cafeaua a fost adaugata cu succes.', 'green'))
            self.handle_afisare_cafele()
        except ValueError as ve:
            print(str(ve))

    def handle_undo_la_update(self):
        try:
            self.__crt_undo = self.__cafea_service.undo3(self.__crt_undo)
            print(colored('S-a refacut cu succes ultima operatie de update!', 'green'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))
        self.handle_afisare_cafele()

    def delete_cafea(self):
        idc = input('Dati id-ul cafelei care se va sterge: ')

        self.__crt_undo = self.__cafea_service.update_undo2(self.__crt_undo,
                                                            int(idc))  # adauga la lista de undo produsele ce urmeaza a fi sterse

        try:
            self.__cafea_service.delete_cafea(idc)
            self.handle_afisare_cafele()
        except KeyError as ke:
            print(ke)

    def handle_undo_stergere_normala(self):
        try:
            self.__crt_undo = self.__cafea_service.undo2(self.__crt_undo)
            print(colored('S-a refacut cu succes ultima operatie de stergere!', 'green'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))
        self.handle_afisare_cafele()

    def handle_delete_cafele_cu_cifra_continuta(self):
        cifra = input('Dati cifra: ')

        self.__crt_undo = self.__cafea_service.update_undo(self.__crt_undo,
                                                           int(cifra))  # adauga la lista de undo produsele ce urmeaza a fi sterse
        sterse = self.__cafea_service.delete_cafele_cu_cifra_continuta(cifra)

        self.__cafea_service.delete_cafele_cu_cifra_continuta(cifra)
        print(colored('Au fost sterse ' + str(sterse) + ' produse!', 'green'))
        self.handle_afisare_cafele()

    def handle_undo_dupa_stergere_cifra(self):
        """
        Reface ultima operatie de stergere.
        """
        try:
            self.__crt_undo = self.__cafea_service.undo(self.__crt_undo)
            print(colored('S-a refacut cu succes ultima operatie de stergere dupa cifre!', 'green'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))
        self.handle_afisare_cafele()

    def cautare_cafea_dupa_id(self):
        id_cafea = input('Dati id-ul cafelei pe care o cautati: ')
        self.handle_show_all(self.__cafea_service.cautare_cafea_dupa_id(id_cafea))

    def cautare_cafea_dupa_nume(self):
        nume_cafea = input('Dati numele cafelei pe care o cautati: ')
        self.handle_show_all(self.__cafea_service.cautare_cafea_dupa_nume(nume_cafea))

    def handle_afis_cafele_ord_desc_pret(self):
        rez = self.__cafea_service.afis_cafele_ord_desc_pret()
        for cafea in rez:
            print(cafea)

    def handle_afis_cafele_tara_desc_nume(self):
        tara = input('Dati tara de origine a cafelei: ')
        rez = self.__cafea_service.afis_cafele_tara_desc_nume(tara)
        for cafea in rez:
            print(cafea)

    def handle_delete_cafele_aceeasi_tara(self):
        tara = input('Dati tara de origine a cafelei: ')
        rez = self.__cafea_service.delete_cafele_aceeasi_tara(tara)
        for cafea in rez:
            print(cafea)

    def handle_delete_cafele_aceeasi_tara_de_tot(self):
        tara = input('Dati tara de origine a cafelei: ')
        self.__cafea_service.delete_cafele_aceeasi_tara_de_tot(tara)
        self.handle_afisare_cafele()

    def handle_delete_cafele_cu_pret_maxim(self):
        self.__cafea_service.delete_cafele_pret_maxim()
        self.handle_afisare_cafele()

    def handle_generare_cafea(self):
        n = int(input('Nr de cafele ce se doresc generate: '))
        str_tari = input('Introduceti tari de origine ale cafelelor cu , intre ele: ')
        lista_tari = str_tari.split(',')
        str_preturi = input('Introduceti preturi de cafele cu , intre ele: ')
        lista_preturi = str_preturi.split(',')

        self.__cafea_service.add_random(n, lista_tari, lista_preturi)
        print(colored('Au fost adaugate cu succes ' + str(n) + ' cafele!', 'green'))

    def handle_export(self):
        filename = input('Dati numele fisierului unde se va exporta: ')
        self.__cafea_service.export(filename)
        print(colored('Cafelele sortate dupa id si pret au fost exportate cu succes!', 'green'))

    def handle_import(self):
        """
        Genereaza jucatori cu nume si prenume dintr-un fisier existent.
                """
        cnt = self.__cafea_service.generare_import()
        print(colored('Au fost importate ' + str(cnt) + ' cafele', 'green'))

    def handle_show_all(self, objects):
        for obj in objects:
            print(obj)

# update in care se dau doar 2 parametri ca la fata aia

# lista de studenți și notele lor la o disciplină dată, ordonat: alfabetic după nume, după notă.
#  Primi 20% din studenți ordonat dupa media notelor la toate disciplinele (nume și notă)

# lista de studenți și notele lor la o problema de laborator dat, ordonat: alfabetic după nume,
# după notă.
#  Toți studenții cu media notelor de laborator mai mic decât 5. (nume student și notă)

#
# Clienți cu filme închiriate ordonat dupa: nume, după numărul de filme închiriate
#  Cele mai inchiriate filme.
#  Primi 30% clienti cu cele mai multe filme (nume client și numărul de filme închiriate)

# Cele mai inchiriate cărți.
#  Clienți cu cărți închiriate ordonat dupa: nume, după numărul de cărți închiriate
#  Primi 20% dintre cei mai activi clienți (nume client si numărul de cărți închiriate)


# Lista de evenimente la care participă o persoană ordonat alfabetic după descriere, după dată
#  Persoane participante la cele mai multe evenimente
#  Primele 20% evenimente cu cei mai mulți participanți (descriere, număr participanți)
