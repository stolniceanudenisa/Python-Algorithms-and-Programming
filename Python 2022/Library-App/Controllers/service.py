from Domain.entities import *
from operator import attrgetter
import copy

class ServiceBooks:
    def __init__(self,bookRepo,bookValidator,undoRedoRepo,entriesGenerator):
        self.__BookRepo = bookRepo
        self.__UndoRedoRepo = undoRedoRepo
        self.__validBook = bookValidator
        if entriesGenerator:
            self.__BookRepo.AddRepo(entriesGenerator.getGeneratedBooks())
            self.__UndoRedoRepo.addOperation(['generateBooks', self.__BookRepo.getAll()])

    def getBookTitleAuthor(self, ID):
        book = self.__BookRepo.getObj(ID)
        return book.getTitle(), book.getAuthor()
    def srv_getBookList(self):
        return self.__BookRepo.getAll()

    @staticmethod
    def check_matching(field, split_search_input):
        field = field.casefold()
        for part in split_search_input:
            if part.casefold() not in field:
                return False
        return True

    def search_books(self, field, split_search_input):
        found_books = []
        for book in self.__BookRepo.getAll():
            if self.check_matching(str(book.get_field(field)), split_search_input):
                found_books.append(book)
        if not len(found_books):
            raise SearchError("There are no books with this {}.".format(field))
        return found_books

    def add_book(self, ID, title, author):
        """
        Function that creates a book and adds it to repo.
        :param ID: int
        :param title: str
        :param author: str
        :return: nothing
        """
        book = Book(ID, title, author)
        self.__validBook.validate(book)
        self.__UndoRedoRepo.addOperation(['addBook', book])
        self.__BookRepo.add(book)

    def update_book(self, ID, newTitle, newAuthor):
        """
        Function that updates a book from the library.
        ID: int
        newTitle: str
        newAuthor : str
        :return: nothing
        """
        oldBook = self.__BookRepo.getObj(ID)
        newBook = Book(ID, newTitle, newAuthor)
        self.__validBook.validate(newBook)
        self.__UndoRedoRepo.addOperation(['updateBook', oldBook, newBook])
        self.__BookRepo.update(oldBook, newBook)

class ServiceClients:
    def __init__(self,clientRepo,clientValidator,undoRedoRepo,entriesGenerator):
        self.__ClientRepo = clientRepo
        self.__UndoRedoRepo = undoRedoRepo
        self.__validClient = clientValidator
        if entriesGenerator:
            self.__ClientRepo.AddRepo(entriesGenerator.getGeneratedClients())
            self.__UndoRedoRepo.addOperation(['generateClients', self.__ClientRepo.getAll()])

    def getClientName(self,clientID):
        client = self.__ClientRepo.getObj(clientID)
        return client.getName()

    def srv_getClientList(self):
        return self.__ClientRepo.getAll()

    @staticmethod
    def check_matching(field, split_search_input):
        field = field.casefold()
        for part in split_search_input:
            if part.casefold() not in field:
                return False
        return True

    def search_clients(self, field, split_search_input):
        found_clients = []
        for client in self.__ClientRepo.getAll():
            if self.check_matching(str(client.get_field(field)),split_search_input):
                found_clients.append(client)
        if not len(found_clients):
            raise SearchError("There are no clients with this {}.".format(field))
        return found_clients

    def add_client(self,ID,name):
        """
        Function that creates a book and adds it to repo.
        :param ID: int
        :param name: str
        :return: nothing
        """
        client = Client(ID,name)
        self.__validClient.validate(client)
        self.__UndoRedoRepo.addOperation(['addClient',client])
        self.__ClientRepo.add(client)

    def update_client(self,ID,newName):
        """
        Function that updates a client of the library.
        ID , newID: int
        name , newName: str
        :return: nothing
        """
        oldClient = self.__ClientRepo.getObj(ID)
        newClient = Client(ID,newName)
        self.__validClient.validate(newClient)
        self.__UndoRedoRepo.addOperation(['updateClient',oldClient,newClient])
        self.__ClientRepo.update(oldClient,newClient)

class ServiceRentals:
    def __init__(self,rentRepo,rentalValidator,bookRepo,clientRepo,undoRedoRepo,entriesGenerator):
        self.__BookRepo = bookRepo
        self.__ClientRepo = clientRepo
        self.__RentRepo = rentRepo
        self.__UndoRedoRepo = undoRedoRepo
        self.__validRental = rentalValidator
        if entriesGenerator:
            self.__RentRepo.AddRepo(entriesGenerator.getGeneratedRentals())
            self.__UndoRedoRepo.addOperation(['generateRentals', self.__RentRepo.getAll()])

    def srv_getRentalList(self):
        return self.__RentRepo.getAll()

    def select_rentals(self,objName,objID):
        """
        Function that selects all the rentals having given book/client ID.
        :param objName: str - 'book' or 'client'
        :param objID: int
        :return: the list of rentals that were selected
        """
        selected_rentals = []
        ClientBookID = {'book': Rental.getBookID, 'client': Rental.getClientID}
        for rental in self.__RentRepo.getAll():
           if ClientBookID[objName](rental) == objID:
                selected_rentals.append(rental)
        return selected_rentals

    def remove_book_and_rentals(self,ID):
        """
        Function that removes a given book from the library.
        :param ID: int
        :return: nothing
        """
        book = self.__BookRepo.getObj(ID)
        selected_rentals = self.select_rentals('book',ID)
        self.__RentRepo.removeObjects(selected_rentals)
        self.__BookRepo.remove(book)
        self.__UndoRedoRepo.addOperation(['removeBook',book,selected_rentals])

    def remove_client_and_rentals(self, ID):
        """
        Function that removes a given client of the library.
        :param ID: int
        :return: nothing
        """
        client = self.__ClientRepo.getObj(ID)
        selected_rentals = self.select_rentals('client',ID)
        self.__RentRepo.removeObjects(selected_rentals)
        self.__UndoRedoRepo.addOperation(['removeClient',client,selected_rentals])
        self.__ClientRepo.remove(client)

    def rent_book(self,bookID,clientID,date):
        wantedBook = self.__BookRepo.getObj(bookID)
        if wantedBook.getAvailability():
            wantedBook.setAvailability(False)
            wantedBook.incrementTimesRented()
        else:
            raise RentalError("This book is not available. Try again later.")
        rentalID = 1
        if self.__RentRepo.size():
            rentalID += max([r.getID() for r in self.__RentRepo.getAll()])
        rental = Rental(rentalID,bookID,clientID,date,None)
        self.__validRental.validate(rental)
        self.__RentRepo.add(rental)
        self.__UndoRedoRepo.addOperation(['rentBook',copy.deepcopy(rental)])
        try:
            self.__BookRepo.updateRepoFile()
        # if there was an attribute error, the repo is in memory, so we let it pass
        except AttributeError: pass

    def return_book(self,bookID,date):
        ok = False
        for rental in self.__RentRepo.getAll():
            if rental.getBookID() == bookID and rental.getReturnDate() is None:
                rental.setReturnDate(date)
                try:
                    self.__validRental.validate(rental)
                except Exception as ex:
                    rental.setReturnDate(None)
                    raise ex
                self.__BookRepo.getObj(bookID).setAvailability(True)
                self.__ClientRepo.getObj(rental.getClientID()).addRentalDays((date-rental.getRentDate()).days)
                ok = True
                self.__UndoRedoRepo.addOperation(['returnBook',copy.deepcopy(rental)])
                break
        if ok is False:
            raise RentalError("This rental doesn't exist!")
        try:
            self.__RentRepo.updateRepoFile()
            self.__BookRepo.updateRepoFile()
            self.__ClientRepo.updateRepoFile()
        except AttributeError: pass

class ServiceStatistics:
    def __init__(self,bookRepo,clientRepo,rentRepo):
        self.__BookRepo = bookRepo
        self.__ClientRepo = clientRepo
        self.__RentRepo = rentRepo

    def most_rented_books(self):
        rentedBookList = []
        for book in self.__BookRepo.getAll():
            if book.getTimesRented() > 0:
                rentedBookList.append(book)
        if not len(rentedBookList):
            raise SearchError("No books were rented!")
        sortedBookList = sorted(rentedBookList,key=lambda obj:obj.getTimesRented(),reverse=True)
        return sortedBookList

    def most_active_clients(self):
        activeClientsList = []
        for client in self.__ClientRepo.getAll():
            if client.getRentalDays() > 0:
                activeClientsList.append(client)
        if not len(activeClientsList):
            raise SearchError("There are no returned books!")
        sortedClientList = sorted(activeClientsList,key=attrgetter('_Client__rentalDays'),reverse=True)
        return sortedClientList

    def most_rented_authors(self):
        authors = {} #dictionary of apparitions
        for rental in self.__RentRepo.getAll():
            rentedBook = self.__BookRepo.getObj(rental.getBookID())
            author = rentedBook.getAuthor()
            if author not in authors:
                authors[author] = 1
            else: authors[author] += 1
        if not len(authors):
            raise SearchError("No books were rented!")
        sortedAuthors = sorted(authors,key=authors.__getitem__,reverse=True)
        sortedAuthorsDict = {}
        for author in sortedAuthors:
            sortedAuthorsDict[author] = authors[author]
        return sortedAuthorsDict

class ServiceUndoRedo:
    def __init__(self,bookRepo,clientRepo,rentRepo,undoRedoRepo):
        self.__BookRepo = bookRepo
        self.__ClientRepo = clientRepo
        self.__RentRepo = rentRepo
        self.__UndoRedoRepo = undoRedoRepo

    def undoRent(self,rental):
        book = self.__BookRepo.getObj(rental.getBookID())
        book.decrementTimesRented()
        book.setAvailability(True)
        self.__RentRepo.remove(rental)
        try: self.__BookRepo.updateRepoFile()
        except AttributeError: pass

    def undoReturn(self,rental):
        self.__BookRepo.getObj(rental.getBookID()).setAvailability(False)
        self.__ClientRepo.getObj(rental.getClientID()).subtractRentalDays((rental.getReturnDate()-rental.getRentDate()).days)
        self.__RentRepo.getObj(rental.getID()).setReturnDate(None)
        try:
            self.__RentRepo.updateRepoFile()
            self.__BookRepo.updateRepoFile()
            self.__ClientRepo.updateRepoFile()
        except AttributeError: pass

    def redoRent(self,rental):
        self.__RentRepo.add(rental)
        book = self.__BookRepo.getObj(rental.getBookID())
        book.incrementTimesRented()
        book.setAvailability(False)
        try: self.__BookRepo.updateRepoFile()
        except AttributeError: pass

    def redoReturn(self,rental):
        r = self.__RentRepo.getObj(rental.getID())
        r.setReturnDate(rental.getReturnDate())
        self.__BookRepo.getObj(rental.getBookID()).setAvailability(True)
        self.__ClientRepo.getObj(rental.getClientID()).addRentalDays((rental.getReturnDate() - rental.getRentDate()).days)
        try:
            self.__RentRepo.updateRepoFile()
            self.__BookRepo.updateRepoFile()
            self.__ClientRepo.updateRepoFile()
        except AttributeError: pass

    def undo(self):
        prevOp = self.__UndoRedoRepo.getPreviousOperation()
        UndoOperations = {'addBook':self.__BookRepo.remove,
                          'removeBook': self.__BookRepo.add,
                          'updateBook': self.__BookRepo.update,
                          'addClient':self.__ClientRepo.remove,
                          'removeClient': self.__ClientRepo.add,
                          'updateClient': self.__ClientRepo.update,
                          'rentBook': self.undoRent,
                          'returnBook': self.undoReturn,
                          'generateBooks': self.__BookRepo.cleanRepo,
                          'generateClients': self.__ClientRepo.cleanRepo,
                          'generateRentals': self.__RentRepo.cleanRepo}
        n = len(prevOp)
        if n==2: #add - obj , rent/return book
            if 'generate' in prevOp[0]: #generate books/clients/rentals
                UndoOperations[prevOp[0]]()
            else:
                UndoOperations[prevOp[0]](prevOp[1])
        elif n == 3:
            if 'remove' in prevOp[0]: #remove - obj, removed_rentals - add these rentals back
                UndoOperations[prevOp[0]](prevOp[1])
                self.__RentRepo.addObjects(prevOp[2])
            else: UndoOperations[prevOp[0]](prevOp[2],prevOp[1]) #update - oldObj, newObj

    def redo(self):
        prevOp = self.__UndoRedoRepo.getPreviousUndoneOp()
        RedoOperations = {'addBook': self.__BookRepo.add,
                          'removeBook': self.__BookRepo.remove,
                          'updateBook': self.__BookRepo.update,
                          'addClient': self.__ClientRepo.add,
                          'removeClient': self.__ClientRepo.remove,
                          'updateClient': self.__ClientRepo.update,
                          'rentBook': self.redoRent,
                          'returnBook':self.redoReturn,
                          'generateBooks': self.__BookRepo.AddRepo,
                          'generateClients': self.__ClientRepo.AddRepo,
                          'generateRentals': self.__RentRepo.AddRepo}
        n = len(prevOp)
        if n == 2: #add - obj, rent/return book, generate books,clients,rentals
            RedoOperations[prevOp[0]](prevOp[1])
        elif n == 3:
            if 'remove' in prevOp[0]: #remove obj, removed_rentals - delete these rentals
                RedoOperations[prevOp[0]](prevOp[1])
                self.__RentRepo.removeObjects(prevOp[2])
            else: RedoOperations[prevOp[0]](prevOp[1], prevOp[2]) #update
