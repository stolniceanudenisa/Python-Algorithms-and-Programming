#Verify if a number n is a square root
n=49

print(n**(1/2)) #(var gresita) trebuie considerate float, acuma is int
print(n**(1.0/2.0))  #le-am pus un punct

print ( int( n ** (1.0 / 2.0) ) == n** (1.0 / 2.0) )
#true if n=49,64,81
#false if not square root





#Show what number is on position k in the set
#1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
print "Second problem comes now:"

import math

k=10
delta=math.sqrt(1+8*k)


if delta!=int(delta):
    if delta%2==0:
        delta=int(delta) + 1
    else:
        delta=int(delta) + 2
           

result = (-1 + delta)/2
print ('The element on position ', k, ' is: ', result)
