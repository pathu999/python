# the one task in multiple process and again
# you brake down into a thread (each part is called thread )
from time import sleep
from threading import *

# every program has one default thread called main thread
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello() #object of hello
t2 = Hi() # object of hi

t1.start()
sleep(0.2) #sleep is used to skip the 0.2 time after one time this print
t2.start()

t1.join()
t2.join()

print("Bye program is close now")