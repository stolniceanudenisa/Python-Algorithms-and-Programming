n = int(input("n="))
p = 1
for i in range(2,n-1,1):
    if n%i==0:
        p = 0
        print("n=",n," is not prime")
        break
if p == 1:
    print("n=",n," is prime")
