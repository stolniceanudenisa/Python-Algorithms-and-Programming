'''
Created on Nov 13, 2017

@author: iuan
'''
import globalVariables as gV

#from domain import vectorOperations as vO
from domain import withNumpy as vO

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
    return readUserInput()    

def readVector():
    '''
    Reads a 2D vector from the keyboard.
    IN: - 
    OUT: a 2D vector, lists within a list
    '''
    print("How many lines:")
    l = readUserInput()
    print("How many columns:")
    c = readUserInput()
    vect = [[]for i in range(l)]
    
    for i in range(l):
        for j in range(c):
            print( "Give element", "[", i, "]", "[", j, "]", ":" )
            vect[i].append( readUserInput() )
    return vect

def writeVectors():
    '''
    Prints to the screen the vectors contained in the list 'repo'
    IN: - 
    OUT: prints on screen 2D vectors
    '''
    print("\nThe vectors in repository are:")
    for i in range(len(gV.repo)):
        print(gV.repo[i])
        
    print("---")

#================================= RUN ==========================================
def run():
    '''
    Asks and executes the operation demanded on the list of vectors
    IN:-
    OUT:-
    Condis: the number inserted from the keyboard must be
    within the options numbers
    '''
    while True:
        writeVectors()
        print("What option do you choose?  Exit=0, NewVector=1, AddScalar=2, AddVects=3, DifVects=4, ProdVects=5,")
        print("SumElems=6, ProdElems=7, MaxElem=8, MinElem=9, AvgElem=10")
        n=readUserInput()
        
        if n==0:#Exit
            print("Program ended.")
            break
        
        elif n==1:#Add New Vector
            addVectorCommand()
                
        elif n==2:#Add Scalar
            addScalarCommand()
            
        elif n==3:#Add 2 vects
            sumaVectorCommand()
                
        elif n==4:#Subtract 2 vects
            difVectorCommand()
                
        elif n==5:#Product 2 vects
            prodVectorCommand()   
                
        elif n==6:#Sum of elements
            sumElemsVectCommand()
             
        elif n==7:#Prod of elements
            prodElemsVectCommand()
                
        elif n==8:#Maximum element
            maxElemsVectCommand()
                
        elif n==9:#Minimum element
            minElemsVectCommand()
                
        elif n==10:#AVG of elements
            avgElemsVectCommand()
                   

def addVectorCommand():
    '''
    Appends a new vector to the repository.
    '''
    try:
        vect = readVector()
        gV.repo.append(vect)
        
    except Exception as e:
        print("Error!", e)
   
def addScalarCommand():
    '''
    Adds a scalar to each vector from the repository.
    '''
    try:
        print("What scalar:")
        sca = readUserInput()
        
        for i in range(len(gV.repo)):#iterates through each vector   
            vO.addScalar(sca, gV.repo[i])
        print("Scalar", sca, "has been added to each vector.")   
         
    except Exception as e:
        print("Error!", e)

def sumaVectorCommand():
    '''
    Reads 2 vectors and prints the sum.
    '''
    try:
        print("First vector.")
        v1 = readVector()
        print("Second vector.")
        v2 = readVector()
        print(v1, "+", v2)
        print("The sum is:", vO.sumaVector(v1, v2))
        
    except Exception as e:
        print("Error!", e)

def difVectorCommand():
    '''
    Reads 2 vectors and prints the difference.
    '''
    try:
        print("First vector.")
        v1 = readVector()
        print("Second vector.")
        v2 = readVector()
        print(v1, "-", v2)
        print("The difference is:", vO.difVector(v1, v2))
        
    except Exception as e:
        print("Error!", e)
            
def prodVectorCommand():
    '''
    Reads 2 vectors and prints the product.
    '''
    try:
        print("First vector.")
        v1 = readVector()
        print("Second vector.")
        v2 = readVector()
        print(v1, "x", v2)
        print("The product is:", vO.prodVector(v1, v2))
    except Exception as e:
        print("Error!", e)    
              
def sumElemsVectCommand():
    '''
    Prints the sum of elements from each vector from the repository.
    '''
    try:
        res = [] 
        for i in range(len(gV.repo)):
            res.append(vO.sumElemsVect( gV.repo[i] ))
        print("The sum of elements from each vect is:", res)
    except Exception as e:
        print("Error!", e)
  
def prodElemsVectCommand():
    '''
    Prints the product of elements from each vector from the repository.
    '''
    try:
        res = [] 
        for i in range(len(gV.repo)):
            res.append(vO.prodElemsVect( gV.repo[i] ))
        print("The product of elements from each vect is:", res)
    except Exception as e:
        print("Error!", e)

def maxElemsVectCommand():
    '''
    Prints the maximum element from each vector from the repository.
    '''
    try:
        res = []
        for i in range(len(gV.repo)):
            res.append(vO.maxElemsVect( gV.repo[i] ))
        print("The max element from each vect is:", res)
    except Exception as e:
        print("Error!", e) 
        
def minElemsVectCommand():
    '''
    Prints the minimum element from each vector from the repository.
    '''
    try:
        res = [] 
        for i in range(len(gV.repo)):
            res.append(vO.minElemsVect( gV.repo[i] ))
        print("The minimum element from each vect is:", res)
    except Exception as e:
        print("Error!", e)
        
def avgElemsVectCommand():
    '''
    Prints the average from each vector from the repository.
    '''
    try:
        res = [] 
        for i in range(len(gV.repo)):
            res.append(vO.avgElemsVect( gV.repo[i] ))
        print("The average of elements from each vect is:", res)
    except Exception as e:
        print("Error!", e)    
        
