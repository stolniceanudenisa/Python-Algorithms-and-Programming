'''
Created on Nov 28, 2017

@author: iuan
'''
import unittest
from application.complexNumberController import ComplexNumberController
from domain.complexNumber import ComplexNumber


class ComplexNumberControllerTest(unittest.TestCase):


    def test_Create(self):
        '''
        '''
        ctrl = ComplexNumberController()
        c1 = ComplexNumber(3, 4)        
        











if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()