'''Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]
'''
#method 1
def swaplist(newlist):
    size = len(newlist)
    
    temp = newlist[0]
    newlist[0] = newlist[size -1]
    newlist[size -1] = temp
    return newlist

newlist = [12,35,9,56,24]
print(swaplist(newlist))


#method2

def swapnewlist1(newlist1):
    newlist1[0],newlist1[-1] = newlist1[-1],newlist1[0]
    return newlist1
newlist1 = [12,35,9,56,24]
print(swapnewlist1(newlist1))

#method3 
def swapnewlist2(newlist2):
    get = newlist2[-1],newlist2[0]
    get = newlist2[0],newlist2[-1]
    return newlist2
newlist2 =  [12,35,9,56,24]
print(swapnewlist2(newlist2))