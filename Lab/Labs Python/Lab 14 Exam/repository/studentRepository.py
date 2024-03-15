'''
Created on Jan 16, 2018

@author: iuan
'''
from infrastructure.utils import  mySearch
#from repository.studentRepositoryException import StudentRepositoryException

class StudentRepository:
    '''
    composed of a list with students
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__data = []
        
    def addNew(self, s):
        '''
        adds student to repo
        IN: object student
        '''
        self.__data.append(s)
    
    def findHigh(self):
        '''
        finds highest grade students from all groups
        '''
        myList1 = self.getAll1()
        myList2 = self.getAll2()
        
        '''
        Credeam ca trebuie sort.
        res = []
        mySort(myList1, lambda x,y: x.getGrade() > y.getGrade())
        mySort(myList2, lambda x,y: x.getGrade() > y.getGrade())

        res.append("Group 811:")
        max1 = myList1[0].getGrade()
        for el in myList1:
            if el.getGrade() == max1:    
                res.append(el)
        #res.append("\n")
        res.append("Group 812:")
        max1 = myList2[0].getGrade()
        for el in myList2:
            if el.getGrade() == max1:    
                res.append(el)
        return res
        '''
        
        max1 = -1
        for el in myList1:
            if el.getGrade() > max1:
                max1 = el.getGrade()   
        
        max2 = -1
        for el in myList2:
            if el.getGrade() > max2:
                max2 = el.getGrade() 
        
        #ORICATE GRUPE adaugi repui codul acesta
        # Trebuia sa fie generica functia, trebuia functie de gasit maximul in given list
        fin = []        
        fin.append("Group 811:")
        for el in mySearch(myList1, lambda x: x.getGrade() == max1):
            fin.append(el)
            
        fin.append("Group 812:")
        for el in mySearch(myList2, lambda x: x.getGrade() == max2):
            fin.append(el)

        return fin
     
    def getAll1(self):
        '''
        returns all from group 811
        '''
        res = []
        for el in self.__data:
            if el.getGroup() == 811:
                res.append(el)
        return res  
    
    def getAll2(self):
        '''
        returns all from group 812
        '''
        res = []
        for el in self.__data:
            if el.getGroup() == 812:
                res.append(el)
        return res
                
    def __str__(self):
        '''
        string representation
        '''
        res = ""
        for el in self.__data:
            if el.getGroup() == 811:
                res += str(el)
        res += "\n"        
        for el in self.__data:
            if el.getGroup() == 812:
                res += str(el)
                
        return res
    
    def __len__(self):
        '''
        length of list
        '''
        return len(self.__data)
                    
                