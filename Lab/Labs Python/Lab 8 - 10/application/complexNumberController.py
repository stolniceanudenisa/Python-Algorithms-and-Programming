'''
Created on Nov 21, 2017

@author: iuan
'''
from infrastructure.complexNumberRepository import ComplexNumberRepository

class ComplexNumberController:
    '''
    Handles different operations on a repository of complex numbers.
    cn = complex number
    '''

    def __init__(self, repository):
        '''
        Initializes with a class composed of a list and operations on the list
        and a list '__undo' that stores the previous version of the list from repo
        IN: a class 'complexNumberRepository'
        OUT: -
        CONDIS: -
        '''
        self.__repo = repository
        self.__undo = []
    
    def addNew(self, cn):
        '''
        Appends a new complex number to the repo.
        '''
        self.__undo = self.__repo.getAll()[:]
        self.__repo.addComplexNumber(cn)
    
    def default(self, fis):
        '''
        Adds all the complex numbers from a file into a repository.
        IN: a string with multilines
        OUT: -
        CONDIS: -
        '''
        s = fis.split("\n")
        for el in s:
            self.addNew( self.__repo.toComplex(el)  )
    
    def cartesianFormCommand(self):
        '''
        Returns a list with strings.
        '''
        return self.__repo.cartesianFormRepo()
    
    def polarFormCommand(self):
        '''
        Returns a list with strings.
        '''
        return self.__repo.polarFormRepo() 
        
    def conjugateCommand(self):
        '''
        Returns a list with complex nums.
        '''
        return self.__repo.conjugateRepo()
        
    def mulByRealCommand(self, value):
        '''
        Returns a list with complex nums.
        '''
        return self.__repo.mulByRealRepo(value)
     
    def mulByImaginaryCommand(self, value):
        '''
        Returns a list with complex nums.
        '''
        return self.__repo.mulByImaginaryRepo(value)
    
    def sumCommand(self, c1):
        '''
        Returns a list with complex nums.
        '''
        return self.__repo.sumRepo(c1)    
    
    def prodCommand(self, c1):
        '''
        Returns a list with complex nums.
        '''
        return self.__repo.prodRepo(c1)
        
        
    def matrixCommand(self):
        '''
        Returns a list with complex nums.
        '''
        return self.__repo.matrixRepo()      
     
    def powerCommand(self, p):
        '''
        Returns a list with complex nums.
        '''
        return self.__repo.powerRepo(p) 
     
    def squareRootCommand(self):
        '''
        Returns a list with complex nums.
        '''
        return self.__repo.squareRootRepo()
    
    def exponentialCommand(self):
        '''
        Returns a list with complex nums.
        '''
        return self.__repo.exponentialRepo() 
     
     
     
        
    def removeByIndex(self, index):
        if index < 0 or index >= len(self.__repo):
            raise Exception("Index out of range!")
        
        self.__undo = self.__repo.getAll()[:]
        self.__repo.deleteByIndex(index)
    
    def showRepo(self):
        '''
        Prints on screen each complex nr from the repository.
        '''
        res = "The repository is:" + str(self.__repo) + "\n"
        return res
        
    def undo(self):
        if len(self.__undo) != 0:
            self.__repo.clearAll()
        
        for i in range(len(self.__undo)):
            self.__repo.addContact(self.__undo[i])
    
        
