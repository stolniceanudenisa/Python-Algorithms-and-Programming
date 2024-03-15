

def f():
    global l
    l=[0,0,0]
    l[1]=9




#Main
print "Testing: "
l=[4,5,7,8]

print "l is: ", l

f()
print l








print

a=[2,3,4]
b =a[:]
print id(a)
a.remove(3)
print id(b)
print b
t=12,21,67


print t[0]
