Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
num = int(input())
root = math.sqrt(num)
if int(root) == root:
    print("Number is perfect square")
else:
    print("Number is not perfect square")
    
SyntaxError: multiple statements found while compiling a single statement
>>> 