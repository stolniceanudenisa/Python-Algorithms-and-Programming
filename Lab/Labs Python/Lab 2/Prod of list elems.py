#Description: Compute the product of n given numbers from a list
#IN: a list named "a_list"
#OUT: the product int named "prod"
def prodFunction(a_list):
    prod=1
    for i in a_list:
        prod *=i
    return prod


#MAIN Program
l=[]
n=int(input("How many elements are in the list: "))

#indexing starts at 0
for i in range(n):
    temp=int( input("Give the element ["+ str(i+1)+ "] of the list: ") )
    l.append(temp)
    
print "The product is: ", prodFunction(l)
