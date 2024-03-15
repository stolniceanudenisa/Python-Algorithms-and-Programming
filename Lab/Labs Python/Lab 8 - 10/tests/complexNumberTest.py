'''
Created on Nov 20, 2017

@author: iuan
'''
from domain.complexNumber import ComplexNumber
from unittest import main, TestCase

class ComplexNumberTest(TestCase):
    '''
    Asserts the methods from class ComplexNumber in order to check if they work properly.
    '''
    
    def test_Create(self):
        '''
        Tests the initialization of the class ComplexNumber.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        c = ComplexNumber( 2, -9 )
        #test getters
        self.assertEqual( c.getReal(), 2 )
        self.assertEqual( c.getImaginary(), -9 )
        
        #test setters
        c.setReal(5)
        self.assertEqual( c.getReal(), 5 )
        c.setImaginary(1)
        self.assertEqual( c.getImaginary(), 1 )
        
        '''try:
            c2 = ComplexNumber( -1, "k" )
            assert False
        except ValueError:
            assert True
        '''
    
    def test_strComplexNumber(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        c = ComplexNumber( 2, -9 )
        self.assertEqual( str(c), "2-9i")
    
    def test_modulus(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        c = ComplexNumber( 2, -9 )
        self.assertAlmostEqual( c.modulus(), 9.22)
        
    def test_argument(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        c = ComplexNumber( 3, 4 )
        self.assertAlmostEqual( c.argument(), 0.93 ) 
        
    def test_polarForm(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        c = ComplexNumber( 3, 4 )
        self.assertEqual( c.polarForm(), "5.0(cos( 53.29 ) + i sin( 53.29 ))" )
    
    def test_conjugate(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        c = ComplexNumber( 3, 4 )
        c2 = c.conjugate()
        self.assertEqual(c2.getReal(), 3)
        self.assertEqual(c2.getImaginary(), -4)
    
    def test_multiplyByReal(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        c1 = ComplexNumber( 2, -9 )
        c2 = c1.multiplyByReal(2)
        
        self.assertEqual(c2.getReal(), 4)
        self.assertEqual(c2.getImaginary(), -18)
        
    def test_multiplyByImaginary(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: - 
        CONDIS: -
        '''
        c1 = ComplexNumber( 3, 4 )
        c2 = c1.multiplyByImaginary(3)
        
        self.assertEqual(c2.getReal(), -12)
        self.assertEqual(c2.getImaginary(), 9)
        
    def test_sumComplexNumbers(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: - 
        CONDIS: -
        '''
        c1 = ComplexNumber( 3, 4 )
        c2 = ComplexNumber( 3, 4 )
        res = c1.sumComplexNumbers(c2)
        
        self.assertEqual(res.getReal(), 6)
        self.assertEqual(res.getImaginary(), 8)
        
    def test_prodComplexNumbers(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: - 
        CONDIS: -
        '''
        c1 = ComplexNumber( 3, 4 )
        c2 = ComplexNumber( 3, -2 )
        res = c1.prodComplexNumbers(c2)
        
        self.assertEqual(res.getReal(), 17)
        self.assertEqual(res.getImaginary(), 6)    
        
        
    def test_matrix(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: - 
        CONDIS: -
        '''
        c1 = ComplexNumber( 3, 4 )
        c2 = ComplexNumber( 3, -2 )
        res = c1.matrix()
        self.assertEqual( res, [ [3, -4], [4, 3] ] )
        res = c2.matrix()
        self.assertEqual( res, [ [3, 2], [-2, 3] ] )
        
    def test_power(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: - 
        CONDIS: -
        '''
        c1 = ComplexNumber( 3, 4 )
        res = c1.power(3)
        self.assertEqual(res.getReal(), -117)
        self.assertEqual(res.getImaginary(), 44)
        
        try:
            res2 = c1.power(-2)
            assert False
        except Exception:
            assert True 
    
    def test_squareRoot(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: - 
        CONDIS: -
        '''
        c1 = ComplexNumber( 3, 4 )
        res = c1.squareRoot()
        self.assertAlmostEqual(res.getReal(), 2)
        self.assertEqual(res.getImaginary(), 1)  
        
    def test_exponential(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: - 
        CONDIS: -
        '''
        c1 = ComplexNumber( 3, 4 )
        res = c1.exponential()
        self.assertAlmostEqual(res.getReal(), -13.13)
        self.assertEqual(res.getImaginary(), -15.2)         
#=============================== MAIN =============================

            
if __name__ == "__main__" :
    main() 