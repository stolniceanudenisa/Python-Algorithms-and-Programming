'''
Created on Dec 5, 2017

@author: iuan
'''
from domain.city import City

class CityRepository():
    '''
    A list with cities and operations on it.
    '''
    def __init__(self):
        '''
        Constructs a repository storagin cities within a list of instances.
        '''
        self.__data = []
    
    def addNew(self, n, pop):
        '''
        Adds new city.
        '''
        if pop < 0:
            raise Exception("Adding population value is negative!")
        
        c = City(n, pop)
        self.__data.append(c)
    
    def get(self, index):
        '''
        Returns an object 'City' from the list from a given index.
        IN: a natural number 'index'
        OUT: an object of type class City from the list
        CONDIS: index >=0 and index < length of list
        '''
        if index < 0 or index >= len(self.__data):
            raise ValueError("Index out of range!")
        return self.__data[index]
    
    
    def getAll(self):
        '''
        Returns the list of cities.
        '''
        return self.__data
        
    def totalPopulationRepo(self, letter):
        '''
        Computes the sum of pop size of cities starting with given letter.
        IN: a char
        OUT: a natural number
        CONDIS: 'letter' is char
        '''
        ok = False # there is no city with letter
        sum1 = 0
        for elem in self.__data:
            if elem.firstLetter() == letter:
                sum1 += elem.getPopulation()
                ok = True
                
        if ok==False:
            raise Exception("There is no such city with given letter!")
        
        return sum1          
    
    def delHigherThan(self, value):
        '''
        Removes from the repository all elements with pop size higher than given value.
        IN: a natural number
        OUT: a repository of cities with lesser elements
        CONDIS: value is positive
        '''    
        if value < 0:
            raise Exception("Value given is negative!")
        
        for i in range( len(self)-1 , -1, -1):
            if self.get(i).getPopulation() > value:
                #must be removed
                del self.__data[i]  
                
        return self
        
    def __len__(self):
        '''
        Returns how many cities.
        IN: -
        OUT: a number
        '''
        return len(self.__data)
    
    def __str__(self):
        '''
        String representation of repository.
        OUT: a string
        '''
        s = ""
        for elem in self.__data:
            s += "[" + elem.getName() + " " + str(elem.getPopulation()) + "], "
        s += "\n"
        return s