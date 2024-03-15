'''
Created on Jan 16, 2018

@author: iuan
'''

class StudentRepositoryException(Exception):
    '''
    Handles the errors appearing when working with class Patient.
    '''

    def __init__(self, message):
        self.__message = message
        
        
    def __str__(self):
        return self.__message
