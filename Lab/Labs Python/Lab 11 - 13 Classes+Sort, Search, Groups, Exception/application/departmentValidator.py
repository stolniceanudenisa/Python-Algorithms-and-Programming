'''
Created on Dec 18, 2017

@author: iuan
'''

class DepartmentValidator:
    '''
    Checks if a department is valid.
    '''
    #name, number, number of beds,and list of patients

    def validate(self, d):
        '''
        Checks if department respects the conditions defined by the programmer.
        IN: an instance class Department
        OUT: -
        CONDIS: -
        '''
        errors = ""
    #name, number, number of beds,and list of patients
        if d.getName() == "":
            errors += "Name not valid!"
        
        if d.getNumber() < 0:
            errors += "Number not valid!"
        
        if d.getNrBeds() < 0:
            errors += "Number of beds not valid!"
        
        if len(errors) > 0:
            raise ValueError(errors)
