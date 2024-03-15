'''
Created on Nov 26, 2017

@author: iuan
'''
import unittest
from repository.patientRepository import PatientRepository 
from domain.patient import Patient

class PatientRepositoryTest(unittest.TestCase):
    '''
    Asserts the methods from a class in order to check if they work properly.
    '''
    
    def test_Create(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = PatientRepository()
        self.assertEqual( repo.getAll(), [] )
        p1 = Patient("Pop", "Andrei", "1234567890123", "tusa")
        p2 = Patient("Pop", "Ioana", "2234567890123", "febra")
        repo.addNew( p1 )
        repo.addNew( p2 )
        self.assertEqual( repo.get(1), p2 )
        #__len__
        self.assertEqual( len(repo), 2 )
        #clear all
        repo.clearAll()
        self.assertEqual( repo.getAll(), [] )

        
    def test_Read(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = PatientRepository()
        p1 = Patient("Pop", "Andrei", "1234567890123", "tusa")
        p2 = Patient("Pop", "Ioana", "2234567890123", "febra")
        repo.addNew( p1 )
        repo.addNew( p2 )
        self.assertEqual( repo.findByIndex(1), p2 )
        try:
            repo.findByIndex(9)
            repo.findByIndex(-2)
            assert False
        except Exception:
            assert True
        #test_findByCnp
    
    def test_Update(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = PatientRepository()
        p1 = Patient("Pop", "Andrei", "1234567890123", "tusa")
        p2 = Patient("Pop", "Ioana", "2234567890123", "febra")
        p3 = Patient("Blaga", "Vasile", "1946573850346", "durere")
        repo.addNew( p1 )
        repo.addNew( p2 )
        
        repo.updatePatientByIndex(0, p3)
        self.assertEqual( repo.get(0), p3 )
        try:
            repo.updatePatientByIndex(9, p3)
            repo.updatePatientByIndex(-2, p3)
            assert False
        except Exception:
            assert True
    
    def test_Delete(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = PatientRepository()
        p1 = Patient("Pop", "Andrei", "1234567890123", "tusa")
        p2 = Patient("Pop", "Ioana", "2234567890123", "febra")
        #p3 = Patient("Blaga", "Vasile", "1946573850346", "durere")
        repo.addNew( p1 )
        repo.addNew( p2 )
        size = len(repo)
        repo.deleteByIndex(0)
        self.assertEqual( len(repo), size-1 )
        try:
            repo.deleteByIndex(9)
            repo.deleteByIndex(-2)
            assert False
        except Exception:
            assert True        




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()