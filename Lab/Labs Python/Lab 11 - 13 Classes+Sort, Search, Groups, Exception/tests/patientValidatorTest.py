'''
Created on Dec 19, 2017

@author: iuan
'''
import unittest

from domain.patient import Patient
from application.patientValidator import PatientValidator
class PatientValidatorTest(unittest.TestCase):

    def testValidate(self):
        '''
        Checks the validator.
        '''
        c = Patient("Ana", "Vada", "0123", "dis")
        v = PatientValidator()
        try:
            v.validate(c)
            assert False
        except Exception:
            assert True

        c = Patient("Andrei", "Marian", "1234567890123", "dis")
        try:
            v.validate(c)
            assert True
        except ValueError:
            assert False


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()