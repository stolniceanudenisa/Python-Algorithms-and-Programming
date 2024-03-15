'''
Created on Dec 18, 2017

@author: iuan
'''

class PatientValidator:
    '''
    Checks if a patient is valid.
    '''
    #first name, last name, personal numerical code and disease

    def validate(self, p):
        '''
        Checks if patient respects the conditions defined by the programmer.
        IN: an instance class Patient
        OUT: -
        CONDIS: -
        '''
        errors = ""
        
        if p.getFirstName() == "":
            errors += "First name not valid!"
        
        if p.getLastName() == "":
            errors += "Last name not valid!"
        
        if p.getDisease() == "":
            errors += "Disease not valid!"
        
        if len(p.getCnp()) != 13:
            errors += "CNP is not valid!"
        
        if p.getCnp()[0] != '1' and p.getCnp()[0] != '2':
            errors += "CNP invalid. Not boy or girl!"
            
        if len(errors)>0:
            raise ValueError(errors)

        