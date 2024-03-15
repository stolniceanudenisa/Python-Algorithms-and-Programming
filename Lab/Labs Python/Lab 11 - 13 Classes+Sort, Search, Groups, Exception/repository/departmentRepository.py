'''
Created on Nov 20, 2017

@author: iuan
'''
#from domain.department import Department
from infrastructure.utils import mySort, mySearch, myBacktracking
import copy

class DepartmentRepository:
    '''
    A list that contains instances of class department.
    '''
    
    #name, number, number of beds,and list of patients
    def __init__(self):
        '''
        Each instance of the class will have a list of objects Department
        '''
        self.__data = []
     
    #CREATE   
    def addNew(self, c):
        '''
        Adds new instance of a class in the repository.
        IN: an instance class
        OUT: -
        CONDIS: no other instance with same number
        '''
        if (self.findDepartmentByNumber( c.getNumber() ) == None) or (self.findByName(c.getName()) == None):
            self.__data.append(c)
        else:
            raise DepartmentRepositoryException("This department exists already!")

    
    #READ
    def findByIndex(self, index):
        '''
        Reads a specific element from the list and returns it.
        IN: a number
        OUT: an instance class
        CONDIS: index is positive and less than length
        '''
        if index < 0 or index >= len(self.__data):
            raise DepartmentRepositoryException("Index out of range!")
        return self.__data[index]
    
    #helps at addNew, inexistent in controller
#     def findByNumber(self, number):
#         '''
#         Searches for a Department with specific 'number'
#         IN: a number
#         OUT: an instance class
#         CONDIS: -
#         '''
#         for elem in self.__data:
#             if elem.getNumber() == number:
#                 return elem
#         return None
#     
    #READ
    def findDepartmentByNumber(self, number):
        '''
        Reads a department with given number.
        IN: a number
        OUT: an instance class
        CONDIS: nr is positive
        '''
        if number < 0:
            raise DepartmentRepositoryException("Number of dep is negative!")
        
        for i in range(len(self.__data)):
            if self.__data[i].getNumber() == number:
                return self.__data[i]
        return None
        raise DepartmentRepositoryException("Department with given number doesn't exist!")
    
    #helps at addNew, inexistent in controller
    def findByName(self, name):

        '''
        Searches for a Department with specific 'name'
        IN: a string
        OUT: a list with Departments or None if empty list
        CONDIS: -
        '''
        res = []
        for elem in self.__data:
            if elem.getName() == name:
                res.append(elem)
        if res == []:
            return None
        return res
      
    #UPDATE  
    def updateDepartmentByIndex(self, index, d):
        '''
        Replaces element from given index in repo.
        IN: a number, an instance class
        OUT: -
        CONDIS: index positive and less than length of repo
        '''
        if index < 0 or index >= len(self.__data):
            raise DepartmentRepositoryException("Index out of range!")
        self.__data[index] = d  
    
    #DELETE    
    def deleteByIndex(self, index):
        '''
        Removes an element at a given index.
        IN: a number
        OUT: -
        CONDIS: index is positive and less than length of repo
        '''
        if index < 0 or index >= len(self.__data):
            raise DepartmentRepositoryException("Index out of range!")    
        del self.__data[index]
        
                   
    def getAll(self):
        '''
        Returns the list of departments.
        '''
        return self.__data
    
    def get(self, index):
        '''
        Returns an object from the repository at a given index.
        IN: a natural number 'index'
        OUT: an object of type class Department from the list
        CONDIS: index >=0 and index < length of list
        '''
        if index < 0 or index >= len(self.__data):
            raise DepartmentRepositoryException("Index out of range!")
        return self.__data[index]
    
    def clearAll(self):
        '''
        Clears the list of departments.
        '''
        self.__data.clear()
    
    def __len__(self):
        '''
        Returns the number of departments.
        '''
        return len(self.__data)

    def __repr__(self):
        '''
        Returns the representation of the repository.
        '''
        res = ""
        for elem in self.__data:
            res += str(elem) + "\n"
        return res
    
    def __str__(self):
        '''
        Returns the visual representation of the repository as a string.
        '''
        res = ""
        for elem in self.__data:
            res += str(elem) + "\n"
        return res
    
    def findPatientInDepartment(self, p):
        '''
        Check in list of patients of every department if given patient p exists.
        IN: a patient
        OUT: 2 indices, one of department and one of patient from deparment's list
        if not found returns False
        CONDIS: -
        '''
        for i in range( len(self.getAll()) ):
            for j in range( len(self.getAll()[i].getListPatients()) ):
                if self.getAll()[i].getListPatients()[j].equal(p) == True:
                    return i, j
        return False
    
    def sortPatientsByCnp(self, d):
        '''
        Sorts patients in a given department list of patients by cnp.
        IN: -
        OUT: a list with 1 department
        CONDIS: -
        '''
        co = copy.deepcopy(d)
        mySort(co.getListPatients(), lambda x,y: x.getCnp() < y.getCnp())
        res = [co]
        return res
    
    def sortPatsByName(self, d):
        '''
        Sorts in a department the patients by their name.
        IN: a Department
        OUT: the Department changed
        '''
        mySort(d.getListPatients(), lambda x,y: x.getFirstName() < y.getFirstName() or x.getLastName() < 
               y.getLastName() and x.getFirstName() == y.getLastName())
        return d
        
    def sortDByNrPatientsAge(self, value):
        '''
        Sorts departments by which one has more patients with higher age than given value.
        IN: a natural number
        OUT: -
        CONDIS: -
        '''
        if value < 0:
            raise DepartmentRepositoryException("Given age is negative!")
        
        myDepartments = self.__data[:]
        mySort( myDepartments, lambda x,y: x.higherAgePatients(value) > y.higherAgePatients(value) )
        return myDepartments
    
    def sortDByNrPatients(self):
        '''
        Sorts departments by which one has more number of patients.
        IN: -
        OUT: a list with departments
        CONDIS: -
        '''
        myDepartments = self.__data[:] #list with departments
        mySort( myDepartments, lambda x,y: x.numberOfPatients() > y.numberOfPatients() )
        return myDepartments
    
    def sortDByNrPatsAndPatsAlph(self):
        '''
        Sorts departments by which one has more patients and the patients in these departments are alphabetically ordered
        IN: - 
        OUT: a list with departments
        CONDIS: -
        '''
        myDepartments = self.sortDByNrPatients()
        for i in range( len(myDepartments) ):         
            self.sortPatsByName(myDepartments[i])
        return myDepartments

    def findDWithPatsUnderAge(self, age):
        '''
        Returns a list with departments which have patients under given age.
        IN: -
        OUT: a list with departments
        CONDIS: age is positive
        '''
        if age < 0:
            raise DepartmentRepositoryException("Given age is negative!")
        myList = self.__data[:]
        return mySearch(myList, lambda x: x.patsUnderAge(age) > 0)
        
    def findPatsWithStrInName(self, d, st):
        '''
        Returns patients from given department that contain st in first/last name.
        IN: a Department, a string
        OUT: a list with Patients
        CONDIS: -
        '''
        return mySearch( d.getListPatients(), lambda x: st in x.getFirstName() or st in x.getLastName() )
        
    def findDByPatsFirstName(self, fN):
        '''
        Identifies the departments where there are patients with a given first name.
        IN: a string
        OUT: a list with departments
        CONDIS: -
        '''
        def checkDepartment(d):
            #macar un membru are first name = f
            for el in d.getListPatients():
                if el.getFirstName() == fN:
                    return True
            return False
        return mySearch(self.__data, checkDepartment )        
    
    def constructSolution(self, sol, myList):
        '''
        Transforms a list of indices in a list with objects from a list at the given indices.
        IN: a list with numbers, a list with objects
        OUT: a list like myList but with elems positioned differently or the same
        CONDIS: -
        '''
        aux  = []
        for i in sol:
            aux.append( myList[i] )
        return aux
    
    def groupPatientsByDisease(self, gs, d):
        '''
        From specific department, group patients with same disease.
        IN: an int, a department
        OUT: string if patients with same disease were not found
        a list with lists if we can group
        CONDIS: handled in controller
        '''
        def c1(sol, myList):
            '''
            Checks if all elements are unique after they are added.
            If they have same diseases.
            '''
            for i in range(len(sol) - 1):
                if myList[sol[i]].getDisease() != myList[sol[len(sol) - 1]].getDisease():
                    return False
            return True
        
        def c2(sol, myList):
            '''
            Checks if all elements are unique after they are added.
            If they have different name.
            '''
            for i in range(len(sol) - 1):
                if myList[sol[i]].getFirstName() == myList[sol[len(sol) - 1]].getFirstName():
                    if myList[sol[i]].getLastName() == myList[sol[len(sol) - 1]].getLastName():
                        return False
            return True
        
        myList = d.getListPatients()
        param = [gs]
        constraints = [c1, c2]
        aux = []
        for el in myBacktracking(param, myList, constraints):
            aux.append( self.constructSolution(el, myList) )
        if aux == []:
            return "This department doesnt have valid patients for grouping."
        return aux    
     
    def groupDepartments(self, gs, p):
        '''
        Group departments by patients and same disease
        IN: an int, a department
        OUT: a list with lists consisted of departments
        CONDIS: -
        ''' 
        def c1(sol, myList):
            '''
            Checks if last element added from sol has at most p patients with same disease.
            IN: sol - list with indexes, myList - list with departments
            OUT: true or false
            CONDIS: -
            '''
            d = myList[ sol[len(sol) - 1] ]
            if self.groupPatientsByDisease(p, d) == "This department doesnt have valid patients for grouping.":
                return False
            return True
         
        def c2(sol, myList):
            '''
            Checks if all elements are unique after they are added.
            If they have different name.
            '''
            for i in range(len(sol) - 1):
                if myList[sol[i]].getName() == myList[sol[len(sol) - 1]].getName():
                    return False
            return True   
        
        myList = self.__data[:]
        param = [gs]
        constraints = [c1, c2]
        aux = []
        
        for el in myBacktracking(param, myList, constraints):
            aux.append( self.constructSolution(el, myList) )
            
        if aux == []:
            raise DepartmentRepositoryException("This repository doesnt have valid departments for grouping.")
        return aux
         
class DepartmentRepositoryException(Exception):
    def __init__(self, message):
        self.__message = message
        
    def __str__(self):
        return self.__message



from domain.patient import Patient
from domain.department import Department
 
p1 = Patient("Pop", "Ioana", "2164567890123", "Gastrita")
p2 = Patient("Gradinita", "Emilutzbac", "1644567890146", "Obezitate")
p3 = Patient("Baciu", "Tudose", "1246582789345", "Fractura Coloana")
p4 = Patient("Enigma", "Otiliei", "2647698729365", "Ecoli")
p5 = Patient("Baciu", "Gheorghe", "2647684529365", "Febra")
p6 = Patient("Baciu", "Aihai", "298784529365", "Febra")
p7 = Patient("Ion", "Creanga", "2123484529365", "Febra")

d1 = Department("Boli stomac", 702, 5, [p1, p2])
d2 = Department("Boli grave", 100, 3, [p3, p4])
d3 = Department("Boli speciale", 500, 10, [ p5, p6, p7])
repo = DepartmentRepository()
repo.addNew(d1)
repo.addNew(d2)
repo.addNew(d3)

def c2(sol, myList):
    '''
    Checks if all elements are unique after they are added.
    If they have same name.
    '''
    for i in range(len(sol) -1):
        if myList[sol[i]].getFirstName() == myList[sol[len(sol) - 1]].getFirstName():
            if myList[sol[i]].getLastName() == myList[sol[len(sol) - 1]].getLastName():
                return False
            
    return True

aux = []
for el in myBacktracking([3], repo.get(1).getListPatients(), [c2]):
    aux.append( repo.constructSolution( el, repo.get(1).getListPatients() ) )
#rint(aux)    
#print( myBacktracking([2], repo.get(1).getListPatients, []) )







