n = int(input("n="))
s = 0
for i in range(0,n+1,1):
    if i%2==0:
        s = s + i
    else:
        i = i + 1
print("The sum of even numbers up to ",n," is ",s)
        
