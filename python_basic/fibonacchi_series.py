#0,1,1,2,3,5,8,13
def fibo(n):
    a = 0
    b = 1

    if n == 1:
        print(1)
    else:    
     print(a)
    print(b)

    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
fibo(0)