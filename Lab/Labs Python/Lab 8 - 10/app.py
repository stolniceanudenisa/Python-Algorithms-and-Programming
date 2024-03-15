'''
Created on Nov 20, 2017

@author: iuan
'''
#from infrastructure.contactRepository import ContactRepository
from application.complexNumberController import ComplexNumberController
from UI.complexNumberUI import ComplexNumberUI
from domain.complexNumber import ComplexNumber
from infrastructure.complexNumberRepository import ComplexNumberRepository
import math as m
import numpy as np

def start():
    #create repo
    repo = ComplexNumberRepository()
#     repo.addComplexNumber( ComplexNumber( 3, 4 ) )
#     repo.addComplexNumber( ComplexNumber( 3, -2 ) )
#     repo.addComplexNumber( ComplexNumber( -7.9, 0.3 ) )
#     repo.addComplexNumber( ComplexNumber( 2, 1 ) )
    
    #create controller, provide repository
    controller = ComplexNumberController(repo)
    
    #create UI, provide controller
    ui = ComplexNumberUI(controller)
    ui.run()
    
start()