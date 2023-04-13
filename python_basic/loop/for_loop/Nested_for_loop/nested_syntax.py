#user input number of rows 
rows=int(input("Enter the number of rows"))

#outer loop print the number of rows
for i in range(0,rows+1):

#internal(nested loop)
        for j in range(i):
                print ("*",end=" ")
        print( )
