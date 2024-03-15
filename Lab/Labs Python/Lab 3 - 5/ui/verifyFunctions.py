'''
Created on Nov 4, 2017

@author: iuan
'''

def readUserInput():
    '''
    Reads from the keyboard until a number is given, else an exception is raised
    IN: -
    OUT: a number
    CONDIS: -
    '''
    try:
        a = int(input())
        return a
    except ValueError:
        print("Not a number.")
    return readUserInput()


def isValidScore(score):
    '''
    Checks if variable score respects the problem conditions
    '''
    if isinstance(score, int) == 0:
        print("Error! The input __", score, "__ is not integer")
        score = isValidScore(readUserInput())
    elif score < 0:
        print("Error! The score can't be lower than 0 points")
        score = isValidScore(readUserInput())
    elif score > 100:
        print("Error! The score can't be more than 100 points")
        score = isValidScore(readUserInput())
    return score


def isValidIndex(index, a_list):
    if isinstance(index, int) == 0:
        print("Error! The index is not an integer")
        index = isValidIndex(readUserInput(), a_list)
    elif abs(index) >= len(a_list) or index < 0:
        print("Error! The index should be between", 0, "and",len(a_list)-1)
        index = isValidIndex(readUserInput(), a_list)
    return index
        
      
def isValidInterval(index1,index2, a_list):
    if isinstance(index1, int) == 0:
        print("Error! The first index is not an integer! Please type in a new one!")
        index1,index2 = isValidInterval(readUserInput(), index2, a_list)
        
    elif isinstance(index2, int) == 0:
        print("Error! The second index is not an integer! Please type in a new one!")
        index1,index2 = isValidInterval(index1,readUserInput(), a_list)
        
    elif index1 > index2:
        print("Error! The first index should be smaller than the second one! Please type new indexes!")
        index1,index2 =isValidInterval(readUserInput(),readUserInput(), a_list)
        
    elif index1 >= len( a_list) or index1 < 0:
        print("Error! The first index is not valid. Type new one!")
        index1,index2 = isValidInterval(readUserInput(), index2, a_list)
        
    elif index2 >= len( a_list) or index2 < 0:
        print("Error! The second index is not valid.Type new one!")
        index1,index2 = isValidInterval( index1, readUserInput(), a_list )
    
    return [index1,index2]
