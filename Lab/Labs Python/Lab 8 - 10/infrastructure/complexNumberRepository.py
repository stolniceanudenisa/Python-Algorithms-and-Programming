'''
Created on Nov 21, 2017

@author: iuan
'''
from domain.complexNumber import ComplexNumber

class ComplexNumberRepository:
    '''
    A collection of objects 'ComplexNumber'.
    '''
    #Create, Read, Update, Delete
    
    def __init__(self):
        '''
        Each instance of the class will have a list of objects
        '''
        self.__data = []
    
    #c = complex number
    def addComplexNumber(self, c):
        '''
        Increments the length of the list __data and adds a new complex number at the end of the list.
        IN: a 'ComplexNumber'
        OUT: -
        CONDIS: -
        '''
        self.__data.append(c)
    
    def cartesianFormRepo(self):
        '''
        Returns the cartesian form of each element from the list.
        in: -
        out: a list with complex numbers
        condis: -
        '''
        res = []
        for elem in self.__data:
            res.append( elem.cartesianForm() )
        return res
            
    def polarFormRepo(self):
        '''
        Returns the polar form of each element from the list.
        in: -
        out: a list with complex numbers
        condis: -
        '''
        res = []
        for elem in self.__data:
            res.append(elem.polarForm())
        return res
    
    def conjugateRepo(self):
        '''
        Returns the conjugate of each element from the list.
        in: -
        out: a list with complex numbers
        condis: -
        '''
        res = []
        for elem in self.__data:
            res.append(elem.conjugate())
        return res
    
    def mulByRealRepo(self, value):
        '''
        Returns the product of each element from the list with value.
        in: a real number
        out: a list with complex numbers
        condis: -
        '''
        res = []
        for elem in self.__data:
            res.append( elem.multiplyByReal(value) )
        return res
    
        
    def mulByImaginaryRepo(self, value):
        '''
        Returns the product of each element from the list with value.
        in: an imaginary number
        out: a list with complex numbers
        condis: - 
        '''
        res = []
        for elem in self.__data:
            res.append(elem.multiplyByImaginary(value))
        return res
    
    def sumRepo(self, c1):
        '''
        Returns the sum of each element from the list with c1.
        in: a complex number
        out: a list with complex numbers
        condis: -
        '''
        res = []
        for elem in self.__data:
            res.append( elem.sumComplexNumbers(c1) )
        return res    
        
    def prodRepo(self, c1):
        '''
        Returns the product of each element from the list with c1.
        in: a complex number
        out: a list with complex numbers
        condis: -
        '''
        res = []
        for elem in self.__data:
            res.append( elem.prodComplexNumbers(c1) )
        return res
     
    def matrixRepo(self):
        '''
        Returns the matrix representation of each element from the list.
        in: -
        out: a list with complex numbers
        condis: -
        '''
        res = []
        for elem in self.__data:
            res.append(elem.matrix())
        return res    
    
    def powerRepo(self, p):
        '''
        Raises each element at power p and return a list with complex numbers.
        in: an integer p
        out: a list with complex numbers
        condis: p is positive and not float
        '''
        res = []
        for elem in self.__data:
            res.append(elem.power(p))
        return res 
     
    def squareRootRepo(self):
        '''
        Returns the square root of each element from the list.
        in: -
        out: a list with complex numbers
        condis: -
        '''
        res = []
        for elem in self.__data:
            res.append(elem.squareRoot())
        return res
     
    def exponentialRepo(self):
        '''
        Returns the exponential of each element from the list.
        in: -
        out: a list with complex numbers
        condis: -
        '''
        res = []
        for elem in self.__data:
            res.append(elem.exponential())
        return res 
     
     
        
    def updateComplexNumber(self, index, c):
        '''
        Changes an existing object with a new 'c' at a given index in the list.
        IN: a natural number 'index', a 'ComplexNumber'
        OUT: -
        CONDIS: index >=0 and index < length of list
        '''
        if index < 0 or index >= len(self.__data):
            raise ValueError("Index out of range!")
        
        self.__data[index] = c
        
    def deleteByIndex(self, index):
        '''
        Removes an object 'c' from the list '__data' from a given index.
        IN: a natural number 'index'
        OUT: -
        CONDIS: index >=0 and index < length of list
        '''
        if index < 0 or index >= len(self.__data):
            raise ValueError("Index out of range!")    
        
        del self.__data[index]
        
                   
    def getAll(self):
        '''
        Returns the list of objects 'ComplexNumber'.
        IN: -
        OUT: a list with objects
        CONDIS: -
        '''
        return self.__data
    
    def get(self, index):
        '''
        Returns an object 'ComplexNumber' from the list from a given index.
        IN: a natural number 'index'
        OUT: an object of type class ComplexNumber from the list
        CONDIS: index >=0 and index < length of list
        '''
        if index < 0 or index >= len(self.__data):
            raise ValueError("Index out of range!")
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
    
    def __str__(self):
        '''
        Returns the visual representation of the list of complex numbers as a string.
        '''
        res = ""
        for elem in self.__data:
            res += "[ " + str(elem) + " ]" + ", "
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
        except Exception:
            print(s)
            raise Exception("String to number contains unconvertable characters!")
    
    def toComplex(self, s):
        '''
        Transforms a string into a complex number.
        IN: a single line string
        OUT: a complex number
        CONDIS: s contains only digits, dot, minus, plus and i character
        '''
        #+conditie daca mai contine si altceva -> raise exception!!
        if s.find('i') == -1:
            raise Exception("The string from file doesn't contain character 'i'!")
        real = 1
        imag = 1
        #-34.6-49.6i
        if s[0] == "-":
            real = -1
            i = 1  #iterates through string s
        else:
            real = 1
            i = 0
        
        first = ""
        second = ""   
        while (s[i]!='-' and s[i]!='+'):
            first += s[i]
            i += 1
        
        if s[i]=='-':#check if imag is negative
            imag = -1
        i+=1
        while s[i]!='i' or i == len(s):
            second += s[i]
            i += 1
        
        real = ComplexNumberRepository.strToNum(first)*real
        imag = ComplexNumberRepository.strToNum(second)*imag
        return ComplexNumber(real, imag)
    
# repo = ComplexNumberRepository()
# print(repo.strToNum("3+4j"))    
#     