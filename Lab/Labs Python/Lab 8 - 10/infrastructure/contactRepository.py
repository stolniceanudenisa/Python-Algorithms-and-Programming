'''
Created on Nov 20, 2017

@author: iuan
'''
from domain.contact import Contact

class ContactRepository:
    '''
    A list that contains instances of class Contact.
    '''

    def __init__(self):
        '''
        Each instance of the class will have a list of objects Contact
        '''
        self.__data = []
    
    def addContact(self, c):
        self.__data.append(c)
        
    def updateContact(self, index, c):
        if index < 0 or index >= len(self.__data):
            raise ValueError("Index out of range!")
        self.__data[index] = c
        
    def deleteByIndex(self, index):
        if index < 0 or index >= len(self.__data):
            raise ValueError("Index out of range!")    
        
        del self.__data[index]
        
    def deleteByNumber(self, number):
        for i in range(len(self.__data)):
            if self.__data[i].getNumber() == number:
                del self.__data[i]
                break
                   
    def getAll(self):
        return self.__data
    
    def get(self, index):
        if index < 0 or index >= len(self.__data):
            raise ValueError("Index out of range!")
        return self.__data[index]
    
    def findByNum(self, number):
        '''
        '''
        for elem in self.__data:
            if elem.getNumber() == number:
                return elem
        return None
    
    def findByName(self, name):
        res = []
        for elem in self.__data:
            if elem.getName() == name:
                res.append(elem)
        return res
    
    def clearAll(self):
        self.__data.clear()
    
    def __len__(self):
        return len(self.__data)
    
    def __str__(self):
        '''
        Returns the visual representation of the list of contacts as a string.
        '''
        res = ""
        for elem in self.__data:
            res += str(elem) + "\n"
        return res
    
    
    
