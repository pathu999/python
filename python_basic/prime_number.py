#prime number 
num=10
for i in range(2,num):
    if num % i == 0: 
        print("the number is not a prime")
        break
else:
    print("the number is prime")