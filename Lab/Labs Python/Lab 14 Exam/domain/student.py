'''
Created on Jan 16, 2018

@author: iuan
'''
from domain.studentException import StudentException

class Student:
    '''
    composed of name, grade and group
    '''

    def __init__(self, n, gr, gro):
        '''
        Constructor
        '''
        self.__name = n
        self.__grade = gr
        self.__group = gro
        
    def getName(self):
        '''
        getter method for object studdent
        '''
        return self.__name
    
    def getGrade(self):
        '''
        getter method for object studdent
        '''
        return self.__grade
    
    def getGroup(self):
        '''
        getter method for object studdent
        '''
        return self.__group
    
    def setName(self, v):
        '''
        setter method for object studdent
        '''
        self.__name = v
        
    def setGrade(self, v):
        '''
        setter method for object studdent
        '''
        if v < 0:
            raise StudentException("Grade not valid")
        self.__grade = v
        
    def setGroup(self, v):
        '''
        setter method for object studdent
        '''
        if v!=811 and v!=812:
            raise StudentException("Group not valid")
        
        self.__group = v
        
    def __str__(self):
        '''
        string repsentation
        '''
        s = ""
        s += self.getName() + " " + str(self.getGrade()) + " " + str(self.getGroup()) + "\n" 
        return s   

    