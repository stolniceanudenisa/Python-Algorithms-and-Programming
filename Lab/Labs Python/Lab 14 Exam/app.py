'''
Created on Jan 16, 2018

@author: iuan
'''

from ui.appUI import AppUI
from domain.studentValidator import StudentValidator
from application.controller import StudentController
from repository.studentRepository import StudentRepository

def start():
    #create repo
    repo = StudentRepository()
    
    #create controller, provide repositories and validators
    sv = StudentValidator()
    controller = StudentController(repo, sv)
    
    #create UI, provide controller
    ui = AppUI(controller)
    ui.run()
    
start()