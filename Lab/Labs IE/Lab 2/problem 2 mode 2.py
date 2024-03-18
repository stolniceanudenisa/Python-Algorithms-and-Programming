n = int(input("n="))
for i in range(2,n-1,1):
    if n%i==0:
        print("n=",n," is not prime")
    else:
        print("n=",n," is prime")
