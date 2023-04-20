#inheritance poly
class Birds():
    def intro(self):
        print("many birds")

    def fly(self):
        print("many birds fly")

class Sparrow(Birds):
    def fly(self):
        print("sparrow can fly")

class pengion(Birds):
    def fly(self):
        print("pengion don't fly")
        
# create object
obj_birds = Birds()
obj_sparrow = Sparrow()
obj_pen = pengion()

#call object Birds()
obj_birds.intro()
obj_birds.fly()

#call object Sparrow()
obj_sparrow.fly()

#call obj pen
obj_pen.fly()

