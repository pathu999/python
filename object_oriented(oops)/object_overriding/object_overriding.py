#object over riding
#create class animal
class Animal:
    def make_sound(self):
        print("Animals make a sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog is barks")


a = Animal()
b = Dog()

a.make_sound()
b.make_sound()
