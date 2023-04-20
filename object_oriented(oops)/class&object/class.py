# class is the blueprint for creating the object with share the attribuits and behaviour 
# its define set of attributes and method that are common to all instances of the class.
# Here's an example of a class definition in Python:  
'''class Dog():
    def __init__(self,bread,color):
        self.bread = bread
        self.color = color

    def bark(self):
        print("woolf")    

    my_Dog = ("Fido", "Golden Retriever")
    return f"{self.bread}"
'''
class Car: 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
