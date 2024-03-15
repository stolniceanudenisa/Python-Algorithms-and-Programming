'''
Created on Dec 5, 2017

@author: iuan
'''

class CityUI(object):
    '''
    User Interface for cities.
    '''

    def __init__(self, repository):
        '''
        Constructs a repository of cities and operations on it
        '''
        self.__repo = repository
    
    @staticmethod
    def printMenu():
        s = "Operations:\n"
        s += "1 - add new\n"
        s += "2 - total population size starting with given letter\n"
        s += "3 - remove all cities with population size higher than a given value\n"
        
        print(s)
        
    @staticmethod
    def readUserInput():
        '''
        Reads from keyboard a number. Repeats until a number is given and nothing else.
        IN: -
        OUT: an integer
        '''
        try:
            a = int(input("\t"))
            return a
        except Exception:
            print("Not a number!")
        return CityUI.readUserInput()
        
    def run(self):
        '''
        Runs the options until exited with 0.
        '''
        while True:
            CityUI.printMenu()
            
            try:
                print(str(self.__repo))
                print("What option do you choose: ")
                opt =CityUI.readUserInput()
                
                if opt == 0:
                    print("Program ended.")
                    return None
                
                elif opt == 1:
                    nam = input("Give name:")
                    pop = int(input("Give pop size:"))
                    self.__repo.addNew(nam, pop)
                
                elif opt == 2:
                    letter = input("Give a letter:")
                    #->condition if letter is not char and is number!
                    print( "The total pop size of requested cities is: ", self.__repo.totalPopulationRepo(letter) )
                
                elif opt == 3:
                    print("Give a positive number:")
                    value = CityUI.readUserInput()
                    self.__repo.delHigherThan(value)
                
            except Exception as e:
                print("Error!", e)
        