from Domain.inchiriere import Inchiriere
from Repository.carte_file_repository import CarteFileRepository
from Repository.client_file_repository import ClientFileRepository
from Repository.inchiriere_file_repository import InchiriereFileRepository


# from Repository.carte_repository import CarteRepository
# from Repository.client_repository import ClientRepository
# from Repository.inchiriere_repository import InchiriereRepository


class InchiriereService:

    def __init__(self, inchiriere_repository: InchiriereFileRepository, client_repository: ClientFileRepository,
                 carte_repository: CarteFileRepository):
        self.__inchiriere_repository = inchiriere_repository
        self.__client_repository = client_repository
        self.__carte_repository = carte_repository

    def get_all(self):
        return self.__inchiriere_repository.get_all()

    def cautare_inchiriere_dupa_id(self, id_inchiriere):
        return self.__inchiriere_repository.cauta_inchiriere_dupa_id(id_inchiriere)

    def adauga(self, id_inchiriere, client_id, carte_id):
        inchiriere = Inchiriere(id_inchiriere, client_id, carte_id)
        self.__inchiriere_repository.adauga(inchiriere)

    def returnare_carte(self, client_id, carte_id):
        try:
            if self.exista_inchiriere_carte(carte_id) is False:
                raise ValueError(
                    f"Nu exista inchirierea pentru cartea {self.__carte_repository.get_by_id(carte_id).titlu_carte}.")
        except ValueError as ve:
            print(ve)
        lista_noua = self.__inchiriere_repository.get_all()
        i = 0
        while i < len(lista_noua):
            inchiriere_curenta = lista_noua[i]
            if inchiriere_curenta.carte_id == carte_id and inchiriere_curenta.client_id == client_id:
                lista_noua.pop(i)
                i = i - 1
            i = i + 1

    def exista_inchiriere_carte(self, carte_id):
        return self.__inchiriere_repository.exista_inchiriere_carte(carte_id)

    # def returneaza_clienti_la_carte_ordonati_dupa_nume(self, nume_carte):
    #     '''
    #     Metoda ce returneaza studentii de la o disciplina cautata cu notele la acea disciplina, ordonati crescator dupa note, apoi (daca doi studenti au aceeasi nota) dupa numele studentului
    #     :param nume_carte: numele disciplinei cautate
    #     :return: dictionar sortat dupa note (apoi, in caz de note egale, dupa nume student) cu numele studentilor si notele lor la disciplina cautata
    #     '''
    #     carte = self.__carte_repository.get_by_title(nume_carte)
    #     if carte is None:
    #         raise KeyError("Cartea cu acest nume nu exista!")
    #     else:
    #         carte_id = carte.get_id_carte()
    #         dictionar_client_nume = self.get_clienti_cu_carti(carte_id)
    #         # dictionar_client_nume are forma {"NumeStudent":nota_student, ...}
    #         # exemplu: {"Sara":9, "Dana":10, "Andrei":10} -> {"Sara":9, "Andrei":10, "Dana":10}
    #         # in functia predefinita sorted() d[0] se refera la "NumeStudent", iar d[1] se refera la nota_student
    #         dictionar_sortat = sorted(dictionar_client_nume.items(), key=lambda d: (d[1], d[0]))
    #         return dictionar_sortats

    def sortare_clienti_inchiriere_dupa_nume(self):
        dict_clienti_inchiriere = {}
        lista_inchirieri = self.get_all()
        for inchiriere in lista_inchirieri:
            lista_carti_client = []
            for inchiriere2 in lista_inchirieri:
                if inchiriere.client_id == inchiriere2.client_id:  # and inchiriere.get_carte_id() != inchiriere2.get_id_inchiriere():
                    lista_carti_client = lista_carti_client + [
                        self.__carte_repository.get_by_id(inchiriere2.carte_id)]

            dict_clienti_inchiriere[
                self.__client_repository.get_by_id(inchiriere.client_id).nume_client] = lista_carti_client
        return sorted(dict_clienti_inchiriere.items(), key=lambda d: (d[0], d[1]))

    def print_sortare_clienti_inchiriere_dupa_nume(self):
        sortare_clienti = self.sortare_clienti_inchiriere_dupa_nume()
        for inchiriere in sortare_clienti:
            print(f"{inchiriere[0]} : {','.join([x.titlu_carte for x in inchiriere[1]])}")

    def sortare_clienti_inchiriere_dupa_nr_inchirieri(self):
        dict_clienti_inchiriere = {}
        lista_inchirieri = self.get_all()
        for inchiriere in lista_inchirieri:
            lista_carti_client = []
            for inchiriere2 in lista_inchirieri:
                if inchiriere.client_id == inchiriere2.client_id:
                    lista_carti_client = lista_carti_client + [
                        self.__carte_repository.get_by_id(inchiriere2.carte_id)]

            dict_clienti_inchiriere[
                self.__client_repository.get_by_id(inchiriere.client_id).nume_client] = [lista_carti_client,
                                                                                         len(lista_carti_client)]
        return sorted(dict_clienti_inchiriere.items(), key=lambda d: (d[1][1], d[0]), reverse=True)

    def print_sortare_clienti_inchiriere_dupa_nr_inchirieri(self):
        sortare_clienti = self.sortare_clienti_inchiriere_dupa_nr_inchirieri()
        for inchiriere in sortare_clienti:
            print(
                f"{inchiriere[0]} :  {','.join([x.titlu_carte for x in inchiriere[1][0]])} [ {inchiriere[1][1]} ]")

    def cei_mai_activi_clienti(self):
        lista_clienti = self.sortare_clienti_inchiriere_dupa_nr_inchirieri()
        lungime = int(50 / 100 * len(lista_clienti))
        for clienti in lista_clienti[:lungime]:
            print(f"{clienti[0]} : {','.join([x.titlu_carte for x in clienti[1][0]])} {clienti[1][1]}")

    # def get_clienti_cu_carti(self, carte_id):
    #     '''
    #     Metoda ce returneaza un dictionar care mapeaza numele studentului si nota obtinuta la disciplina cu id-ul dat
    #     :param carte_id: id-ul disciplinei cautate
    #     :return: un dictionar care mapeaza numele studentului si nota obtinuta la disciplina cu id-ul dat
    #     '''
    #     # vom salva intr-un dictionar numele si nota fiecarui student, ex: {nume_student1: nota_student1, nume_student2: nota_student2, ...}
    #     dictionar_client_carte = {}  # in acest dictionar cheile vor fi numele studentilor, iar valorile vor fi cartile inchiriate
    #     inchirieri = self.get_all()  # luam lista de inscrieri a studentilor la discipline
    #     for inchiriere in inchirieri:  # o parcurgem inchiriere cu inchiriere
    #         if inchiriere.get_carte_id() == carte_id:  # daca am gasit o inchiriere la o carte cautata
    #             client_id = inchiriere.get_client_id()  # luam id-ul studentului inscris la acea disciplina
    #             client = self.__client_repository.get_by_id(
    #                 client_id)  # in student_repository, cautam obiectul student cu acel id si il returnam
    #             nume_client = client.get_nume_client()  # am avut nevoie de obiectul student, ca sa putem lua numele studentului -> acum nume_student este numele studentului inscris la disciplina cautata
    #
    #             # carte = inchiriere.get_carte_id()
    #             carte = self.__carte_repository.get_by_id(carte_id)
    #
    #             dictionar_client_carte[
    #                 nume_client] = carte  # adaugam in dictionar la cheia aferenta numelui studentului, nota lui la disciplina cautata
    #     return dictionar_client_carte

    # def returneaza_studenti_ordonati_medie(self, nr_maxim_studenti_afisati):
    #     '''
    #     Metoda ce returneaza cei mai buni studenti, ordonati dupa mediile la toate materiile
    #     :param nr_maxim_studenti_afisati:
    #     :return: cei mai buni <nr_maxim_studenti_afisati> studenti, ordonati dupa mediile la toate materiile
    #     '''
    #     dictionar_student_medie = {}  # vom tine un dictionar care va mapa numele studentului si media notelor lui la toate materiile
    #     dictionar_student_numar_note = {}  # si un dictionar care va mapa numele studentului si numarul materiilor la care a primit nota
    #     # pentru ca initial in dictionar_student_medie vom face suma notelor studentilor la toate materiile
    #     # iar apoi ne vom folosi de dictionar_student_numar_note pentru a calcula media corect pentru fiecare student(vom imparti suma notelor studentului la numarul de note primite de el)
    #     inscrieri = self.get_all()  # luam toate inscrierile
    #     for inscriere in inscrieri:  # le parcurgem una cate una
    #         student_id = inscriere.get_student_id()  # luam din inscriere id-ul fiecarui student
    #         student = self.__student_repository.get_student_by_id(
    #             student_id)  # in student_repository, cautam obiectul student cu acel id si il returnam
    #         nume_student = student.get_nume()  # am avut nevoie de obiectul student, ca sa putem lua numele studentului -> acum nume_student este numele studentului de la inscrierea curenta
    #         nota = inscriere.get_nota()  # luam din inscriere nota studentului
    #         if nume_student not in dictionar_student_medie:  # daca numele studentului nu apare inca in dictionar_student_medie
    #             dictionar_student_medie[nume_student] = nota  # il adaugam dandu-i ca valoare nota curenta
    #             dictionar_student_numar_note[
    #                 nume_student] = 1  # marcam in dictionar_student_numar_note ca studentul cu acest nume are nota la o materie
    #         else:  # daca numele studentului apare deja in dictionar_student_medie
    #             dictionar_student_medie[nume_student] = dictionar_student_medie[
    #                                                         nume_student] + nota  # adunam la suma notelor noua nota gasita
    #             dictionar_student_numar_note[nume_student] = dictionar_student_numar_note[
    #                                                              nume_student] + 1  # adunam la numarul notelor studentului inca 1
    #
    #     for nume_student in dictionar_student_medie:  # pentru fiecare student din dictionar_student_medie
    #         dictionar_student_medie[nume_student] = dictionar_student_medie[nume_student] / \
    #                                                 dictionar_student_numar_note[
    #                                                     nume_student]  # facem media notelor studentului impartind suma notelor la numarul lor
    #         # pentru asta ne folosim de ambele dictionare create: dictionar_student_medie care avea inainte suma notelor studentului si dictionar_student_numar_note care ne arata numarul notelor studentului
    #
    #     # sortam dictionarul dictionar_student_medie in functie de medie in ordine inversa si returnam doar primele nr_maxim_studenti_afisati elemente
    #     dictionar_ordonat_dupa_medie = sorted(dictionar_student_medie.items(), key=lambda d: (d[1]), reverse=True)[
    #                                    :nr_maxim_studenti_afisati]
    #     return dictionar_ordonat_dupa_medie

    def clienti_ce_au_inchiriata_carte(self, nume_carte):
        '''
        Metoda ce returneaza lista clientilor ce au inchiriat o anumita carte
        :param nume_carte:
        :return: lista clienti
        '''
        lista_clienti = []
        lista_inchirieri = self.__inchiriere_repository.get_all()
        for inchiriere in lista_inchirieri:
            id_carte = inchiriere.carte_id
            carte = self.__carte_repository.get_by_id(id_carte)
            if carte.titlu_carte == nume_carte:
                client_id = inchiriere.client_id
                client = self.__client_repository.get_by_id(client_id)
                nume = client.nume_client

                lista_clienti.append(nume)
        return lista_clienti

    # def sterge_disciplina_cascada(self, id_disciplina):
    #     '''
    #     Metoda care sterge fortat o disciplina din lista de discipline.
    #     Adica pe langa faptul ca sterge disciplina din lista de discipline, sterge si toate inscrierile studenilor la acea disciplina
    #     :param id_disciplina:
    #     :return:
    #     '''
    #     self.__inscriere_repository.sterge_inscrieri_disciplina(id_disciplina)
    #     self.__disciplina_repository.sterge(id_disciplina)

    def numar_inchirieri_carte(self, carte_id):
        numar_inchiriere = 0
        lista_inchirieri = self.__inchiriere_repository.get_all()
        for inchiriere in lista_inchirieri:
            if inchiriere.carte_id == carte_id:
                numar_inchiriere += 1
        return numar_inchiriere

    def cele_mai_inchiriate_carti(self):
        dict_numar_inchiriere = {}
        inchirieri = self.get_all()
        for inchiriere in inchirieri:
            dict_numar_inchiriere[inchiriere.carte_id] = self.numar_inchirieri_carte(inchiriere.carte_id)

        return sorted(dict_numar_inchiriere.items(), key=lambda d: (d[1], d[0]), reverse=True)

    def print_cele_mai_inchiriate_carti(self):
        carti_inchiriate = self.cele_mai_inchiriate_carti()
        for carti in carti_inchiriate:
            print(
                f"Cartea {self.__carte_repository.get_by_id(carti[0]).titlu_carte} a fost inchirata de {carti[1]} ori.")

    def print_cele_mai_inchiriate_carti_procent(self):
        carti_inchiriate = self.cele_mai_inchiriate_carti()
        lungime = int(len(carti_inchiriate) * 20 / 100)
        for carti in carti_inchiriate[:lungime]:
            print(
                f"Cartea {self.__carte_repository.get_by_id(carti[0]).titlu_carte} a fost inchirata de {carti[1]} ori.")

#
# class ServiceRentals:
#     def __init__(self, rentRepo, rentalValidator, bookRepo, clientRepo, undoRedoRepo, entriesGenerator):
#         self.__BookRepo = bookRepo
#         self.__ClientRepo = clientRepo
#         self.__RentRepo = rentRepo
#         self.__UndoRedoRepo = undoRedoRepo
#         self.__validRental = rentalValidator
#         if entriesGenerator:
#             self.__RentRepo.AddRepo(entriesGenerator.getGeneratedRentals())
#             self.__UndoRedoRepo.addOperation(['generateRentals', self.__RentRepo.getAll()])
#
#     def srv_getRentalList(self):
#         return self.__RentRepo.getAll()
#
#     def select_rentals(self, objName, objID):
#         """
#         Function that selects all the rentals having given book/client ID.
#         :param objName: str - 'book' or 'client'
#         :param objID: int
#         :return: the list of rentals that were selected
#         """
#         selected_rentals = []
#         ClientBookID = {'book': Rental.getBookID, 'client': Rental.getClientID}
#         for rental in self.__RentRepo.getAll():
#             if ClientBookID[objName](rental) == objID:
#                 selected_rentals.append(rental)
#         return selected_rentals
#
#     def remove_book_and_rentals(self, ID):
#         """
#         Function that removes a given book from the library.
#         :param ID: int
#         :return: nothing
#         """
#         book = self.__BookRepo.getObj(ID)
#         selected_rentals = self.select_rentals('book', ID)
#         self.__RentRepo.removeObjects(selected_rentals)
#         self.__BookRepo.remove(book)
#         self.__UndoRedoRepo.addOperation(['removeBook', book, selected_rentals])
#
#     def remove_client_and_rentals(self, ID):
#         """
#         Function that removes a given client of the library.
#         :param ID: int
#         :return: nothing
#         """
#         client = self.__ClientRepo.getObj(ID)
#         selected_rentals = self.select_rentals('client', ID)
#         self.__RentRepo.removeObjects(selected_rentals)
#         self.__UndoRedoRepo.addOperation(['removeClient', client, selected_rentals])
#         self.__ClientRepo.remove(client)
#
#     def rent_book(self, bookID, clientID, date):
#         wantedBook = self.__BookRepo.getObj(bookID)
#         if wantedBook.getAvailability():
#             wantedBook.setAvailability(False)
#             wantedBook.incrementTimesRented()
#
#         rentalID = 1
#         if self.__RentRepo.size():
#             rentalID += max([r.getID() for r in self.__RentRepo.getAll()])
#         rental = Rental(rentalID, bookID, clientID, date, None)
#         self.__validRental.validate(rental)
#         self.__RentRepo.add(rental)
#         self.__UndoRedoRepo.addOperation(['rentBook', copy.deepcopy(rental)])
#         try:
#             self.__BookRepo.updateRepoFile()
#         # if there was an attribute error, the repo is in memory, so we let it pass
#         except AttributeError:
#             pass
#
#     def return_book(self, bookID, date):
#         ok = False
#         for rental in self.__RentRepo.getAll():
#             if rental.getBookID() == bookID and rental.getReturnDate() is None:
#                 rental.setReturnDate(date)
#                 try:
#                     self.__validRental.validate(rental)
#                 except Exception as ex:
#                     rental.setReturnDate(None)
#                     raise ex
#                 self.__BookRepo.getObj(bookID).setAvailability(True)
#                 self.__ClientRepo.getObj(rental.getClientID()).addRentalDays((date - rental.getRentDate()).days)
#                 ok = True
#                 self.__UndoRedoRepo.addOperation(['returnBook', copy.deepcopy(rental)])
#                 break
#
#         try:
#             self.__RentRepo.updateRepoFile()
#             self.__BookRepo.updateRepoFile()
#             self.__ClientRepo.updateRepoFile()
#         except AttributeError:
#             pass
