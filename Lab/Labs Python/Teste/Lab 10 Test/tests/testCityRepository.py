'''
Created on Dec 5, 2017

@author: iuan
'''
import unittest
from infrastructure.cityRepository import CityRepository
from domain.city import City

class CityRepositoryTest(unittest.TestCase):

    def test_Create(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = CityRepository()
        self.assertEqual( repo.getAll(), [] )
#       c1 = City()
        c2 = City("Budapest", 5)
        repo.addNew( "Londra", 200 )
        repo.addNew( "Budapest", 5 )
        self.assertEqual( repo.get(1), c2 )
        
    #totalPopulationRepo
    #delHigherThan
    def test_totalPopulationRepo(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = CityRepository()
#         c1 = City()
#         c2 = City()
        repo.addNew( "Londra", 200 )
        repo.addNew( "Ludapest", 5 )
        
        self.assertEqual( repo.totalPopulationRepo('L'), 205 )
        
    def test_delHigherThan(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        repo = CityRepository()
#         c1 = City()
#         c2 = City()
#         c3 = City()
#         c4 = City()
        repo.addNew( "Londra", 200 )
        repo.addNew( "Ludapest", 5 )
        repo.addNew( "Bonjur", 50 )
        repo.addNew( "Goia", 10 )

        repo2 = CityRepository()
        repo2.addNew( "Ludapest", 5 )
        repo2.addNew( "Goia", 10 )
       
        repo2 = repo.delHigherThan(20)
        
        self.assertEqual( repo.getAll(), repo2.getAll() )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()