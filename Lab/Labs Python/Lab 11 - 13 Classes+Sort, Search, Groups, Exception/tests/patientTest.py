'''
Created on Nov 20, 2017

@author: iuan
'''
from domain.patient import Patient
from unittest import main, TestCase

class PatientTest(TestCase):
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
        p = Patient("Pop", "Andrei", "1234567890123", "tusa")
        #test getters
        self.assertEqual( p.getFirstName(), "Pop" )
        self.assertEqual( p.getLastName(), "Andrei" )
        self.assertEqual( p.getCnp(), "1234567890123" )
        self.assertEqual( p.getDisease(), "tusa" )        
        #test setters
        p.setFirstName("Matei")
        self.assertEqual( p.getFirstName(), "Matei" )
        p.setLastName("Corvin")
        self.assertEqual( p.getLastName(), "Corvin" )
        p.setCnp("2364758693526")
        self.assertEqual( p.getCnp(), "2364758693526" )
        p.setDisease("fractura")
        self.assertEqual( p.getDisease(), "fractura" )
        
    
    def test_strPatient(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p = Patient("Pop", "Andrei", "1234567890123", "tusa")
        self.assertEqual( str(p), "Pop Andrei 1234567890123 tusa")
    
    def test_getAge(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p = Patient("Pop", "Andrei", "1984567890123", "tusa")
        self.assertEqual( p.getAge(), 19)
        
           
#=============================== MAIN =============================           
if __name__ == "__main__" :
    main() 