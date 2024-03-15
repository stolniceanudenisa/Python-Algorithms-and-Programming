'''
Created on Oct 24, 2017

@author: iuan
'''
#==============================ADD==================================
def test_addScore():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function addScore does not work properly
    Conditions:-
    '''
    assert addScore(69, [4,5,6])==[4,5,6,69]
    assert addScore(110, [1,2,3])==[1,2,3]
    assert addScore(-1, [1,2])==[1,2]
    assert addScore(10, [])==[10]
    assert addScore(23.5, [1])==[1, 23.5]

def addScore(score, a_list):
    '''
    Descr: Adds the score of a competitor to the list with all competitor's scores
    IN: a number score
    a list with integers named a_list
    OUT: the changed a_list having the variable score appended
    at the end of it
    CONDIS: score >=0 and score <=100
    '''
    if not(score >=0 and score <=100):
        return a_list
    
    a_list.append(score)
    return a_list

#=================================INSERT==========================
def test_insertScore():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function insertScore does not work properly
    Conditions:-
    '''
    assert insertScore(98, 3, [1,2,3])==[1,2,3,98]
    assert insertScore(10.5, 1, [1,2,3])==[1, 10.5, 2, 3]
    assert insertScore(20, -1, [1,2])==[1,2]
    assert insertScore(50, 3, [])==[]
    assert insertScore(-200, 1, [1,2,3])==[1,2,3]
    assert insertScore(20, 0, [])==[20]
    

def insertScore(score, index, a_list):
    '''
    Inserts the score of the concurent at a given index in a list
    IN: a number 'score',
    a position in list starting from 0,
    a list with numbers
    OUT: if conditions are met it returns the changed function
    CONDITIONS: index must be lesser or equal than the length of the list and positive
    score >=0 and score <=100
    '''
    if not(score >=0 and score <=100):
        return a_list
    
    if index<0 or index > len(a_list):
        return a_list

    #goes backwards and changes the position of elems from list
    a_list.append(0)
    for i in range(len(a_list)-1, index, -1):
        a_list[i]=a_list[i-1]
    a_list[index]=score
    
    return a_list

#=================================REMOVE==========================
def test_removeScore():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function removeScore does not work properly
    Conditions:-
    '''
    assert removeScore(2, [3,4,21,2,5]) == [3,4,2,5]
    assert removeScore(1, []) == []
    assert removeScore(6, [1,2])==[1,2]
    assert removeScore(-1, [7])==[7]
    assert removeScore(0, [4])==[]
    
def removeScore(index, a_list):
    '''
    Delete score of participant at given index
    IN: a natural number and a list
    OUT: the list without one element if condis respected
    Condis: index >= 0 and index <= length of list
    '''
    if index<0 or index > len(a_list)-1:
        return a_list
    
    for i in range(index, len(a_list)-1):
        a_list[i] = a_list[i+1]
    a_list.pop()
    
    return a_list

#=================================REMOVE FROM==========================
def test_removeFrom():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not work properly
    Conditions:-
    '''
    
    assert removeFrom(0,2, [1,2,3,4,5,6,7,8]) == [4,5,6,7,8]
    assert removeFrom(3, 3, [1,2,3,4]) == [1,2,3]
    assert removeFrom(3, 5, [1,2,3,4,5,6,7]) == [1,2,3,7]
    assert removeFrom(0, 2, []) == []
    assert removeFrom(5, 6, [1,2]) == [1,2]
    assert removeFrom(0, 2, [1,2,3]) == []
    assert removeFrom(0,0, []) == []

def removeFrom(index1, index2, a_list):
    '''
    Delete score of participants from index1 to index2
    IN: a natural number 
    OUT: the list without one element if condis respected
    CONDIS: 
    index2 >= index1, index1 positive, index2 less than length of list
    '''
    if index2 < index1 or index2>= len(a_list) or index1<0:
        return a_list
    
    dif=index2-index1 + 1
    for i in range(index1, len(a_list)-dif):
        if i+dif >= len(a_list):
            break
        a_list[i] = a_list[i + dif]

    for i in range(0, dif):
        a_list.pop()

    return a_list


#================================REPLACE===============================
def test_replaceScore():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    
    assert replaceScore(1, 20, [10,30,30,40]) == [10,20,30,40]
    assert replaceScore(0, 40, []) == []
    assert replaceScore(2, 50, [1,2]) == [1,2]
    assert replaceScore(1, 110, [2]) == [2]
    assert replaceScore(2, 10, [1,2,3]) == [1,2,10]

def replaceScore(index, score, a_list):
    '''
    Replace score of element at given index
    IN: a number 'index'
        the replacing number score
        and a list
    OUT: the list with 1 element replaced
    CONDIS: score between 0 and 100
        index between 0 and length of list-1
    '''
    if not(score >=0 and score <=100):
        return a_list
    if index>= len(a_list):
        return a_list

    a_list[index] = score
    return a_list
    
#=================================PRINT PRIME==========================
from utils.numlibrary import isPrime

def test_printPrime():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    
    assert printPrime(1, 5, [2,3,4,5,6,7,8,9]) == [3,5,7]
    assert printPrime(0, 0, [4,5,6]) == []
    assert printPrime(0, 0, [2,4,6]) == [2]
    assert printPrime(3, 6, [1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == [5,7]
    assert printPrime(5, 2, [1,2,3]) == [1,2,3]

def printPrime(index1, index2, a_list):
    '''
    Prints the prime numbers from index1 til index2
    IN: two indices and a list
    OUT: return a list with numbers that respect the condition in the description
    CONDIS:  index2 >= index1, index1 positive, index2 less than length of list
    '''
    if index2 < index1 or index2>= len(a_list) or index1<0:
        return a_list

    aux = []
    for i in range(index1, index2+1):
        elem = a_list[i]
        if isPrime(elem):
            aux.append(elem)
            
    return aux

#================================== PRINT ODD ============================
def printOdd(index1, index2, a_list):
    '''
    Prints the odd numbers from index1 til index2
    IN: two indices and a list
    OUT: return a list with numbers that respect the condition in the description
    CONDIS:  index2 >= index1, index1 positive, index2 less than length of list
    '''
    if index2 < index1 or index2>= len(a_list) or index1<0:
        return a_list

    aux = []
    for i in range(index1, index2+1):
        elem = a_list[i]
        if elem %2==1:
            aux.append(elem)
            
    return aux

def test_printOdd():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    assert printOdd(0, 2, [1,2,3,4,5,6,7]) == [1,3]
    assert printOdd(1, 1, [1,2,3,4]) == []
    assert printOdd(0, 3, []) == []
    assert printOdd(1, 4, [2,3,4,5,6,7,8,9]) == [3,5]
    assert printOdd(0, 3, [2,4,6,8,10,12,2,2]) == []

#================================= LESS 40 ==========================N
def test_less40():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    assert less40(40,[3,4,40,50,60,52]) == [3,4]
    assert less40(40, [] ) == []
    assert less40(40,[39,41,38] ) ==[39,38]
    assert less40(40, [45,47,48,57,90] ) == []
    assert less40(40, [1] ) == [1]

def less40(score, a_list):
    '''
    Prints the sum of elements from index1 to index 2
    IN: two indices and a list
    OUT: return a list with scores less than 40
    CONDIS:  
    '''
    temp = []
    for elem in a_list:
        if elem < score:
            temp.append(elem)

    return temp

#================================= SORT ==========================
def test_sort():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    
    assert sort( [10,20,30] )== [30,20,10]
    assert sort( [9,8,7,6,5] ) == [9,8,7,6,5]
    assert sort( [] ) == []
    assert sort( [2,2,2,2] ) == [2,2,2,2]
    assert sort( [1,0,1,0] ) == [1,1,0,0]

def sort(a_list):
    '''
    Sorts a given list in descending order
    IN: a list
    OUT: return a sorted list
    CONDIS:-
    '''
    l = len(a_list)
    a2_list = a_list[:]
    for i in range(0, l-1):
        for j in range(i+1, l):
            if a2_list[i] < a2_list[j]: #interchange
                aux = a2_list[i]
                a2_list[i] = a2_list[j]
                a2_list[j] = aux

    return a2_list

#================================= SORT GREATER 90 ==========================
def test_sortG90():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    
    assert sortG90(90, [10,20,30,90] )== []
    assert sortG90(90, [90,91,100] ) == [100,91]
    assert sortG90(90, [] ) == []
    assert sortG90(90, [92,95,93,94,97,96] ) == [97,96,95,94,93,92]
    assert sortG90(90, [100] ) == [100]

def sortG90(score, a_list):
    '''
    Prints the scores greater than n
    IN: a list
    OUT: return a list with scores greater than 90 sorted in descending order, empty if none greater than 90
    CONDIS:-
    '''
    temp=[]
    for elem in a_list:
        if elem > score:
            temp.append(elem)
    temp = sort(temp)
    return temp
 
#=========================================== AVG FROM =======================================
def test_avgFrom():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    
    assert avgFrom( 1, 3, [10,20,30,10,20] ) == 20
    assert avgFrom( 0, 2, [1,2,5,7,8] ) == 8.0/3
    assert avgFrom( 0, 3, [10,10,10,9] ) == 9.75
    assert avgFrom( 0, 1, [10,9,10,9] ) == 9.5
    assert avgFrom( 0, 0, [] ) == []
    

def avgFrom(index1, index2, a_list):
    '''
    Calculates the average score of elements between index1 and index2
    IN: 2 indices and a list
    OUT: a float data type
    CONDIS: index2 >= index1, index1 positive, index2 less than length of list
    '''
    if index2 < index1 or index2>= len(a_list) or index1<0:
        return a_list
    suma = 0
    nr = index2 - index1 + 1
    for i in range(index1, index2+1):
        suma += a_list[i]
        
    res = float(suma) / nr
    return res

#=========================================== MIN FROM =======================================
def test_minFrom():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    assert minFrom( 1, 3, [10,20,30,10,20] ) == 10
    assert minFrom( 0, 2, [1,2,5,7,8] ) == 1
    assert minFrom( 0, 5, [1,1,1,1,1,0] ) == 0
    assert minFrom( 0, 0, [100] ) == 100
    assert minFrom( 0, 2, [1,1,1] ) == 1

def minFrom(index1, index2, a_list):
    '''
    Calculates the average score of elements between index1 and index2
    IN: 2 indices and a list
    OUT: a float data type
    CONDIS: index2 >= index1, index1 positive, index2 less than length of list
    '''
    if index2 < index1 or index2>= len(a_list) or index1<0:
        return a_list
    minim = 110

    for i in range(index1, index2+1):
        if a_list[i] < minim:
            minim = a_list[i]
        
    return minim

#=========================================== MUL SCORE FROM =======================================
def test_mulScoreFrom():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    assert mulScoreFrom(10, 1, 3, [10,20,30,10,20] ) == [20,30,10]
    assert mulScoreFrom(2, 0, 2, [1,2,5,7,8] ) == [2]
    assert mulScoreFrom(10, 0, 5, [1,1,1,1,1,0] ) == []
    assert mulScoreFrom(2, 0, 0, [100] ) == [100]
    assert mulScoreFrom(1, 0, 2, [1,50,90] ) == [1,50,90]

def mulScoreFrom(score, index1, index2, a_list):
    '''
    Returns a list with scores between indices which are multiples of 'score'
    IN: a positive number, two positive numbers, a list
    OUT: a list with elements multiples of 'score'
    CONDIS: index2 >= index1, index1 positive, index2 less than length of list
    score between 1 and 100
    '''
    if score == 0:
        #raise ValueError('Multiples of 0.')
        return a_list
    if index2 < index1 or index2>= len(a_list) or index1<0:
        return a_list
    temp = []
    for i in range(index1, index2+1):
        if a_list[i]!=0 and a_list[i] % score == 0:
            temp.append(a_list[i])
             
    return temp