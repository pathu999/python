#recursion is function calling it self
import sys

print(sys.getrecursionlimit()) # this function is used to calculate limit of recursion

def greet():
    print("hello")
    greet()

#greet() if you want to  to print 1000 time 
