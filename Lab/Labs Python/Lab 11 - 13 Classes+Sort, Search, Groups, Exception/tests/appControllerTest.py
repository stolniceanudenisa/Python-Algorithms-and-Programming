'''
Created on Nov 28, 2017

@author: iuan
'''
import unittest
from application.appController import AppController
from application.departmentValidator import DepartmentValidator
from application.patientValidator import PatientValidator
from repository.departmentRepository import DepartmentRepository
from repository.patientRepository import PatientRepository 
from domain.patient import Patient
from domain.department import Department

class AppControllerTest(unittest.TestCase):
    '''
    Asserts the methods from a class in order to check if they work properly.
    '''

    '''
    NOTE: prepo and drepo are populated before with some values from the init function in controller.
    Not only those that you see here.
    '''

    def test_Create(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)
        
        p1 = Patient("Pop", "Andrei", "1234567890123", "tusa")
        p2 = Patient("Pop", "Ioana", "2555567890123", "febra")
        l1 = [p1, p2]
        d1 = Department("Boli simple", 100, 2, l1)
        
        #test create patient
        cp1 = ("Pop", "Andrei", "1234567890123", "tusa")
        cp2 = ("Pop", "Ioana", "2555567890123", "febra")
        cpp = ctrl.createPatient(cp1[0], cp1[1], cp1[2], cp1[3])
        self.assertEqual( p1.equal(cpp), True)
        
        #test create department
        l1 = [cp1, cp2]
        cd1 = ("Boli simple", 100, 2, l1)
        cdd = ctrl.createDepartment(cd1[0], cd1[1], cd1[2], cd1[3])
        self.assertEqual( d1.equal(cdd), True)
        
        #test add patient
        size = len(ctrl.getPrepo())
        cp3 = ("Po", "Oana", "2555567899923", "apendicita")
        ctrl.addPatient(cp3[0], cp3[1], cp3[2], cp3[3])
        self.assertEqual( len(ctrl.getPrepo()), size+1)
        
        #test add department
        size = len(ctrl.getDrepo())
        ctrl.addDepartment( cd1[0], cd1[1], cd1[2], cd1[3] )
        self.assertEqual( len(ctrl.getDrepo()), size+1)     
        
        #check if know when one patient exists already
        try:
            cp3 = ("Po", "Oana", "2555567899923", "apendicita")
            ctrl.addPatient(cp3[0], cp3[1], cp3[2], cp3[3]) 
            assert False
        except Exception:
            assert True
        
    def test_Read(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)
        
        ''' Repositories are populated by default with some elements in init.'''
#         p1 = ("Pop", "Andrei", "1234567890123", "tusa")
#         p2 = ("Pop", "Ioana", "2234567890123", "febra")
#         p3 = ("Blaga", "Vasile", "1946573850346", "durere")
#         p4 = ("Tuduce", "Matei", "1948523850346", "durere")
#         l1 = [p1, p2]
#         d1 = ("Boli simple", 100, 2, l1)
#         l2 = [p3, p4]
#         d2 = ("Boli grave", 200, 20, l2)
#         ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
#         ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        #test find patient by index
        self.assertEqual( ctrl.findPatientCommand(2), ctrl.getPrepo().get(2) )
        
        #test find department by index
        self.assertEqual( ctrl.findDepartmentCommand(1), ctrl.getDrepo().get(1) )

    def test_Update(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)
        
        p1 = ("Pop", "Andrei", "1234567890123", "tusa")
        p2 = ("Pop", "Ioana", "2234567890123", "febra")
        p3 = ("Blaga", "Vasile", "1946573850346", "durere")
        p4 = ("Tuduce", "Matei", "1948523850346", "durere")
        l1 = [p1, p2]
        d1 = ("Boli simple", 100, 2, l1)
        l2 = [p3, p4]
        d2 = ("Boli grave", 200, 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        #test update patient
        p4 = ("Rick", "Morty", "1948123450346", "gripa")
        vp4 = ctrl.createPatient("Rick", "Morty", "1948123450346", "gripa")
        ctrl.updatePatientByIndexCommand(p4[0], p4[1], p4[2], p4[3], 3)
        self.assertEqual( ctrl.getPrepo().get(3).equal(vp4), True )
        self.assertEqual( ctrl.getDrepo().get(1).getListPatients()[1].equal(vp4), True )
        
        #test update department
        l3 = [p1, p4]
        d3 = ("Boli grave", 200, 20, l3)
        vd3 = ctrl.createDepartment("Boli grave", 200, 20, l3)
        ctrl.updateDepartmentByIndexCommand( d3[0], d3[1], d3[2], d3[3], 1 )
        self.assertEqual( ctrl.getDrepo().get(1).equal(vd3), True )

    def test_Delete(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)
        
        p1 = ("Pop", "Andrei", "1234567890123", "tusa")
        p2 = ("Pop", "Ioana", "2234567890123", "febra")
        p3 = ("Blaga", "Vasile", "1946573850346", "durere")
        p4 = ("Tuduce", "Matei", "1948523850346", "durere")
        l1 = [p1, p2]
        d1 = ("Boli simple", 100, 2, l1)
        l2 = [p3, p4]
        d2 = ("Boli grave", 200, 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        #test delete patient
        size = len(ctrl.getPrepo().getAll())
        sizeDepartmentPatients = len(ctrl.getDrepo().get(1).getListPatients())
        ctrl.deletePatientByIndexCommand(2)
        self.assertEqual( len(ctrl.getPrepo().getAll()), size-1 )
        self.assertEqual( len(ctrl.getDrepo().get(1).getListPatients()), sizeDepartmentPatients-1)
        ctrl.deletePatientByIndexCommand(4) #delete one inexistent in any department
        self.assertEqual( len(ctrl.getDrepo().get(1).getListPatients()), sizeDepartmentPatients-1)
        
        #test delete department
        size = len(ctrl.getDrepo().getAll())
        ctrl.deleteDepartmentByIndexCommand(0)
        self.assertEqual( len(ctrl.getDrepo().getAll()), size-1 )


    def test_sortPatientsByCnpCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)
        
        p1 = ("Pop", "Andrei", "2234567890123", "tusa")
        p2 = ("Pop", "Ioana", "1234567890123", "febra")
        p3 = ("Blaga", "Vasile", "1946573850346", "durere")
        p4 = ("Tuduce", "Matei", "1948523850346", "durere")
        l1 = [p1, p2]
        d1 = ("Boli simple", 100, 2, l1)
        l2 = [p3, p4]
        d2 = ("Boli grave", 200, 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        l1 = [p2, p1]
        d3 = Department("Boli simple", 100, 2, l1)

        self.assertEqual( d3.equal(ctrl.sortPatientsByCnpCommand(100)[0]), False )
     
     
    def test_sortDByNrPatientsAgeCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''  
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)
        ctrl.clearRepos()
        
        p1 = ("Pop", "Andrei", "2234567890123", "tusa")
        p2 = ("Pop", "Ioana", "1234567890123", "febra")
        p3 = ("Blaga", "Vasile", "1946573850346", "durere")
        p4 = ("Tuduce", "Matei", "1948523850346", "durere")
        l1 = [p1, p2]
        d1 = ("Boli simple", 100, 2, l1)
        l2 = [p3, p4]
        d2 = ("Boli grave", 200, 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        res = [ctrl.getDrepo().get(0), ctrl.getDrepo().get(1) ]
        self.assertEqual( ctrl.sortDByNrPatientsAgeCommand(50), res  )            

    def test_sortDByNrPatsAndPatsAlphCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''  
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)  
        
        res = [ctrl.getDrepo().get(2), ctrl.getDrepo().get(1), ctrl.getDrepo().get(0)]
        self.assertEqual( ctrl.sortDByNrPatsAndPatsAlphCommand(), res  )            

    def test_findDWithPatsUnderAgeCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''  
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)
        ctrl.clearRepos()
        
        p1 = ("Pop", "Andrei", "2234567890123", "tusa")
        p2 = ("Pop", "Ioana", "1234567890123", "febra")
        p3 = ("Blaga", "Vasile", "1946573850346", "durere")
        p4 = ("Tuduce", "Matei", "1948523850346", "durere")
        l1 = [p1, p2]
        d1 = ("Boli simple", 100, 2, l1)
        l2 = [p3, p4]
        d2 = ("Boli grave", 200, 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        res = [ ctrl.getDrepo().get(1) ]
        self.assertEqual( ctrl.findDWithPatsUnderAgeCommand(50), res )            

    def test_findPWithStrInNameCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''  
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)
        ctrl.clearRepos()
        
        p1 = ("Pop", "Andrei", "2234567890123", "tusa")
        p2 = ("Pop", "Ioana", "1234567890123", "febra")
        p3 = ("Blaga", "Vasile", "1946573850346", "durere")
        p4 = ("Tuduce", "Matei", "1948523850346", "durere")
        l1 = [p1, p2]
        d1 = ("Boli simple", 100, 2, l1)
        l2 = [p3, p4]
        d2 = ("Boli grave", 200, 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        res = [ ctrl.getDrepo().get(0).getListPatients()[0], ctrl.getDrepo().get(0).getListPatients()[1] ]
        self.assertEqual( ctrl.findPWithStrInNameCommand(100, "Pop"), res )
    
    def test_findDByPatsFirstNameCommand(self):  
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''  
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)
        ctrl.clearRepos()
        
        p1 = ("Pop", "Andrei", "2234567890123", "tusa")
        p2 = ("Pop", "Ioana", "1234567890123", "febra")
        p3 = ("Blaga", "Vasile", "1946573850346", "durere")
        p4 = ("Tuduce", "Matei", "1948523850346", "durere")
        l1 = [p1, p2]
        d1 = ("Boli simple", 100, 2, l1)
        l2 = [p3, p4]
        d2 = ("Boli grave", 200, 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        res = [ ctrl.getDrepo().get(0) ]
        self.assertEqual( ctrl.findDByPatsFirstNameCommand("Pop"), res )  
     
    def test_groupPatientsByDiseaseCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)
        ctrl.clearRepos()
        p1 = ("Pop", "Andrei", "2234567890123", "tusa")
        p2 = ("Pop", "Ioana", "1234567890123", "febra")
        p3 = ("Blaga", "Vasile", "1946573850346", "durere")
        p4 = ("Tuduce", "Matei", "1948523850346", "durere")
        l1 = [p1, p2]
        d1 = ("Boli simple", 100, 2, l1)
        l2 = [p3, p4]
        d2 = ("Boli grave", 200, 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        res = list(ctrl.groupPatientsByDiseaseCommand(2))
        self.assertEqual( len(res), 2)  
        self.assertEqual( len(res[1]), 2)  
    
    def test_groupDepartmentsCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        drepo = DepartmentRepository()
        prepo = PatientRepository()
        ctrl = AppController(prepo, drepo, pv, dv)
        ctrl.clearRepos()
        p1 = ("Pop", "Andrei", "2234567890123", "tusa")
        p2 = ("Pop", "Ioana", "1234567890123", "tusa")
        p3 = ("Blaga", "Vasile", "1946573850346", "durere")
        p4 = ("Tuduce", "Matei", "1948523850346", "durere")
        l1 = [p1, p2]
        d1 = ("Boli simple", 100, 2, l1)
        l2 = [p3, p4]
        d2 = ("Boli grave", 200, 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )   
        
        res = list(ctrl.groupDepartmentsCommand(2, 2))
        self.assertEqual( len(res), 2) 
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()