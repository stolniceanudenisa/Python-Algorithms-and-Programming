'''
Created on Dec 16, 2017

@author: iuan
'''
import unittest
from domain.department import Department
from domain.patient import Patient

class DepartmentTest(unittest.TestCase):
    '''
    Asserts the methods from a class in order to check if they work properly.
    '''
    
    def test_Create(self):
        '''
        Tests the initialization of the class.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p1 = Patient("Pop", "Andrei", "1234567890123", "tusa")
        p2 = Patient("Pop", "Ioana", "2234567890123", "febra")
        l = [p1, p2]
        d = Department("Boli simple", 100, 2, l)
        #test getters
        self.assertEqual( d.getName(), "Boli simple" )
        self.assertEqual( d.getNumber(), 100 )
        self.assertEqual( d.getNrBeds(), 2 )
        self.assertEqual( d.getListPatients(), l )   
             
        #test setters
        d.setName("Matei")
        self.assertEqual( d.getName(), "Matei" )
        d.setNumber(5)
        self.assertEqual( d.getNumber(), 5 )
        d.setNrBeds(7)
        self.assertEqual( d.getNrBeds(), 7 )
        l2 = [p1]
        d.setListPatients(l2)
        self.assertEqual( d.getListPatients(), l2 )
        
    
    def test_strPatient(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p1 = Patient("Pop", "Andrei", "1234567890123", "tusa")
        p2 = Patient("Pop", "Ioana", "2234567890123", "febra")
        l = [p1, p2]
        d = Department("Boli simple", 100, 2, l)
        res = "DEPARTMENT: Boli simple\nNo. 100\nNumber of beds: 2\nPatients: \n"
        res += "\tPop Andrei 1234567890123 tusa\n"
        res += "\tPop Ioana 2234567890123 febra\n"
        self.assertEqual( str(d), res)
    
    def test_HigherAge(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p1 = Patient("Pop", "Andrei", "1234567890123", "tusa")
        p2 = Patient("Pop", "Ioana", "2934567890123", "febra")
        l = [p1, p2]
        d = Department("Boli simple", 100, 2, l)
        self.assertEqual( d.higherAgePatients(50), 1 )
    
    def test_numberOfPatients(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p1 = Patient("Pop", "Andrei", "1234567890123", "tusa")
        p2 = Patient("Pop", "Ioana", "2934567890123", "febra")
        l = [p1, p2]
        d = Department("Boli simple", 100, 2, l)
        self.assertEqual( d.numberOfPatients(), 2 )
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()