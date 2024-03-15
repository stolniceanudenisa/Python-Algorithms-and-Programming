'''
Created on Dec 19, 2017

@author: iuan
'''
import unittest

from domain.patient import Patient
from domain.department import Department
from application.departmentValidator import DepartmentValidator
class DepartmentValidatorTest(unittest.TestCase):

    def testValidate(self):
        '''
        Checks the validator.
        '''
        p1 = Patient("Pop", "Andrei", "1234567890123", "tusa")
        p2 = Patient("Pop", "Ioana", "2934567890123", "febra")
        l = [p1, p2]
        d = Department("Boli simple", -2, 2, l)
        v = DepartmentValidator()
        try:
            v.validate(d)
            assert False
        except Exception:
            assert True

        d = Department("Boli simple", 9, 2, l)
        try:
            v.validate(d)
            assert True
        except ValueError:
            assert False
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()