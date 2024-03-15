a=2
b=lambda x: {x: x+a}
c=b(2)
a=0
d=b(2)
print(c==d)

print(c== {2:3})
print(id(c)== id({2:3}))
print(c[2]==d[2])