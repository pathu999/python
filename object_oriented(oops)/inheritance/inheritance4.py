class A: #parent class 
    def __init__(self) -> None:
        print("the A init")

    def features1(self):
        print("this is features first")

    def features2(self):
        print("features2")

class B (A):# b is a child class its access all the features of parents class
    def __init__(self) -> None:  #by defult created this method 
        print("The B init ")

    def features1(self):
        print("features2 second")

    def features2(self):
        print("the features2 second")


a1 = B()



