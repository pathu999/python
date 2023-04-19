#nheritance: Inheritance is a mechanism in OOP that allows us to create 
#a new class based on an existingS class. 
#The new class inherits all the attributes and methods of the existing class, 
#and can also define its own attributes and methods. Here's an example of 
class Electric_car():
    def __init__(self,make,model,year,battery_size):
        super().__init__(make,model,year)
        self.battery_size = battery_size

    def get_info(self):
        return f"{self.make} {self.model} {self.year} with {self.battery_size} kwh baattery"
        