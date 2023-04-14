''' A B C D 
    A B C
    A B
    A'''
for i in range(4):
    for j in range(4-i):
        print(chr(j+65),end=" ")
    print( )