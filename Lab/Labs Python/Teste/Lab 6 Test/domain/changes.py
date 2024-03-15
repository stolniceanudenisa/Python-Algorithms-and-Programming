'''
Created on Nov 7, 2017

@author: iuan
'''
from utils.listChanges import deleteElem
from utils.numLibrary import containsDigit

def test_deleteElemDigit():
    assert deleteElemDigit(3, [234, 33, 45, 3, 10]) == [45,10]
    

def deleteElemDigit(d, a_list):
    '''
    Deletes from the list all elements that contain the given digit 'd'
    IN: a digit, a list
    OUT: the list without some elements or not
    CONDIS: d>=0 and d<=9
    '''    
    for i in range(len(a_list)-1, -1, -1):
        print(i)
        if (containsDigit(d, a_list[i])):
            deleteElem(i, a_list)
    
    return a_list
            

a_list = [234, 33, 45, 3, 10]
d=int(input("Give digit:"))

test_deleteElemDigit()

print (deleteElemDigit(d, a_list))