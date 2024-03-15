'''
Created on Nov 21, 2017

@author: iuan
'''
#from domain.patient import Patient

class PatientRepository:
    '''
    Composed of a list of objects.
    '''
    
    def __init__(self):
        '''
        Each instance of the class will have a list of objects Patient
        '''
        self.__data = []
    #first name, lastname, personal numerical code and disease
    
    #CREATE
    def addNew(self, m):
        '''
        Adds new instance of a class in the repository.
        IN: an instance class
        OUT: -
        CONDIS: no other instance with same Cnp
        '''
        if self.findByCnp( m.getCnp() ) == None:
            self.__data.append(m)
        else:
            raise PatientRepositoryException("This patient exists already!")
    
    #READ
    def findByIndex(self, index):
        '''
        Reads a specific element from the list and returns it.
        IN: a number
        OUT: an instance class
        CONDIS: index is positive and less than length
        '''
        if index < 0 or index >= len(self.__data):
            raise PatientRepositoryException("Index out of range!")
        return self.__data[index]
    
    #helps at AddNew, inexistent in controller
    def findByCnp(self, cnp):
        '''
        Reads a specific element from the list and returns it.
        IN: a string
        OUT: an instance class or None if doesn't exist
        CONDIS: - 
        '''
        for elem in self.__data:
            if elem.getCnp() == cnp:
                return elem
        return None
        raise PatientRepositoryException("The searched Patient doesn't exist!")
    
    #UPDATE
    def updatePatientByIndex(self, index, d):
        '''
        Replaces element from given index in repo.
        IN: a number, an instance class
        OUT: -
        CONDIS: index is positive and less than length of repo
        '''
        if index < 0 or index >= len(self.__data):
            raise PatientRepositoryException("Index out of range!")
        self.__data[index] = d
     
    #DELETE        
    def deleteByIndex(self, index):
        '''
        Removes an element at a given index.
        IN: a number
        OUT: -
        CONDIS: index is positive and less than length of repo
        '''
        if index < 0 or index >= len(self.__data):
            raise PatientRepositoryException("Index out of range!")    
        del self.__data[index]
 
    #inexistent in controller
    def updatePatientByCnp(self, cnp, f, l , dis):
        '''
        Update
        '''
        for el in self.__data:
            if el.getCnp() == cnp:
                el.setFirstName(f)
                el.setLastName(l)
                el.setDisease(dis)
                break
               
    def getAll(self):
        '''
        Returns the list of objects from repository.
        IN: -
        OUT: a list with objects
        CONDIS: -
        '''
        return self.__data
    
    def get(self, index):
        '''
        Returns an object from the repository at a given index.
        IN: a natural number 'index'
        OUT: an object of type class Patient from the list
        CONDIS: index >=0 and index < length of list
        '''
        if index < 0 or index >= len(self.__data):
            raise PatientRepositoryException("Index out of range!")
        return self.__data[index]
    
    def clearAll(self):
        '''
        Makes the list '__data' empty without any element.
        IN: -
        OUT: -
        CONDIS: -
        '''
        self.__data.clear()
    
    def __len__(self):
        '''
        Returns the length of the list.
        IN: -
        OUT: a positive number
        CONDIS: -
        '''
        return len(self.__data)
    
    def __repr__(self):
        '''
        Returns the representation of the list of patients.
        IN: -
        OUT: -
        CONDIS: -
        '''
        res = ""
        for elem in self.__data:
            res += "[ " + str(elem) + " ]" + ",\n"
        return res
    
    def __str__(self):
        '''
        Returns the visual representation of the list of patients as a string.
        IN: -
        OUT: -
        CONDIS: -
        '''
        res = ""
        for elem in self.__data:
            res += "[ " + str(elem) + " ]" + ",\n"
        return res
        
    @staticmethod
    def strToNum(s):
        '''
        Transforms a string into an integer or float number.
        IN: a string 's'
        OUT: an int or a float
        CONDIS: s contains only digits and dot char '.'
        '''
        try:
            res = 0
            try:
                res = int(s)
            except ValueError:
                res = float(s)
            return res
        except PatientRepositoryException:
            print(s)
            raise PatientRepositoryException("String to number contains unconvertable characters!")
    
class PatientRepositoryException(Exception):
    
    def __init__(self, message):
        self.__message = message
        
    def __str__(self):
        return self.__message    
    