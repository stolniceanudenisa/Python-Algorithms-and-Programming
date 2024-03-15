'''
Created on Dec 5, 2017

@author: iuan
'''
import unittest
from domain.city import City

class CityTest(unittest.TestCase):

    def test_Create(self):
        '''
        Tests the initialization of the class ComplexNumber.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        c = City( "Londra", 500 )
        #test getters
        self.assertEqual( c.getName(), "Londra" )
        self.assertEqual( c.getPopulation(), 500 )
        
        #test setters
        c.setName("Budapest")
        self.assertEqual( c.getName(), "Budapest" )
        c.setPopulation(1)
        self.assertEqual( c.getPopulation(), 1 )
        
        try:
            c2 = City( "Londra", -1 )
            assert False
        except ValueError:
            assert True
        
    def test_firstLetter(self):
        '''
        Tests the initialization of the class ComplexNumber.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        c = City( "Londra", 500 )
        self.assertEqual(c.firstLetter(), 'L')
        
    def test_str(self):
        '''
        Tests the initialization of the class ComplexNumber.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        c = City( "Londra", 500 )
        self.assertEqual( str(c), "Londra population size:500")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()