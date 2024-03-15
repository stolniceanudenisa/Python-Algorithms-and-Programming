'''
Created on Dec 5, 2017

@author: iuan
'''
from infrastructure.cityRepository import CityRepository
from domain.city import City
from ui.cityUI import CityUI
from tests.testCity import CityTest
from tests.testCityRepository import CityRepositoryTest

def start():
    '''
    Starts the program.
    '''
    
    #create repo
    repo = CityRepository()
    repo.addNew( "londra", 1000 )
    repo.addNew( "Budapesta", 5 )
    repo.addNew( "Satu-Mare", 7000 )
    repo.addNew( "Bucuresti", 20 )

    
    #create ui, provide repo
    ui = CityUI(repo)
    ui.run()
    
start()