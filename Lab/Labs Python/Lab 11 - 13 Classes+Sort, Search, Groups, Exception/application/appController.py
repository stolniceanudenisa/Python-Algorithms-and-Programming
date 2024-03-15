'''
Created on Dec 12, 2017

@author: iuan
'''
#from repository.patientRepository import PatientRepository
from domain.patient import Patient
#from repository.departmentRepository import DepartmentRepository
from domain.department import Department

class AppController:
    '''
    Controlls the patient and department repository.
    Composed of 2 classes.
    '''
    def __init__(self, prepo, drepo, pv, dv):
        '''
        Initializes the controller.
        '''
        self.__prepo = prepo
        self.__drepo = drepo
        self.__patientValidator = pv
        self.__departmentValidator = dv
        #fn, ln, cnp, disease
        #name, number, beds, l
        
        #Boli stomac
        p1 = Patient("Pop", "Ioana", "2164567890123", "Obezitate")
        p2 = Patient("Gradinita", "Emilutzbac", "1644567890146", "Obezitate")
        
        #Boli grave
        p3 = Patient("Baciu", "Tudose", "1246582789345", "Ecoli")
        p4 = Patient("Enigma", "Otiliei", "2647698729365", "Ecoli")
        p5 = Patient("Baciu", "Gheorghe", "2647684529365", "Ecoli")
        
        #Boli speciale
        p6 = Patient("Baciu", "Aihai", "298784529365", "Febra")
        p7 = Patient("Ion", "Creanga", "2123484529365", "Febra")
        p8 = Patient("Mester", "Pelea", "2123467529365", "Febra")
        p9 = Patient("Garbau", "Opris", "2123484522465", "Durere")
        
        #Boli psihice
        p10 = Patient("Eminescu", "Mihai", "298784729365", "Schizofrenic")
        p11 = Patient("Pintea", "Vasile", "2123484522365", "Schizofrenic")
        p12 = Patient("Term", "Enescu", "2123466789365", "Febra")
        p13 = Patient("Ulise", "Zeu", "2123412322465", "Durere")
        
        d1 = Department("Boli stomac", 702, 5, [p1, p2])
        d2 = Department("Boli grave", 100, 3, [p3, p4, p5])
        d3 = Department("Boli speciale", 500, 10, [ p6, p7, p8, p9])
        d4 = Department("Boli psihice", 10, 5, [ p10, p11, p12, p13])
        
        self.__prepo.addNew(p1)
        self.__prepo.addNew(p2)
        self.__prepo.addNew(p3)
        self.__prepo.addNew(p4)
        self.__prepo.addNew(p5)
        self.__prepo.addNew(p6)
        self.__prepo.addNew(p7)
        self.__prepo.addNew(p8)
        self.__prepo.addNew(p9)
        self.__prepo.addNew(p10)
        self.__prepo.addNew(p11)
        self.__prepo.addNew(p12)
        self.__prepo.addNew(p13)
        
        self.__drepo.addNew(d1)
        self.__drepo.addNew(d2)
        self.__drepo.addNew(d3)
        self.__drepo.addNew(d4)
    
    def getPrepo(self):
        '''
        Returns the repository of patients.
        '''
        return self.__prepo
    
    def getDrepo(self):
        '''
        Returns the repository of departments.
        '''
        return self.__drepo
    
    #CREATE
    def createPatient(self, fn, ln, cnp, dis):
        '''
        Creates a new instance of Patient.
        IN: 4 strings
        OUT: a Patient
        CONDIS: -
        '''
        p = Patient(fn, ln, cnp, dis)
        self.__patientValidator.validate(p)
        return p
    
    #CREATE
    def createDepartment(self, n, number, beds, l):
        '''
        Creates a new instance of Department.
        IN: string, int, int, list of tuples
        OUT: a Department
        CONDIS: number and beds are positive numbers
        '''
#         if number < 0 or beds < 0:
#             raise AppControllerException("Number or number of beds of department is negative!")
        
        #l contains tuple of 4 strings, we transform them in list with Patients
        l2 = []
        for el in l:
            p = self.createPatient(el[0], el[1], el[2], el[3])
            l2.append(p)
        
        d = Department(n, number, beds, l2)
        self.__departmentValidator.validate(d)
        return d
    
    def addPatient(self, fn, ln, cnp, dis):
        '''
        Add/Create
        IN: 4 strings
        OUT: -
        CONDIS: - 
        '''
        p = self.createPatient(fn, ln, cnp, dis)
        self.__prepo.addNew(p)
       
    def addDepartment(self, n, number, beds, l):
        '''
        Adds/Creates a new instance of Department in the repository.
        IN: string, int, int, list of tuples
        OUT: -
        CONDIS: -
        '''
        d = self.createDepartment(n, number, beds, l)
#         for el in d.getListPatients():
#             self.__prepo.addNew(el)
        self.addListPRec(d.getListPatients())
            
        self.__drepo.addNew(d)
    
    def addListPRec(self, l):
        '''
        Adds recursively a list of patients to the patients repository.
        IN: -
        OUT: -
        CONDIS: -
        '''
        #varianta recursiva
        if len(l) == 0:
            return
        else:   
            self.__prepo.addNew(l[0])
            self.addListPRec(l[1:])
      
    #READ
    def findPatientCommand(self, index):
        '''
        Finds an instance of a class from a repository.
        IN: a positive number
        OUT: an instance class
        CONDIS: handled in get() function
        '''
        return self.__prepo.get(index)
    
    #READ
    def findDepartmentCommand(self, index):
        '''
        Finds an instance of a class from a repository.
        IN: a positive number
        OUT: an instance class
        CONDIS: handled in get() function
        '''
        return self.__drepo.get(index)  
    
    #READ, ut
    def findDepartmentByNumberCommand(self, nr):
        '''
        Finds an instance of a class from a repository.
        IN: a positive number
        OUT: an instance class
        CONDIS: nr is positive
        '''
        return self.__drepo.findDepartmentByNumber(nr)
    
    #UPDATE    
    def updatePatientByIndexCommand(self, fn, ln, cnp, dis, index):
        '''
        Replaces an element from both repositories if exists.
        IN: a positive number
        OUT: -
        CONDIS: handled in updateDepartementByIndex function
        '''
        newP = self.createPatient(fn, ln, cnp, dis)
        p = self.findPatientCommand(index)
        
        #check if patient exists in department
        if self.getDrepo().findPatientInDepartment(p) != False:
            indices = self.getDrepo().findPatientInDepartment(p)
            #update patient in department
            self.getDrepo().getAll()[indices[0]].getListPatients()[indices[1]] = newP
        
        #update in patients repository            
        self.__prepo.updatePatientByIndex(index, newP)
        
        
    #UPDATE    
    def updateDepartmentByIndexCommand(self, name, number, beds, l, index):
        '''
        Replaces an element from the repository.
        IN: a positive number
        OUT: -
        CONDIS: handled in updateDepartementByIndex function
        '''
        d = self.createDepartment(name, number, beds, l)
        self.__drepo.updateDepartmentByIndex(index, d)

    #DELETE    
    def deletePatientByIndexCommand(self, index):
        '''
        Removes an instance of a class from a specific repository.
        IN: a number
        OUT: -
        CONDIS: handled in deleteByIndex function
        '''
        p = self.findPatientCommand(index)
        
        #check if patient exists in department
        if self.getDrepo().findPatientInDepartment(p) != False:
            indices = self.getDrepo().findPatientInDepartment(p)
            #delete patient in department
            del self.getDrepo().getAll()[indices[0]].getListPatients()[indices[1]]
        self.__prepo.deleteByIndex(index)
        
        
    #DELETE    
    def deleteDepartmentByIndexCommand(self, index):
        '''
        Removes an instance of a class from a specific repository.
        IN: a number
        OUT: -
        CONDIS: handled in deleteByIndex function
        '''
        self.__drepo.deleteByIndex(index)
      
    def showPatientRepo(self):
        '''
        Shows the patient repository.
        '''
        return str(self.__prepo)    
        
    def showDepartmentRepo(self):
        '''
        Shows the department repository.
        '''
        return str(self.__drepo) 
    
    def clearRepos(self):
        '''
        Clears the repositories.
        '''
        self.__drepo.clearAll()
        self.__prepo.clearAll()
    
    def sortPatientsByCnpCommand(self, number):
        '''
        Calls a function that sorts patients in a department with given number.
        IN: -
        OUT: a list with one object department and its patients sorted
        CONDIS: -
        '''
        d = self.findDepartmentByNumberCommand(number)
        return self.__drepo.sortPatientsByCnp(d)    

    def sortDByNrPatientsAgeCommand(self, value):
        '''
        Sorts departments by which one has more patients with higher age than given value.
        IN: a natural number
        OUT: a list with departments
        CONDIS: -
        '''
        return self.__drepo.sortDByNrPatientsAge(value)
    
    def sortDByNrPatsAndPatsAlphCommand(self):
        '''
        Sorts departments by which one has more patients and the patients in these departments are alphabetically ordered
        IN: - 
        OUT: a list with departments
        CONDIS: -
        '''
        return self.__drepo.sortDByNrPatsAndPatsAlph()
    
    def findDWithPatsUnderAgeCommand(self, age):
        '''
        Returns departments which have patients under age
        IN: -
        OUT: a list with departments
        CONDIS: 
        '''
        return self.__drepo.findDWithPatsUnderAge(age)
    
    def findPWithStrInNameCommand(self, nr, st):
        '''
        Returns a list with patients containing the string st in first or last name from a given department
        IN: a string
        OUT: a list with Patients
        CONDIS: - 
        '''
        d = self.findDepartmentByNumberCommand(nr)
        #la creare se considera ca nu pot avea acelasi nr, deci exista un singur d
        return self.__drepo.findPatsWithStrInName(d, st)
    
    def findDByPatsFirstNameCommand(self, fN):
        '''
        Identifies the departments where there are patients with a given first name.
        IN: a string
        OUT: a list with departments
        CONDIS: -
        '''
        return self.__drepo.findDByPatsFirstName(fN)
        
    def groupPatientsByDiseaseCommand(self, gs):
        '''
        For each department it groups the patients having the same disease.
        IN: an int
        OUT: a list with lists of patients
        CONDIS: gs is > 0
        '''
        if gs <= 0:
            raise AppControllerException("Group size is not valid! <= 0")
        
        aux = []
        for dep in self.__drepo.getAll():
            aux.append( self.__drepo.groupPatientsByDisease(gs, dep) )
        return aux
    
    
    def groupDepartmentsCommand(self, gs, p):
        '''
        Groups departments with at most p pats with same disease.
        IN: 2 natural numbers
        OUT: a list with lists consisted of departments
        CONDIS: gs and p are positive and p > 0
        '''
        if gs <= 0 or p < 1:
            raise AppControllerException("Group size or most patients number is not valid! <= 0")
          
        return self.__drepo.groupDepartments(gs, p)
        
        
class AppControllerException(Exception):
    '''
    Handles the errors appearing when working with class Patient.
    '''
    def __init__(self, message):
        self.__message = message
        
    def __str__(self):
        return self.__message 
        
# prepo = PatientRepository()
# drepo = DepartmentRepository()
# ctrl = AppController(prepo, drepo)
# l = [("a","b","C","d"), ("z","Y","f","v")]
# 
# print( ctrl.createDepartment("Boli simple", 100, 5, l) )