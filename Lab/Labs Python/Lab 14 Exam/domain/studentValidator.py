'''
Created on Jan 16, 2018

@author: iuan
'''
from domain.studentException import StudentException
class StudentValidator:
    '''
    validates the student calss
    '''
    
    def validate(self, s):
        '''
        validates the student
        '''
        err = ""
        
        if s.getName() == "":
            err += "Name is empty!"
        
        if s.getGrade() < 0:
            err += "Grade is not valid!"
        
        if s.getGroup() != 811 and s.getGroup() != 812:
            err += "Group is not valid!"
            
        if err != "":
            raise StudentException(err)