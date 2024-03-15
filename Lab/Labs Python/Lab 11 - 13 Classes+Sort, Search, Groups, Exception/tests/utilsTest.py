'''
Created on Dec 19, 2017

@author: iuan
'''
import unittest
from infrastructure.utils import mySort, mySearch, myBacktracking

class UtilsTest(unittest.TestCase):


    def test_sort(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        l = [ 4, 2, 3]
        mySort(l, lambda x,y: x < y)
        self.assertEqual( l, [2,3,4] )

    def test_search(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        l = [ 4, 2, 3, 2, 2]
        res = mySearch(l, lambda x: x == 2)
        self.assertEqual( res, [2, 2, 2] )
        
    def test_backtracking(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        l = [ 3, 2, 1]
        
        def c1(sol, myList):
            '''
            Groups unique elements.
            '''
            for i in range(len(sol) - 1):
                if myList[sol[i]] == myList[sol[len(sol) - 1]]:
                    return False
            return True
        
        res = list(myBacktracking([2], l, [c1]))
        #[[1,2], [1,3], [2,1], [2,3], [3,1], [3,2]]
        self.assertEqual( len(res), 6 )

if __name__ == "__main__":
    unittest.main()