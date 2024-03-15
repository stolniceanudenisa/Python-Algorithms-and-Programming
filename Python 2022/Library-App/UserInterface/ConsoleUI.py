from Domain.entities import UIError
import datetime
from os import system,name

class ConsoleMenu:
    """
    The user interface class for the library app.
    """
    def __init__(self,BookSrv,ClientSrv,RentalSrv,StatisticsSrv,UndoRedoSrv):
        self.__BookSrv = BookSrv
        self.__ClientSrv = ClientSrv
        self.__RentalSrv = RentalSrv
        self.__StatSrv = StatisticsSrv
        self.__UndoRedoSrv = UndoRedoSrv
        self.__menu = """Press:  [1] to add book        [6] to remove client     [11] to search for books            [16] to list the rentals
        [2] to remove book     [7] to update client     [12] to search for clients          [u] to undo
        [3] to update book     [8] to list the clients  [13] to see the most rented books   [r] to redo
        [4] to list the books  [9] to rent book         [14] to see the most active clients [c] to clear screen(OS console)   
        [5] to add client      [10] to return book      [15] to see the most rented authors [x] to exit"""
    @staticmethod
    def readType(msg,typ):
        x = input(msg)
        while True:
            try:
                x = typ(x)
                return x
            except ValueError:
                print("Invalid value!")
                x = input(msg)
    @staticmethod
    def readDate():
        while True:
            day = ConsoleMenu.readType("Insert day: ", int)
            month = ConsoleMenu.readType("Insert month(1-12): ", int)
            year = ConsoleMenu.readType("Insert year: ", int)
            return day,month,year
    @staticmethod
    def print_objects(objList):
        nr = 0
        for obj in objList:
            nr += 1
            print('{}.  {}'.format(nr,obj))
        print()

    #BOOKS
    def add_book(self):
        ID = ConsoleMenu.readType('Insert ID: ', int)
        title = ConsoleMenu.readType('Insert title: ', str).strip()
        author = ' '.join(ConsoleMenu.readType('Insert author: ', str).split())
        self.__BookSrv.add_book(ID,title,author)
        print("Book added successfully!")
    def remove_book(self):
        ID = ConsoleMenu.readType('Insert ID: ', int)
        self.__RentalSrv.remove_book_and_rentals(ID)
        print("Book removed successfully!")
    def update_book(self):
        ID = ConsoleMenu.readType('Insert ID: ', int)
        print("Now enter the new characteristics for this book: ")
        newTitle = ConsoleMenu.readType('Insert new title: ', str).strip()
        newAuthor = ' '.join(ConsoleMenu.readType('Insert new author: ', str).split())
        self.__BookSrv.update_book(ID,newTitle,newAuthor)
        print("Book updated successfully!")
    def list_books(self):
        bookList = self.__BookSrv.srv_getBookList()
        if not len(bookList):
            raise Exception("There are no books in the list!\n")
        print("\nThe books of this library are: ")
        ConsoleMenu.print_objects(bookList)

    #CLIENTS
    def add_client(self):
        ID = ConsoleMenu.readType('Insert ID: ', int)
        Name = " ".join(ConsoleMenu.readType('Insert name: ', str).split())
        self.__ClientSrv.add_client(ID,Name)
        print("Client added successfully!")
    def remove_client(self):
        ID = ConsoleMenu.readType('Insert ID: ', int)
        self.__RentalSrv.remove_client_and_rentals(ID)
        print("Client removed successfully!")
    def update_client(self):
        ID = ConsoleMenu.readType('Insert ID: ', int)
        newName = " ".join(ConsoleMenu.readType('Insert the new name: ', str).split())
        self.__ClientSrv.update_client(ID,newName)
        print("Client updated successfully!")
    def list_clients(self):
        clientList = self.__ClientSrv.srv_getClientList()
        if not len(clientList):
            raise Exception("There are no clients!\n")
        print("\nThe clients of this library are: ")
        ConsoleMenu.print_objects(clientList)

    #RENTALS
    def rent_book(self):
        bookID = ConsoleMenu.readType('Insert the ID of the book you want to rent: ', int)
        title, author = self.__BookSrv.getBookTitleAuthor(bookID)
        clientID = ConsoleMenu.readType('Please insert the client ID: ', int)
        clientName = self.__ClientSrv.getClientName(clientID)
        day,month,year = ConsoleMenu.readDate()
        rentDate = datetime.date(year,month,day)
        self.__RentalSrv.rent_book(bookID,clientID,rentDate)
        print("'{}' by {} was rented by {} successfully!".format(title,author,clientName))
    def return_book(self):
        bookID = ConsoleMenu.readType('Please insert the book ID: ', int)
        title, author = self.__BookSrv.getBookTitleAuthor(bookID) #check book
        day,month,year = ConsoleMenu.readDate()
        retDate = datetime.date(year,month,day)
        self.__RentalSrv.return_book(bookID,retDate)
        print("'{}' by {} was returned successfully!".format(title,author))
    def list_rentals(self):
        rentalList = self.__RentalSrv.srv_getRentalList()
        if not len(rentalList):
            raise Exception("There are no rentals!\n")
        print("\nThe rentals of this library are:")
        ConsoleMenu.print_objects(rentalList)

    #Search
    def search_book(self):
        s_choice = ConsoleMenu.readType("Press: [1] to search by ID, [2] to search by title, [3] to search by author\n>", int)
        if s_choice not in (1,2,3):
            raise UIError("Non-existent option!")
        search_input = input("Insert search: ")
        split_search_input = search_input.split()
        fields = ('ID','title','author')
        found_books = self.__BookSrv.search_books(fields[s_choice-1],split_search_input)
        ConsoleMenu.print_objects(found_books)
    def search_client(self):
        s_choice = ConsoleMenu.readType("Press: [1] to search by ID, [2] to search by name\n>", int)
        if s_choice not in (1,2):
            raise UIError("Non-existent option!")
        search_input = input("Insert search: ")
        split_search_input = search_input.split()
        fields = ('ID', 'name')
        found_clients = self.__ClientSrv.search_clients(fields[s_choice-1], split_search_input)
        ConsoleMenu.print_objects(found_clients)

    #Statistics
    def most_rented_books(self):
        sorted_bookList = self.__StatSrv.most_rented_books()
        print("The most rented books are:")
        nr=0
        for book in sorted_bookList:
            nr+=1
            print('{}. {} - rented {} time(s)'.format(nr,book,book.getTimesRented()))
        print()
    def most_active_clients(self):
        sorted_clientList = self.__StatSrv.most_active_clients()
        print("The most active clients are:")
        nr=0
        for client in sorted_clientList:
            nr+=1
            print("{}. {} - {} rental days".format(nr,client,client.getRentalDays()))
    def most_rented_authors(self):
        sortedAuthors = self.__StatSrv.most_rented_authors()
        print("The most rented authors are:")
        nr=0
        for author in sortedAuthors:
            nr+=1
            print("{}. {} - {} book rental(s)".format(nr,author,sortedAuthors[author]))

    #Undo/Redo
    def undo(self):
        self.__UndoRedoSrv.undo()
        print("Undo complete!")
    def redo(self):
        self.__UndoRedoSrv.redo()
        print("Redo complete!")

    @staticmethod
    def clearScreen():
        # for windows
        if name == 'nt':
            _ = system('cls')
            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    #The program start point
    def run(self):
        print("W E L C O M E   T O   T H E   L I B R A R Y   A P P  !")
        options = {'1': self.add_book,
                   '2': self.remove_book,
                   '3': self.update_book,
                   '4': self.list_books,
                   '5': self.add_client,
                   '6': self.remove_client,
                   '7': self.update_client,
                   '8': self.list_clients,
                   '9': self.rent_book,
                   '10': self.return_book,
                   '11': self.search_book,
                   '12': self.search_client,
                   '13': self.most_rented_books,
                   '14': self.most_active_clients,
                   '15': self.most_rented_authors,
                   '16': self.list_rentals,
                   'u': self.undo,
                   'r': self.redo}
        while True:
            try:
                print(self.__menu)
                choice = input('-> ').strip()
                if choice not in ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','u','r','c','x'):
                    raise UIError("Non-existent option!")
                if choice == 'x': return
                elif choice == 'c':
                    self.clearScreen() #works only when using the OS console
                else:
                    options[choice]()
            except Exception as ex:
                print(ex)