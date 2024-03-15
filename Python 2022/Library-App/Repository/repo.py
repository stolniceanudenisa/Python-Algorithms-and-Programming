import random
#import names
import pickle
import json
from Domain.entities import *

class Repo:
    def __init__(self,objName):
        self._objList = []
        self._RepoName = objName
    def getAll(self):
        return self._objList[:]
    def size(self):
        return len(self._objList)
    def getObj(self,ID):
        for obj in self._objList:
            if obj.getID() == ID:
                return obj
        raise RepoError("The {} with this ID does not exist!".format(self._RepoName))
    def add(self,obj):
        if obj in self._objList:
            raise RepoError("This {} is already stored!".format(self._RepoName))
        self._objList.append(obj)
    def remove(self,obj):
        if obj not in self._objList:
            raise RepoError("The {} you want to remove is not in the list!".format(self._RepoName))
        self._objList.remove(obj)
    def update(self,obj,newObj):
        if obj not in self._objList:
            raise RepoError("The {} you want to update is not in the list!".format(self._RepoName))
        index = self._objList.index(obj)
        self._objList[index] = newObj
    def cleanRepo(self):
        self._objList.clear()
    def AddRepo(self,objects):
        if len(self._objList):
            raise RepoError("Can't generate entries - the repository is not empty!")
        self._objList = [obj for obj in objects]
    def addObjects(self,objects):
        for obj in objects:
            self.add(obj)
    def removeObjects(self,objects):
        for obj in objects:
            self.remove(obj)

class FileRepo(Repo):

    def __init__(self, filename, read_object, write_object, objName, fileType):
        self.__filename = filename
        self.__read_object = read_object
        self.__write_object = write_object
        Repo.__init__(self,objName)
        self.__fType = fileType
        self.__fileOp = {'txt': (self.__read_all_from_file,self.__write_all_to_file),
                  'binary': (self.__read_all_from_binary_file,self.__write_all_to_binary_file)}
        self.__fileOp[self.__fType][0]()

    def __read_all_from_binary_file(self):
        self._objList = []
        f = open(self.__filename,"rb")
        try:
            self._objList = pickle.load(f)
        except EOFError:
            """
                This is raised if input file is empty
            """
            f.close()
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occurred - " + str(e))
            raise e
        f.close()
    def __write_all_to_binary_file(self):
        f = open(self.__filename,"wb")
        pickle.dump(self._objList,f)
        f.close()

    def __read_all_from_file(self):
        self._objList = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    obj = self.__read_object(line)
                    self._objList.append(obj)
        f.close()
    def __write_all_to_file(self):
        with open(self.__filename, "w") as f:
            for obj in self._objList:
                line = self.__write_object(obj)
                f.write(line + "\n")
        f.close()

    def updateRepoFile(self):
        self.__fileOp[self.__fType][1]()

    def add(self, obj):
        Repo.add(self, obj)
        self.updateRepoFile()
    def update(self,obj,newObj):
        Repo.update(self, obj,newObj)
        self.updateRepoFile()
    def remove(self,obj):
        Repo.remove(self, obj)
        self.updateRepoFile()
    def cleanRepo(self):
        Repo.cleanRepo(self)
        self.updateRepoFile()
    def AddRepo(self,objects):
        Repo.AddRepo(self,objects)
        self.updateRepoFile()

class JSONFileRepo(Repo):

    def __init__(self, filename,objAsDict,dictAsObj, objName):
        self.__filename = filename
        self.__objAsDict = objAsDict
        self.__dictAsObj = dictAsObj
        Repo.__init__(self,objName)
        self.__read_all_from_json_file()

    def __read_all_from_json_file(self):
        dictList = []
        with open(self.__filename,'r') as f:
            try:
                dictList = json.load(f)
            except ValueError: pass
        f.close()
        for d in dictList:
            self._objList.append(self.__dictAsObj(d))
    def __write_all_to_json_file(self):
        objectsD = []
        for obj in self._objList:
            objectsD.append(self.__objAsDict(obj))
        with open(self.__filename,"w") as f:
            json.dump(objectsD,f)
        f.close()

    def updateRepoFile(self):
        self.__write_all_to_json_file()

    def add(self, obj):
        Repo.add(self, obj)
        self.updateRepoFile()
    def update(self,obj,newObj):
        Repo.update(self, obj,newObj)
        self.updateRepoFile()
    def remove(self,obj):
        Repo.remove(self, obj)
        self.updateRepoFile()
    def cleanRepo(self):
        Repo.cleanRepo(self)
        self.updateRepoFile()
    def AddRepo(self,objects):
        Repo.AddRepo(self,objects)
        self.updateRepoFile()

class RepoUndoRedo:
    """
    undo/redo for add book/client, remove book/client, update book/client, rent/return book
    """
    def __init__(self):
        self.__opHistory = []
        self.__stackPointer = -1
    def addOperation(self,operation):
        #delete the operations left to redo
        if len(self.__opHistory[self.__stackPointer+1:]):
            del self.__opHistory[self.__stackPointer+1:]
        #add the new operation
        self.__opHistory.append(operation)
        self.__stackPointer += 1
    def getPreviousOperation(self):
        if self.__stackPointer < 0:
            raise UndoRedoError("There are no previous operations!")
        self.__stackPointer -= 1
        return self.__opHistory[self.__stackPointer+1]
    def getPreviousUndoneOp(self):
        if not len(self.__opHistory[self.__stackPointer+1:]):
            raise UndoRedoError("You have reached the redo limit!")
        self.__stackPointer += 1
        return self.__opHistory[self.__stackPointer]
    def getOpHistory(self):
        return self.__opHistory

class EntriesGenerator:
    def __init__(self):
        self.__generatedBooks = []
        self.__generatedClients = []
        self.__generatedRentals = []
        self.generateBooks()
        self.generateClients()
        self.generateRentals(self.getGeneratedBooks(),self.getGeneratedClients())

    def getGeneratedBooks(self):
        return self.__generatedBooks[:]
    def getGeneratedClients(self):
        return self.__generatedClients[:]
    def getGeneratedRentals(self):
        return self.__generatedRentals[:]

    def generateBooks(self):
        f = open("RepoFiles/BookEntries.txt", "r")
        lines = f.readlines()
        f.close()
        IDs = [i for i in range(1000,9000)]
        random.shuffle(IDs)
        for i in range(100):
            book_index = random.randrange(0, 200, 2)
            title = lines[book_index].strip().casefold().title()
            author = lines[book_index+1][3:].strip()
            self.__generatedBooks.append(Book(IDs[i],title,author))
    def generateClients(self):
        IDs = [i for i in range(1,900)]
        random.shuffle(IDs)
        for i in range(12):
            self.__generatedClients.append(Client(IDs[i],names.get_full_name()))
        return self.__generatedClients
    def generateRentals(self,books,clients):
        random.shuffle(books)
        random.shuffle(clients)
        for i in range(1,21):
            client = random.choice(clients)
            book = random.choice(books)
            book.incrementTimesRented()
            rentDate = datetime.date(random.randint(1999,2020), random.randint(1,12), random.randint(1,28))
            retDate = random.choice((None,datetime.date(random.randint(rentDate.year,rentDate.year+1), random.randint(rentDate.month,12), random.randint(rentDate.day,28))))
            if retDate is None:
                book.setAvailability(False)
                books.remove(book)
            else:
                difference = retDate - rentDate
                client.addRentalDays(int(difference.days))
            self.__generatedRentals.append(Rental(i,book.getID(),client.getID(),rentDate,retDate))