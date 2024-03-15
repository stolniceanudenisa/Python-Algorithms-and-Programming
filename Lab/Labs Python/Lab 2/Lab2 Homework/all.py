#1
def controlDigit(n):
    '''

    '''
    if(n/10==0):
        return n
    suma=0
    while n!=0:
        suma += n%10
        n /= 10
    return controlDigit(suma)

#2
def dayMonth(year, days):
    i=0
    if days <= 31:
        i+=1
    days -= 31

    if year%4==0:
        if days <= 29:
            

    print str(days) + ".0" + str(i), ".", year











#MAIN
print controlDigit(1971)
print dayMonth(2004, 15)
