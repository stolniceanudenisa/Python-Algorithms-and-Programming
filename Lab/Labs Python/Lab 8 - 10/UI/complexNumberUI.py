'''
Created on Nov 21, 2017

@author: iuan
'''
#from application.complexNumberController import ComplexNumberController
from domain.complexNumber import ComplexNumber

class AppUI:
    '''
    User interface for the complex numbers. 
    '''
    def __init__(self, ctrl):
        '''
        IN: a class 'ComplexNumberController'
        OUT: -
        CONDIS: -
        '''
        self.__control = ctrl
        
    @staticmethod
    def printMenu():
        '''
        Prints on screen the list of options of operations on a repository composed of complex nums
        '''
        s = ""
        s += "The list of operations: \n"
        s += "1 - add new \n"
        s += "2 - cartesian form of each \n"
        s += "3 - polar form of each \n"
        s += "4 - conjugate of each \n"
        s += "5 - multiply by real each \n"
        s += "6 - multiply by imaginary each \n"
        s += "7 - sum of 2 cn \n"
        s += "8 - prod of 2 cn \n"
        s += "9 - matrix representation of each \n"
        s += "10 - at power 'p' each \n"
        s += "11 - square root of each \n"
        s += "12 - exponential of each \n"
        print(s)
    
    @staticmethod
    def readUserInput():
        '''
        Reads from keyboard a number. Repeats until a number is given and nothing else.
        IN: -
        OUT: an integer
        '''
        try:
            a = float(input("\t"))
            return a
        except Exception:
            print("Not a number!")
        return AppUI.readUserInput()
    
    @staticmethod
    def readComplexNumber():
        '''
        Reads 2 real numbers and constructs an instance of class 
        ComplexNumber with real part 'r' and im part 'i'.
        '''
        print("Give the real part: ")
        r = AppUI.readUserInput()
        print("Give the imaginary part: ")
        i = AppUI.readUserInput()
        return ComplexNumber( r, i )   
    
    @staticmethod
    def readFile():
        '''
        Reads from a file more strings representing complex numbers.
        IN: - 
        OUT: a multilines string
        CONDIS: -
        '''
        try:
            fin = open("cnFile.in", "r")
            return fin.read()
            fin.close()
        except IOError as e:
            print("File Error!", e)
        
    def run(self):
        '''
        Asks and executes the operation demanded on the list of complex nums
        IN:-
        OUT:-
        Condis: the number inserted from the keyboard must be
        within the options numbers
        '''
        try:
            defaultString = AppUI.readFile()
            self.__control.default(defaultString)
            fout = open("results.out", "a")
            #clear functions
            fout.seek(0)
            fout.truncate()
            fout.write( self.__control.showRepo() )
        except Exception as e:
            print("Error!", e, "\nPlease fix file!")
            return None
        
        while True:
            try:                
                AppUI.printMenu()
                print( self.__control.showRepo() )
                print("What option do you choose: ")
                opt = AppUI.readUserInput()
                
                if opt == 0:
                    print("Program closed.")
                    fout.close()
                    exit()
                    
                elif opt == 1:
                    c = AppUI.readComplexNumber()
                    self.__control.addNew(c)
                    fout.write( "\nAdded new element.\n" + self.__control.showRepo() )
                    
                elif opt == 2:
                    fout.write("\nCartesian forms:\n")
                    for elem in self.__control.cartesianFormCommand():
                        print(str(elem))
                        fout.write(str(elem))
                    
                elif opt == 3:
                    fout.write("\nPolar forms:\n")
                    for elem in self.__control.polarFormCommand():
                        fout.write(str(elem) +"\n")
                
                elif opt == 4:
                    fout.write("\nConjugate forms:\n")
                    for elem in self.__control.conjugateCommand():
                        print(str(elem))
                        fout.write(str(elem)+"\n")
                
                elif opt == 5:
                    print("Give real number:")                    
                    value = AppUI.readUserInput()
                    fout.write("\nMultiplying by real number:\n")
                    for elem in self.__control.mulByRealCommand(value):
                        print(str(elem))
                        fout.write(str(elem) +"\n" )
                
                elif opt == 6:
                    print("Give imaginary number:")
                    value = AppUI.readUserInput()
                    fout.write("\nMultiplying by imaginary number:\n")
                    for elem in self.__control.mulByImaginaryCommand(value):
                        print(str(elem))
                        fout.write(str(elem) +"\n" )

                
                elif opt == 7:
                    print("Give complex number.")
                    c1 = AppUI.readComplexNumber()
                    for elem in self.__control.sumCommand(c1):
                        print(str(elem))
                    
                elif opt == 8:
                    print("Give complex number.")
                    c1 = AppUI.readComplexNumber()
                    for elem in self.__control.prodCommand(c1):
                        print(str(elem))
                
                elif opt == 9:
                    for elem in self.__control.matrixCommand():
                        print(str(elem))
                
                elif opt == 10:
                    print("At which power:")                    
                    value = AppUI.readUserInput()
                    for elem in self.__control.powerCommand(value):
                        print(str(elem))
                
                elif opt == 11:#square root
                    for elem in self.__control.squareRootCommand():
                        print(str(elem))
                
                elif opt == 12:#exponential
                    for elem in self.__control.exponentialCommand():
                        print(str(elem))
                else:
                    raise Exception("Not a number from the options!\n")
            
            
            except Exception as e:
                    print("Error!", e) 
                       
            