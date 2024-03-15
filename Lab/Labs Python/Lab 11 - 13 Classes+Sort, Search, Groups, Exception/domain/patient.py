'''
Created on Nov 20, 2017

@author: iuan
'''
import datetime

class Patient:
    '''
    Composed of first name, last name, personal numerical code and disease
    '''
    #first name, last name, personal numerical code and disease
    
    def __init__(self, fn, ln, cnp, dis):
        '''
        Constructor
        '''
        self.__firstName = fn
        self.__lastName = ln
        self.__cnp = cnp
        self.__disease = dis
    
    def getFirstName(self):
        '''
        Returns a variable of the class.
        '''
        return self.__firstName
    
    def getLastName(self):
        '''
        Returns a variable of the class.
        '''
        return self.__lastName
    
    def getCnp(self):
        '''
        Returns a variable of the class.
        '''
        return self.__cnp
    
    def getDisease(self):
        '''
        Returns a variable of the class.
        '''
        return self.__disease    
    
    def setFirstName(self, value):
        '''
        Sets new value to a variable of the class.
        '''
        self.__firstName = value
    
    def setLastName(self, value):
        '''
        Sets new value to a variable of the class.
        '''
        self.__lastName = value
    
    def setCnp(self, value):
        '''
        Sets new value to a variable of the class.
        '''
        self.__cnp = value
    
    def setDisease(self, value):
        '''
        Sets new value to a variable of the class.
        '''
        self.__disease = value
    
    def equal(self, p2):
        '''
        Checks if 2 Patients have the same attributes.
        IN: 2 instances of a class
        OUT: True if equal, else False
        CONDIS: -
        '''
        if self.getFirstName() != p2.getFirstName() or self.getLastName() != p2.getLastName():
            return False
        if self.getCnp() != p2.getCnp() or self.getDisease() != p2.getDisease():
            return False
        return True
    
    def __repr__(self):
        '''
        Returns the attributes of the class as strings in order to be printed.
        '''
        #first name, last name, cnp, disease
        return self.__firstName + " " + self.__lastName + " " + self.__cnp + " " + self.__disease +"" 
    
#untested  
    def getAge(self):
        '''
        Computes age of person if age is less than 101.
        IN: -
        OUT: integer
        CONDIS:
        '''
        #year = 2017
        year = datetime.date.today().year
        dif = year - 2000
        s = self.getCnp() #string cnp
        birth = int(s[2]) + 10*int(s[1])
        if birth <= dif:
            #its been born this millenia
            birth = 2000 + birth
        else:
            birth = 1900 + birth
        
        res = year - birth
        if res < 0:
            raise PatientException("Age is negative!") 
        return res

class PatientException(Exception):
    '''
    Handles the errors appearing when working with class Patient.
    '''

    def __init__(self, message):
        self.__message = message
        
        
    def __str__(self):
        return self.__message

