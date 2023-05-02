class Base1():
    def __init__(self):
        self.str1="VJ"
        print("BAse1")

class Derived(Base1):
    def __init__(self):

        #calling base
#parentclassname.fun/constrname with parameter
        Base1.__init__(self)
        print("Derived")

#object call

obj=Derived()
