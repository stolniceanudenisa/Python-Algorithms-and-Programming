
def test_mySearch():
    '''
    Tests the function
    '''
    assert mySearch([1,2,3,4,5,6], lambda x: x%2==0) == [2,4,6]

def mySearch(myList, cond):
    '''
    Searches the list elements that are in condition.
    IN: a list, a function
    OUT: a list
    CONDIS: -
    '''
    res = []
    for i in range(len(myList)):
        if cond(myList[i]):
            res.append(myList[i])
    return res


def test_mySort():
    '''
    Tests the function
    '''
    
    assert mySort( [1,2,3,4,5,6], lambda x, y: x > y) == [6,5,4,3,2,1]


def mySort(l, relation):
    '''
    Sorts the elements from a list by a given relation.
    IN: a list, a function
    OUT: -
    CONDIS: -
    '''
    for i in range(0, len(l)-1):
        for j in range(i+1, len(l)):
            if not relation(l[i], l[j]):
                #print("ai aj")
                l[i], l[j] = l[j], l[i]    
    return l
    
test_mySort()   
    