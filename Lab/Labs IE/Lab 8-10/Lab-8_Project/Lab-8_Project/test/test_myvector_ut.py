'''
Created on Nov 24, 2020

@author: Sergiu Ciubotariu
'''
import unittest
from domain.myvector import MyVector

class TestVector(unittest.TestCase):


    def testCreate(self):
        v = MyVector("salut", "y", 1, [1,2,3])
        
        self.assertEqual(v.get_name_id(), "salut")
        self.assertEqual(v.get_colour(), "y")
        self.assertEqual(v.get_type(), 1)
        self.assertEqual(v.get_values(), [1,2,3])
        
        v.set_name_id(100)
        self.assertEqual(v.get_name_id(), 100)
        v.set_colour("c")
        self.assertEqual(v.get_colour(), "c")
        v.set_type(3)
        self.assertEqual(v.get_type(), 3)
        v.set_values([2,3,4])
        self.assertEqual(v.get_values(), [2,3,4])
        
    def testAddScalarToVector(self):
        v = MyVector("salut", "y", 1, [1,2,3])
        v.addScalarToVector(2)
        self.assertEqual(v.get_values(), [3,4,5])
        v.addScalarToVector(1)
        self.assertEqual(v.get_values(), [4,5,6])
        v.addScalarToVector(-3)
        self.assertEqual(v.get_values(), [1,2,3])
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()