#Problem 1:
# a) Compute the sum of the first n natural numbers
# b) Check if a given integer number n is prime
# c) Compute the greatest common divisor between two integers a and b
# d) Compute the first prime number greater than a given integer n
# e) Print the first k prime numbers grater than a given integer n 

def readNumber():
    print("Give a natural number")
    try:
        n = int(input())
        return n
    except:
        return readNumber()

def writeResult(result):
    print("Result is: ",result)

def problemA(n):
    sum = 0
    for i in range(0,n+1):
        sum += i
    return sum

def problemB(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

def problemC(a, b):
    while b != 0:
        (a,b) = (b, a%b)
    return a

def problemD(n):
    n += 1
    while(problemB(n) == False):
        n += 1
    return n

def problemE(n, k):
    while(k > 0):
        n = problemD(n)
        print("Prime numer:",n)
        k -= 1

if __name__ == '__main__':
    # n = readNumber()
    # sum = problemA(n)
    # writeResult(sum)
    
    # result = problemB(n)
    # writeResult(result)

    # a = readNumber()
    # b = readNumber()
    # gdc = problemC(a, b)
    # writeResult(gdc)

    # n = readNumber()
    # result = problemD(n)
    # writeResult(result)

    # n = readNumber()
    # k = readNumber()
    # problemE(n,k)

    a = [1,2,3,4,5,6]
    a[3,:] = (2,7)
    print(a)


