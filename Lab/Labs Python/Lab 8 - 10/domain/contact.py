'''
Created on Nov 20, 2017

@author: iuan
'''

class Contact:
    '''
    A Contact is composed of a name (string) and a telefone number (string)
    '''
    
    def __init__(self, n="", nr="" ):
        '''
        Constructs an instance of a class with a name and a phone number.
        IN: 2 strings 'n', 'nr'
        OUT: -
        CONDIS: len of 'nr' is 10 and contains only digits
        variable 'n' contains only letters and spaces
        '''
        if len(nr) != 10:
            raise Exception("Telephone number not valid!")
        #checking if nr is composed of digits
        self.__name = n
        self.__number = nr
        
    def getName(self):
        '''
        Returns the name of the called contact.
        '''
        return self.__name
    
    def getNumber(self):
        '''
        Returns the telephoen number of the called contact.
        '''
        return self.__number
    
    def setName(self, value):
        '''
        Sets the name of an instance of Contact.
        IN: a string 'value'
        OUT: an instance of Contact changed through reference parameter 'self'
        CONDIS: 'value' consists only of letters and spaces
        '''
        self.__name = value 
    
    def setNumber(self, value):
        '''
        Sets the name of an instance of Contact.
        IN: a string 'value'
        OUT: an instance of Contact changed through reference parameter 'self'
        CONDIS: 'value' consists only of digits
        '''
        if len(value) != 10:
            raise Exception("Telephone number not valid!")
        self.__number = value   
        
    def __str__(self):
        '''
        Returns the attributes of the class as strings in order to be printed.
        '''
        return self.__name + " " + self.__number    
        
        
        
        