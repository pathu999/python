''' A
    AB
    ABC
    ABCD
    ABCD
'''
n=5
for i in range(n):
    for j in range(i+1):
        print(chr(j+65), end=" ") # end is used to take a space in two character
    print( ) #this print is use for next line print character
