'''
Created on Oct 30, 2017

@author: iuan
'''

#======================================FILTER MULTIPLES============================
def test_filMul():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    assert filMul(10, [0,5,10,15,20,90,100]) == [10,20,90,100]
    assert filMul(5, [0,5,10,15,20,90,100]) == [5,10,15,20,90,100]
    assert filMul(1, [0,5,10,15,20,90,100]) == [5,10,15,20,90,100]
    assert filMul(5, [2,4,6,8,12,14,16]) == []
    assert filMul(10, []) == []

def filMul(score, a_list):
    '''
    Removes from a list the scores which are not multiples of var 'score'
    IN: a positive number and a list with numbers
    OUT: same list in memory only with multiples of score
    CONDIS: score between 1 and 100
    '''
    if score == 0:
        #raise ValueError('Multiples of 0.')
        return a_list
    aux=[]
    for i in range(len(a_list)):
        if a_list[i]!=0 and a_list[i] % score == 0: #is multiple of score?
            aux.append(a_list[i])
    a_list[:] =aux[:]
    return a_list
    
#======================================FILTER GREATER THAN============================
def test_filGT():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    assert filGT(10, [0,5,10,15,20,90,100]) == [10,15,20,90,100]
    assert filGT(10, []) == []
    assert filGT(1, [0,5,10,15,20,90,100]) == [5,10,15,20,90,100]
    assert filGT(100, [0,5,10,15,20,90,100]) == [100]
    assert filGT(90, [0,5,10,15,20]) == []

def filGT(score, a_list):
    '''
    Removes from a list the elements lesser than a given value
    IN: a positive number and a list with numbers
    OUT: same list in memory only with elements greater than 'score'
    CONDIS: score between 1 and 100
    '''
    aux=[]
    for i in range(len(a_list)):
        if a_list[i] >= score: #is greater than score?...HIGHER OR EQUAL
            aux.append(a_list[i])
    a_list[:]=aux[:]
    return a_list


def undoOnce(a_list, prev_list):
    '''
    Changes the list with the previous version of it
    IN: the initial list, the previous one
    OUT: initial list takes the eelems from the previous one
    CONDIS: -
    '''
    a_list[:] = prev_list[:]
    return a_list
