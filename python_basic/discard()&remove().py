#discard keys to be deleted from the set from the discard() doesent exist in the set\
#the python is not give the error the programs maintain is control flow 
#on the other hand if the item to be deleted from the  set using remove()
#dosen't exist in the set the python will not give a error the programs maintain its contain flow


month=set(["jan","feb","march","april","may","jun","jully"])
print("/befor using descard method")

print(month)

month.discard("feb")

print("after discard")

print(month)

print("looping through the element")

for i in month:
    print(i)

month2=set(["jan","feb","march","april","may","jun","jully"])
#remove() 
print("after remove() is used")

month2.remove("jan")

print(month2)

#if the loop is done you have got the sequencly data flow
print("looping through to element")
for a in month2:
    print(a)