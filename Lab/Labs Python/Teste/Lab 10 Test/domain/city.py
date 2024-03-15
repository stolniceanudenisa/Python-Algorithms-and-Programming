'''
Created on Dec 5, 2017

@author: iuan
'''

class City():
    '''
    A city is composed of a name and a population size.
    '''
    def __init__(self, n, p):
        '''
        Constructor
        '''
        if p<0:
            raise ValueError("Population negative!")
        
        self.__name = n
        self.__population = p
        
    def getName(self):
        '''
        Returns name of city.
        '''
        return self.__name
    
    def getPopulation(self):
        '''
        Returns population size of city.
        '''
        return self.__population
    
    def setName(self, value):
        '''
        Sets new value to the name of the city.
        '''
        self.__name = value
        
    def setPopulation(self, value):
        '''
        Sets new value to the population of the city.
        '''
        if value < 0:
            raise Exception("Setting population negative!")
        self.__population = value
        
    def firstLetter(self):
        '''
        Returns the first letter from name.
        IN: - 
        OUT: a char
        '''
        return self.getName()[0]
    
    def __str__(self):
        '''
        The string representation of the class.
        '''
        return self.getName() + " population size:" + str(self.getPopulation())