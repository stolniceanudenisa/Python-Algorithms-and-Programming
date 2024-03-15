'''
Created on Nov 20, 2017

@author: iuan
'''
import math
import numpy as np

class ComplexNumber(object):
    '''
    A complex number is composed of a real and imaginary part (2 real numbers).
    i^2 = -1
    '''

    def __init__(self, r = 0, i = 0):
        '''
        Constructor
        '''
        #Value error if they are chars
        self.__realPart = r
        self.__imaginaryPart = i
        
    def getReal(self):
        '''
        Returns the real part of a complex number.
        IN: -
        OUT: -
        CONDIS: -
        '''
        return self.__realPart
    
    def getImaginary(self):
        '''
        Returns the real part of a complex number.
        IN: -
        OUT: -
        CONDIS: -
        '''
        return self.__imaginaryPart
    
    def setReal(self, value):
        '''
        Replaces the real part of a complex number with a given value.
        IN: value - an integer
        OUT: -
        CONDIS: - 
        '''
        self.__realPart = value
    
    def setImaginary(self, value):
        '''
        Replaces the imaginary part of a complex number with a given value.
        IN: value - an integer
        OUT: -
        CONDIS: - 
        '''
        self.__imaginaryPart = value
        
    def __str__(self):
        '''
        Returns the attributes of the class as strings in order to be printed.
        '''
        sign = "+"
        if self.__imaginaryPart < 0:
            sign = ""
        
        return str(self.__realPart) + sign + str(self.__imaginaryPart) + "i"
    
    def cartesianForm(self):
        '''
        Returns a string representing the cartesian form.
        IN: -
        OUT: a string
        CONDIS: - 
        '''
        res = str(self)
        res += "  ---> real = " + str(self.getReal()) + ", imaginary = " + str(self.getImaginary()) + "\n"
        return res
    
    def modulus(self):
        '''
        Returns the modulus of a complex number.
        IN: -
        OUT: a real number equal to square root of a square plus b square
        CONDIS: -
        '''
        a = self.__realPart
        b = self.__imaginaryPart
        return round( math.sqrt(a*a + b*b), 2)
    
    def argument(self):
        '''
        Returns the argument of a complex number.
        IN: -
        OUT: a real number equal to arctg(b/y), the angle in radians!
        CONDIS: - 
        '''
        a = self.__realPart
        b = self.__imaginaryPart
        return round( math.atan(b/a), 2)
    
    def polarForm(self):
        '''
        Transforms a complex number into its polar form.
        IN: -
        OUT: a string 's' representing the polar form
        CONDIS: -
        '''
        #If c1 = 3 + 4i, then modulus = 5 and argument = 53.13⁰ (or
        #0.93 radians) or c1 = 5(cos( 53.13⁰ ) + i sin( 53.13⁰ ))
        s = ""
        m = str( float(self.modulus()) )
        
        arg = str( round( self.argument() * 180 / math.pi, 2) ) #convert radians to degrees
        
        s += m
        s += "(cos( " + arg + " ) + i sin( " + arg + " ))"
        return s
    
    def conjugate(self):
        '''
        Transforms the instance of a complex number in its conjugate = negating the imaginary part.
        IN: -
        OUT: a ComplexNumber 's' with imaginary part negated
        CONDIS: - 
        '''
        s = ComplexNumber( self.__realPart, self.__imaginaryPart * (-1) )
        return s
    
    def multiplyByReal(self, value):
        '''
        Multiplies the complex number by a given real number 'value'.
        Changes the parameter self. (pass by reference)
        IN: a real number
        OUT: a ComplexNumber changed
        CONDIS: -
        '''
        s = ComplexNumber( self.__realPart * value, self.__imaginaryPart * value)
        return s
        
    def multiplyByImaginary(self, value):
        '''
        Multiplies the complex number by a given imaginary number 'value'.
        Changes the parameter 'self'. (pass by reference)
        IN: an imaginary number teoretically, but a real number interpreted by Python
        OUT: a ComplexNumber changed
        CONDIS: -
        '''
        s = ComplexNumber( self.__imaginaryPart * value * (-1), self.__realPart * value)
        return s
        
    def sumComplexNumbers(self, complex2):
        '''
        Computes the sum of 2 complex numbers and returns an instance of class ComplexNumber.
        IN: a ComplexNumber
        OUT: a ComplexNumber representing the sum of self and 'complex2'
        CONDIS: -
        '''
        res = ComplexNumber(0, 0)
        res.__realPart = self.__realPart + complex2.__realPart    
        res.__imaginaryPart = self.__imaginaryPart + complex2.__imaginaryPart    
        return res
    
    def prodComplexNumbers(self, complex2):
        '''
        Computes the product of 2 complex numbers and returns an instance of class ComplexNumber.
        IN: a ComplexNumber
        OUT: another ComplexNumber representing the product of self and 'complex2'
        CONDIS: -
        '''
        res = ComplexNumber(0, 0)
        # (a+b*i) * (c+d*i)
        a = self.getReal()
        b = self.getImaginary()
        c = complex2.getReal()
        d = complex2.getImaginary()
        res.setReal( a * c - b * d  )   
        res.setImaginary( a * d + c * b )     
        return res
    
    def matrix(self):
        '''
        Transforms a complex number into a matrix.
        IN:-
        OUT: a 2d matrix, 2 lines and 2 columns
        CONDIS: -
        
        a+bi = (a -b
                b  a)
        '''
        res = [ [0, 0], [0, 0] ]
        res[0][0] = self.getReal()
        res[0][1] = self.getImaginary() * (-1)
        res[1][0] = self.getImaginary()
        res[1][1] = self.getReal()
        return res
    
    def power(self, p):
        '''
        Computes the complex number at a given power 'p'.
        IN: a positive natural number
        OUT: a complex number
        CONDIS: p >= 0
        '''
        if p < 0:
            raise Exception("Power of cn is negative!")
        elif p != int(p):
            raise Exception("The power cannot be a float number!")
        elif p == 0:
            return ComplexNumber(1, 0)
        print("ajunge")
        res = ComplexNumber( self.getReal(), self.getImaginary() )
        for i in range(p-1):
            res = res.prodComplexNumbers(self)
        return res
    
    def squareRoot(self):
        '''
        Computes the square root of a complex number. 
        IN: - 
        OUT: a ComplexNumber
        CONDIS: -
        '''
        a = self.getReal()
        b = self.getImaginary()
        z = complex( a, b ) #python predefined object complex number
        z = np.sqrt(z) # = e**(z)
        
        a2 = z.real
        b2 = z.imag
        if a2 >= 1 or a2 <= -1:
            a2 = round( z.real, 2 )
        if b2 >= 1 or b2 <= -1:
            b2 = round( z.imag, 2)
            
        res = ComplexNumber( a2, b2 )
        return res
        
        
    def exponential(self):
        '''
        Computes the exponential of a complex number. The constant e at a power equal to a complex number.
        IN: - 
        OUT: a ComplexNumber
        CONDIS: -
        e**(self)
        '''
        a = self.getReal()
        b = self.getImaginary()
        #e = m.e #constant
        z = complex( a, b ) #python predefined object complex number
        z = np.exp(z) # = e**(z)
        
        #if numbers are in form 0.09123.. we do NOT round them to 2 decimal digits
        a2 = z.real
        b2 = z.imag
        if a2 >= 1 or a2 <= -1:
            a2 = round( z.real, 2 )
        if b2 >= 1 or b2 <= -1:
            b2 = round( z.imag, 2)
            
        res = ComplexNumber( a2, b2 )
        return res
    
    
#====================================== MAIN =================================


# c1 = ComplexNumber(3.5, 4)
# print( c1.power(3) )
# print( c1.multiplyByImaginary(3) )



















         