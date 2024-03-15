'''
Created on Nov 20, 2017

@author: iuan
'''
from infrastructure.contactRepository import ContactRepository

class ContactController(object):
    '''
    classdocs
    '''

    def __init__(self, repository):
        '''
        Constructor
        '''
        self.__repo = repository
        self.__undo = []
    
    def addContact(self, contact):
        self.__undo = self.__repo.getAll()[:]
        self.__repo.addContact(contact)
        
    def removeBy(self, index):
        if index < 0 or index >= len(self.__repo):
            raise Exception("Index out of range!")
        
        self.__undo = self.__repo.getAll()[:]
        self.__repo.delByIndex(index)
        
    def undo(self):
        if len(self.__undo) != 0:
            self.__repo.clearAll()
        
        for i in range(len(self.__undo)):
            self.__repo.addContact(self.__undo[i])
    
        
