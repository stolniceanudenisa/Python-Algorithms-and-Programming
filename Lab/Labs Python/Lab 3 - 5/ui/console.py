'''
Created on Oct 24, 2017

@author: iuan
'''

from domain.activities import *
from domain.changes import *
import ui.verifyFunctions as vFunc

#================================= RUN ==========================================
def run():
    '''
    Asks and executes the operation demanded on the list of scores named a_list
    IN:-
    OUT: the list with the changes demanded by the user
    Condis: the number inserted from the keyboard must be
    within the options numbers
    '''
    #Here you can add an option to choose a list
    a_list = [90,20,50,100,10,99,33,3]
    prev_list = a_list[:]
    
    while True:
        print("\nThe list is:", a_list)
        n=int(input("\nWhat option do you choose? Add=1, Insert=2, Remove=3, RemoveFrom=4,\nReplace=5, Less40=6, Sorted=7, SortGreater90=8, avgFrom=9" 
                     +" minFrom=10, \nmulFrom=11, FilterMul=12, FilterHigh=13, Undo=14, Exit=0 \n"))
        if n==1:#Add
            prev_list = a_list[:]
            print("The score to add:")
            score = vFunc.readUserInput()
            score = vFunc.isValidScore(score)
            addScore(score, a_list) 
            print("The score", score, "has been added to the list.")
            
        elif n==2:#Insert
            prev_list = a_list[:]
            print("The score to insert:")
            score = vFunc.isValidScore(vFunc.readUserInput())
            print("What will be the index at which you insert?\n")
            index = vFunc.isValidIndex(vFunc.readUserInput(), a_list)
            insertScore(score, index, a_list)
            print("The score", score, "has been added at index", index, "in the list.")
            
        elif n==3:#Remove
            prev_list = a_list[:]
            print("What will be the index at which you delete?\n")
            index = vFunc.isValidIndex(vFunc.readUserInput(), a_list) 
            removeScore(index, a_list)
            print("Score at index", index,"has been deleted.")

        elif n==4:#RemoveFrom
            prev_list = a_list[:]
            print("The indexes to delete from: ")
            index1, index2 = vFunc.isValidInterval(vFunc.readUserInput(), vFunc.readUserInput(), a_list)
            removeFrom(index1, index2, a_list)
            print("Scores from index", index1,"to index", index2,"have been deleted.")
            
        elif n==5:#Replace
            prev_list = a_list[:]
            print("What will be the index at which you replace?\n")
            index = vFunc.isValidIndex(vFunc.readUserInput(), a_list) 
            print("The replacing score:")
            score = vFunc.isValidScore(vFunc.readUserInput())
            replaceScore(index, score, a_list)
            print ("Element at index", index,"has been replaced with", score,".")

        elif n==6:#Less40
            print("Scores less than:")
            score = vFunc.isValidScore(vFunc.readUserInput())
            r = less40(score, a_list) #r is a temporary variable to make print easier to use
            print("The participants with less than given score are:", r)

        elif n==7:#Sort
            r = sort(a_list)
            print("The list sorted is:", r)            
        
        elif n==8:#SortG90
            print("Scores greater than:")
            score = vFunc.isValidScore(vFunc.readUserInput())
            r = sortG90(score, a_list)
            print("The list with scores greater than", score,"sorted is:", r)            
            
        elif n==9:#AVG From
            print("The indexes to calculate avg from: ")
            index1, index2 = vFunc.isValidInterval(vFunc.readUserInput(), vFunc.readUserInput(), a_list)
            r = avgFrom(index1, index2, a_list)
            print ("The average from index", index1,"to", index2,"is:", r)
            

        elif n==10:#MIN From
            print("The indexes to calculate minimum from: ")
            index1, index2 = vFunc.isValidInterval(vFunc.readUserInput(), vFunc.readUserInput(), a_list)
            r = minFrom(index1, index2, a_list)
            print ("The minimum number between indexes", index1,"and", index2,"is:", r)

        elif n==11:#MulScoreFrom
            print("The multiples of which score:")
            score = vFunc.isValidScore(vFunc.readUserInput())
            print("The indexes to find multiples from: ")
            index1, index2 = vFunc.isValidInterval(vFunc.readUserInput(), vFunc.readUserInput(), a_list)
            r = mulScoreFrom(score, index1, index2, a_list)
            print ("The multiples are:", r)   
            
        elif n==12: #Filter Multiple
            prev_list = a_list[:] 
            print("The multiples of which score to keep:")
            score = vFunc.isValidScore(vFunc.readUserInput())
            filMul(score, a_list)
            
        elif n==13: #Filter Greater Than
            prev_list = a_list[:]
            print("The elements greater than which score to keep:")
            score = vFunc.isValidScore(vFunc.readUserInput())
            filGT(score, a_list)
        
        elif n==14: #UNDO
            print("Undo operation called.")
            undoOnce(a_list, prev_list)
            #a_list = prev_list[:]
            
        elif n==0:
            print("Program closed.")
            break
        
        else:
            print("Please insert a number from the options!")




    #10 examples to see what does the program do
    print("\n\nThe 10 examples: \n")
    filGT(1, a_list)
    filMul(1, a_list)
    filGT(10, a_list)
    filMul(10, a_list)
    filGT(50, a_list)
    filMul(20, a_list)
    filGT(90, a_list)
    filMul(1, a_list)
    filGT(5, a_list)
    filMul(80, a_list)             

#======================================================================= MAIN =========================================================================================


