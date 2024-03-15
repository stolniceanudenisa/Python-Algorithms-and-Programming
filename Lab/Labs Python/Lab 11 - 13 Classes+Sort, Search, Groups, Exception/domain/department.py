'''
Created on Nov 20, 2017

@author: iuan
'''
#from domain.patient import Patient

class Department:
    '''
    Composed of name, number, number of beds and list of class Patient.
    '''
    
    def __init__(self, n, nr, beds, pats):
        '''
        Initialization of the class.
        '''
        #name, number, number of beds,and list of patients
        self.__name = n
        self.__number = nr
        self.__nrBeds = beds
        self.__listPatients = pats
        
    def getName(self):
        '''
        Returns a variable of the class.
        '''
        return self.__name
    
    def getNumber(self):
        '''
        Returns a variable of the class.
        '''
        return self.__number
    
    def getNrBeds(self):
        '''
        Returns a variable of the class.
        '''
        return self.__nrBeds
    
    def getListPatients(self):
        '''
        Returns a variable of the class.
        '''
        return self.__listPatients
    
    def setName(self, value):
        '''
        Sets new value to a variable of the class.
        '''
        self.__name = value 
    
    def setNumber(self, value):
        '''
        Sets new value to a variable of the class.
        '''
        self.__number = value   
    
    def setNrBeds(self, value):
        '''
        Sets new value to a variable of the class.
        '''
        self.__nrBeds = value 
     
    def setListPatients(self, value):
        '''
        Sets new value to a variable of the class.
        '''
        self.__listPatients = value    
    
    def equal(self, p2):
        '''
        Checks if 2 Departments have the same attributes.
        IN: 2 instances of a class
        OUT: True if equal, else False
        CONDIS: -
        '''
        if self.getName() != p2.getName() or self.getNumber() != p2.getNumber():
            return False
        if self.getNrBeds() != p2.getNrBeds() or len(self.getListPatients()) != len(p2.getListPatients()):
            return False 
        for i in range( len(p2.getListPatients()) ):
            if self.getListPatients()[i].equal( p2.getListPatients()[i] ) == False:
                return False
        return True
          
    def __repr__(self):
        '''
        Returns the attributes of the class as strings in order to be printed.
        '''
        #name, number, number of beds,and list of patients
        res = "DEPARTMENT: "
        res += self.__name + "\nNo. " + str(self.__number)
        res += "\nNumber of beds: " + str(self.__nrBeds) 
        res += "\nPatients: \n"
        for el in self.getListPatients():
            res += "\t" + str(el) + "\n"
        return res
    
#
    def higherAgePatients(self, value):
        '''
        Computes how many patients in a department's list of patients has age higher than a given value.
        IN: a natural number
        OUT: a natural number
        CONDIS: value is positive
        '''
        res = 0
        for el in self.getListPatients():
            if el.getAge() > value:
                res += 1
        #print(self.getName(), " cu varstnici: ", res, "\n")
        return res
    
    def numberOfPatients(self):
        '''
        Returns how many patients are in a department.
        IN: -
        OUT: a positive number
        CONDIS: -
        '''
        return len(self.__listPatients)  
    
    def patsUnderAge(self, value):
        '''
        Returns how many patients are under given age in department.
        IN: a natural number
        OUT: an int
        CONDIS: value is positive
        '''
        res = 0
        for el in self.getListPatients():
            if el.getAge() < value:
                res += 1
        return res
    
    
class DepartmentException(Exception):
    '''
    Handles the errors appearing when working with class Patient.
    '''

    def __init__(self, message):
        self.__message = message
        
    def __str__(self):
        return self.__message      
        