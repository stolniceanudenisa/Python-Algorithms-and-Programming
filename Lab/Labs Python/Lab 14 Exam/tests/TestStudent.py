'''
Created on Jan 16, 2018

@author: iuan
'''
import unittest
from domain.student import Student

class TestStudent(unittest.TestCase):

    def test_Create(self):
        '''
        tests creation
        '''
        s = Student("Maria", 7, 811)
        
        self.assertEqual( s.getName(), "Maria" )
        self.assertEqual( s.getGrade(), 7 )
        self.assertEqual( s.getGroup(), 811 )
        
        s.setName("a")
        s.setGrade(1)
        s.setGroup(812)
        
        self.assertEqual( s.getName(), "a" )
        self.assertEqual( s.getGrade(), 1 )
        self.assertEqual( s.getGroup(), 812 )
        
        try:
            s = Student("", -2, 100)
            assert False
        except Exception:
            assert True
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()