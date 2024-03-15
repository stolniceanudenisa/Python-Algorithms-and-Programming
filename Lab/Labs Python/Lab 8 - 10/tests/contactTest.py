'''
Created on Nov 20, 2017

@author: iuan
'''
from domain.contact import Contact
from unittest import main, TestCase

class ContactTest(TestCase):
    '''
    classdocs
    '''
    
    def testCreate(self):
        c = Contact( "Raul", "0741234567" )
        #test getters
        self.assertEqual( c.getName(), "Raul" )
        self.assertEqual( c.getNumber(), "0741234567" )
        
        #test setters
        c.setName("Ranga")
        self.assertEqual( c.getName(), "Raul" )
        c.setNumber("0731234567")
        self.assertEqual( c.getNumber(), "0731234567" )
        
        try:
            c2 = Contact( "Truta", "02473" )
            assert False
        except ValueError:
            assert True
    
    
    
    
            
if __name__ == "__main__" :
    main()   
            
            