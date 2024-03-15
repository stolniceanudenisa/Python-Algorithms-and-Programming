'''
Created on Nov 14, 2017

@author: iuan
'''

def test_validVectors():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function addScore does not work properly
    Conditions:-
    '''
    try:
        assert validVectors([[1], [2]], [[5], [6]]) == True
        assert validVectors([[1, 9], [2, 5]], [[5], [6]]) == False
        assert validVectors([[1], [2]], [ [6,9,8] ]) == False
    except Exception as e:
        print("Assertion error! validVectors:", e)

def validVectors(a, b):
    '''
    Checks if the vectors have the same lines and columns.
    IN: 2 matrices
    OUT: a boolean value, true if they are valid and have same dimensions, false if else
    CONDIS: -
    '''
    if len(a)!=len(b):
        return False 
    
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            return False  
         
    return True

test_validVectors()  