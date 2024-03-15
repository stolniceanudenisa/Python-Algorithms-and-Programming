'''
Created on Oct 24, 2017

@author: iuan
'''

#================================= PRIME ==========================
def test_isPrime():
    '''
    Checks if the function works properly and handles the exceptions cases
    IN:-
    OUT: error message in case the function does not give the expected output
    Conditions:-
    '''
    assert isPrime(0)==False
    assert isPrime(1)==False
    assert isPrime(4)==False
    assert isPrime(2)==True
    assert isPrime(37)==True
    assert isPrime(39)==False
    assert isPrime(17)==True

def isPrime(n):
    '''
    Checks if a given number is prime or not
    IN: the number 'n'
    OUT: a boolean value, true if its prime, false if its not
    CONDIS: n is positive and less than 2*10^9
    '''
    if n<2:
        return False
    elif n==2 or n==3:
        return True
    elif n%2==0:
        return False
    d=3
    while(d*d<=n and n%d!=0):
        d+=2
    if n%d==0:
        return False
    return True
