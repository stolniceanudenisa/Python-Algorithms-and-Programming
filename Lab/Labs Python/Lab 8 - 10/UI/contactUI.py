'''
Created on Nov 20, 2017

@author: iuan
'''
from application.contactController import ContactController

class ContactUI:
    '''
    User interface for the contacts. 
    '''
    def __init__(self, ctrl):
        '''
        Constructor
        '''
        self.__control = ctrl
        
    @staticmethod
    def printMenu():
        '''
        '''
        s = ""
        s += "What option do you choose?"
    
    @staticmethod
    def readContact():
        '''
        '''
        
    def start(self):
        '''
        '''
        while True:
            try:
                ContactUI.printMenu()
                opt = int(input("What option:"))
                if opt == 0:
                    exit()
                elif opt == 1:
                    c = ContactUI.readContact()
                    self.__control.addContact(c)
                #elif....
                
                else:
                    print("Not a number from options!")
                    
            except Exception as e:
                print("Error!", e)        
                    
import app
app.start()                  
                    