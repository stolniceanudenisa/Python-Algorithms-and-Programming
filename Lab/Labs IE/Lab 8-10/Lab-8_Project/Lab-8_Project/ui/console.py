'''
Created on Nov 24, 2020

@author: Sergiu Ciubotariu
'''

from domain.myvector import MyVector
from builtins import staticmethod

class VectorUI():
    '''
    classdocs
    '''


    def __init__(self, vrepo):
        '''
        Constructor
        '''
        self.__repo = vrepo
    
    @staticmethod
    def printMenu():
        msg = "Menu:\n"
        msg += "\t 1 - View all vectors\n"
        msg += "\t 2 - Add vector\n"
        msg += "\t 3 - Return a vector by index\n"
        msg += "\t 4 - Update a vector at a given index\n"
        msg += "\t 5 - Update a vector with a given NameID\n"
        msg += "\t 6 - Sum of all elements of all vectors\n" 
        msg += "\t 7 - Creates a vector that is the sum of all vectors\n"
        msg += "\t 8 - Prints a list of vectors that have the sum equal to a given sum\n"
        msg += "\t 9 - Prints a list of vectors that have the min less than a given value\n"
        msg += "\t 0 - Exit\n"
        print(msg)
        
    def printAllVectors(self):
        print("List of vectors is: ")
        for vector in self.__repo.getData():
            print(vector)
    
    @staticmethod   
    def readVector():
        nameId = input("Enter NameID:")
        colour = input("Enter colour:")
        
        try:
            type_v = int(input("Enter type:"))
        except:
            type_v = 0
            
        try:
            val1 = int(input("Enter value 1:"))
        except:
            val1 = 0
        try:
            val2 = int(input("Enter value 2:"))
        except:
            val2 = 0
        try:
            val3 = int(input("Enter value 3:"))
        except:
            val3 = 0
        
        values =[val1,val2,val3]
        
        return MyVector(nameId, colour, type_v, values)
    
    
    def start(self):
        while True:
            VectorUI.printMenu()
            option = input("Your option: ")
            if option == "1":
                self.printAllVectors()
            elif option == "2":
                v = VectorUI.readVector()
                self.__repo.addVector(v)
            elif option == "3":
                try:
                    index = int(input("Give the index: "))
                    print(self.__repo.returnVectorAtIndex(index))
                except:
                    print("The given index was not correct")
            elif option == "4":
                try:
                    index = int(input("Give the index: "))
                    nameId = input("Enter NameID:")
                    colour = input("Enter colour:")
        
                    try:
                        type_v = int(input("Enter type:"))
                    except:
                        type_v = 0
            
                    try:
                        val1 = int(input("Enter value 1:"))
                    except:
                        val1 = 0
                    try:
                        val2 = int(input("Enter value 2:"))
                    except:
                        val2 = 0
                    try:
                        val3 = int(input("Enter value 3:"))
                    except:
                        val3 = 0
        
                    values =[val1,val2,val3]
                    
                    self.__repo.updateVectorAtIndex(index, nameId, colour, type_v, values)
                except:
                    print("The given index was not correct")
            elif option =="5":
                nameId = input("Enter NameID:")
                colour = input("Enter colour:")
        
                try:
                    type_v = int(input("Enter type:"))
                except:
                    type_v = 0
            
                try:
                    val1 = int(input("Enter value 1:"))
                except:
                    val1 = 0
                try:
                    val2 = int(input("Enter value 2:"))
                except:
                    val2 = 0
                try:
                    val3 = int(input("Enter value 3:"))
                except:
                    val3 = 0
        
                values =[val1,val2,val3]
                    
                self.__repo.updateVectorByName_Id(nameId, colour, type_v, values)
            elif option == "6":
                print("The sum is: " + str(self.__repo.sumOfElementsOfAllVectors()))
            elif option == "7":
                print("The sum of all vectors is: ")
                print(self.__repo.sumOfAllVectors())
            elif option == "8":
                s = int(input("Give the sum to search for: "))
                result = self.__repo.listOfVectorsBySum(s)
                for elem in result:
                    print(elem)
            elif option == "9":
                less = int(input("Give the value: "))
                result = self.__repo.listOfVectorsMinLessThan(less)
                for elem in result:
                    print(elem)
            elif option == "0":
                print("Good bye... ")
                break
            else:
                print("Option does not exist...")