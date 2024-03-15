'''
Created on Jan 16, 2018

@author: iuan
'''
#from domain.studentValidator import StudentValidator
from domain.student import Student

class StudentController:
    '''
    controller for student repo
    '''

    def __init__(self, repo, v):
        '''
        Constructor
        '''
        self.__repo = repo
        self.__validator = v
        
        s1 = ("Martin", 10, 811)
        s2 = ("Katie", 10, 811)
        s3 = ("Marcel", 10, 811)
        
        s4 = ("Iosif", 3, 812)
        s5 = ("Ionut", 8, 812)
        s6 = ("Andra", 1, 812)
        
        self.add(s1[0], s1[1], s1[2])
        self.add(s2[0], s2[1], s2[2])
        self.add(s3[0], s3[1], s3[2])
        self.add(s4[0], s4[1], s4[2])
        self.add(s5[0], s5[1], s5[2])
        self.add(s6[0], s6[1], s6[2])
        
    def createStudent(self, name, grade, group):
        '''
        Creates the object Student.
        IN: string, int, int
        OUT: object student
        '''
        s = Student(name, grade, group)
        self.__validator.validate(s)
        return s
    
    def add(self, name, grade, group):
        '''
        adds new student to repo
        '''
        s = self.createStudent(name, grade, group)
        self.__repo.addNew(s)
        
    def findHighCommand(self):
        '''
        identifies the highest grade students from groups.
        IN: -
        OUT: a list with 2 objects
        '''
        return self.__repo.findHigh()
        
    def printRepo(self):
        '''
        String of students. Separated by group
        '''
        return str(self.__repo)
        
           
        