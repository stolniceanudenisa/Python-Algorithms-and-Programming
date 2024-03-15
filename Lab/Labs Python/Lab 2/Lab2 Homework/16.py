def numberFigure():
    '''
    Description: reads numbers until input is 0 and returns how many have unit
    figure smaller than tens figure
    IN: -
    OUT: an int result showing how many numbers respect the condition
    '''
    n=int(input("Give a number: "))
    result=0
    
    while n!=0:
        if n%10 < n/10%10:
            result +=1
        n=int(input("Give a number: "))
        
    return result


#MAIN
print numberFigure(), " numbers have unit figure smaller than tens figure."

