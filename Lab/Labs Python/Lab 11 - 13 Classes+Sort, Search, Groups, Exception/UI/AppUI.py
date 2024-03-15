'''
Created on Nov 21, 2017

@author: iuan
'''
#from application.appController import AppController

class AppUI:
    '''
    User interface for the program. 
    '''
    def __init__(self, ctrl):
        '''
        IN: a class
        OUT: -
        CONDIS: -
        '''
        self.__control = ctrl
    
    #@staticmethod
    def printData(self):
        '''
        Prints on screen the repositories with which we work.
        '''
        print("\nThe patients repository:")
        print( self.__control.showPatientRepo() )
        print("The departments repository:")
        print( self.__control.showDepartmentRepo() )
        
    @staticmethod
    def printMenu():
        '''
        Prints on screen the list of options of operations on a repository composed of complex nums
        '''
        s = ""
        s += "The list of operations: \n"
        s += "1 - add new Patient\n"
        s += "2 - add new Department \n"
        s += "3 - find Patient by index \n"
        s += "4 - find Department by index \n"
        s += "5 - update Patient by index \n"
        s += "6 - update Department by index \n"
        s += "7 - delete Patient by index \n"
        s += "8 - delete Department by index \n"
        s += "9 - sort patients from a department by cnp \n"
        s += "10 - sort departments by the number of patients having the age above a given limit\n"
        s += "11 - sort departments by the number of patients and the patients in a department alphabetically\n"
        s += "12 - identify departments where there are patients under a given age\n"
        s += "13 - identify patients from a given department for which the first name or last name contain a given string\n"
        s += "14 - identify department/departments where there are patients with a given first name\n"
        s += "15 - groups of k patients from same department and disease\n"
        s += "16 - groups of k departments with most p patients having same disease\n"
        print(s)
    
    @staticmethod
    def printResult(l):
        '''
        Prints on screen the str of each element from the list.
        IN: a list
        OUT: - 
        CONDIS: -
        '''
        if len(l) == 0:
            print("No such element found. List is empty.")
            return
          
        for el in l:
            print(el)
    
    @staticmethod
    def readUserInput():
        '''
        Reads from keyboard a number. Repeats until a number is given and nothing else.
        IN: -
        OUT: an integer
        '''
        try:
            a = int(input("\t"))
            return a
        except Exception:
            print("Not a number!")
        return AppUI.readUserInput()
    
    @staticmethod
    def readPatient():
        '''
        Reads the neccesarry variables for initialization of a class.
        IN: -
        OUT: string, string, string, string
        CONDIS: -
        '''
        fn = input("First Name:") 
        ln = input("Last Name:")
        cnp = input("CNP:")
        dis = input("Disease:")  
        return fn, ln, cnp, dis
    
    @staticmethod
    def readDepartment():
        '''
        Reads the neccesarry variables for initialization of a class.
        IN: -
        OUT: string, int, int, list of tuples
        CONDIS: length of list is positive
        '''        
        n = input("Name of department:")
        print("Number id:")
        number = AppUI.readUserInput()
        print("Number of beds: ")
        beds = AppUI.readUserInput()
        l = []
        print("Give length of list of patients: ")
        nr = AppUI.readUserInput()
        if nr < 0:
            raise Exception("Negative length of list!")
        for i in range(nr):
            print("\tPatient ", i+1, " .")
            l.append(AppUI.readPatient())
        return n, number, beds, l
        
    @staticmethod
    def readFile():
        '''
        Reads from a file more strings representing complex numbers.
        IN: - 
        OUT: a multilines string
        CONDIS: -
        '''
        try:
            fin = open("cnFile.in", "r")
            return fin.read()
            fin.close()
        except IOError as e:
            print("File Error!", e)
      
      
    def run(self):
        '''
        Asks and executes the operation demanded on the list of complex nums
        IN:-
        OUT:-
        Condis: the number inserted from the keyboard must be
        within the options numbers
        '''
        '''
        try:
            defaultString = AppUI.readFile()
            self.__control.default(defaultString)
            fout = open("results.out", "a")
            #clear functions
            fout.seek(0)
            fout.truncate()
            fout.write( self.__control.showRepo() )
        except Exception as e:
            print("Error!", e, "\nPlease fix file!")
            return None
        '''
        AppUI.printMenu()
        while True:
            try:                
                
                self.printData()
                print("What option do you choose: ")
                opt = AppUI.readUserInput()

                if opt == 0:
                    self.printData()
                    print("Program closed.")
                    exit()
                    
                elif opt == 1: #add patient
                    fn, ln, cnp, dis = AppUI.readPatient()
                    self.__control.addPatient(fn, ln, cnp, dis)
                    print("We added a new patient.")    
                
                elif opt == 2: #add department
                    name, number, beds, l = AppUI.readDepartment()
                    self.__control.addDepartment(name, number, beds, l)
                    print("We added a new department.")    
                    
                elif opt == 3:#find patient by index
                    print("Give index:")
                    index = AppUI.readUserInput()
                    res = self.__control.findPatientCommand(index)
                    print("Wanted patient: \n", str(res) )
                
                elif opt == 4:#find department by index
                    print("Give index:")
                    index = AppUI.readUserInput()
                    res = self.__control.findDepartmentCommand(index)
                    print("Wanted department: \n", str(res) )    
                
                elif opt == 5: #update patient by index
                    print("Give index:")
                    index = AppUI.readUserInput()
                    fn, ln, cnp, dis = AppUI.readPatient()
                    self.__control.updatePatientByIndexCommand(fn, ln, cnp, dis, index)
                    print("We updated the patient at index ", index, " ." ) 
                
                elif opt == 6: #update department by index
                    print("Give index:")
                    index = AppUI.readUserInput()
                    name, number, beds, l = AppUI.readDepartment()
                    self.__control.updateDepartmentByIndexCommand(name, number, beds, l, index)
                    print("We updated the department at index ", index, " ." ) 
                
                elif opt == 7: #delete patient by index
                    print("Give index:")
                    index = AppUI.readUserInput()
                    self.__control.deletePatientByIndexCommand(index)
                    print("We deleted the patient at index ", index, " ." ) 

                elif opt == 8: #delete department by index
                    print("Give index:")
                    index = AppUI.readUserInput()
                    self.__control.deleteDepartmentByIndexCommand(index)
                    print("We deleted the department at index ", index, " ." ) 
                
                elif opt == 9: #sort patients in department with number nr by cnp
                    print("What department to sort (No. of it):")
                    nr = AppUI.readUserInput()
                    res = self.__control.sortPatientsByCnpCommand(nr)
                    #res - list with a department with sorted patients
                    print("Patients in department are now sorted.\n")
                    AppUI.printResult(res)
                
                elif opt == 10: #sort departments by number of patients with higher age than value
                    print("Give age:")
                    value = AppUI.readUserInput()
                    res = self.__control.sortDByNrPatientsAgeCommand(value)
                    print("Departments (by higher age pats) are sorted.")
                    AppUI.printResult(res)
                    
                elif opt == 11: #sort departments by nr of pats and pats sorted alphabetically
                    res = self.__control.sortDByNrPatsAndPatsAlphCommand()
                    print("Departments (by nr of pats) are sorted.")
                    AppUI.printResult(res)
                
                elif opt == 12: #identify departments where there are patients under a given age
                    print("Give age (departments where are pats under age):")
                    value = AppUI.readUserInput()
                    res = self.__control.findDWithPatsUnderAgeCommand(value)
                    print("Here they are.")
                    AppUI.printResult(res)
                    
                elif opt == 13:
                    #identify patients from a given department for which the first name or last name 
                    #contain a given string
                    print("Give string (first or last name to contain): ")
                    st = input()
                    print("Number of department:")
                    nr = AppUI.readUserInput()
                    res = self.__control.findPWithStrInNameCommand(nr, st)
                    print("Patients containing string:")
                    AppUI.printResult(res)
                    
                elif opt == 14:
                    #identify department/departments where there are patients with a given first name
                    fN = input("Give first name:")
                    res = self.__control.findDByPatsFirstNameCommand(fN)
                    print("Departments with patients with given first name:")
                    AppUI.printResult(res)
                
                elif opt == 15:
                    #group patients
                    print("Give size of groups:") 
                    gs = AppUI.readUserInput()
                    res = self.__control.groupPatientsByDiseaseCommand(gs)   
                    print("Backtracking patients begins...")
                    AppUI.printResult(res)   
                    
                elif opt == 16:
                    #group departments   
                    print("Give size of groups:") 
                    gs = AppUI.readUserInput()
                    print("Give how many pats must have same disease:")
                    p = AppUI.readUserInput()
                    res = self.__control.groupDepartmentsCommand(gs, p)
                    print("Backtracking departments begins...")
                    AppUI.printResult(res)
                              
                else:
                    raise Exception("Not a number from the options!")
            
            
            except Exception as e:
                    print("Error!", e, "\n") 
                       
import app 
app       