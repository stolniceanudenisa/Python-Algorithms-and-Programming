'''
Created on Nov 7, 2017

@author: iuan
'''
def test_deleteElem():
    assert deleteElem(0, [1,2,3,4]) == [2,3,4]
    assert deleteElem(1, [1,2,3,4]) == [1,3,4]
    assert deleteElem(3, [1,2,3,4]) == [1,2,3]
    assert deleteElem(2, [1,2,3,4]) == [1,2,4]
    assert deleteElem(0, [1]) == []

def deleteElem(index, a_list):
    '''
    Deletes element from a list at index 'index'
    IN: a positive number, a list
    OUT: the list without the elem at given index
    Condis: index >= 0 and index <= length of list
    '''
    if index<0 or index > len(a_list)-1:
        return a_list
    
    for i in range(index, len(a_list)-1):
        a_list[i] = a_list[i+1]
    a_list.pop()
    
    return a_list

test_deleteElem()