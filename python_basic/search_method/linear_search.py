pos = -1

def search(list, n):
    i=0

    while i < len(list):
        if list[i] ==n:
            globals()['pos'] = i
            return True
        i = i + 1
    
    return False

list=[2,4,5,6,7,8,9]  

n=2
if search(list,n):
    print("Fond as", pos+1)
else:
    print("not Found")