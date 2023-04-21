class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name,"," ,self.roll)
        self.lap.show()


    class Laptop:
        def __init__(self):
            self.brand = "dell"
            self.cpu = "i5"
            self.storage = "1tb"

        def show(self):
            print(self.brand , self.cpu , self.storage)

s1 = Student("navin",101)
s2 = Student("prathamesh",102)

lap1 = s1.lap
lap2 = s2.lap

s1.show()
s2.show()

