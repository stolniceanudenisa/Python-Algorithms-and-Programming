'''
Created on Jan 16, 2018

@author: iuan
'''
import unittest
from repository.studentRepository import StudentRepository
from domain.student import Student

class TestRepository(unittest.TestCase):
    '''
    tests repository
    '''
    def test_create(self):
        '''
        checks if function works.
        '''
        s1 = Student("Martin", 10, 811)
        s2 = Student("Katie", 6, 811)
        s3 = Student("Marcel", 7, 811)
        
        s4 = Student("Iosif", 3, 812)
        s5 = Student("Ionut", 8, 812)
        s6 = Student("Andra", 10, 812)
        repo = StudentRepository()
        
        self.assertEqual( repo.getAll1(), [] )
        
        repo.addNew(s1)
        repo.addNew(s2)
        repo.addNew(s3)
        repo.addNew(s4)
        repo.addNew(s5)
        repo.addNew(s6)
        
        self.assertEqual( len(repo), 6 )
        
    def test_findHigh(self):
        '''
        checks if function works.
        '''
        s1 = Student("Martin", 10, 811)
        s2 = Student("Katie", 6, 811)
        s3 = Student("Marcel", 7, 811)
        s4 = Student("Iosif", 3, 812)
        s5 = Student("Ionut", 8, 812)
        s6 = Student("Andra", 10, 812)
        repo = StudentRepository()        
        repo.addNew(s1)
        repo.addNew(s2)
        repo.addNew(s3)
        repo.addNew(s4)
        repo.addNew(s5)
        repo.addNew(s6)
        
        self.assertEqual( repo.findHigh(), ["Group 811:", s1, "Group 812:",s6] )
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()