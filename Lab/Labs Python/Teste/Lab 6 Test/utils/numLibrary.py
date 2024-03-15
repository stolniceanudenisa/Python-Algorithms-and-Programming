'''
Created on Nov 7, 2017

@author: iuan
'''
def test_containsDigit():
    assert containsDigit(0, 24820) == True
    assert containsDigit(1, 1999) == True
    assert containsDigit(98, 2000) == False

def containsDigit(d, number):
    '''
    Checks if variable number contains the digit 'd'
    IN: d- a digit, number an integer
    OUT: true if contains, else returns boolean value 'False'
    CONDIS: d<=9 and d>=0
    '''
    if not(d<=9 and d>=0):
        return False
    
    while number!=0:
        if number %10 == d:
            return True
        number //= 10
        
    return False

test_containsDigit()