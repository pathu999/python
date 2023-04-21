#object overriding
#create class animal
class Animal:
    def make_sound(self): # method
        print("Animals make a sound")
''' This code defines the Animal class, which has a single method make_sound. 
    This method simply prints out the string "Animals make a sound".
    python
'''

class Dog(Animal):
    def make_sound(self):
        print("Dog is barks")
''' This code defines the Dog class, which is a subclass of Animal. 
    It defines its own make_sound method, which prints out the string "Dog is barks".'''

a = Animal()
b = Dog()
'''This code creates an instance of Animal called a, and an instance of Dog called b.'''

a.make_sound()
b.make_sound()
#These lines of code call the make_sound method on both the a and b objects. When called on the a object, the method prints out "Animals make a sound".
# When called on the b object, the method prints out "Dog is barks".
