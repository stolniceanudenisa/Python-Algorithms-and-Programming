'''
Created on Jan 16, 2018

@author: iuan
'''

class AppUI:
    '''
    user interface for app
    '''

    def __init__(self, ctrl):
        '''
        Constructor
        '''
        self.__ctrl = ctrl
     
    @staticmethod 
    def readInput():
        '''
        reads a number from keyboard. loops until number is given.
        '''
        try:
            a = int(input())
            return a
        except Exception:
            AppUI.readInput() 
    
    @staticmethod
    def readStudent():
        '''
        Reads the necesarries for the object student.
        IN: -
        OUT: a string, an int, an int
        CONDIS: the input for last 2 is a natural number, for group is only 811 or 812
        '''
        name = input("Give name: ")
        print("Give grade: ")
        grade = AppUI.readInput()
        print("Give group: ")
        group = AppUI.readInput()
        return name, grade, group
     
    @staticmethod
    def printResult(l):
        '''
        Prints the str of whatever element from list.
        IN-  a list
        OUT:-
        ''' 
        for el in l:
            print(str(el))
            
    @staticmethod
    def printMenu():
        '''
        PRINTS MENU
        '''
        menu = ""
        menu += "1 - add new student \n"
        menu += "2 - identify student with highest grade in both groups \n"
        menu += "3 - view students \n"
        print(menu)
        
            
    def run(self):
        '''
        runs the app
        '''
        AppUI.printMenu()
        print("Students are: \n", self.__ctrl.printRepo(), "------------")
        
        while True:
            try:
                print("Give option: ")
                opt = AppUI.readInput()
                
                if opt == 0:
                    exit()
                
                elif opt == 1:
                    #add
                    name, grade, group = AppUI.readStudent()
                    self.__ctrl.add(name, grade, group)
                    
                elif opt == 2:
                    res = self.__ctrl.findHighCommand()
                    print("Students with highest grade are: ")
                    AppUI.printResult(res)
                
                elif opt == 3:
                    print("STUDENTS ARE: \n", self.__ctrl.printRepo())
                    
                else:
                    raise Exception("Option not valid!")
            except Exception as e:
                print("\nError! ", e)