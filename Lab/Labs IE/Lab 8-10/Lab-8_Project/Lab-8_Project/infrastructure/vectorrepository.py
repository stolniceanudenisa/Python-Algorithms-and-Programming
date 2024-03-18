'''
Created on Nov 17, 2020

@author: Sergiu Ciubotariu
'''
from domain.myvector import MyVector

class VectorRepository():
  
    def __init__(self):
        '''
        Constructor
        '''
        self.__data = []
    
    def getData(self):
        return self.__data
    
    def addVector(self, vector):
        '''
        Adds a vector to the repository 
        Input: vector - object of type MyVector
        '''
        self.__data.append(vector)
    
    def returnVectorAtIndex(self, index):
        '''
        Returns a vector at the index
        '''
        return self.__data[index]
    
    def updateVectorAtIndex(self, index, ni, c, t, v):
        '''
        Updates a vector
        Input : ni - new name id
            c - new colour
            t - new type
            v - new values
            index - the index of the vector that needs to be modified
        '''
        self.__data[index].set_name_id(ni)
        self.__data[index].set_colour(c)
        self.__data[index].set_type(t)
        self.__data[index].set_values(v)
        
    def updateVectorByName_Id(self, ni, c, t, v):
        '''
        Updates a vector
        Input : ni - the name id for the vector to be identified
            c - new colour
            t - new type
            v - new values
        '''
        for elem in self.__data:
            if elem.get_name_id() == ni:
                elem.set_colour(c)
                elem.set_type(t)
                elem.set_values(v)
        
    def deleteVectorByIndex(self, index):
        '''
        Deletes a vector at the given index
        Input: index - the given index
        '''
        del self.__data[index]
    
    def deleteVectorByName_Id(self, ni):
        '''
        Deletes a vector identified by name_id
        Input: ni - the name_id
        '''
        for elem in self.__data:
            if elem.get_name_id() == ni:
                self.__data.remove(elem)
                
    def sumOfElementsOfAllVectors(self):
        '''
        NEW
        Returns the sum of the elements of every vector
        Output : result - the sum
        '''
        result = 0
        for elem in self.__data:
            result += elem.sumOfElements()
        return result
        
    def sumOfAllVectors(self):
        '''
        NEW
        Returns a list of values 
        '''
        vector = MyVector("", "", 0, [0,0,0])
        for elem in self.__data:
            vector.addVectorToVector(elem)
        return vector
    
    def listOfVectorsBySum(self, s):
        '''
        NEW
        Returns a list of vectors which have a given sum
        Input: s - the sum
        Output: result - the list
        '''
        result = []
        for elem in self.__data:
            if elem.sumOfElements() == s:
                result.append(elem)
        return result
    
    def listOfVectorsMinLessThan(self, less):
        '''
        NEW
        Returns a list of vectors which have min less than a given value
        Input: less - the comparing variable
        Output: result - the list 
        '''
        result = []
        for elem in self.__data:
            if elem.minOfAVector() < less:
                result.append(elem)
        return result
    
    
    
        
        
        