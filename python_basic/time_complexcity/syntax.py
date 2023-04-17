'''Time complexity is an important concept in algorithm analysis, and it is applicable in any programming language, including Python. The time complexity of an algorithm describes how the running time of the algorithm increases with the size of the input.
In Python, you can analyze the time complexity of your code by using the built-in time module or 
the third-party timeit module. The time module provides functions for measuring 
the elapsed time of a Python code block, while the timeit module provides a simple way to time small bits of Python code.'''

#constant time complexcity
def constant_algo(n):
    return n*2

#linear time complexcity
def linear_algo(n):
    for i in range(n):
        print(i)

#quadtric_time complexcity
def quadratic_algo(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

#logairtmatic time complexcity
def logarithmic_algo(n):
    i = n
    while i >= 1:
        print(i)
        i //= 2

#Exceponential time complexcity        
def exponential_algo(n):
    if n <= 1:
        return n
    return exponential_algo(n-1) + exponential_algo(n-2)
