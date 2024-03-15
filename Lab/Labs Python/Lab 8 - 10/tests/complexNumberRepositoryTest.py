'''
Created on Nov 26, 2017

@author: iuan
'''
import unittest
from infrastructure.complexNumberRepository import ComplexNumberRepository 
from domain.complexNumber import ComplexNumber

class ComplexNumberRepositoryTest(unittest.TestCase):
    
    
    def test_Create(self):
        '''a
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = ComplexNumberRepository()
        self.assertEqual( repo.getAll(), [] )
        
        c1 = ComplexNumber(3, 4)
        c2 = ComplexNumber(3, -2)
        repo.addComplexNumber( c1 )
        repo.addComplexNumber( c2 )
        self.assertEqual( repo.get(1), c2 )
        
    def test_cartesianFormRepo(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = ComplexNumberRepository()
        c1 = ComplexNumber(3, 4)
        c2 = ComplexNumber(3, -2)
        repo.addComplexNumber( c1 )
        repo.addComplexNumber( c2 )
        
        self.assertEqual( repo.cartesianFormRepo(), [  "3+4i  ---> real = 3, imaginary = 4\n",
                                                                                "3-2i  ---> real = 3, imaginary = -2\n"] )
        
    def test_polarFormRepo(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = ComplexNumberRepository()
        c1 = ComplexNumber(3, 4)
        c2 = ComplexNumber(3, -2)
        repo.addComplexNumber( c1 )
        repo.addComplexNumber( c2 )
        
        self.assertEqual( repo.polarFormRepo(), [  "5.0(cos( 53.29 ) + i sin( 53.29 ))",
                                                                                "3.61(cos( -33.8 ) + i sin( -33.8 ))"] )    
        
    def test_mulByRealRepo(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = ComplexNumberRepository()
        c1 = ComplexNumber(3, 4)
        c2 = ComplexNumber(3, -2)
        repo.addComplexNumber( c1.multiplyByReal(2) )
        repo.addComplexNumber( c2.multiplyByReal(2) )
        
        repo2 = ComplexNumberRepository()
        repo2.addComplexNumber( c1 )
        repo2.addComplexNumber( c2 )

        self.assertEqual( repo.getAll(), repo2.mulByRealRepo(2))    
           
    def test_sumRepo(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = ComplexNumberRepository()
        c1 = ComplexNumber(3, 4)
        c2 = ComplexNumber(3, -2)
        c3 = ComplexNumber(1, 1)
        
        c5 = ComplexNumber(4, 5)
        c6 = ComplexNumber(4, -1)
        repo.addComplexNumber( c1 )
        repo.addComplexNumber( c2 )
        #self.assertEqual( repo.sumRepo(c3), [c5, c6])    
    
    def test_matrixRepo(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = ComplexNumberRepository()
        c1 = ComplexNumber(3, 4)
        repo.addComplexNumber( c1 )
        
        self.assertEqual( repo.matrixRepo(), [  [[3, -4], [4, 3]]  ])  
          
    def test_powerRepo(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = ComplexNumberRepository()
        c1 = ComplexNumber(3, 4)
        repo.addComplexNumber( c1 )
        #self.assertEqual( repo.powerRepo(3), [[-117+44i]]) 
        
    def test_squareRootRepo(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = ComplexNumberRepository()
        c1 = ComplexNumber(3, 4)
        repo.addComplexNumber( c1 )
        #self.assertEqual( repo.squareRootRepo(), [  ]) 

    def test_exponentialRepo(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = ComplexNumberRepository()
        c1 = ComplexNumber(3, 4)
        repo.addComplexNumber( c1 )
        #self.assertEqual( repo.exponentialRepo(), [  ]) 






if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()