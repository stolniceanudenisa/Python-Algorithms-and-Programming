import datetime

class Book:
    def __init__(self,ID,title,author):
        self.__ID = ID
        self.__title = title
        self.__author = author
        self.__available = True
        self.__timesRented = 0
    def getID(self):
        return self.__ID
    def getTitle(self):
        return self.__title
    def getAuthor(self):
        return self.__author
    def get_field(self,field):
        if field == 'ID':
            return self.getID()
        elif field == 'title':
            return self.getTitle()
        elif field == 'author':
            return self.getAuthor()
        else:
            raise SearchError("This field is not searchable!")
    def getAvailability(self):
        return self.__available
    def getTimesRented(self):
        return self.__timesRented
    def setID(self,other):
        self.__ID = other
    def setTitle(self,other):
        self.__title = other
    def setAuthor(self,other):
        self.__author = other
    def setAvailability(self,other):
        self.__available = other
    def incrementTimesRented(self):
        self.__timesRented += 1
    def decrementTimesRented(self):
        self.__timesRented -= 1
    def __eq__(self,other):
        return self.__ID == other.__ID
    def __str__(self):
        return "ID: " + str(self.__ID) + "  ~  TITLE: " + self.__title + "  ~  AUTHOR: " + self.__author + "  ~  STATUS: {}".format('available' if self.__available else 'unavailable')
    @staticmethod
    def readBook(line):
        parts = line.split(";")
        book = Book(int(parts[0].strip()), parts[1].strip(),parts[2].strip())
        book.__available = bool(parts[3].strip())
        book.__timesRented = int(parts[4].strip())
        return book
    @staticmethod
    def writeBook(book):
        return str(book.__ID) + ";" + book.__title + ";" + book.__author + ";" + str(book.__available) + ";"+ str(book.__timesRented)
    @staticmethod
    def BookToDict(book):
        return {'ID':book.__ID,'title':book.__title,'author':book.__author,'av':book.__available,'tr':book.__timesRented}
    @staticmethod
    def DictToBook(d):
        #print(type(d['ID']))
        book = Book(d['ID'],d['title'],d['author'])
        book.__available = d['av']
        book.__timesRented = d['tr']
        return book

class Client:
    def __init__(self,ID,name): # constructor
        self.__ID = ID
        self.__name = name
        self.__rentalDays = 0
    def getID(self):
        return self.__ID
    def getName(self):
        return self.__name
    def get_field(self,field):
        if field == 'ID':
            return self.getID()
        elif field == 'name':
            return self.getName()
        else:
            raise SearchError("This field is not searchable!")
    def getRentalDays(self):
        return self.__rentalDays
    def setID(self,other):
        self.__ID = other
    def setName(self,other):
        self.__name = other
    def addRentalDays(self,nr):
        self.__rentalDays += nr
    def subtractRentalDays(self,nr):
        self.__rentalDays -= nr
    def __eq__(self,other):
        return self.__ID == other.__ID
    def __str__(self):
        return "ID: " + str(self.__ID) + " - NAME: " + self.__name
    @staticmethod
    def readClient(line):
        parts = line.split(",")
        client = Client(int(parts[0].strip()),parts[1].strip())
        client.__rentalDays = int(parts[2].strip())
        return client
    @staticmethod
    def writeClient(client):
        return str(client.__ID)+","+client.__name+","+str(client.__rentalDays)
    @staticmethod
    def ClientToDict(client):
        return {'ID': client.__ID, 'name': client.__name,'rd':client.__rentalDays}
    @staticmethod
    def DictToClient(d):
        client = Client(d['ID'], d['name'])
        client.__rentalDays = d['rd']
        return client

class Rental:
    def __init__(self,rentalID,bookID,clientID,rentedDate,returnedDate):
        self.__ID = rentalID
        self.__bookID = bookID
        self.__clientID = clientID
        self.__rentedDate = rentedDate
        self.__returnedDate = returnedDate
    def getID(self):
        return self.__ID
    def getBookID(self):
        return self.__bookID
    def getClientID(self):
        return self.__clientID
    def getRentDate(self):
        return self.__rentedDate
    def getReturnDate(self):
        return self.__returnedDate
    def setReturnDate(self,other):
        self.__returnedDate = other
    def __eq__(self,other):
        return self.__ID == other.__ID
    def __str__(self):
        return "ID: " + str(self.__ID) + " ~ book ID: " + str(self.__bookID) + " ~ client ID: " + str(self.__clientID) + " ~ rented on: " + str(self.__rentedDate) + " ~ returned on: " + str(self.__returnedDate)
    @staticmethod
    def readRental(line):
        parts = line.split(",")
        dateParts = parts[3].strip().split('-')
        rentDate = datetime.date(int(dateParts[0]),int(dateParts[1]),int(dateParts[2]))
        retDate = parts[4].strip()
        if retDate == 'None':
            retDate = None
        else:
            dateParts = retDate.split('-')
            retDate = datetime.date(int(dateParts[0]),int(dateParts[1]),int(dateParts[2]))
        return Rental(int(parts[0].strip()), int(parts[1].strip()), int(parts[2].strip()), rentDate, retDate)
    @staticmethod
    def writeRental(rental):
        return str(rental.__ID) + "," + str(rental.__bookID) + "," + str(rental.__clientID) + "," + str(rental.__rentedDate) + "," + str(rental.__returnedDate)
    @staticmethod
    def RentalToDict(rental):
        return {'ID':rental.__ID,'bID':rental.__bookID,'cID':rental.__clientID,'rentDate':str(rental.__rentedDate).split('-'),'retDate':str(rental.__returnedDate).split('-')}
    @staticmethod
    def DictToRental(d):
        rentD = datetime.date(int(d['rentDate'][0]), int(d['rentDate'][1]), int(d['rentDate'][2]))
        if d['retDate'] == ['None']: retD = None
        else: retD = datetime.date(int(d['retDate'][0]), int(d['retDate'][1]), int(d['retDate'][2]))
        return Rental(int(d['ID']), int(d['bID']), int(d['cID']), rentD, retD)

class Settings:
    def __init__(self,settingsFileName):
        self.__file = open(settingsFileName,"r")
        self.__settings = self.__file.readlines()
        self.__file.close()
        if len(self.__settings) < 6:
            raise SettingsError("The settings file is incomplete!")

    def getRepos(self,*repos):
        if not len(repos):
            raise SettingsError("There are no given repositories!")
        repoType = self.__settings[0].split('=')[1].strip().rstrip('files')
        booksFile = self.__settings[1].split('=')[1].strip().strip('"')
        clientsFile = self.__settings[2].split('=')[1].strip().strip('"')
        rentalsFile = self.__settings[3].split('=')[1].strip().strip('"')
        if len(repos)>1 and repoType in ('txt', 'binary'):
            Books_Repository = repos[1](booksFile, Book.readBook, Book.writeBook, 'book', repoType)
            Clients_Repository = repos[1](clientsFile, Client.readClient, Client.writeClient, 'client', repoType)
            Rentals_Repository = repos[1](rentalsFile, Rental.readRental, Rental.writeRental, 'rental', repoType)
        elif len(repos)>2 and repoType in ('json','JSON'):
            Books_Repository = repos[2](booksFile,Book.BookToDict,Book.DictToBook,'book')
            Clients_Repository = repos[2](clientsFile,Client.ClientToDict,Client.DictToClient,'client')
            Rentals_Repository = repos[2](rentalsFile,Rental.RentalToDict,Rental.DictToRental,'rental')
        #add elif for more repos
        else:
            Books_Repository = repos[0]('book')
            Clients_Repository = repos[0]('client')
            Rentals_Repository = repos[0]('rental')
        return Books_Repository,Clients_Repository,Rentals_Repository

    def getEntries(self,*entriesGenerators):
        entries = self.__settings[5].split('=')[1].strip().strip('"')
        if entries in ('no','nope','false','none','',' ') or not len(entriesGenerators):
            return False
        return entriesGenerators[0]()

    def getUI(self,*UIs):
        if not len(UIs):
            raise SettingsError("There is no given UI!")
        UI = self.__settings[4].split('=')[1].strip().strip('"')
        if len(UIs)>1 and UI == 'GUI':
            return UIs[1]
        return UIs[0]

class SettingsError(Exception):
    pass

class RepoError(Exception):
    def __init__(self,msg):
        Exception.__init__(self,msg)

class UIError(Exception):
    pass

class RentalError(Exception):
    pass

class SearchError(Exception):
    pass

class UndoRedoError(Exception):
    pass