#hecks if a is prime or not
#IN: an int "a"
#OUT: true if a is prime or false if a is not prime
def prim(a):
    if a==0 or a==1:
        return False
    elif a==2 or a==3:
        return True
    elif a%2==0:
        return False
    d=3
    while (d*d<=a and not(a%d==0)):
        d+=2
    if a%d==0:
        return False
    return True



#Infinite loop to not start again and again the program
while True:
    
    a=int(input("The number which we want to check if its prime is: "))
    if a<0:
        a*=-1
    #Calls the function prime
    if prim(a)==True:
        print(a, "is prime.")
    else:
        print(a, "is NOT prime.")
