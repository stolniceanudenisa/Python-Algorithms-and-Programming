#Problem 2
# Compute the age of a person in number of days
# input date birth 3 integers dd mm yyyy & current date
# output number of days
from s01_p1 import readNumber, writeResult


def bisect(y):
    if y % 4 == 0 and y%100 != 0:
        return True
    elif y%400 == 0:
        return True
    else:
        return False
def computeYears(y):
    days = 0
    for i in range(0,y):
        if bisect(i) == True:
            days += 366
        else:
            days += 365
    return days

def computeMonths(m, is_bisect):
    days = 0
    long_months = [1,3,5,7,8,10,12]
    for i in range (1, m):
        if i == 2:
            if is_bisect == True:
                days += 29
            else:
                days += 28
        elif i in long_months:
            days += 31
        else:
            days += 30
    return days

def computeDays(d,m,y):
    days = computeYears(y)
    days += computeMonths(m, bisect(y))
    days += d
    return days

if __name__ == '__main__':
    d = readNumber()
    m = readNumber()
    y = readNumber()
    result_birth = computeDays(d,m,y)
    d = readNumber()
    m = readNumber()
    y = readNumber()
    result_current = computeDays(d,m,y)
    diff = result_current- result_birth
    writeResult(diff)