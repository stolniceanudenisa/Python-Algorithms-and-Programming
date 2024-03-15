'''
Created on Nov 14, 2017

@author: iuan
# '''

import numpy as np
import verifyFunctions as vF

 
#================================ ADD SCALAR ==============================
def test_addScalar():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function addScore does not work properly
    Conditions:-
    '''
    try:
        assert addScalar( 1, [[1,0], [2,0], [0,1]] ) ==   [[2,1], [3,1], [1,2]]
        assert addScalar( 0, [[1,0], [2,0], [0,1]] ) ==   [[1,0], [2,0], [0,1]]
        assert addScalar( 2, [[1,0], [2,0], [0,1]] ) ==   [[3,2], [4,2], [2,3]]
        assert addScalar( -3, [[1,0], [2,0], [0,1]] ) ==  [[-2, -3], [-1, -3], [-3, -2]]
    except Exception as e:
        print("Assertion error! addScalar:", e)
 
def addScalar(sca, ar):
    '''
    Adds a scalar to a vector
    IN: an integer, a bidimensional list
    OUT: the 2d list changed
    CONDIS: -
    '''
    if not ar:
        raise Exception("The vector is empty!")
     
    ba = ar   
    #convert to numpy array
    ar = np.array(ar)
        
    #adds scalar
    ar += sca
     
    #convert to list
    ar = ar.tolist()
    ba[:] = ar
    return ar
     
#================================= SUMA ==================================
def test_sumaVector():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function addScore does not work properly
    Conditions:-
    '''
    try:
        assert sumaVector( [[1, 2, 3],[10, 12, 23]] , [[4, 2, 2],[1, 2, 2]] ) == [[5, 4, 5],[11, 14, 25]]
        assert sumaVector( [[1, 2, 3],[10, 12, 23]] , [[0, 0, 0],[0, 0, 0]] ) == [[1, 2, 3],[10, 12, 23]]
        assert sumaVector( [[1, 2, 3],[10, 12, 23]] , [[-1, -1, -1],[0, 0, 0]] ) == [[0, 1, 2],[10, 12, 23]]
        assert sumaVector( [[1, 2, 3],[10, 12, 23]] , [[-1, -1, -1],[0, 100, 0]] ) == [[0, 1, 2],[10, 112, 23]]
    except Exception as e:
        print("Assertion error! sumVector:", e)

def sumaVector(a, b):
    '''
    Calculates the sum of 2 vects of any dimensions
    IN: 2 lists with lists as elements (matrix)
    OUT: a list with lists as elements (representing a vector)
    CONDIS: lines of a = lines of b, same with columns
    '''
    if not a:
        raise Exception("The vector is empty!")
    if not b:
        raise Exception("The vector is empty!")
    
    if vF.validVectors(a, b) != True:
        raise Exception("Dimensions not equal!")
        return None   
    
    ar1 = np.array(a)
    ar2 = np.array(b) 
    suma = ar1 + ar2
    suma = suma.tolist()
    return suma

#================================== SUBTRACTION =========================
def test_difVector():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function addScore does not work properly
    Conditions:-
    '''
    try:
        assert difVector( [[1,2,3],[10,12,23]] , [[4,2,2],[1,2,2]] ) == [[-3, 0, 1], [9, 10, 21]]
        assert difVector( [[1,2,3],[10,12,23]] , [[0,0,0],[0,0,0]] ) == [[1, 2, 3], [10, 12, 23]]
        assert difVector( [[1,2,3],[10,12,23]] , [[1, 1, 1],[0, 0, 0]] ) == [[0, 1, 2],[10, 12, 23]]
        assert difVector( [[1,2,3],[10,12,23]] , [[0,0,0],[0,0,0]] ) == [[1, 2, 3], [10, 12, 23]]
        assert difVector( [[1,2,3],[10,12,23]] , [[-1, -1, -1],[0, 0, 0]] ) == [[2, 3, 4], [10, 12, 23]]
    except Exception as e:
        print("Assertion error! difVector", e)
 
def difVector(a, b):
    '''
    Returns the difference between a and b
    IN: 2 lists representing vectors2d
    OUT: a list repr. a vector2d
    CONDIS: lines of a = lines of b, same with columns
    '''
    if not a:
        raise Exception("The vector is empty!")
    if not b:
        raise Exception("The vector is empty!")
    
    if vF.validVectors(a, b) != True:
        raise Exception("Dimensions not equal!")
        return None
    
    ar1 = np.array(a)
    ar2 = np.array(b) 
    dif = ar1 - ar2
    dif = dif.tolist()
    return dif

#================================= PRODUCT ========================================
def test_prodVector():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function addScore does not work properly
    Conditions:-
    '''
    try:
        assert prodVector([[1,2,3],[10,12,23]], [[4,2],[1,2],[1,2]]) == [[9,12],[75,90]]
        assert prodVector(   [[0, 0]], [[0], [0]]  ) == [[0]]
        assert prodVector([ [1, 1], [1, 1] ], [ [2,2,2,2], [2,2,2,2] ]) == [[4,4,4,4], [4,4,4,4]]
        assert prodVector( [[5, 2]], [[7], [8]]) == [[51]]
    except Exception as e:
        print("Assertion error! prodVector:", e)
    
def prodVector(a, b):
    '''
    Calculates the product of 2 vectors2D (matrices).
    IN: two matrices
    OUT: a matrix representing the product of the given parameters
    CONDIS: columns of 'a' equal to lines of 'b'
    '''
    if not a:
        raise Exception("The vector is empty!")
    if not b:
        raise Exception("The vector is empty!")
    
    if len(a[0]) != len(b):
        raise Exception("Columns of 'a' not equal to lines of 'b'!")
    
    ar1 = np.array(a)
    ar2 = np.array(b) 
    res = np.dot( ar1, ar2 )
    res = res.tolist()
    return res

#=============================== REDUCTION OPERATIONS ========================== 'views module'
#=============================== ELEMENTS SUM ===================================
def test_sumElemsVect():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function addScore does not work properly
    Conditions:-
    '''
    try:
        assert sumElemsVect( [[10,9]] ) == 19
        assert sumElemsVect( [[9,9,9,9,9,9,9]] ) == 63
        assert sumElemsVect( [[10, 8, 5, 8, 5, 3]] ) == 39 
        assert sumElemsVect( [[10,10], [9, 9]] ) == 38  
        assert sumElemsVect( [[-1,-9], [9, 9]] ) == 8 
    except Exception as e:
        print("Assertion error! sumElemsVect", e)

def sumElemsVect(vect):
    '''
    Returns the sum of all elements from a vector 'vect'
    IN: a matrix 'vect'
    OUT: an integer
    CONDIS: vector not empty
    '''
    if not vect:
        raise Exception("The vector is empty!")
    
    ar = np.array(vect)
    suma = np.sum(ar) 
    return suma

#======================= ELEMENTS PRODUCT ===========================
def test_prodElemsVect():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function addScore does not work properly
    Conditions:-
    '''
    try:
        assert prodElemsVect( [[10,9]] ) == 90
        assert prodElemsVect( [[9,9,9,9,9,9,9]] ) == 4782969
        assert prodElemsVect( [[10, 8, 5, 8, 5, 3]] ) == 48000
        assert prodElemsVect( [[10,10], [9, 9]] ) == 8100   
    except Exception as e:
        print("Assertion error! prodElemsVect", e)

def prodElemsVect(vect):
    '''
    Returns the product of all elements from a vector 'vect'
    IN: a matrix 'vect'
    OUT: an integer
    CONDIS: vector not empty
    '''
    if not vect:
        raise Exception("The vector is empty!")
    
    ar = np.array(vect)
    res = np.prod(ar)
    return res

#================================= ELEMENTS AVERAGE =============================
def test_avgElemsVect():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function addScore does not work properly
    Conditions:-
    '''
    try:
        assert avgElemsVect( [[10,9]] ) == 9.5
        assert avgElemsVect( [[9,9,9,9,9,9,9]] ) == 9
        assert avgElemsVect( [[10, 8, 5, 8, 5, 3]] ) == 6.5
        assert avgElemsVect( [[10,10], [9, 9]] ) == 9.5   
    except Exception as e:
        print("Assertion error! avgElemsVect", e)

def avgElemsVect(vect):
    '''
    Returns the average of all elements from a vector 'vect'
    IN: a matrix 'vect'
    OUT: a float
    CONDIS: vector not empty
    '''
    if not vect:
        raise Exception("The vector is empty!")
    
    ar = np.array(vect)
    res = np.mean(ar)
    return res
            
#================================= ELEMENTS MIN =============================
def test_minElemsVect():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function addScore does not work properly
    Conditions:-
    '''
    try:
        assert minElemsVect( [[1,2,3],[10,12,23]] ) == 1
        assert minElemsVect( [[1,-5,3],[10,12,23]] ) == -5
        assert minElemsVect( [[1,2,3],[10,12,0]] ) == 0
        assert minElemsVect( [[1, 1, 1],[1, 1, 1]] ) == 1
    except Exception as e:
        print("Assertion error! minElemsVect", e)

def minElemsVect(vect):
    '''
    Returns the minimum of all elements from a matrix 'vect'
    IN: a matrix 'vect'
    OUT: an integer
    CONDIS: vector not empty
    '''
    if not vect:
        raise Exception("The vector is empty!")
    
    ar = np.array(vect)
    res = np.min(ar)
    return res 
    
#================================= ELEMENTS MAX =============================
def test_maxElemsVect():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function addScore does not work properly
    Conditions:-
    '''
    try:
        assert maxElemsVect( [[1,2], [4,5]] ) == 5
        assert maxElemsVect( [[1,2], [4,1]] ) == 4
        assert maxElemsVect( [[-1, -1], [-1, -1]] ) == -1
        assert maxElemsVect( [[0, 0], [2, 2]] ) == 2
    except Exception as e:
        print("Assertion error! maxElemsVect", e)

def maxElemsVect(vect):
    '''
    Returns the maximum of all elements from a matrix 'vect'
    IN: a matrix 'vect'
    OUT: an integer
    CONDIS: vector not empty
    '''
    if not vect:
        raise Exception("The vector is empty!")
    
    ar = np.array(vect)
    res = np.max(ar)
    return res
    
def assertFunctions():
    '''
    Runs functions that check the main commands
    IN: -
    OUT: -
    '''
    test_addScalar()
    test_difVector()
    test_sumaVector()
    test_prodVector()
    
    test_maxElemsVect()
    test_minElemsVect()
    test_avgElemsVect()    
    test_prodElemsVect()
    test_sumElemsVect()
              
