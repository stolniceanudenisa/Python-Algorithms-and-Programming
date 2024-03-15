'''
Created on Nov 20, 2017

@author: iuan
'''
from application.patientValidator import PatientValidator
from application.departmentValidator import DepartmentValidator
from application.appController import AppController
from repository.departmentRepository import DepartmentRepository
from repository.patientRepository import PatientRepository
from UI.AppUI import AppUI

def start():
    #create repo
    prepo = PatientRepository()
    drepo = DepartmentRepository()
    
    #create controller, provide repositories and validators
    pv = PatientValidator()
    dv = DepartmentValidator()
    controller = AppController(prepo, drepo, pv, dv)
    
    #create UI, provide controller
    ui = AppUI(controller)
    ui.run()
    
start()