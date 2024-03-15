from Service.carte_service import CarteService
from Service.client_service import ClientService
from Service.inchiriere_service import InchiriereService


class Console:
    def __init__(self, carte_service: CarteService, client_service: ClientService,
                 inchiriere_service: InchiriereService):
        self.__carte_service = carte_service
        self.__client_service = client_service
        self.__inchiriere_service = inchiriere_service

    def print_menu_carte(self):
        print("""
        1. Adaugare carte.
        2. Modificare carte.
        3. Stergere carte.
        4. Cautare carte dupa id.
        5. Cautare carte dupa titlu.
        6. Cautare carte dupa descriere.
        7. Cautare carte dupa autor.
        a. Afisare carti.
        b. back
        """)

    def print_menu_client(self):
        print("""
        1. Adaugare client.
        2. Modificare client.
        3. Stergere client.
        4. Cautare client dupa id.
        5. Cautare client dupa nume.
        6. Cautare client dupa cnp.
        a. Afisare clienti.
        b. back
        """)

    def show_menu1(self):
        print("""
        1. Carti.
        2. Clienti.
        3. Exit.
        """)

        # 4. sortare_carti_desc_dupa_autor.

    def show_menu2(self):
        print("""
        1. Adaugare carte.
        2. Modificare carte.
        3. Stergere carte.
        4. Cautare carte dupa id.
        5. Cautare carte dupa titlu.
        6. Cautare carte dupa descriere.
        7. Cautare carte dupa autor.
    	8. Adaugare client.
        9. Modificare client.
        10. Stergere client.
    	11. Cautare client dupa id.
        12. Cautare client dupa nume.
        13. Cautare client dupa cnp.	
        14. Inchiriere carte.
        141. Returnare carte.
        142. Cele mai inchiriate carti.
        143. Sortare clienti dupa nume
        144. Sortare clienti dupa nr carti
        145. Primi 20% dintre cei mai activi clienți 
        a1. Afisare toate cartile.
        a2. Afisare toti clientii.
        a3. Afisare toate inchirierile.
        x. Exit
        """)
        # 15. Lista de clienti si cartile lor ordonati dupa nume.
        # 16. Lista nume de clienti ce au o anumita carte inchiriata.

    def handle_carti(self):
        while True:
            self.print_menu_carte()
            opt = input('Alegeti optiunea: ')
            if opt == '1':
                self.handle_add_carte()
            elif opt == '2':
                self.handle_update_carte()
            elif opt == '3':
                self.handle_delete_carte()
            elif opt == '4':
                self.handle_cautare_carte_dupa_id()
            elif opt == '5':
                self.handle_cautare_carte_dupa_titlu()
            elif opt == '6':
                self.handle_cautare_carte_dupa_descriere()
            elif opt == '7':
                self.handle_cautare_carte_dupa_autor()
            elif opt == 'a':
                self.handle_show_all(self.__carte_service.get_all_carti())
            elif opt == 'b':
                break
            else:
                print('Comanda invalida. Reincercati.')

    def handle_clienti(self):
        while True:
            self.print_menu_client()
            opt = input('Alegeti optiunea: ')
            if opt == '1':
                self.handle_add_client()
            elif opt == '2':
                self.handle_update_client()
            elif opt == '3':
                self.handle_delete_client()
            elif opt == '4':
                self.handle_cautare_client_dupa_id()
            elif opt == '5':
                self.handle_cautare_client_dupa_nume()
            elif opt == '6':
                self.handle_cautare_client_dupa_cnp()
            elif opt == 'a':
                self.handle_show_all(self.__client_service.get_all_clienti())
            elif opt == 'b':
                break
            else:
                print('Comanda invalida. Reincercati.')

    def run_console1(self):
        while True:
            # self.handle_show_all(self.carte_service.get_all_carti())
            # self.handle_show_all(self.client_service.get_all_clienti())
            self.show_menu1()
            option = input('Alegeti optiunea: ')
            if option == '1':
                self.handle_carti()
            elif option == '2':
                self.handle_clienti()
            # elif option == '4':
            #     self.sortare_carti_desc_dupa_autor()
            elif option == '8':
                self.handle_adauga_inchiriere_carte()
            elif option == '3':
                break
            else:
                print('Comanda invalida. Reincercati.')

    def run_console2(self):
        while True:
            self.show_menu2()
            option = input('Alegeti optiunea: ')
            if option == '1':
                self.handle_add_carte()
            elif option == '2':
                self.handle_update_carte()
            elif option == '3':
                self.handle_delete_carte()
            elif option == '4':
                self.handle_cautare_carte_dupa_id()
            elif option == '5':
                self.handle_cautare_carte_dupa_titlu()
            elif option == '6':
                self.handle_cautare_carte_dupa_descriere()
            elif option == '7':
                self.handle_cautare_carte_dupa_autor()

            elif option == '8':
                self.handle_add_client()
            elif option == '9':
                self.handle_update_client()
            elif option == '10':
                self.handle_delete_client()
            elif option == '11':
                self.handle_cautare_client_dupa_id()
            elif option == '12':
                self.handle_cautare_client_dupa_nume()
            elif option == '13':
                self.handle_cautare_client_dupa_cnp()


            elif option == '14':
                self.handle_adauga_inchiriere_carte()
            elif option == '141':
                self.handle_returnare_carte()
            elif option == '142':
                self.handle_cele_mai_inchiriate_carti()
            elif option == '143':
                self.handle_sortare_clienti_inchiriere_dupa_nume()
            elif option == '144':
                self.handle_sortare_clienti_inchiriere_dupa_nr_inchirieri()
            elif option == '145':
                self.handle_cei_mai_activi_clienti()

            # elif option == '15':
            #     self.ui_studenti_la_disciplina_ordonati_nota_nume()

            elif option == '16':
                self.ui_clienti_ce_au_o_carte()
            elif option == 'a1':
                self.handle_show_all(self.__carte_service.get_all_carti())

            elif option == 'a2':
                self.handle_show_all(self.__client_service.get_all_clienti())

            elif option == 'a3':
                self.ui_tipareste_inchirieri()

            elif option == 'x':
                break
            else:
                print('Comanda invalida. Reincercati.')

    def handle_add_carte(self):
        try:
            id_carte = input('Dati id-ul cartii: ')
            titlu_carte = input('Dati titlul cartii: ')
            descriere_carte = input('Dati descrierea cartii: ')
            autor_carte = input('Dati autorul cartii: ')

            self.__carte_service.add_carte(id_carte, titlu_carte, descriere_carte, autor_carte)

        except ValueError as ve:
            print('Eroare de validare: ', ve)
        except KeyError as ke:
            print('Eroare de ID:', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_add_client(self):
        try:
            id_client = input('Dati id-ul clientului: ')
            nume_client = input('Dati numele clientului: ')
            cnp_client = input('Dati cnp-ul clientului: ')
            if not cnp_client.isnumeric():  # or len(cnp_client) != 13
                raise ValueError('CNP-ul este format doar din cifre.')

            self.__client_service.add_client(id_client, nume_client, cnp_client)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except ValueError as ve:
            print('Eroare de validare: ', ve)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_update_carte(self):
        try:
            id_carte = input('Dati id-ul cartii care se va modifica: ')
            titlu_carte = input('Dati titlul nou al cartii: ')
            descriere_carte = input('Dati descrierea cartii: ')
            autor_carte = input('Dati autorul cartii: ')

            self.__carte_service.update_carte(id_carte, titlu_carte, descriere_carte, autor_carte)

        except ValueError as ve:
            print('Eroare de validare: ', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_update_client(self):
        try:
            id_client = input('Dati id-ul clientului care se va modifica: ')
            nume_client = input('Dati noul nume al clientului: ')
            cnp_client = input('Dati cnp-ul clientului: ')
            if not cnp_client.isnumeric():
                raise ValueError('CNP-ul este format doar din cifre.')

            self.__client_service.update_client(id_client, nume_client, cnp_client)

        except ValueError as ve:
            print('Eroare de validare: ', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_delete_carte(self):
        try:
            id_carte = input('Dati id-ul cartii care se va sterge: ')

            self.__carte_service.delete_carte(id_carte)

        except ValueError as ve:
            print('Eroare de validare: ', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_delete_client(self):
        try:
            id_client = input('Dati id-ul clientului care se va sterge: ')

            self.__client_service.delete_client(id_client)

        except ValueError as ve:
            print('Eroare de validare: ', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_show_all(self, objects):
        for obj in objects:
            print(obj)

    def sortare_carti_desc_dupa_autor(self):
        result = self.__carte_service.sort_carti_autor()
        for carti in result:
            print(carti)

    def handle_cautare_carte_dupa_id(self):
        id_carte = input('Dati id-ul cartii pe care o cautati: ')
        # validare confortul citit de la tastatura (optional)
        self.handle_show_all(self.__carte_service.cautare_carte_dupa_id(id_carte))

    def handle_cautare_carte_dupa_titlu(self):
        try:
            titlu_carte = input('Dati titlul cartii pe care o cautati: ')
            if not titlu_carte.isalpha():
                raise ValueError('Titlul cartii este format doar din litere.')
        except ValueError:
            print('Titlul cartii este format doar din litere.')
        self.handle_show_all(self.__carte_service.cautare_carte_dupa_titlu(titlu_carte))

    def handle_cautare_carte_dupa_descriere(self):
        try:
            descriere_carte = input('Dati descrierea cartii pe care o cautati: ')
            if not descriere_carte.isalpha():
                raise ValueError('Descrierea cartii este formata doar din litere.')
        except ValueError:
            print('Descrierea cartii este formata doar din litere.')
        self.handle_show_all(self.__carte_service.cautare_carte_dupa_descriere(descriere_carte))

    def handle_cautare_carte_dupa_autor(self):
        try:
            autor_carte = input('Dati autorul cartii pe care o cautati: ')
            if not autor_carte.isalpha():
                raise ValueError('Numele autorului cartii este format doar din litere.')
        except ValueError:
            print('Numele autorului cartii este format doar din litere.')
        self.handle_show_all(self.__carte_service.cautare_carte_dupa_autor(autor_carte))

    def handle_cautare_client_dupa_id(self):
        id_client = input('Dati id-ul clientului pe care il cautati: ')
        self.handle_show_all(self.__client_service.cautare_client_dupa_id(id_client))

    def handle_cautare_client_dupa_nume(self):
        try:
            nume_client = input('Dati numele clientului pe care il cautati: ')
            if not nume_client.isalpha():
                raise ValueError('Numele clientului este format doar din litere.')
        except ValueError:
            print('Numele clientului este format doar din litere.')
        self.handle_show_all(self.__client_service.cautare_client_dupa_nume(nume_client))

    def handle_cautare_client_dupa_cnp(self):
        try:
            cnp_client = input('Dati cnp-ul clientului pe care il cautati: ')
            if not cnp_client.isnumeric():  # or len(client.cnp_client) != 13
                raise ValueError('CNP-ul este format doar din cifre.')
        except ValueError:
            print('CNP-ul este format doar din cifre.')
        self.handle_show_all(self.__client_service.cautare_client_dupa_cnp(cnp_client))

    def handle_adauga_inchiriere_carte(self):
        try:
            id_inchiriere = input("Introduceti id-ul inchirierii:")
            client_id = input("Introduceti ID client:")
            carte_id = input("Introduceti ID carte:")

            self.__inchiriere_service.adauga(id_inchiriere, client_id, carte_id)

        except ValueError:
            print("Date gresite! Reincercati!")
        except KeyError as ke:
            print(ke)

    def handle_returnare_carte(self):
        client_id = input("Introduceti ID client care returneaza cartea:")
        carte_id = input("Introduceti cartea care va fi returnata:")

        self.__inchiriere_service.returnare_carte(client_id, carte_id)

    def handle_cele_mai_inchiriate_carti(self):
        self.__inchiriere_service.print_cele_mai_inchiriate_carti()

    def handle_sortare_clienti_inchiriere_dupa_nume(self):
        self.__inchiriere_service.print_sortare_clienti_inchiriere_dupa_nume()

    def handle_sortare_clienti_inchiriere_dupa_nr_inchirieri(self):
        self.__inchiriere_service.print_sortare_clienti_inchiriere_dupa_nr_inchirieri()

    def handle_cei_mai_activi_clienti(self):
        self.__inchiriere_service.cei_mai_activi_clienti()

    def ui_tipareste_inchirieri(self):
        inchirieri = self.__inchiriere_service.get_all()
        if len(inchirieri) == 0:
            print("Lista de inchirieri e goala!")
        for inchiriere in inchirieri:
            print(inchiriere, 'Cartea:',
                  self.__carte_service.cautare_carte_dupa_id(inchiriere.carte_id)[0].titlu_carte,
                  'Clientul:',
                  self.__client_service.cautare_client_dupa_id(inchiriere.client_id)[
                      0].nume_client)  # self.__carte_repository.get_by_id(carti[0]).get_titlu_carte()
            print('\n')

    # def ui_studenti_la_disciplina_ordonati_nota_nume(self):
    #     try:
    #         carte = input("Numele cartii:")
    #         clienti = self.__inchiriere_service.returneaza_clienti_la_carte_ordonati_dupa_nume(carte)
    #         print(clienti)
    #     except KeyError as ke:
    #         print(ke)

    def ui_clienti_ce_au_o_carte(self):
        # try:
        nume_carte = input("Titlul cartii:")
        lista_clienti = self.__inchiriere_service.clienti_ce_au_inchiriata_carte(nume_carte)
        print(lista_clienti)
        # except:
        #     print("Date incorecte! Reincercati!")

    # def rent_book(self):
    #     bookID = Console.readType('Insert the ID of the book you want to rent: ', int)
    #     title, author = self.__carte_service.getBookTitleAuthor(bookID)
    #     clientID = Console.readType('Please insert the client ID: ', int)
    #     clientName = self.__client_service.getClientName(clientID)
    #     day, month, year = Console.readDate()
    #     rentDate = datetime.date(year, month, day)
    #     self.__RentalSrv.rent_book(bookID, clientID, rentDate)
    #     print("'{}' by {} was rented by {} successfully!".format(title, author, clientName))
    #
    # def return_book(self):
    #     bookID = Console.readType('Please insert the book ID: ', int)
    #     title, author = self.__BookSrv.getBookTitleAuthor(bookID)  # check book
    #     day, month, year = Console.readDate()
    #     retDate = datetime.date(year, month, day)
    #     self.__RentalSrv.return_book(bookID, retDate)
    #     print("'{}' by {} was returned successfully!".format(title, author))
    #
    # def list_rentals(self):
    #     rentalList = self.__RentalSrv.srv_getRentalList()
    #     if not len(rentalList):
    #         raise Exception("There are no rentals!\n")
    #     print("\nThe rentals of this library are:")
    #     Console.print_objects(rentalList)
    #
    # @staticmethod
    # def print_objects(objList):
    #     nr = 0
    #     for obj in objList:
    #         nr += 1
    #         print('{}.  {}'.format(nr, obj))
    #     print()
    #
    # @staticmethod
    # def readType(msg, typ):
    #     x = input(msg)
    #     while True:
    #         try:
    #             x = typ(x)
    #             return x
    #         except ValueError:
    #             print("Invalid value!")
    #             x = input(msg)

    #########mai sus

    # def handle_rent_book(self):
    #     id_client = input("Id-ul clientului care inchiriaza cartea: ")
    #     id_carte = input("Id-ul cartii care este inchiriata: ")
    #     id_rental = int(input("Id-ul inchirierii: "))
    #     rentedDate = int(input("Ziua inchirierii este: "))
    #     self.__serviceRental.rentBook(cid, bid, rid, rentedDate, self.__serviceClient)

    # def show_menu2(self):
    #     print('a[carte | client] - adaugare carte sau client. ')
    #     print('u[carte | client] - modificare carte sau client . ')
    #     print('d[carte | client] - stergere carte sau client . ')
    #     print('s[carte | client] - afisare carte sau client . ')
    #     print('5. Sortare carti descrescator dupa autor. ')
    #     print('x. Exit')

    # def run_console2(self):
    #     while True:
    #         # self.handle_show_all(self.carte_service.get_all_carti())
    #         # self.handle_show_all(self.client_service.get_all_clienti())
    #         self.show_menu()
    #         option = input('Alegeti optiunea: ')
    #         if option == 'acarte':
    #             self.handle_add_carte()
    #         elif option == 'aclient':
    #             self.handle_add_client()
    #         elif option == 'scarte':
    #             self.handle_show_all(self.carte_service.get_all_carti())
    #         elif option == 'sclient':
    #             self.handle_show_all(self.client_service.get_all_clienti())
    #         elif option == 'ucarte':
    #             self.handle_update_carte()
    #         elif option == 'uclient':
    #             self.handle_update_client()
    #         elif option == 'dcarte':
    #             self.handle_delete_carte()
    #         elif option == 'dclient':
    #             self.handle_delete_client()
    #         elif option == '5':
    #             self.sortare_carti_desc_dupa_autor()
    #         elif option == 'x':
    #             break
    #         else:
    #             print('Comanda invalida. Reincercati.')
