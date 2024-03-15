'''
Created on Dec 16, 2017

@author: iuan
'''
#sort and search

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
                
def mySearch(l, cond):
    '''
    Searches elements in a list that respect a given condition and appends them in a list.
    IN: a list, a function
    OUT: a list
    CONDIS: -
    '''
    res = []
    for elem in l:
        if cond(elem):
            res.append(elem)
    return res

def getNext(index):
    return index+1

def initSolution(domain):
    return domain[0]   

def isConsistent(sol, myList, constraints):
    for c in constraints:
        if not c(sol, myList):
            return False
    return True

def getLast(domain):
    return domain[ len(domain) - 1 ]

def isSolution(sol, param):
    return len(sol) == param[0] 

def myBacktracking(param, myList, constraints):
    '''
    Forms groups of elements from the myList.
    IN: a list, a list, a list with functions.
    OUT: one or more lists with indices
    CONDIS: -
    '''
    domain = [  i  for i in range(-1, len(myList))   ]
    
    k = 0 #indexul curent din solutie 'sol

    sol = [] #solutia, la fiecare pas, lista cu indici

    sol.append(initSolution(domain))

    while(k >= 0):
        isSelected = False
        while not isSelected and sol[k] < getLast(domain):
            sol[k] = getNext( sol[k] )
            isSelected = isConsistent( sol, myList, constraints )
        
        if isSelected:
            if isSolution(sol, param):
                #print("YIELDEZ!!!!", sol)
                yield sol
            else:
                k = k+1
                sol.append(initSolution(domain))
        else:
            sol.pop()
            k = k - 1





