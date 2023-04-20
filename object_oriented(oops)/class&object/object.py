#An object is a instance of a class it's contain of the its contains 
#all the attributes of the class and methods defined by its class. 
#Here's an example of creating an object of the Car class:
class Car:  #class
    def __init__(self, make, model, year): #init method is a spacial method that is called automatically when object of class is created
        self.make = make   #__init__ method take at least one argument called self referce to the instance of the class that is b e a created 
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

my_car = Car("Toyota", "Corolla", 2020) #object
print(my_car.get_info()) # Output: 2020 Toyota Corolla
